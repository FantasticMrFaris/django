from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = "Rango says hey there partner! <a href='/rango/about/'>About</a>"
    #return HttpResponse(response)

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    
    context_dict = {'boldmessage': 'here is the about page.'}
    return render(request, 'rango/about.html', context=context_dict)  
