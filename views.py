from django.shortcuts import render
# Refer the opc_client.py file and call the OPCUAClient Class
from .opc_client import OPCUAClient
from django.views import View
from opcua import Client

# Create your views here.
# Home Page website call function
def home(request):
	return render(request,'home.html',{}) 
   

# Real time Monitoring Website call function
def realtime(request):
	return render(request,'realtime.html',{})

# Main AMS Analytics Website call function
def mainams(request):
	return render(request,'mainams.html',{})

#Slave AMS Analytics Website call function

def slaveams(request):
	return render(request,'slaveams.html',{})





#------------------Fetch Data From OPC UA------------------------------------------



def opcua_data_view(request):
   
    # Assign opc.tcp://192.168.0.10:4840 OPC UA Address to server_url variable
    server_url = "opc.tcp://192.168.0.10:4840"  
     # Instantiate , create a new OPC connection object  from OPCUAClient Class , the new object instantiate is name opcua_client
    opcua_client = OPCUAClient(server_url)
    
    # Connect to the OPC UA server by calling the .connect function on the new object created from class OPCUAClient
    opcua_client.connect()
    
    
    # Define a callback to store the latest data
    latest_data = [None]  

    def data_change_callback(node, data):
        latest_data[0] = data  

    # Subscribe to the OPC UA node by calling the .subscribe_to_node function on the new object created from class OPCUAClient
    opcua_client.subscribe_to_node("ns=3;i=16844288", data_change_callback)

    # Pass the latest data to the template
    context = {"opcua_data": latest_data[0]}

    # Render the HTML template with the data from the node Value to home.html
    return render(request, "home.html", context)
