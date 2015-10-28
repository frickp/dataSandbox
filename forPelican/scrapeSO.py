from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
from nltk.corpus import stopwords
import pandas as pd
import numpy as np

def soJobs(BASE_URL):
    html = urlopen(BASE_URL)
    soup = BeautifulSoup(html, "lxml")
    skillList = ''
    for desc in soup.findAll("div", { "class" : "description" }):
        skills =  desc.findAll('li')
        skills = unicode.join(u'\n',map(unicode,skills))   #Switch away from ResultSet
        skills = re.sub('<[^>]*>', '', skills)             #Remove elements from text
        skills = re.sub('[:;()/!@#$,]', ' ', skills)         #Get rid of spurious characters
        skillList += skills
    jobName = soup.find("a", {"class" : "title job-link"}).text.split()[0:3]
    jobName = re.sub(r'\W+', '',  unicode.join(u'',map(unicode,jobName)))
    # Get rid of common words
    filtWords = [i for i in skillList.split() if i not in stopwords.words('english')]
    # Export words as a data frame
    df = pd.DataFrame({"words": filtWords})
    df['title'] = jobName
    df['url'] = BASE_URL.rsplit('/',3)[2]
    if jobName.upper().find('DATA') == -1:
        df['data'] = False
    else:
        df['data'] = True
    return df