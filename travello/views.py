from django.shortcuts import render
from travello.models import Destination

# Create your views here.
def index(request):
    
    # dest1 = Destination()
    # dest1.name = "mengistu"
    # dest1.img = "destination_1.jpg"
    # dest1.price = 456
    # dest1.desc = "adadasdasdadasdadsada"
    # dest1.offer = False
    
    # dest2 = Destination()
    # dest2.name = "Abebe"
    # dest2.img = "destination_2.jpg"
    # dest2.price = 789
    # dest2.desc = "adadasdasdadasdadsada"
    # dest2.offer = True
    
    # dest3 = Destination()
    # dest3.name = "Legesse"
    # dest3.img = "destination_3.jpg"
    # dest3.price = 213
    # dest3.desc = "adadasdasdadasdadsada"
    # dest3.offer = False
    
    # dests = [dest1,dest2,dest3]
    dest = Destination.objects.all().values()
    
    return render(request,'index.html', {'dests':dest})