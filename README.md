# Project-name

### Team name: Finders

## Team members
* Member-1 : Dushant Panchbhai 
  Email : dushantrpanchbhai@gmail.com
* Member-2 : Mithilesh Patil
  Email : mithileshpatil2000@gmail.com
  
## Mentors
* Mentor-1 : Parth
* Mentor-2 : Priyesh Vakharia

## Description
In this project we had made a website constisting of chatbot functioning.

this chatbot model is based on the web scrapping. whatever the question we give to the chatbot, the chatbot do a google search based on the topic.

```
        from googlesearch import search
        search_result_list = list(search(question, tld="co.in",start=0,num=10, stop=10, pause=2))
```

after doing google search the bot will pickup the first hyperlink.extract the whole text and do the natural language processing it and display the appropriate result based on it.
```     #getting page of particular hyperlink. here index means hyperlink number
        page = requests.get(search_result_list[index])
        tree = html.fromstring(page.content)
        #prints the whole .html script
        soup = BeautifulSoup(page.content, features="lxml")
        
        article_text = ''
        article = soup.findAll('p')
        
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        first_sentence = article_text.split('\n')
        #first_sentence consist of list of text of the webpage seprated by newline. 
```

we had also embedded some greeting syntax file which will deal with some greeting and natural conversaation questions like: who are you? , tell me a joke etc. 
```
        def filter(question):
            # path1 is the address of greeting.yml file which consist of all the greeting syntax.
            a_yaml_file = open(path1)
            par = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
```
so, the model will first check if the entered question is greeting type or not. if the question is not greeting type then it will show result according to webscrapping

* GitHub repo link: [Link to repository](https://github.com/dushantpanchbhai/chatbot2.git)
* Drive link: [Drive link here](https://drive.google.com/)

## Technology stack

1. Python
2. Django
3. Natural language processing libraries include Spacy,nltk.
4. html,css and javascript.

## Project Setup
1. clone the project from the github [link](https://github.com/dushantpanchbhai/chatbot2.git)
2. open terminal and create a virtual environment
```
      pip install virtualenv
      virtualenv [virtual environment name]
      *to enter virtual environment syntax is:
      source (environment name)/bin/activate
      NOTE: you should be in the folder containing environment while doing this.
```
3. install the requirement.txt file present in the folder in that environment
```
      syntax: pip install -r requirements.txt
```
4. In terminal enter following command to install 'en_core_web_sm'.
```
        python -m spacy download en_core_web_sm
```
>Include your project setup basics here. Steps for how someone else can setup your project on their machine. Add any relevant details as well.

## Usage
>Steps to run your project once its setup. If you have an app or website, list how the user can go about using it.

## Applications
>How can your project do its part in solving a real-life problem? What are its possible applications? Decribe here.

## Future scope
>Mention ways in which the project can be improved and built upon in the future.

## Screenshots
Add a few screenshots here to give the viewer a quick idea of what your project looks like. After all, a picture speaks a thousand words.

You'll have to link the screenshots from your drive folder here.

![Screenshot alt text](https://edtimes.in/wp-content/uploads/2018/09/NikeMeme10-640x633.jpg "Here is a screenshot")

Use this template as a guide for writing your documentation. Feel free to customize and adapt it for you project.
For more Markdown syntax help, visit [here](https://www.markdownguide.org/basic-syntax/)
