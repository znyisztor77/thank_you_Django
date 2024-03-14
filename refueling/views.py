from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Refuel
from . serializers import RefueSerializer
from django.shortcuts import redirect

from django.contrib.auth.models import AnonymousUser

@api_view(['GET'])
def getRefuels(request):
    if not isinstance(request.user, AnonymousUser):
        refuels = Refuel.objects.filter(user = request.user).order_by('-refuel_date')
        serialized = RefueSerializer(refuels, many = True)
        return Response(serialized.data)
    return Response({'message': 'User is undefiened'})

@api_view(['GET'])
def getFuel_Consuption(request):
    if isinstance(request.user, AnonymousUser):
        return Response({'message': 'User is undefiened'})

    refuels = Refuel.objects.filter(user = request.user).order_by('-refuel_date')


    if len(refuels)<2:
            return Response({'message': 'Not enogh data.'})

    
    last = refuels[0]
    before = refuels[1]    

    distance = last.distance_km - before.distance_km
    
    consuption = (last.petrol_amount_liter / before.distance_km)*100    
    return Response({'consuption': round(consuption, 1)})

@api_view(['POST'])
def saveNewRefuel(request):
    refuel = Refuel()
    refuel.user = request.user
    refuel.distance_km = request.POST['distance_km']
    refuel.petrol_amount_liter =request.POST['petrol_amount_liter']
    print(request.POST['refuel_date'])
    refuel.refuel_date = request.POST['refuel_date']
    refuel.save()

    return redirect('index')


