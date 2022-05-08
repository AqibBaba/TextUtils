# I have created this file - aqib

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("hello")
    # params={'name':'aqib','place':'srinagar'}
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # checking check box values

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-+[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Getting everything in uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed extra lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if charcount=='on':
        count=0
        for char in djtext:
            count=count+1
        params = {'purpose': 'Getting characters length', 'analyzed_text': f"the number of characters you entered are :- {count}"}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(removepunc!='on' and extraspaceremover!='on' and newlineremover!='on' and fullcaps!='on' and charcount!='on'):
        return HttpResponse("please select any option")

    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

# def about(request):
#     return HttpResponse("<h1>hello this is about page</h1>")
#
# def task(request):
#     path = r"C:\Users\user\PycharmProjects\textutils\textutils\textutils\1.txt"
#     file = open(path, "r")
#     return HttpResponse(file.read())
#
# def navigator(request):
#     return HttpResponse('''<a href="https://www.youtube.com"> goto youtube site </a>''')