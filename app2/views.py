from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':60 , 'b':85 , 'c':87}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'shamsheer'}
    return render(request,'a2_second.html',d)