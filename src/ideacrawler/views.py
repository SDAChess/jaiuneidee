from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_protect


def index(request):
    template = loader.get_template('ideacrawler/crawler.html')
    context = {}
    return HttpResponse(template.render(context, request))


def idea(request, idea_id):
    # template = loader.get_template('ideacrawler/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
    pass


@csrf_protect
def signup(request):
    #if request.method == "POST":
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        username = form.cleaned_data.get('username')
    #        raw_password = form.cleaned_data.get('password1')
    #        user = authenticate(username=username, password=raw_password)
    #        login(request, user)

    #        return redirect('/')
    #else:
    #    form = UserCreationForm()

    #return render(request, 'ideacrawler/signup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('OUIIIIIIIIII')
            return redirect('/')
        else:
            print('INVALID')
    else:
        form = UserCreationForm()

    context = {
            'form': form
            }

    return render(request, 'ideacrawler/signup.html', context)

