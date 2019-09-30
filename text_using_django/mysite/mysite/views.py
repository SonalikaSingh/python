#first file

# from django.http import HttpResponse
#
# def index(request):
#     return  HttpResponse('''<a href="https://www.tutorialspoint.com/python/python_data_science_introduction.htm">youtube</a>''')
#
# def about(request):
#     return  HttpResponse("hello Sona")

#second

from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def  analyze(request):

    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    newlineremove = request.POST.get('newlineremover', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaveremover = request.POST.get('extraspaveremover', 'off')
    count = request.POST.get('countLetters', 'off')

    if removepunc=='on':
        analyzed = ""
        punctuations="...::::;;;"

        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char

        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)



    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()

        params = {'purpose': 'capitilized', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if extraspaveremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char

        params = {'purpose': 'remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)



    if count == 'on':
        c = len(djtext)

        #for char in djtext:
            #c+=1

        #params = {'purpose': 'count letters', 'analyzed_text': c}
        print(HttpResponse("count is",c))
        #djtext = analyzed
        #return render(request, 'analyze.html', params)



    if newlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char.upper()

        params = {'purpose': 'newlineremove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if newlineremove == 'off' and extraspaveremover=='off' and fullcaps=='off'and removepunc=='off':
        return HttpResponse("error")
    return render(request, 'analyze.html', params)

# def  capitilize(request):
#     return HttpResponse("capitilize")
#
# def  newlineremove(request):
#     return HttpResponse("new line remove")
#
# def  spaceremover(request):
#     return HttpResponse("spaceremover")
#
# def  countchar(request):
#     return HttpResponse("countchar")
#
