from django.urls import path
from  . import views
urlpatterns = [
    path('areas',views.areas,name ='areas')
]
