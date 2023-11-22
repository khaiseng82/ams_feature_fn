from django.urls import path
from . import views
from .views import opcua_data_view


urlpatterns = [
    path('',views.opcua_data_view,name="home"),
    # path('',opcua_data_view,name="opcua_data_view"),
    path('realtime',views.realtime,name="realtime"),
    path('mainams',views.mainams,name="mainams"),
    path('slaveams',views.slaveams,name="slaveams"),
    path('setData',views.set_data,name="setData"),
    


]
