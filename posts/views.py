from django.shortcuts import render

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
def list_post(request):
    #
    return render(request, 'feed.html',{'posts': posts})