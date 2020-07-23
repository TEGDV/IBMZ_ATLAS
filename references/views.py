from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def references_db(request):
    return render(request, 'references/reference.html')
