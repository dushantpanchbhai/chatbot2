import sys
import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import spacy
import random
output=sys.argv[1]

def chatbot_query(question, index=0):
    nlp = spacy.load('en_core_web_sm')
    q1=nlp(question)
    #ent=[i.text for i  in q1.ents ]
     #print(ent)
    q=[i for i in q1]
    #print(q)

    error = "sorry, i can't understand what are you asking"
    result = ''


    search_result_list = list(search(question, tld="co.in", num=10, stop=3, pause=1))
    #search_result_list = list(search(question, tld="co.in",start=2,num=10, stop=10, pause=2))

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
    #article_text = article_text.replace('\n', '')
    first_sentence = article_text.split('\n')
    #first_sentence = first_sentence.remove('')
    while('' in first_sentence) :
        first_sentence.remove('')
    #print(first_sentence)
    k=nlp(first_sentence[0])
    arr=[]
    list2=[]
    for l in q:
        arr.append(str(l).lower())
    for j in k:
        list2.append(str(j).lower())
    check = any(item in arr for item in list2)

    if check==True:
        second=first_sentence[1]
        first_sentence = first_sentence[0]
        chars_without_whitespace = second.translate(
            { ord(c): None for c in string.whitespace }
        )
    else:
        first_sentence = first_sentence[1]

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
    #result = first_sentence
    return result



def greeting(sentence):
    GREETING_INPUTS = ["hi", "hello",  "hola", "greetings",  "wassup","hey","hii","hiii"]
#Greeting responses back to the user
    GREETING_RESPONSES = ["hi ","hey ","hey","Hello ","Hello Human"]
    #Function to return a random greeting response to a users greeting
   #If user's input is a greeting, return a randomly chosen greeting response
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def chat(user_response):
    flag=True
    #print("ChatBot: I am Electronic BOT for short. I will answer your queries about Electronics. If you want to exit, type Bye!")
    while(flag==True):
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                print ("Bot: You're welcome!, Chat with you later !")
            else:
                if(greeting(user_response)!=None):
                    print ("Bot: "+greeting(user_response)+" how may i help you?")
                else:
                    #try:
                    #    print ("Bot: "+chatbot_query(user_response,0))
                    #except:
                        print ("bot2: "+chatbot_query(user_response,1))
        else:
            flag=False
            print ("Bot: Chat with you later !")
def chat2(user_response):
    if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                print ("Bot: You're welcome!, Chat with you later !")
            else:
                if(greeting(user_response)!=None):
                    print ("Bot: "+greeting(user_response)+" how may i help you?")
                else:
                    try:
                        print ("Bot: "+chatbot_query(user_response,0))
                    except:
                        print ("bot2: "+chatbot_query(user_response,1))
    else:
        flag=False
        print ("Bot: Chat with you later !")
chat2(output)
