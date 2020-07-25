from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def references_db(request):
    return render(request, 'features/reference.html')

@login_required
def list_post(request):
    #
    return render(request, 'feed.html')

@login_required
def status(request):
    #
    return render(request, 'feed.html')

@login_required
def teamz(request):
    #
    return render(request, 'feed.html')

@login_required
def manuals(request):
    #
    return render(request, 'feed.html')

@login_required
def vocabulary(request):
    #
    return render(request, 'feed.html')