from django.shortcuts import render

# Create your views here.

def buildWebsite(request):
    #import os
    #return_val = os.system("manage.py build")
    import subprocess
    return_val = subprocess.run("manage.py build", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    err = return_val.stderr
    out = return_val.stdout
    return_code = return_val.returncode
    context = {
        'return_val' : return_val,
        'return_code' : return_code,
        'out' : out,
        'err' : err,
    }
    return render(request, 'builder/build_website.html', context)