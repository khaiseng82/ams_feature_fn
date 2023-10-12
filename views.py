from django.shortcuts import render
# Refer the opc_client.py file and call the OPCUAClient Class
from .opc_client import OPCUAClient
from django.views import View
import time
import datetime
import signal
import sys
#from opcua import Client
#import threading  # Add this line to import the threading module
#----Variable Declariation -----------------------------------------

session=None

ASM00_Flow_Id = "ns=3;i=16844032"
ASM00_Pressure_Id = "ns=3;i=16844544"
ASM00_Temperature_Id = "ns=3;i=16844288"
ASM00_AccumFlow_Id = "ns=3;i=16843776"

ASM01_Flow_Id = "ns=3;i=16848896"
ASM01_Pressure_Id = "ns=3;i=16849408"
ASM01_Temperature_Id = "ns=3;i=16849152"
ASM01_AccumFlow_Id = "ns=3;i=16848640"

#----- Vairable Declaration  ---------------------------------------

ASM00_Flow_Value = 0
ASM00_Pressure_Value = 0
ASM00_Temperature_Value = 0
ASM00_AccumFlow_Value = 0 

ASM01_Flow_Value = 0
ASM01_Pressure_Value = 0
ASM01_Temperature_Value = 0
ASM01_AccumFlow_Value = 0



# Define a list of node IDs to loop through
node_ids = [
    ASM00_Flow_Id, ASM00_Pressure_Id, ASM00_Temperature_Id, ASM00_AccumFlow_Id,
    ASM01_Flow_Id, ASM01_Pressure_Id, ASM01_Temperature_Id, ASM01_AccumFlow_Id
]




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


#------------------Fetch Data From OPC UA------------------------------------------

server_url = "opc.tcp://192.168.0.10:4840"
opcua_client = OPCUAClient(server_url)


'''
opcua_client.connect()
node_id = "ns=3;i=16844288"
node = opcua_client.client.get_node(node_id)
print(node)
value = node.get_value()
print("Variable Value:" ,value)

'''
#--------------------------------------------------------------------------------------

'''

try:
    opcua_client.connect()
    #session = opcua_client.create_session()
    #node_id = "ns=3;i=16849152"
    #node = opcua_client.client.get_node(node_id)
    ASM00_Flow_Data = opcua_client.client.get_node(ASM00_Flow_Id)
    ASM00_Pressure_Data = opcua_client.client.get_node(ASM00_Pressure_Id)
    ASM00_Temperature_Data = opcua_client.client.get_node(ASM00_Temperature_Id)
    ASM00_AccumFlow_Data = opcua_client.client.get_node(ASM00_AccumFlow_Id)


    ASM01_Flow_Data = opcua_client.client.get_node(ASM01_Flow_Id)
    ASM01_Pressure_Data = opcua_client.client.get_node(ASM01_Pressure_Id)
    ASM01_Temperature_Data = opcua_client.client.get_node(ASM01_Temperature_Id)
    ASM01_AccumFlow_Data = opcua_client.client.get_node(ASM01_AccumFlow_Id)


   
    
    while True:

        current_time = datetime.datetime.now()
        
        try:

            ASM00_Flow_Value = ASM00_Flow_Data.get_value()
            ASM00_Pressure_Value = ASM00_Pressure_Data.get_value()
            ASM00_Temperature_Value = ASM00_Temperature_Data.get_value()
            ASM00_AccumFlow_Value = ASM00_AccumFlow_Data.get_value()


            ASM01_Flow_Value = ASM01_Flow_Data.get_value()
            ASM01_Pressure_Value = ASM01_Pressure_Data.get_value()
            ASM01_Temperature_Value = ASM01_Temperature_Data.get_value()
            ASM01_AccumFlow_Value = ASM01_AccumFlow_Data.get_value()



            #value = node.get_value()
            # Print Value for cell base and RC Value

            print("Cell Base Flow Value:", ASM00_Flow_Value)
            print("Cell Base Pressure Value:", ASM00_Pressure_Value)
            print("Cell Base Temperature Value:", ASM00_Temperature_Value)
            print("Cell Base Accumulation flow  Value:", ASM00_AccumFlow_Value)
            print("CurrentTime:", current_time)


            print("RC Flow Value:", ASM01_Flow_Value)
            print("RC Pressure Value:", ASM01_Pressure_Value)
            print("RC Temperature Value:", ASM01_Temperature_Value)
            print("RC Accumulation flow  Value:", ASM01_AccumFlow_Value)
            print("CurrentTime:", current_time)

            session.close()
            opcua_client.disconnect()
            break





        except Exception as e:
            print("Error getting node value:", e)

        except KeyboardInterrupt:
            print("Ctrl + Break detected. Exiting...")
            sys.exit(0)


       
        
        time.sleep(10)  # Sleep for 0.5 ms (0.0005 seconds)

        
except Exception as e:
    print("Error connecting to OPC UA server:", e)

except ua.UaError as e:
        print(f"Error connecting to OPC UA server: {e}")
        time.sleep(10)    
    

finally:
    session.close()

'''


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
    
    context = {"opcua_data": ASM00_Pressure_Value}
    
    # Render the HTML template with the data from the node Value to home.html
    return render(request, "home.html", context)

