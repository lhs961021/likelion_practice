from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):

    text = request.GET['sentence']

    textList = text.split()

    wordDict = {}

    for word in textList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, "result.html", {'fulltext':text, 'count':len(textList), 'wordDict':wordDict.items})