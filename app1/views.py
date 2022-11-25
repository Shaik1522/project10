from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':10 , 'b':20}
    return render(request,'a1_first.html',d)



def a1_second(request):
    d={'a':50 , 'b':60 , 'c':70}
    return render(request,'a1_second.html',d)