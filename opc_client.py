
# opcua_client.py

from opcua import Client
# OPC UA Connection Class
class OPCUAClient:
    print("Is Instantianting")
   
    #Constructor for Argument to take in OPC UA URL
    def __init__(self, server_url):
        self.client = Client(server_url)
        self.client.session_timeout = 3600000
        #self.client.set_session_timeout(3600000)
      

        
    #Connection function 
    def connect(self):
        print("Is Connected")
        username = "admin"
        password = "admin"

        # Try to Connect
        try:

            self.client.set_user(username)
            self.client.set_password(password)

            self.client.connect()
            # If Successful Connect print  " Connected to OPC UA Server on the termainal"
            if self.client:
                print("Connected to OPC UA Server!")
        #Throw an error if there is an Exception
        except Exception as e:

            print("Error:", e)


        
       
    # Subscrubing to node,
    def subscribe_to_node(self, node_id, callback):
        print("Is Subscribing")
        # Get the Node ID
        node = self.client.get_node(node_id)
        # Get the Node ID Current Value
        #value = node.get_value()
        # Print the  Node ID Current Value
        #print("Variable Value:", value)
        #Call back function to detect changes of data
        subscription = self.client.create_subscription(1, callback)
        
        handle = subscription.subscribe_data_change(node)
        return handle
    # Disconnecting function
    def disconnect(self):
        print("Is Dsiconnecting")
        self.client.disconnect()
