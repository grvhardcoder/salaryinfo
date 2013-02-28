from django.http import  HttpResponse
#from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.cleaned_data('username')
            form.cleaned_data('email')
            form.cleaned_data('password1')
            form.save()
        return HttpResponse('registered.html')
    else: 
        t = loader.get_template('signup.html')
        cform = SignupForm()
        c = RequestContext (request, {'form' : cform,})
        return HttpResponse(t.render(c))      
                
                
