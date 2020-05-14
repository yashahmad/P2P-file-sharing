from server_client.constants import *

class Server:
    def __init__(self, msg):
        try:
            self.msg = msg
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self.connections=[]
            self.peers=[]
            self.s.bind((HOST,PORT))
            self.s.listen(1)
            print("-"*3+"Server Running"+"-"*3+str(HOST)+"-"*3+str(PORT))
            self.run()
        except Exception as e:
            sys.exit()
        

        def handler(self,conn,a):
            try:
                while True:
                    data = conn.recv(BYTE_SIZE)
                    for conn in self.connections:
                        if data and data.decode('utf-8') == REQUEST_STRING:
                            print("-"*3+"UPLOADING"+"-"*3)
                            conn.send(self.msg)
            except Exception as e:
                sys.exit()
        

        def disconnect(self,conn,a):
            self.connections.remove(conn)
            self.peers.remove(a)
            conn.close()
            self.send_peers()
            print("{}, disconnected".format(a))
            print("-"*50)
        
        def run(self):
            while True:
                conn, a = self.s.accept()
                self.peers.append(a)
                print("Peers are:{}".format(self.peers))
                self.send_peers()
                c_thread=threadind.Thread(target=self.handler,args=(connection,a))
                c_thread.daemon=True
                c_thread.start()
                self.connections.append(conn)
                print("{},connected".format(a))
                print("-"*50)
            
        def send_peers(self):
            peer_list = ""
            for peer in self.peers:
                peer_list = peer_list + str(peer[0]) + ","
            
            for conn in self.connections:
                data = PEER_BYTE_DIFFERENTIATOR + bytes(peer_list,'utf-8')
                conn.send(PEER_BYTE_DIFFERENTIATOR+bytes(peer_list,'utf-8'))
