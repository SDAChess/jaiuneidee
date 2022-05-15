from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from ideacrawler.models import Idea


def crawler(request):
    context = {'ideas': Idea.objects.all()}
    return render(request, 'ideacrawler/crawler.html', context)


def idea(request, idea_id):
    idea = Idea.objects.get(pk=idea_id)
    return render(request, 'ideacrawler/idea.html', {'idea': idea})


def upvote(_, idea_id):
    idea = Idea.objects.get(pk=idea_id)
    idea.upvotes += 1
    idea.save()

    return redirect('/')


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
