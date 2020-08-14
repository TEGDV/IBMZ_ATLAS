from django.shortcuts import render, redirect

# Create your views here.
from features.models import Refcode
from django.contrib.auth.decorators import login_required
from features.forms import NewRefcodeForm


@login_required
def references_db(request):
    try:
        profile = request.user.employeeprofile
        refcodes = list(Refcode.objects.all().order_by('pk'))
        form = NewRefcodeForm(request.POST)

    # ADD INSTANCE
    
        if 'query' in request.GET:
            refcodes = list(Refcode.objects.filter(ref_code__contains=request.GET['query']))
            if len(refcodes) == 0:
                refcodes = list(Refcode.objects.all().order_by('pk'))
                return render(request, 'features/reference.html', {
                    'profile' : profile,
                    'refcodes' : refcodes,
                    'user': request.user,
                    'form': form,
                    'error' : 'Any result for this query',
                        }
                )        
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
    except:
                form = NewRefcodeForm()
                return render(request, 'features/reference.html', {
                'profile' : profile,
                'refcodes' : refcodes,
                'user': request.user,
                'form': form,
                'error': 'duplicated refcode'
                    }
                )
        



    return render(request, 'features/reference.html', {
    'profile' : profile,
    'refcodes' : refcodes,
    
        }
     )

@login_required
def deleteRefcode(request):
    profile = request.user.employeeprofile
    refcodes = list(Refcode.objects.all().order_by('ref_code'))
    # DELETE INSTANCE 
    try:
        if request.method == 'POST':
            refcode_pk = request.POST['pk']
            instance = Refcode.objects.get(id=refcode_pk)
            instance.delete()
        return redirect('reftable')
        
    except:
            return render(request, 'features/reference.html', {
                'profile' : profile,
                'refcodes' : refcodes,
                'error' : 'Something wrong with delete'
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
