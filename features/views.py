from django.shortcuts import render

# Create your views here.
from features.models import Refcode
from django.contrib.auth.decorators import login_required
from features.forms import NewRefcodeForm


@login_required
def references_db(request):
    profile = request.user.employeeprofile
    refcodes = list(Refcode.objects.all().order_by('ref_code'))
    if request.method == 'POST':
        form = NewRefcodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            refcode = Refcode.create()
            refcode.ref_code = data['ref_code']
            refcode.system_number = data['system_number']
            refcode.operation_number = data['operation_number']
            refcode.operation_name = data['operation_name']
            refcode.hmdescription = data['hmdescription']
            refcode.fix_action = data['fix_action']

            refcode.save()
            return redirect('reftable')


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
