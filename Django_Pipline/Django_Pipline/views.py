from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("greetinf to the server")
    return render(request,"index.html")


def analyze(request):
    #To bring the user's data from our website
    d_text = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    # print(d_text)
    # print(removepunc)
    if removepunc == "on":
        # analyzed = d_text
        punctuations = '''!@#$%/^&*()_+:?.><{"}|'''
        analyzed = ""
        for char in d_text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'removed puncuations', 'analyzed_text': analyzed}
        d_text = analyzed
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in d_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'UPPERCASE TEXT', 'analyzed_text': analyzed}
        d_text = analyzed
    

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(d_text):
                if not(d_text[index]) == " " and d_text[index + 1] == "  ":
                    analyzed = analyzed + char

        params = {'purpose': 'UPPERCASE TEXT', 'analyzed_text': analyzed}
        d_text = analyzed

    return render(request, 'analyze.html', params)


# def funx(request):
#     dict = {'name':"Yash", 'skills':"python.django"}
#     # return HttpResponse("3rd function of this file ")
#     return render(request, "index.html", dict)
