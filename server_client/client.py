from server_client.constants import *

class Client:
    def __init__(self, addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.s.connect((addr,PORT))
        self.previous_data = None
        i_thread = threading.Thread(target=self.send_message)
        i_thread.daemon = True
        i_thread.start()

        while True:
            r_thread = threading.Thread(target=self.receive_message)
            r_thread.start()
            r_thread.join()
            data = self.receive_message()
            if not data:
                print("-"*3+"Server Failed"+"-"*3)
                break
            elif data[0:1] == b'\x11':
                print("Got peers")
                self.update_peers(data[1:])
    
    def receive_message(self):
        try:
            print("Receiving----")
            data = self.s.recv(BYTE_SIZE)
            print(data.decode("utf-8"))
            print("\n Received message on the client side is :")

            if self.previous_data != data:
                fileIO.create_file(data)
                self.previous_data = data
            
            return data
        except KeyboardInterrupt:
            self.send_disconnect_signal()

    def update_peers(self,peers):
        p2p.peers = str(peers, "utf-8").split(',')[:-1]
    
    def send_message(self):
        try:
            self.s.send(REQUEST_STRING.encode('utf-8'))
        except KeyboardInterrupt as e:
            self.send_disconnect_signal()
            return
    
    def send_disconnect_signal(self):
        print("Disconnected from server")
        self.s.send("q".encode('utf-8'))
        sys.exit()