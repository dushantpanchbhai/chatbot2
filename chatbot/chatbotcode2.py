import sys
from newspaper import Article
import random
import numpy as np
import spacy
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import yaml
import requests
import nltk
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt',quiet=True)
warnings.filterwarnings('ignore')
nlp = spacy.load('en_core_web_sm')
remove_punct_dict = dict(  (ord(punct), None) for punct in string.punctuation)

output=sys.argv[1]

import os
path1=os.getcwd()+"/chatbot/greeting.yml"

def chatbot_query(question, index=0):
    q1=nlp(question)
    q=[i for i in q1]
    error = "sorry, i can't understand what are you asking"
    result = ''
    #search_result_list = list(search(question, tld="co.in", num=10, stop=3, pause=1))
    search_result_list = list(search(question, tld="co.in",start=0,num=10, stop=10, pause=2))

    page = requests.get(search_result_list[index])

    tree = html.fromstring(page.content)

    soup = BeautifulSoup(page.content, features="lxml") #prints the whole .html script
    #print(soup)
    article_text = ''
    article = soup.findAll('p')
    #print(article)
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True))
    #print(article_text)
    first_sentence = article_text.split('\n')
    #first_sentence = first_sentence.remove('')
    while('' in first_sentence) :
        first_sentence.remove('')
    #print(first_sentence)
    try:
        k=nlp(first_sentence[0])
    except:
        k=nlp(first_sentence[1])
    arr=[]
    list2=[]
    for l in q:
        arr.append(str(l).lower())
    for j in k:
        list2.append(str(j).lower())
    #check = any(item in arr for item in list2)
    check=False
    #---------------------------------------------------------------------------------
    doc123 = nlp(question)
    ap=[k.text for k in doc123]
    for i2 in doc123:
        if i2.tag_=="WP" or i2.tag_=="VBZ" or i2.pos_=="PUNCT" or i2.tag_=="IN":
            ap.remove(i2.text)
    intersection=list(set(ap) & set(list2))
    if len(intersection)>0:
        check=True
    #-----------------------------------------------------------------------------------------
    if check==True:
        second=first_sentence[1].split('?')[0]
        first_sentence = first_sentence[0].split('?')[0]
        chars_without_whitespace = second.translate(
            { ord(c): None for c in string.whitespace }
        )
    else:
        first_sentence = first_sentence[1].split('?')[0]

    chars_without_whitespace = first_sentence.translate(
        { ord(c): None for c in string.whitespace }
    )
    if len(chars_without_whitespace) > 0:
        if check==True and len(first_sentence)<70:
            result = (first_sentence+" "+ second)
        else:
            result=first_sentence
    else:
        result = 'error'
    return result

def filter(question):
    #a_yaml_file = open("/home/dushant/Desktop/django/chatbot2/chatbot/greeting.yml")
    a_yaml_file = open(path1)
    par = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    q=nlp(question)
    cd=0
    rem=('you','are','it','a','do','of','can','where','know','any','what')
    b=[str(j2) for j2 in q]
    for i2 in q:
         if i2.tag_=="WP" or i2.tag_=="VBZ" or i2.pos_=="PUNCT" or i2.tag_=="PRP$" or (i2.text.lower() in rem):
            b.remove(i2.text)
    b2=" ".join(b)
    for i,j in par:
            q1=nlp(i)
            a=[str(j2) for j2 in q1]
            for i3 in q1:
                if i3.tag_=="WP" or i3.tag_=="VBZ" or i3.pos_=="PUNCT" or i3.tag_=="PRP$" or (i3.text.lower() in rem):
                    a.remove(i3.text)
            a1=" ".join(a)
            if a1.lower()==b2.lower():
                kl=j
                return kl
#Function to return a random greeting response to a users greeting
def greeting(sentence):
    GREETING_INPUTS = ["hi", "hello",  "hola", "greetings",  "wassup","hey","hii","hiii"]
    GREETING_RESPONSES = ["hi ","hey ","hey","Hello ","Hello Human"]
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    search_result_list = list(search(user_response, tld="co.in",start=0,num=10, stop=10, pause=2))
    article = Article(search_result_list[0])
    article.download() #Download the article
    article.parse() #Parse the article
    article.nlp() #Apply Natural Language Processing (NLP)
    corpus = article.text #Store the article text into corpuw
    text = corpus
    sent_tokens = nltk.sent_tokenize(text)# txt to a list of sentences
    robo_response='' #Create an empty response for the bot
    sent_tokens.append(user_response) #Append the users response to the list of sentence tokens
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    score = flat[-2]
    if(score==0):
        robo_response=robo_response+"I apologize, I don't understand."
    else:
        robo_response = robo_response+sent_tokens[idx]
        sent_tokens.remove(user_response)
    return robo_response

def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

def chat2(user_response):
    #user_response=input()
    gi=filter(user_response)
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Bot: You're welcome!, Chat with you later !")
        else:
            if(greeting(user_response)!=None):
                print("Bot: "+greeting(user_response)+" how may i help you?")
            elif(gi!=None):
                print(gi)
            else:
                try:
                    try:
                        pk=("Bot: "+chatbot_query(user_response,0))
                    except:
                        pk=("bot2: "+chatbot_query(user_response,1))
                except:
                    print("bot3: "+response(user_response))
                if pk!="Bot: error":
                    print(pk)
                else:
                    print("bot3: "+response(user_response))
    else:
        print("Bot: Chat with you later !")

chat2(output)
