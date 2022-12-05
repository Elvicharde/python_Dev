# mud_client.py
# Author:
# Description: This is a sample mud game client for playing mud games hosted on the connected server.
#              This client can be duplicated for multi-user connection to the same or different servers.

# importing required libraries
import socket, pickle

class CLIENT():
    ''' This creates a client object for playing a MUD game on the connected server.
    '''
    def _init_(self):
        ''' This is the constructor for the client object. It instantiates an instance of the client and 
            calls the relevant methods for connecting to the desired server.
        '''
        # welcome_message = f"{'Hello! Welcome to this MUD game client.'}"
        # self.greet_user(welcome_message)
        # self.connect()
    
    def greet_user(self, message):
        print("\n")
        print(f"{message:^120}")
        print("\n\n")

    def connect(self):
        ''' This method connects directly to a server using the supplied HOST address and PORT.
        '''
        HOST_ADDRESS = input("[CONNECT] Enter Server address e.g. localhost or 127.0.0.1\n\n>> ")
        PORT = int(input("\n\n[CONNECT] Port e.g. 8080\n\n>> "))
        HEADER_LENGTH = 10
        # connecting to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCP_CLIENT:
            TCP_CLIENT.connect((HOST_ADDRESS, PORT))
            response_length = int(pickle.loads((TCP_CLIENT.recv(HEADER_LENGTH))))    # Getting the expected stream size.
            full_response = pickle.loads((TCP_CLIENT.recv(response_length)))    # Setting buffer size 
        
        render(full_response)


    def render(self, response):
        print(response)

    def request_handler():
        pass


def main():
    client = CLIENT()
    welcome_message = f"{'Hello! Welcome to this MUD game client.'}"
    client.greet_user(welcome_message)
    client.connect()


if __name__ == '__main__':
    main()



