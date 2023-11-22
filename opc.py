# Refer the opc_client.py file and call the OPCUAClient Class
from .opc_client import OPCUAClient
from .database import dBConnect
import time
import datetime
import sys
import requests


#----Variable Declariation -----------------------------------------

session=None

ASM00_Flow_Id = "ns=3;i=16844032"
ASM00_Pressure_Id = "ns=3;i=16844544"
ASM00_Temperature_Id = "ns=3;i=16844288"
ASM00_AccumFlow_Id = "ns=3;i=16843776"
ASM00_Status_Id = "ns=3;i=16845056"

ASM01_Flow_Id = "ns=3;i=16848896"
ASM01_Pressure_Id = "ns=3;i=16849408"
ASM01_Temperature_Id = "ns=3;i=16849152"
ASM01_AccumFlow_Id = "ns=3;i=16848640"
ASM01_Status_Id = "ns=3;i=16849920"

#----- Vairable Declaration  ---------------------------------------

ASM00_Flow_Value = 0
ASM00_Pressure_Value = 0
ASM00_Temperature_Value = 0
ASM00_AccumFlow_Value = 0 
ASM00_Status_Value = 0 

ASM01_Flow_Value = 0
ASM01_Pressure_Value = 0
ASM01_Temperature_Value = 0
ASM01_AccumFlow_Value = 0
ASM01_Status_Value = 0 

server_url = "opc.tcp://192.168.0.10:4840"
#opcua_client = OPCUAClient(server_url)
global opcua_client
opcua_client = OPCUAClient(server_url)

def get_data():

    # requests.post("http://127.0.0.1:8000/setData", {
    #     "data": {
    #         "ASM00_Flow_Value": 0,
    #         "ASM00_Pressure_Value": 0,
    #         "ASM00_Temperature_Value": 0,
    #         "ASM00_AccumFlow_Value": 0,
    #         "ASM00_Status_Value": 0,
    #         "ASM01_Flow_Value": 0,
    #         "ASM01_Pressure_Value": 0,
    #         "ASM01_Temperature_Value": 0,
    #         "ASM01_AccumFlow_Value": 0,
    #         "ASM01_Status_Value": 0,
    #     }
    # })
    try:
        opcua_client.connect()
    # session = opcua_client.create_session()
    #node_id = "ns=3;i=16849152"
    #node = opcua_client.client.get_node(node_id)
        ASM00_Flow_Data = opcua_client.client.get_node(ASM00_Flow_Id)
        ASM00_Pressure_Data = opcua_client.client.get_node(ASM00_Pressure_Id)
        ASM00_Temperature_Data = opcua_client.client.get_node(ASM00_Temperature_Id)
        ASM00_AccumFlow_Data = opcua_client.client.get_node(ASM00_AccumFlow_Id)
        ASM00_Status_Data = opcua_client.client.get_node(ASM00_Status_Id)


        ASM01_Flow_Data = opcua_client.client.get_node(ASM01_Flow_Id)
        ASM01_Pressure_Data = opcua_client.client.get_node(ASM01_Pressure_Id)
        ASM01_Temperature_Data = opcua_client.client.get_node(ASM01_Temperature_Id)
        ASM01_AccumFlow_Data = opcua_client.client.get_node(ASM01_AccumFlow_Id)
        ASM01_Status_Data = opcua_client.client.get_node(ASM01_Status_Id)
    
        while True:

            current_time = datetime.datetime.now()
            
            try:

                ASM00_Flow_Value = ASM00_Flow_Data.get_value()
                ASM00_Pressure_Value = ASM00_Pressure_Data.get_value()
                ASM00_Temperature_Value = ASM00_Temperature_Data.get_value()
                ASM00_AccumFlow_Value = ASM00_AccumFlow_Data.get_value()
                ASM00_Status_Value = ASM00_Status_Data.get_value()


                ASM01_Flow_Value = ASM01_Flow_Data.get_value()
                ASM01_Pressure_Value = ASM01_Pressure_Data.get_value()
                ASM01_Temperature_Value = ASM01_Temperature_Data.get_value()
                ASM01_AccumFlow_Value = ASM01_AccumFlow_Data.get_value()
                ASM01_Status_Value = ASM01_Status_Data.get_value()

                dBConnect("CB", ASM00_Flow_Value, ASM00_Pressure_Value, ASM00_Temperature_Value, 
                    ASM00_AccumFlow_Value, ASM00_Status_Value, current_time)
                dBConnect("RC", ASM01_Flow_Value, ASM01_Pressure_Value, ASM01_Temperature_Value, 
                    ASM01_AccumFlow_Value, ASM01_Status_Value, current_time)


                #value = node.get_value()
                # Print Value for cell base and RC Value

                print("Cell Base Flow Value:", ASM00_Flow_Value)
                print("Cell Base Pressure Value:", ASM00_Pressure_Value)
                print("Cell Base Temperature Value:", ASM00_Temperature_Value)
                print("Cell Base Accumulation Flow Value:", ASM00_AccumFlow_Value)
                print("Cell Base Status Value:", ASM00_Status_Value)
                print("CurrentTime:", current_time)


                print("RC Flow Value:", ASM01_Flow_Value)
                print("RC Pressure Value:", ASM01_Pressure_Value)
                print("RC Temperature Value:", ASM01_Temperature_Value)
                print("RC Accumulation Flow Value:", ASM01_AccumFlow_Value)
                print("RC Status Value:", ASM01_Status_Value)
                print("CurrentTime:", current_time)

                requests.post("http://127.0.0.1:8000/setData", json={
                    "data": {
                        "ASM00_Flow_Value": ASM00_Flow_Value,
                        "ASM00_Pressure_Value": ASM00_Pressure_Value,
                        "ASM00_Temperature_Value": ASM00_Temperature_Value,
                        "ASM00_AccumFlow_Value": ASM00_AccumFlow_Value,
                        "ASM00_Status_Value": ASM00_Status_Value,
                        "ASM01_Flow_Value": ASM01_Flow_Value,
                        "ASM01_Pressure_Value": ASM01_Pressure_Value,
                        "ASM01_Temperature_Value": ASM01_Temperature_Value,
                        "ASM01_AccumFlow_Value": ASM01_AccumFlow_Value,
                        "ASM01_Status_Value": ASM01_Status_Value,
                    }
                })

                session.close()
                opcua_client.disconnect()
                break





            except Exception as e:
                print("Error getting node value:", e)

            except KeyboardInterrupt:
                print("Ctrl + Break detected. Exiting...")
                sys.exit(0)


           
            
            time.sleep(5)  # Sleep for 0.5 ms (0.0005 seconds)

        
    except Exception as e:
        print("Error connecting to OPC UA server:", e)

    except ua.UaError as e:
            print(f"Error connecting to OPC UA server: {e}")
            time.sleep(10)