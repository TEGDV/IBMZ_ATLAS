from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

posts = [
    {
        'name': 'pedro',
    },
    {
        'name': 'mario',
    },
    {
        'name': 'julio',
    },
]
@login_required
def list_post(request):
    #
    return render(request, 'feed.html',{'posts': posts})