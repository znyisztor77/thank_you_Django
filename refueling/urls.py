from django.urls import path
from . import views

urlpatterns= [

    path('refuels/', views.getRefuels),
    path('consuption/', views.getFuel_Consuption),
    path('new/', views.saveNewRefuel, name ="new-refuel"),
]