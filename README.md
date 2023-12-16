## AUTOMATION OF KYC PROCESS FOR DETECTION OF POSSIBLE FINANCIAL CRIMES
  
There are multiple deficiencies in the KYC process, one of the activities analysts perform. The
onboarding process is prolonged due to the time-consuming task of reading and
analyzing companies' information. Additionally, there is a risk of analysts overlooking
certain details. Therefore, a change is necessary to enhance the KYC procedure, making it
faster and more secure in terms of compliance with due diligence.
The objective of this project is to implement a program that helps automate this lengthy
process and check whether the companies operate in countries listed as high-risk by the
Financial Action Task Force (FATF) or if they are involved in high-risk activities.

My proposal is to implement Natural Language Processing (NLP) techniques to analyze
the information received from clients and to check for any matches with the information
extracted from the Financial Action Task Force (FATF) and the list of high-risk activities.
In order to do so, I have defined the following stages:
- Information retrieval and database creation
- Text analysis
- Report creation
- Additional features

## 1.- Information retrieval and database creation
The FAFT uploads to its website two lists on a monthly basis : High-Risk Jurisdictions
subject to a Call for Action & Jurisdictions under Increased Monitoring. The first step is to
retrieve the information from these web pages and create a database that reflects the
countries and their categorization in one of the two records. To do so, I will inspect the
HTML code from the web and create some functions in Python to retrieve the names of
these countries, making use of the libraries requests, to connect to the page and retrieve
its information, and bs4, that will help me parse the html and extract the embedded
country names. Once this is done for the two lists, I shall create a database with the
names of the highlighted countries, whether they are included in the black list or in the
grey list, and all the different names this country might receive, in order to make the
search more thorough.

## 2.- Text analysis
This stage can be divided in two:
#### 2.1 High-risk countries analysis
Once I have the database with the different countries created, I need to look for them in
the client’s information to see if any matches appear. However, I need to be cautious, as it
may occur that the name of a country may appear in a different context and this would
result in a false positive. For example, if “Restaurant France” is included in one of these
texts, and “France” is included in the high-risk countries, the alarm would go on,
although this is not the expected behavior. To tackle this problem, I will use NLP
techniques, and analyze entities of the text instead of words. This way, my program would
detect “Restaurant France” as a unit, which would not match with the country “France”.
To do this, I will use the library spacy in Python.
#### 2.2 High-risk activities analysis
I need to look for matches with the high-risk activities list provided. Nevertheless, I need
to be aware of the different ways in which one of these activities might appear in the texts.
For example, although “mining” is included in the list, I might want to search for words
whose lemma is “mine”, instead of just looking for the word “mining”. This will make my
search more accurate. Once again, this can be done by making use of the functions already
defined on the spacy library mentioned above. Also, it would be a good idea to look not
only for words in the list, but also for synonyms of these activities. Additionally, I must
note that searching by lemma might not always make sense. In some cases, it might be
best to look for the action as a whole. Such is the case for the activity “real state".

## 3.- Report creation
Finally, when the documents have been scanned, it is crucial to present the gathered
information to the analysts. A simple report might be created to showcase the countries or
activities detected in the text, but in order to make this more insightful, creating
visualizations with tools like PowerBi or Kibana would be a better option. This way, an
analyst would see at a glance important information, for instance, the number of times a
country or an activity has been mentioned in the document.

## 4 - Additional features
Once a minimum viable product has been created, it might be interesting to exploit some
other ideas. For example, the possibility of implementing a chatbot, using the Python
library langchain, so that the analysts can find responses to some questions they might
have about the prospective client without having to read the whole document.
