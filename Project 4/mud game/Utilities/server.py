# mud_game_server.py
# Author:
# Description: This application initializes a mud game server. Due to the constraints of this development,
#               this server does not support multiplayer mode. However, it can accept multiple connections 
#               from individual players.
#               This application will be configured and handled mainly from the main.py application which 
#               sets the host server address (default is localhost i.e 127.0.0.1) and the connection port.

# importing all relevant libraries
import socket, threading, json, pickle, os

class SERVER():
    ''' This creates a server object for streaming an associated MUD game to one or more connected clients.
        Although this server allows multiple connections (max-connection is specified in the setup config file), 
        the connected MUD game engine does not support multi-player gaming experience: it is a multi-user game
        configuration.
        Initialize this server with a server_config.json file, which can be edited to modify the behaviour of the 
        instantiated server object.
    '''

    def __init__(self, config_path, start = False):
        ''' This is the constructor for this server class. It accepts a configuration file and assigns values to 
            relevant properties i.e. ipaddress, port, maximum connection.    
        '''
        try:
            self.PATH = os.getcwd()
            server_config = self.PATH + config_path
            credentials = self.PATH + '\\Database\\credentials.json'

            with open (server_config, 'r') as configuration, open (credentials, "r") as credentials_file:
                config = json.load(configuration)
                self.CLIENTS_CREDENTIALS = json.load(credentials_file)

            for parameter, value in config.items():
                setattr(self, parameter, value)
            
        except:
            print("\n[ERROR 2.1]: An error occured! Please check that the configuration file is correctly specified\n")
            return None
        else:
            print("\nServer configured successfully!\n")
            
            if start:
                self.start()    # start the server with the specified configuration

    def start(self):
        ''' This method starts the server with the passed configuration and specifications. Once the server is started,
            it passes control to the client handler for managing the various users that connect to the server.
        '''
        try:
            TCP_SERVER = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            TCP_SERVER.bind((self.HOST, self.PORT))    # binding the server to specified network parameters
            TCP_SERVER.listen(self.MAX_CONNECTION)    # This listens for incoming connections with a limit of 
                                                    # acceptable connections specified by MAX_CONNECTION   
        except:
            print('[ERROR 2.2]: Please ensure the server is configured correctly before starting!\n')
        
        else:
            print(f"\n{' MUD GAME SERVER STARTED ':^100}\n{'-'*35:^100}")
            print(f'\n\nlistening for connections on {self.HOST}:{self.PORT} ...\n\n')

            # setting up a forever-loop for connections and client-server sessions
            while True:
                session, client_address =  TCP_SERVER.accept()    # accept connection on server socket
                
                # implementing threading for each client connection to the server
                with threading.Thread(target=self.client_handler, args=(self, session, client_address)) as thread:
                    thread.start()    # starting each thread

    def client_handler(self, session, client_address):
        ''' This method accepts and handles multiple client connections. It establishes individual sessions
            per client on separate threads via the #threading module, and it verifies client credentials before
            loading up the MUD game engine.
        '''
        # A connection must already established before this method can be called, so the self.connected property 
        # is now true
        self.CONNECTED = True
        print(f"\nClient [{client_address}] connected\n")
        print(f'\nTotal active connections: {threading.activeCount() - 1} client(s)\n')

        while self.CONNECTED:
            while not self.AUTHENTICATED:
                # send a response to client for authentication with valid credentials or create a new one.
                # login
                # register
                self.authenticate(session)
            
            # If authentication is complete, pass control to the game engine.


    def authenticate(self, session):
        ''' This method communicates an authentication requirement to the client. It only takes a client 
            credential and validates against the database of registered users.
        '''
        message = {'msg':'CRED_REQ', 'msg_type': 0}
        client_request = self.send_response(session, message)   # this should contain credentials and 
                                                                # an authentication type
        username = client_request['credentials']['username']
        password = client_request['credentials']['password']

        if client_request['authentication'] == 'register':
            auth_response = self.register(username, password)
        # Otherwise, login
        auth_response = self.login(username, password)

        return auth_response

    def register(self, username, password):
        ''' This method registers a client account as a dictionary containing username and password.
        '''
        if not self.CLIENTS_CREDENTIALS.has_key(username):
                try:
                    new_credentials = {username:password}
                    self.CLIENTS_CREDENTIALS.update(new_credentials) 
                except: 
                    # print("\nNew user registration failed\n")
                    message = {'msg':'CRED_REQ', 'msg_type': 2}       
                else:
                    # print("\nNew user registration successful\n")
                    credentials_path = self.PATH + '\\Database\\credentials.json'

                    with open (credentials_path, 'w') as credentials_file:
                        json.dump(self.CLIENTS_CREDENTIALS, indent = 2)    # update the credentials file
                        message = {'msg':'CRED_REQ', 'msg_type': 1}

        # print('\nUser already exists!\n')
        message = {'msg':'CRED_REQ', 'msg_type': 3}
        return message

    def login(self, username, password):
        ''' This tries to login a user by checking the recieved credentials against the credentials file
        '''
        if self.CLIENTS_CREDENTIALS[username] == password:
            self.AUTHENTICATED = True
            # print('\nLogin Successful!\n')
            message = {'msg':f'Login Successful!\nHello, {username}. Welcome to this MUD GAME!!!', 'msg_type': 4}
            return message

    
    def response_builder(self, srv_msg):
        ''' This method sets up parts of the server response object for interacting with the client. The response object
            will be a Pickle (essentially a binary representation of a python object) that will contain a META_INFO
            and the server message. The META_INFO is meant to inform the client of the expected stream size, for
            its message buffer, and a MSG_TYPE for deciding how to render/handle the server response on the client.
        '''
        MAX_LENGTH = 10    # This corresponds to the byte size required to represent message length and type
                           # up to the exponential power i.e 1,000,000,000. No message can exceed this!
        
        srv_msg = pickle.loads(srv_msg)    # server message is now a binary representation

        META_INFO = f'{len(srv_msg)}'
        response = bytes(f'{META_INFO:<MAX_LENGTH}', 'utf-8') + srv_msg 
        return response
        
    def request_parser(self, session):
        ''' This method recieves a request object from the client, parses the request into a format that can be 
            implemented by the respective server method.
        '''
        MAX_LENGTH = 10    # This is implemented on the client side as well for transmittin META DATA
        request_size = int(session.recv(MAX_LENGTH).decode('utf-8'))  # Recieving the message length info via META data                                                                 # of bytes as a HEADER information.
        request = pickle.loads(session(request_size))['message']

        # disconnect based on client request using 'q, x, quit or exit'
        if request['msg'].lower() in ['q', 'x', 'quit', 'exit']:
            self.CONNECTED = False
            session.close()

        return request
    
    def get_response(self, session, message):
        '''This method sends the required message to the client after the response is built. It returns a 
            parsed response from the client for further processing.
        '''
        response = self.response_builder(message)         # This creates a response object
        session.send(response)                            # sending message to the client
        client_response = self.request_parser(session)    # This recieves and parses the response from client
        return client_response

        
def main():
    import os
    config_file_path = '\\Utilities\\configs\\server_config.json'
    server = SERVER(config_file_path)
    server.start()

if __name__ == '__main__':
    main()





