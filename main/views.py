from django.shortcuts import render
from . import readEmail
from django.views.decorators.clickjacking import xframe_options_exempt
from urlextract import URLExtract


@xframe_options_exempt
def home(request):
    readEmail.read()
    f = open('res.json', 'r')
    lname = []
    for i in f.readlines():
        src = eval(i)
        extractor = URLExtract()
        if "Event::" in src['message']:
            continue
        urls = extractor.find_urls(src['message'])
        for i in urls:
            src['message'] = src['message'].replace(i, "")
        lname.append((src['message'], urls))
    return render(request, 'basic.html', {'list': lname})


@xframe_options_exempt
def homie(request):
    readEmail.read()
    f = open('res.json', 'r')
    lname = []
    for i in f.readlines():
        src = eval(i)
        extractor = URLExtract()
        a = src['message']
        title = ""
        body = ""
        if "Event::" in a:
            title = a[a.index('Title:')+6:a.index('Body:')]
            body = a[a.index('Body:')+5::]
            urls = extractor.find_urls(src['message'])
            print(urls)
            body = body.replace(urls[0], "")
            for i in urls:
                src['message'] = src['message'].replace(i, "")
            lname.append((title, body, urls[0]))
        return render(request, 'event.html', {'list': lname})
