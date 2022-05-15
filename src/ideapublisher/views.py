from django.shortcuts import redirect, render

from .forms import IdeaForm


def index(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = IdeaForm()

    context = {'form': form}
    return render(request, 'ideapublisher/index.html', context)
