from django.shortcuts import render

# Create your views here.
def references_db(request):
    return render(request, 'app_refcodes.html')
