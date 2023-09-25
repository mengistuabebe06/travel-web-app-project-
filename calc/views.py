from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Wengel'})
    # return HttpResponse("helloworld")
    # return JsonResponse({"name":"mengistu"})
def add(request):
    # num1 = request.GET['fnum']
    # num2 = request.GET['snum']
    num1 = request.POST['fnum']
    num2 = request.POST['snum']
    rs = int(num1) + int(num2)
    return render(request,'res.html', {'res': rs})