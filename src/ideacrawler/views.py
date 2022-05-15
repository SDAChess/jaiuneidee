from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from ideacrawler.models import Idea

def crawler(request):
    context = {}
    context['ideas'] = Idea.objects.all()
    return render(request, 'ideacrawler/crawler.html', context)


def idea(request, idea_id):
    # template = loader.get_template('ideacrawler/index.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
    pass


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'ideacrawler/signup.html', context)

