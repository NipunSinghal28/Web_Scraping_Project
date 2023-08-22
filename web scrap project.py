import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
import chromedriver_binary
import os
# 'requests' makes an http request for accessig a paticular webpage
# beautiful soup for parsin html
link='https://en.wikipedia.org/wiki/Mahatma_Gandhi'

def fun1A():
#extracting the html code of the webpage
    
    link='http://quotes.toscrape.com/'
    response1=requests.get(link)
    response2=response1.text
    print(response1)
    print(response2)
    fd=open('main1.txt','w',encoding='utf-8')
    fd.write(response2)
    fd=open('main1.html','w',encoding='utf-8')
    fd.write(response2)
    fd.close()

def fun1B():
#1. extracting complete html code
#2. html.parser to convert html to string/stuctured format
#   so that particular extraction could be done
#3. quote, author are in the span<> tag
#4. find all quotes in the webpage

    #extraction of complete data
    #---------------------
    link='http://quotes.toscrape.com/'
    response3=requests.get(link)
    response4=response3.text
    print(response3)
    print(response4)
    #---------------------
    
    response5=BeautifulSoup(response3.text,'html.parser')
    print(response5)    
    response6=response5.find_all('span')
    for i in response6:
       print(i.text[0:-1])

def fun1C():
#1. html.parser to convert html to string format
#   so that particular extraction could be done
#2. extract a particular quote and its author
#3. div<> is tag inside which 'class' is attribute
#4. span<> is tag inside which 'class' is attribute

    #extraction of data
    #------------------------
    link='http://quotes.toscrape.com/'
    response7=requests.get(link)
    response8=BeautifulSoup(response7.text,'html.parser')
    #------------------------
    print('-\-\-\-\-\-'*10)
    for j in response8.find_all('div', class_='quote'):
        print(j)
        print()
        print('------'*10)
        print('------'*10)
        
    response9=j.find('span', class_='text').text[1:-1]
    response10=j.find('small').text
    print(response9)
    print(response10)
    
def fun2A():
#1. extraction of whole data
#2. html.parser to collect data in structured format
#3. in html format, filtering data with li<> tag and class
#4. print title name and link to the book
    
    link='https://books.toscrape.com/catalogue/page-1.html'
    response1=requests.get(link)
    response2=response1.text
    print(response1)
    print(response2)
    response3=BeautifulSoup(response1.text,'html.parser')
    print(response3)
    response4=response3.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for i in response4:
        print('----')
        a=i.find_all('a')[-1].get('href')      #a-> link
        b=i.find_all('a')[-1].get('title')     #b-> title
        print(a,' || ',b)

def fun2B():
#1. extracting data
#2. reading csv file
#3. finding specific data
    
    import pandas as pd
    link='https://books.toscrape.com/catalogue/page-1.html'
    df=pd.read_csv('book.csv')
    print(df.head())
    for i in df['book_link']:
        response5=requests.get(link)
        response7=BeautifulSoup(response5.text,'html.parser')
        print(response7.find('ul',class_='breadcrumb'))
        break
    
def fun3A():
#1. extracts and converts data to structured format
#2. reads the heading from the wikipedia ie mahatma gandhi
    response1=requests.get(link)
    response2=BeautifulSoup(response1.text,'html.parser')
    print(response2)
    response3=response2.find('h1').text
    print(response3)

def fun3B():
#1. extracts and converts data to structured format
#2. extracts all paragraphs 
    response4=requests.get(link)
    response5=BeautifulSoup(response4.text,'html.parser')
    for i in response5.find_all('p'):
        response6=i.text
        print(response6)
        print('-----'*10)

def fun3C():
#1. writes all paragraphs into a text file
    response7=requests.get(link)
    response8=BeautifulSoup(response7.text,'html.parser')
    for i in response8.find_all('p'):
        response9=i.text
    f=open('mahatma gandhi.txt','w')
    f.write(response9)
    f.close()

def fun3D():
# creates a google link for the topic entered
    title=str(input('enter topic: ')).replace(' ','+')
    link='https://www.google.com/'+ title + 'wikipedia'
    print(link )

def fun4A():
#1. trying to directly access the youtube channel
#2. NOT PROVIDING ANY DATA
    
    link='https://www.youtube.com/@GeeksforGeeksVideos/videos'
    print('###error in directly accessing a private youtube channel!!!!\n\n')
    response1=requests.get(link)
    print(response1.text)
    response2=BeautifulSoup(response1.text,'html.parser')
    print(response2.text)

def fun4B():
#1. WEBDRIVER is a automated process to drive browser
#2. using selenium
    
    print('nipun')
    print(chromedriver_binary.chromedriver_filename)
    webdriver.Chrome('chromedriver')    

def fun5A():
#1. reads data from a csv file having very large amount of data
    
    import pandas as pd
    df=pd.read_csv('finals.csv')
    response1=df.head()
    print(response1)
    for i in df['tags']:
        print(i)
        break
def main():
#    fun1A()
#    fun1B()
#    fun1C()
#    fun2A()
#    fun2B()
#    fun3A()
#    fun3B()
#    fun3C()
#    fun3D()
#    fun4A()
#    fun4B()
#    fun5A()
main()

