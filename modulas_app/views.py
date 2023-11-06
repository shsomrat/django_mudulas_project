from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def addinput(request):
    return render(request,'addinput.html')

def result(request):
    if request.POST['num1'] == "" or request.POST['num2'] == "":
        return render(request, 'addinput.html', {'inputerr': "Please correct the errors in the form."})
    else:
        value1 = int(request.POST['num1'])
        value2 = int(request.POST['num2'])
        return render(request, 'result.html', {'modulas': (value1 % value2)})
