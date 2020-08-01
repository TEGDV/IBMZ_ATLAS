from django.shortcuts import render

# Create your views here.
from features.models import Refcode
from django.contrib.auth.decorators import login_required

@login_required
def references_db(request):
    profile = request.user.employeeprofile
    refcodes = list(Refcode.objects.all().order_by('ref_code'))
    print(refcodes)
    return render(request, 'features/reference.html', {
    'profile' : profile,
    'refcodes' : refcodes
        }
     )

@login_required
def list_post(request):
    #
    profile = request.user.employeeprofile
    return render(request, 'features/blog.html' , { 'profile' : profile })

@login_required
def status(request):
    #
    profile = request.user.employeeprofile
    return render(request, 'features/status.html', { 'profile' : profile })

@login_required
def teamz(request):
    #
    profile = request.user.employeeprofile
    return render(request, 'features/teamz.html', { 'profile' : profile })

@login_required
def manuals(request):
    #
    profile = request.user.employeeprofile
    return render(request, 'features/manuals.html', { 'profile' : profile })

@login_required
def vocabulary(request):
    #
    profile = request.user.employeeprofile
    return render(request, 'features/vocabulary.html', { 'profile' : profile })
