#!/Users/pf494t/anaconda2/bin/python
# nlp helper functions for python 2.7

import re
from scipy.stats import itemfreq 
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer as wnl
from gensim.models import Word2Vec, Doc2Vec, doc2vec
from gensim import corpora, models
from gensim.corpora import Dictionary

###########################################################################################
# Functions related to tweet cleaning
###########################################################################################

def standardize_html(tweet):
	"""map all instances of http* --> 'URL'"""
	return re.sub(r"http\S+", "URL", tweet)

def standardize_www(tweet):
    """map all instances of www* --> 'URL'"""
    return re.sub(r"www\S+", "URL", tweet)

def standardize_mentions(handle):
    """map all instances of @{any handle} --> 'twithandle'"""
    return re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z_]+[A-Za-z0-9_]+)", "twittermention", handle)	
  
def remove_punc(my_word):
    """Function to remove punctuation from string inputs"""
    if my_word is None:
        return my_word
    else:
        return sub('[%".:;()/!--""-=*@$,<>?^\d+]','',my_word)

def remove_ascii(my_word):
    """Function to remove ascii from string input"""
    if my_word is None:
        return my_word
    else:
        return str(sub(r'[^\x00-\x7F]+','', my_word.decode('utf-8').strip()))

def lemmatize(my_word):
    """Function to lemmatize words"""
    if my_word is None:
        return my_word
    else:
        return str(wnl.lemmatize(my_word))

def remove_stop_words(my_word):
    """Function to remove stop words"""
    if my_word is None:
        return my_word
    if my_word not in str(stopwords.words('english')):
        return my_word

def remove_link_user(my_word):
    """Function to remove web addresses and twitter handles"""
    if not my_word.startswith('@') and not my_word.startswith('http'):
        return my_word
        
def not_empty_word(my_word):
    """Function to prevent '' from being included in word list"""
    if my_word is None:
        return my_word
    if my_word != '':
        return my_word

def removeChr10(myWord):
    print(sub('chr\(10\)',' ',myWord))

def prep_text(my_word):
    """Final text pre-processing function"""
    return not_empty_word(
		lemmatize(
			remove_ascii(
				remove_punc(
					remove_link_user(
						my_word.lower()
					)
				)
			)
		)
	)
	
def filter_msg_list(msg_list):
    """Remove stop words, lemmatize, and clean all tweets"""
    return [[prep_text(word) for word
                in removeChr10(msg).split()
                    if prep_text(word) is not None]
                for msg in msg_list]

###########################################################################################
# Functions for creating text features
# see code here:
# https://codecloud.web.att.com/projects/BDCOE/repos/advanceddatascience-twitter_trial/browse/sentiment_analysis/SA_ATT_v4.py
###########################################################################################

def proportion_of_capitalized(x):
	return float((len(re.sub("[^A-Z]","",x))/float(len(x))))

def exclamations(x):
	return len(re.sub("[^!]","",x))
	
def getEmojis(R, encode=False): 
	""" 
	pass True to 'encode' if the string is coming from something that decodes
	utf-8 strings, like a json parser for example. Use False if receiving strings
	directly from stdin
	"""
	if encode:
		row = R.encode('utf-8')
	else:
		row = R
	emojis = []
	nextByte = -1
	L = len(row)
	for i in range(0, L):
		if i < nextByte:
			continue
		s = '{0:08b}'.format( ord(row[i]) )
		if s[:4] == '1111':
		# start of a 4-byte utf-8 sequence, grab the following 3 too.
			c = '{0:08b}'.format( ord(row[i])  )[5:] + \
				'{0:08b}'.format( ord(row[i+1]))[2:] + \
				'{0:08b}'.format( ord(row[i+2]))[2:] + \
				'{0:08b}'.format( ord(row[i+3]))[2:]
			v = int(c, 2)
			emojis.append ( '0x{0:05x}'.format(v) )
			nextByte = i+4
		elif s[:4] == '1110':
		# start of a 3-byte utf-8 sequence, grab the following 2 too.
			c = '{0:08b}'.format( ord(row[i])  )[4:] + \
				'{0:08b}'.format( ord(row[i+1]))[2:] + \
				'{0:08b}'.format( ord(row[i+2]))[2:]
			v = int(c, 2)
			emojis.append ( '0x{0:04x}'.format(v) )
			nextByte = i+3
	return emojis
   
def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = [float(val) for val in splitLine[1:]]
        model[word] = embedding
    print("Done.",len(model)," words loaded!")
    return model

def aggregateWordVectors(tweet, wordVecs, len=200):
	allWords = tweet.split()
	maxVector = [-float("inf")]*len
	minVector = [+float("inf")]*len
	sumVector = [float(0)]*len
	for word in allWords:
		numWordFound = 0
		if wordVecs.has_key(word):
			numWordFound+=1
			maxVector = np.maximum(maxVector, wordVecs.get(word))
			minVector = np.minimum(minVector, wordVecs.get(word))
			sumVector = np.add(sumVector, wordVecs.get(word))
		avgVector = np.divide(sumVector,1+numWordFound) #+1 to avoid -INF 
	return list(maxVector) + list(minVector) + list(avgVector)

###########################################################################################
# Functions related to LDA/doc2vec in gensim
# see code here: 
# 
###########################################################################################

def make_dict(my_msg_list):
    """Create dictionary from list of tokenized documents"""
    return corpora.Dictionary(my_msg_list)

def make_corpus(my_msg_list,my_dict):
    """Create corpus from list of tokenized documents"""
    return [my_dict.doc2bow(msg) for msg in my_msg_list]

# I tried using LdaMulticore, but increasing number of workers (range(1,11)), does not improve training time
def create_LDA(my_corpus, my_dictionary,my_topics=50,my_passes=10,my_iterations=50,my_alpha=0.001,my_workers=None,my_eta=None):
    """LDA model call function"""
#    return models.LdaModel(my_corpus, id2word=my_dictionary, num_topics=my_topics, passes=my_passes,\
    return models.ldamodel.LdaModel(my_corpus, id2word=my_dictionary, num_topics=my_topics, passes=my_passes,\
    		iterations=my_iterations,alpha=my_alpha,eta=my_eta)

###########################################################################################
# Functions for model evaluation
###########################################################################################

def collapse_one_hot(row):
	"""For checking accuracy of multiclass classifiers (e.g., neural nets) 
	Take binary classification with two columns and collapse to a single column. 
	Returns `0` for the first class and `1` for the second class"""
	return 1 if row[0] < row[1] else 0

def eval_classifier_quality(true_labels,pred_labels):
    """Display some performance metrics for a multiclass classifier."""
    print("\nConfusion Matrix:")
    cm = np.matrix(confusion_matrix(true_labels,pred_labels))
    print(cm)
    print("\nClassification Accuracy")
    print("%f percent" % (np.trace(cm)/float(np.sum(cm)) * 100))
    print("\nPrecision-Recall")
    print(classification_report(true_labels, pred_labels))
    print("\nMost recurrent class is (ZERO RULE)", np.max(np.sum(cm,axis=1))/float(np.sum(cm))*100)
    class_fraxn = itemfreq(true_labels)[:,1]/float(len(true_labels))
    print("\nRandom guessing accuracy is", (np.dot(class_fraxn,class_fraxn)*100))



