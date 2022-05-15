from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import IdeaForm


@login_required
def index(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = IdeaForm()

    context = {'form': form}
    return render(request, 'ideapublisher/index.html', context)
