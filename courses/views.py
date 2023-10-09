from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def wellcome_courses(request):
    #return HttpResponse("<h2><b>Wellcome to yours Courses</b></h2>")
    return render(request,'home.html')