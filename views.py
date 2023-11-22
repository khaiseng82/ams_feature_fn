from django.shortcuts import render
# Refer the opc_client.py file and call the OPCUAClient Class
from .opc_client import OPCUAClient
from django.views import View
from django.http import HttpResponse
from .database import dBConnect
import time
import datetime
import signal
import sys
import mysql.connector
import json


#from opcua import Client
#import threading  # Add this line to import the threading module
#----Variable Declariation -----------------------------------------

data = { "opcua_data": {} }




#Killing the OPC UA Session -------------------------------------------
def handle_termination_signal(sig, frame):
    global session
    if session is not None:
        print("Closing OPC UA session...")
        session.close()
    sys.exit(0)
# Register the signal handler for Ctrl + Break (Ctrl + C)
#signal.signal(signal.SIGINT, handle_termination_signal)

# Create your views here.
# Home Page website call function
def home(request):
    return render(request,'home.html',{})
    

	 
    #return render(request, 'home.html', context)
    '''
    opcua_data = opcua_data_view(request)
    context = {
        'opcua_data': opcua_data,
    }
    '''
   

# Real time Monitoring Website call function
def realtime(request):
	return render(request,'realtime.html',{})

# Main AMS Analytics Website call function
def mainams(request):
	return render(request,'mainams.html',{})

#Slave AMS Analytics Website call function

def slaveams(request):
	return render(request,'slaveams.html',{})




#-------------------------------------------------------------------------------------------

#print(node.get_value().cpu_usage_idle)

'''
latest_data = [None] 
def data_change_callback(node, data):
        #latest_data[0] = data 
        latest_data[0] = data.Value.Value  # Assuming Value is the attribute you want to retrieve
        print("Latest Data:", latest_data[0])

handle = opcua_client.subscribe_to_node("ns=3;i=16844288", data_change_callback)

def check_for_data_changes():
        while True:
            pass  # You can add a sleep here to control the update rate


data_check_thread = threading.Thread(target=check_for_data_changes)
data_check_thread.start()
'''

def opcua_data_view(request):
    global data

    print(data)
   
    # Assign opc.tcp://192.168.0.10:4840 OPC UA Address to server_url variable
   # server_url = "opc.tcp://192.168.0.10:4840"  
     # Instantiate , create a new OPC connection object  from OPCUAClient Class , the new object instantiate is name opcua_client
   
   # opcua_client = OPCUAClient(server_url)
    
    # Connect to the OPC UA server by calling the .connect function on the new object created from class OPCUAClient
   # opcua_client.connect()
    
    '''
    # Define a callback to store the latest data
    latest_data = [None]  

    def data_change_callback(node, data):
        latest_data[0] = data  

    # Subscribe to the OPC UA node by calling the .subscribe_to_node function on the new object created from class OPCUAClient
    opcua_client.subscribe_to_node("ns=3;i=16844288", data_change_callback)

    # Pass the latest data to the template
    context = {"opcua_data": latest_data[0]}
    '''
    
    # context = {"opcua_data": ASM00_Pressure_Value}
    
    # Render the HTML template with the data from the node Value to home.html
    return render(request, "home.html", data)

def set_data(request):
    global data

    opcuaData = request.body
    # del opcuaData["csrfmiddlewaretoken"]
    print(json.loads(opcuaData)["data"])

    data["opcua_data"] = json.loads(opcuaData)["data"]

    return HttpResponse("Hello World")