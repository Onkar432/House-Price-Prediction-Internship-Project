from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def Base(requst):
    return render(requst,'Base.html')

def predict(request):
 return render(request,'predict.html')

def result(request):
 return render(request,'predict.html')