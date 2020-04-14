from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return render(request, 'hello.html')
# The HttpResponse function will send a page with the desired string

def home(request):
    return render(request, 'home.html')
# The render function will send the user to the homepage of the website
#since homepage itsn't formatted, we do that in our home.html file

def count(request):
    fulltext = request.GET['fulltext'] # This request.GET is how we can get the info
    #from the 'fulltext' that we called the textbody in count.html and pass it into
    #a useable variable
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'sortedlist': sortedlist}) 
    # This will send the information that was gathered in the variable fulltext 
    # and send it to count.html

def what(request):
    return render(request, 'what.html')

def secret(request):
    return render(request, 'secret.html')

def about(request):
    return render(request, 'about.html')

