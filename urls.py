from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('',views.opcua_data_view,name="opcua_data_view"),
    path('realtime',views.realtime,name="realtime"),
    path('mainams',views.mainams,name="mainams"),
    path('slaveams',views.slaveams,name="slaveams"),


]
