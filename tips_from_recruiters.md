Hey Peter,
 
Great chatting with you!
 
As promised, below is the initial interview prep guide - review and let me know what you think. If the scope of the interview is in line with your expectations, please provide the following information in your reply back so we can get you scheduled:
 
Availability:
Confirm your full availability for the next 5 weeks - I know this time frame seems bananas, but the scheduling team requires this range by default. I promise we’ll do our best to confirm something for sooner than later; the wait to do the initial is the biggest hurdle time-wise, but if the initial goes well, the process from that point forward will move lightning-fast. :)
 
Initial interviews take place on weekdays between 10am and 5pm PST. Your availability spread out across 2-3 days per week is ideal to ensure a quick/optimal match; Wednesdays are generally “no interview/meeting” days for our data scientists, but you can still include them in your availability; our scheduling team will determine if a particular Wednesday may be viable.
 
Coding language:
Confirm which language you’re most comfortable with – SQL, R or Python (though you’ll still have flexibility to choose whichever language you like during the interview).
 
Hear from you soon!
 
THE ROLE - DATA SCIENTIST, ANALYTICS
 
Let’s kick off this guide by clarifying what the “Data Scientist, Analytics” role is NOT:
 
Not working in a centralized function that responds to ad-hoc requests from all or various parts of the organization. As a data scientist (DS) at FB, you’re embedded in the product team of your choice. You’re a strategic partner all aspects of decision-making, end to end, driving high-level direction and day-to-day initiatives through the data lens.  
Not coding and training machine learning (ML) models from scratch, though, as a DS, you may identify opportunities within the context of a particular product/business problem for new or improved ML application and evaluate ML models. At core, the DS role, appeals to a broad range of analytical, technical and problem-solving interests for the FB domain. 
Not focused primarily on ETL or pipelining or other data infrastructure tasks; we have data engineers (DE) who do this and partner with DS’s.
Not conducive to rigorous academic approaches to FB data that might form the basis for publishing white papers; we have core data scientists (CDS) who do this.
 
 
THE INITIAL INTERVIEW 
 
This interview is roughly split into 2 parts (for a total of 30-45 minutes): 
Analytical (around 10-20 minutes)
Technical (around 10-20 minutes)
 
Note: It’s totally up to the interviewer which part s/he covers first - just be ready to kick off with either. 
 
Analytical 
 
This part involves discussion around either a case study or thought experiment, where the goal is to assess how translatable or transferrable your analytical skills are to the FB world.
 
We’re exploring how you solve real-world hypothetical problems related to business or product improvement, using a broad set of analytical approaches and techniques. 
 
We want to see how creative and methodical you are in thinking through problems and communicating the narratives that drive your ideas and solutions. 
 
For you, as the candidate, the aim is not demonstrating perfection in your knowledge and answers but, more importantly, how effectively you can adapt your critical-thinking and problem-solving skills to new problems and navigate ambiguity. 
 
Tip: Spend time engaging with our core products and features, less as a consumer and more as an expert analyst or researcher who’s been tasked with understanding the big business questions and nuanced data decisions that inform the continual development of our products and features. As you get to know our products, put yourself in the mindset of the FB teams that created them and ask yourself these questions:
 
- What questions had to be asked and what decisions had to be made that ultimately led to the way this product/feature works and looks now?
- Which metrics are considered most critical to FB when solving specific challenges around product health, growth and engagement?
- How is success defined for the FB product ecosystem in general vs. for this particular product - what are overarching and unique elements?
- What are the obvious trends and, more importantly, hidden insights that accurately determine if this product is performing successfully or not? 
- What testing and experimentation had to be done and what were the decisions and risks involved in implementing this new feature or interface? 
- Where do I see room for improvement on this product/feature - what’s my hypothesis, what’s my plan for analysis, how impactful is this to the bigger product vision or roadmap?
 
Introduction to FB products:
Facebook Products
Facebook News
 
FB’s VP of Analytics on product growth:
Alex Schultz talking at Stanford
 
 
Technical 
 
This part involves 1-2 data-processing questions, where the goal is to assess how you use code to transform/translate user data and solve product problems.
 
While the actual data or data sets accompanying the technical questions may vary, you can expect to see event-level data, dimension-level data or both; your interviewer will specify the required parameters. Expect to write code that would best answer data-processing questions based on the schema or set of schemas given by the interviewer. 
 
Note: Data shared for these questions is designed for interview purposes and unrepresentative of actual data sets we work with at FB.
 
Tip: If a coding question strikes you as being especially conducive to a particular language, but that language is not your primary or preferred, it’s generally best to default to your primary or preferred language so that you can fully leverage the extent of your coding knowledge and proficiency. The interviewer will understand that there may be unique capabilities or constraints to the language you’ve chosen, given the problem, and will calibrate his/her evaluation accordingly. If you’re comfortable using multiple languages or list multiple languages on your resume, it’s helpful to announce to the interviewer which language you’ll be using and why - in the interest of keeping the logic of your code clean and consistent, probably best to not switch back and forth between languages, though if you’re super stuck and switching is the only way you can move forward, announce this to the interviewer and be open to any direction or feedback that he/she may offer. Always, always speak out the logic behind your code and explain where it’s heading.  
 
Sample Questions:
- Given timestamps of logins, figure out how many people on FB were active all 7 days of the week and on a mobile phone.
- How do you determine what FB product was used most by non-employee users during the last quarter? 
 
Mock Data + Sample Questions:
Below are a couple examples that don't specifically relate to FB but do mimic the kind of data and format that you may be presented with.
 
Event-level data: an attendance log for every student in a school district
date | student_id | attendance
Dimension-level data: a summary table with demographics for each student in the district
student_id | school_id | grade_level | date_of_birth | hometown
 
Referencing the data above, you may be asked to address things like the following:
- What was the overall attendance rate for the school district yesterday?
- Which grade level currently has the most students in this school district?
- Which school had the highest attendance rate? Which had the lowest?
 
If using SQL, you can expect to be assessed on some subset of the following:
- Write a query or set of queries to derive insights based on the given log(s) or schema(s)
- Work with aggregate functions
- Utilize different types of Joins (IE: Left, Inner, Outer, etc.) 
- Utilize Union and Union All
- Work with concepts including Distinct, Random Sampling, De-Duplication, Optimization
- Apply the results of your analysis to make product decisions or suggestions
 
If using Python:
- Always check for edge cases and corner cases when you are coding and try to provide a bug free solution
- Be prepared to improve your solution when asked 
- Make sure to practice the core CS concepts like arrays, linked list, stacks, queues, hash maps, binary trees and graphs, searching and sorting, recursion and parity
 
If using R:
- Be thoughtful about implementation efficiency
- Be familiar with apply functions family, dplyr package or an equivalent 
- While statistical packages can be called directly in R, please also expect some general programming that needs to be implemented, such as data frame manipulation and control flow
 
Coding tutorials (optional prep if you need to brush up):
SQL Course
Programmer Interview SQL Practice Database
Mode Analytics SQL Tutorials


GENERAL TIPS
 
During the video interview, you’ll need access to a laptop or desktop computer - make sure the Internet connection is stable and that you’re in a space free of distractions. You’ll log onto a site called coderpad, which is basically a chat room that allows your interviewer to observe your code. (You’ll receive additional details about this when the interview is confirmed.)
        
We strongly encourage you to have full understanding of being able to analyze data sets through a coding/scripting language of your choice (SQL, R or Python). If you do not know the basics of one of these languages, you should not be moving forward with this interview; we’re happy to give you additional time to prepare and schedule your interview when you’re ready. 
 
It's critical that you think out loud and provide your interviewer with the narrative leading up to your solution. The interviewer may chime in with prompts at several points as you’re speaking; be ready to pivot your thought process and/or approach. Ask clarifying questions if anything is unclear.
 
As you prepare for this interview, take caution when referencing publicly posted FB DS interview questions; we've discovered several of the posted solutions to be wrong.
 
The interviewer may take notes on his/her computer, notepad or phone; be patient if he/she needs a few moments to document feedback.
 
Prepare 2-3 questions to ask your interviewer and be prepared to discuss your interest in FB - in case there’s time for Q&A, you’ll want to make this rare informal exchange with an FB DS as insightful and as productive as possible. :)
 
--------------

INTERVIEWER’S BACKGROUND:
 
Remember: an interviewer’s background or team at FB does not guarantee that the product he/she supports will be showcased in the case study or thought experiment - in some cases, it does happen; in other cases, it doesn’t. The best thing you can do in preparation is to engage with our core applications and their features (Newsfeed, Instagram, Messenger, etc.). The main thing that the interviewer will be after, no matter his/her background/team, will be “Can this candidate effectively transfer over his/her critical-thinking and problem-solving skills to the unique product problems that we’re solving here at FB?”
 
NAVIGATING THE INTERVIEW DISCUSSIONS: 
 
High/low: A good tip to help you structure a response to a hypothetical case-analysis question is to 1) give the interviewer an aerial (high-level) view of your approach to the problem and your plan for the analysis, then 2) proceed to break down your approach/plan into actionable steps (via a low-level of ground-level view). This is a common organizational tool that many successful candidates seem to use, in some variation or other, in order to bring structure to a problem that is highly unstructured and open-ended. I suspect that the reason why “high-low” is particularly effective in our DS interviews is because the role, itself, involves equally a great deal of zooming out and keeping an eagle-eye on the larger strategic roadmap and zooming in to the nuances of particular analyses and how the related data, tests and experiments all align in practical ways to pushing the roadmap forward. In an interesting way, this idea of “high-low” touches on communication skills or how information is presented to tell a compelling story.
 
Taking lead: For any candidate who has industry experience under their belt (i.e. not a fresh grad), there will be an expectation that he/she will be able to lead a conversation as a subject-matter expert - generally speaking, the more experienced you are, the higher this expectation. When I say “subject-matter expert” I don’t mean an expert on all things FB, so don’t put the pressure on yourself to have to know everything there is to know about the inner workings of FB; what I mean is that you, given your current experience and expertise, should be able to demonstrate a reasonable comfort level in leading the conversation as a data consultant to your business and stakeholders. At FB, you, as a DS, partner closely with Product, SWE, Design, end to end - every decision is data-driven, this means that you play a uniquely compelling role in advising on every aspect of product change or improvement. With so much access to data, so many ideas, so many interesting/cool experiments that could be explored, how do you ensure that you’re optimally aligning your proposals and solutions to the answering the most critical business questions?
 
If you’re unclear on what the interviewer is asking, you should feel empowered to ask clarifying questions and/or ask for more data - don’t ever embark on a proposal or solution until you’re reasonably clear on what’s being asked. But if you ask for more information and the interviewer defers to you or keeps deferring to you, that’s a big, bright flashing green light for you to take the wheel of the discussion - this is your interviewer wanting to see your mind at work. Every candidate sinks his/her teeth into a problem uniquely: what’s your approach, how logical is it, how thorough is it, how relevant is it, how practical is it to the business? You’ll want to articulate aloud what’s going through your mind: what are the first data sets that you might look at, what are the key metrics you’d want to follow (why these metrics vs. those metrics), what kinds of experiments or tests would you want to employ (what are the expectations; what are the implications for evaluating quality and risk) - and, ultimately, how does all of this align with the business goal or question you’re trying to answer.
 
Note: Don’t take taking the lead to extremes, like ignoring your interviewer or overpowering the conversation. Look to the interviewer for cues that he/she wants you to keep going or that he/she wants to ask a question and present new information, etc. If the interviewer interjects with a question or challenges your idea/approach, do the best you can to pivot or offer rationale for what you’re doing - and be open to feedback and knowledge-sharing. While taking lead, you want to demonstrate a balance of independent thinking/problem-solving and collaborative spirit. 
 
Thinking aloud: Trust me, your interviewer is just as interested in how you come to solve a problem as he/she is in the actual solution. Even if you respond with the “correct” answer straight out of the gate, your interviewer will say, “Great! Now, talk me through how you got there, step by step.” Not many companies do what FB is doing, so our interview questions can be really tough to navigate and ace in any formulaic way; often the thing that saves the candidate is the transparency into his/her thought process and the creative and coachable logic that shines through.
 
When asked to code, make sure you’re crystal-clear on the problem before you embark on the solution. The tech analysis or coding question is where we want to see 1) how you translate a product problem or question into query or algorithmic form and 2) how accurately and/or efficiently your code handles product problems, especially in relation to isolating user behavior/trends and pivoting/iterating based on new information and or scalability issues. How accurate and efficient/effective your code is is contingent on how clear you are on the scope of the problem given. Fair warning: coderpad is a very simple platform; it’s akin to using a whiteboard. There will be no fancy packages for you to rely on, so you must brush up as much as possible on syntax, grammar, etc. A huge and common mistake is to not speak aloud through your code; you should absolutely be talking through the logic of what you’re doing. More than anything, the interviewer is looking for the signal that you have a solid coding foundation and that, given a more typical work environment, you’d be able to hit the ground running in leveraging your coding ability to solve problems.
 
Q&A:
 
With technical interviews, there’s always a chance that there won’t be enough time to go over every question that a candidate has. If you run out of time or it seems like you may not have the chance to get through all your questions, be mindful of the clock and choose just 1-2 questions that are top-of-mind or you know can be reasonably covered without rushing. If the initial goes well, you’ll be meeting a bunch of DS’s from different teams during your visit, and you’ll also have lunch 1-on-1 with a DS, who’ll be more than happy to share their experience and answer your questions - I promise that we’ll put all the information you need in your hands, so you can make a fully informed decision on FB in the end.
 
Truly, the best way to tackle our case study questions is to spend time with our core products and understand how their features work. There’s no guarantee that you’ll be asked about a specific FB product, but there are still crucial aspects of how our products are designed and why our features work the way they do that can help you wrap your mind around any product problem.

---- 

Data Scientist, Infrastructure
 
While every interviewer is different, the interview will consist of the following key areas:
 
1. Statistics: We expect all of our data scientists to have a basic level of statistics knowledge that we deem equivalent to what you would learn in an introductory statistics course (hypothesis testing, statistical inference, linear/logistic regression, general experimentation practices and interpretation of data, etc.). Beyond the basics, we focus on open-ended applied statistics problems drawn from the experience on your resume (i.e. predictive analytics, ML) and related areas. 
 
2. SQL: Joins, aggregations, subqueries, etc. Some helpful resources:
http://sqlzoo.net 
http://www.sqlcourse2.com/index.html 
https://www.codecademy.com/learn/learn-sql   
 
3. Coding: (Python, R, etc… but you can use whatever language you are MOST comfortable with) - focus on topics that relate to data science: data processing for structured and unstructured data, data mining/parsing, data structures/algorithms such as arrays, hash tables/dictionaries, etc. Examples: parsing a data file and storing it in a data structure; given a string of characters, find the frequency of a specific character.
While the phone interview will focus mainly on data processing questions, a potential future onsite interview portion requires the ability to manipulate data structures and implement common algorithms. Here is a resource with common data structures/algorithms (arrays, lists, dictionaries/hashtables, trees, graph search, etc.) that we provide for all data scientists that proceed to the onsite interview stage: http://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/. We don’t expect coding at the level of a software engineer, but having some general purpose programming background in the methods listed will set you up for success in that portion of our interviews later on. 
 
Some additional tips: 
-Expect 2-3 questions in each of the 3 areas listed. 
-The questions are designed to be quick due to the short amount of time in a phone interview, so expect to spend no more than 5-10 minutes on each question. 
-For the coding portion, we have found that either R or Python works best in terms of speed and efficiency, but we won't discourage you from using your strongest language as we are a language agnostic company. We recommend a brute force approach to the code and then optimizing afterwards. 
-For the statistics portion, if you encounter questions that you are less familiar with, try to propose a more informal ad-hoc solution if you don't remember exact terms or details.
-Communicate thought process and assumptions aloud to the interviewer and they will be able to provide any guidance on expectations. 
You should have a computer on hand for the interview as the coding portion will involve using a shared screen website (Coderpad: https://coderpad.io/), where you can select and switch between any of the languages available. We will generate a unique link for you to access during your interview.
----
Here is the link to the job description: Data Scientist, Analytics

The primary responsibilities for Data Scientist, Analytics are:
Use quantitative tools to uncover opportunities, set team goals and work with cross-functional partners to guide the product roadmap
Explore, analyze and aggregate large data sets to provide actionable information, and create intuitive visualizations to convey those results to a broad audience
Design informative experiments considering statistical significance, sources of bias, target populations and potential for positive results
Collaborate with Engineers on logging, product health monitoring and experiment design/analysis
The Data Scientist, Analytics role is not characterized by the following:
Working in a centralized service organization, consulting and responding to ad-hoc requests. Data Scientists in the Analytics org are embedded in product teams and expected to be involved in driving both the high-level direction and the day-to-day progress of the team.
Specializing in ETL, pipelining, and other data infrastructure tasks. While it is common for Data Scientists to build and maintain some pipelines, the Data Engineering team focuses more heavily on this.
Taking an academic approach to Facebook data and publishing white papers. That activity typically resides in the Core Data Science team.
Building, training and deploying machine learning models to production. Although a few Analytics roles will involve modeling, most production models are handled by the Engineering team.

OVERVIEW OF THE INITIAL INTERVIEW, SAMPLE QUESTIONS, & ADDITIONAL RESOURCES FOR PREPARING:

The interview will be 2 parts (for a total of 30-45 minutes): 
1 – Analytical (10-20 minutes)
1 – Technical (10-20 minutes)

Analytical Portion (10-20 minutes)

Per our conversation, the analytical case study will focus on questions to gauge your product sense. 

For the analytical questions, the interviewer is trying to understand how you solve business questions and problems, as well as how creative and articulate you are at thinking through these problems while solving them. It’s not about arriving at the perfect or correct answer, but how you engage with the problem.

Spend some time engaging with Facebook products less as a user and more as someone who is tasked with improving or developing these products. This link outlines what we consider a “Facebook product” (Ads, Mobile, Timeline, News Feed, Messaging, etc.). Note: It is not a complete list, and the analysis case may or may not refer to one of the products listed.

Resources:
Facebook News
VP of Analytics Alex Schultz's Talk at Stanford on Growth at Facebook
How Facebook used Science and Empathy to Reach two Billion users
Recent post from Mark Zuckerberg.

Put yourself in the shoes of the product team who built the product / feature
Why do you think they made certain decisions about how it works?
What could be done to improve the product?
What kind of metrics you'd want to consider when solving for questions around health, growth, or the engagement of a product?
How would you measure the success of different parts of the product?
What metrics would you assess when trying to solve business problems related to our products?
How would you tell if a product is performing well or not?
How would you set up an experiment to evaluate any new products or improvements?

Technical Portion (10-20 minutes)

You will be given 1-2 data processing questions during this portion. We are looking not only for coding skills, but also for the ability to translate a high-level question into an execution strategy and explain how the result is relevant and what aspects may still be lacking.

Mock Data and Questions:
This example doesn't pertain to Facebook but is representative of the data and questions you may see:

An attendance log for every student in a school district
attendance_events : date | student_id | attendance
A summary table with demographics for each student in the district
all_students : student_id | school_id | grade_level | date_of_birth | hometown

Using this data, you could answer questions like the following:
What percent of students attend school on their birthday?
Which grade level had the largest drop in attendance between yesterday and today?

Core skills
Regardless of your language, you should be familiar with ALL of the following skills
Work with grouping and aggregate functions
Utilize different types of joins (left, inner, outer, etc.) including when and how to use a self-join
Append multiple data sources (union in SQL, concat in Pandas, bind_rows in R)
Filter data by multiple, complex conditions
De-duplication, sorting, handling missing/incomplete data
Assess efficiency. This will not be a primary focus, but you may be asked to think of more efficient ideas or to explain why you are making certain efficiency/simplicity tradeoffs
Using SQL:
You may work in whatever dialect you like, but all questions will be answerable with ANSI-standard functions (think PostgreSQL). If you use a dialect-specific syntax, you may need to explain it to your interviewer
Try to maintain a consistent capitalization/indentation style for readability
Using Python or R:
Given the heavy focus on data manipulation, most candidates choose to use libraries such as Pandas/Numpy in Python or dplyr in R. It is possible to solve the questions in pure Python/R (or any Turing-complete language!) but doing so will likely be much slower and more difficult.
The interview will either be on a whiteboard or in a plain text environment, so there will be no access to function autocomplete or help documentation.
A few small mistakes in syntax will not automatically disqualify you, but pseudocode or a general explanation is not acceptable. Be sure that you know the function names, input arguments, etc. to implement the core skills listed above.
Interviewers generally know the most widely used libraries, but there's no guarantee that any individual interviewer will be familiar with the libraries you're mentioning. That's okay but you may have to provide more guidance / context around what you're writing.
If you do not have much experience performing joins and aggregations, you may wish to review that functionality for Python or R
Resources:
SQL Course
Programmer Interview SQL Practice Database
Mode Analytics SQL Tutorials


General tips for the interview:
During the video conference interview, you will need access to a computer. You will log in to www.coderpad.io - basically like a chat room - so the person on the other side can look at your code. Please be logged in using the link provided at the interview start time. You will receive additional details, including the link, when the interview is confirmed.
As mentioned above, it is better to delay your interview than proceed before you are ready. There is no penalty for taking a few extra weeks (or longer) to prepare.
It's important that you think out loud/ provide a narrative as you go through the problem so the interviewer has insight into your thought process.
The interviewer will prompt you if you are heading in the wrong direction. Your ability to pivot your answer is a positive signal.
Feel free to ask clarifying questions during the interview.
Additional notes:
While we recognize that candidates may utilize outside sites/resources with posted interview questions and answers, we encourage caution, as we've found many of the proposed solutions to be incorrect.
Your interview confirmation email will contain the names of all your interviewers (this is subject to change). However, just because an interviewer works on Messenger (for example) does not mean they will ask you questions about Messenger.
During the interview, the interviewer may take notes on their phone or computer. Please do not take this as a sign their attention is elsewhere. They are fully committed to you!
Be prepared to answer why you are interested in Facebook. The interviewers like to see people who know about our environment, projects, challenges, etc.
If there is time at the end of the interview, feel free to ask questions about Facebook and analytics.
After the initial interview, I will give you an update regarding next steps as soon as possible. Unfortunately, I will not be able to share direct feedback from your interviews.
Please let me know if you have any questions in the meantime!
----
Below are just some general tips on how to prepare for the initial interview.
The interview will consist of 2 calls:
1 - Analytical Interview (30 minutes)
1 - Technical Interview (30 minutes)
 
Analytical Interview:
This interview is designed to get a general understanding of your background, your comfort with using data to drive product decisions, A/B testing, quantitative methods, and your general analytical abilities. You will be asked to describe relevant projects from your current or past roles. There will also be a case study which focuses on analytical questions on metrics and how you would measure the health of a product (usually a Facebook product you are familiar with).
 
For the analytical questions, the interviewer is trying to understand how you solve business questions and problems, as well as how creative and articulate you are at thinking through these problems while solving them. It’s not about the correct answer, but also about what kind of metrics you would want to consider when solving the problem.
 
I strongly encourage you to use FB products at least a little bit before coming in to the interview and think about:
1) How would you measure the success of different parts of the product? 
2) Put yourself in the shoes of the product team who built the product / feature – why do you think they made certain decisions about how it works? What could be done to improve the product?
 
Technical Interview:
This interview will test your proficiency with SQL and quantitative abilities using a virtual shared coding portal called CoderPad. The technical portion will include:
Writing queries based on a given data set
Reacting to nuances and messiness of data
Note that we are looking not only for SQL skills, but also for the ability to design an operational approach to figure out a concrete answer to a specific question using data.
 
As not everyone has used CoderPad, below are a few links to make sure you feel comfortable using the platform during your interview. You'll also receive further detailed instructions upon the confirmation of your scheduled calls. 
 
Feel free to try out the demo here (note that in your interview you will be using the “Plain text” setting and not executing any code) –
https://coderpad.io/demo
For tips and tricks you can check out –
https://coderpad.io/tips-and-tricks
 
SQL Refreshers/Tips:
SQLZOO: The website http://sqlzoo.net/wiki/Main_Page has lots of cool SQL problems and a self-paced tutorial. I found this to be the most helpful of all the database related resources.
W3 School: The website http://www.w3schools.com/sql/ has also a very good slowly paced tutorial that covers plenty of material. The problems and example cover more topics than SQLZOO but aren't as challenging. 
This page has sample SQL exercises of increasing complexity, which I found to be pretty fun: http://db.grussell.org/sql/
Tutorial around SELECT statements. http://www.sqlcourse2.com/intro2.html
Hacker Rank: https://www.hackerrank.com/domains/sql/select
 
General tips: 
Please send me your current resume. It is likely that you will be asked about experiences listed on your resume (including technology or tools you've used, projects you lead, etc.) - anything you have mentioned on your resume is “fair game.”
Feel free to ask clarifying questions.
It's important that you think out loud/ provide a narrative as you go through the problem so the interviewer has insight into your thought process.
 
Also, please prepare any questions you have before the interview and also be prepared to answer why you are interested in Facebook. The interviewers like to see people who know about our environment, projects, challenges, etc. 
 
If there is time for questions at the end of the interview, please feel free to ask questions focused on Facebook and product quality analytics. Interviewers would be more than happy to answer!
 
Here are a few helpful links to provide insight into our role, Facebook and our products:
Product Quality Analyst
https://www.intern.facebook.com/careers/jobs/a0I1H00000LC6ExUAL/
 
General News:
http://techcrunch.com/tag/facebook/
 
Facebook Products: 
http://newsroom.fb.com/Products
 
Facebook Ads:
https://www.facebook.com/business/news/getting-more-value-from-facebook-
ads
 
http://www.wired.com/2015/09/facebook-doesnt-make-much-money-couldon-purpose/
 
Createflow: 
https://www.facebook.com/ads/create
 
Feel free to reach out if you have any questions, otherwise I will await your availability to continue forward. Please provide as much availability as possible, this will help ease and expedite the scheduling process. 
 
Thank you again for your time and interest in joining our team. 
-----

