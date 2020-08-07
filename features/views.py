from django.shortcuts import render, redirect

# Create your views here.
from features.models import Refcode
from django.contrib.auth.decorators import login_required
from features.forms import NewRefcodeForm


@login_required
def references_db(request):
    profile = request.user.employeeprofile
    refcodes = list(Refcode.objects.all().order_by('ref_code'))
    form = NewRefcodeForm(request.POST)
    if request.method == 'POST':
        form = NewRefcodeForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            refcode = Refcode(
                
                ref_code = data['ref_code'],
                system_number = data['system_number'],
                operation_number = data['operation_number'],
                operation_name = data['operation_name'],
                hmdescription = data['hmdescription'],
                fix_action = data['fix_action'],
                created_by = request.user
            )

            refcode.save()
            return redirect('reftable')
        else:
            form = NewRefcodeForm()
            return render(request, 'features/reference.html', {
            'profile' : profile,
            'refcodes' : refcodes,
            'user': request.user,
            'form': form,
            'error': 'something wrong with POST'
                }
             )


    return render(request, 'features/reference.html', {
    'profile' : profile,
    'refcodes' : refcodes,
    
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
