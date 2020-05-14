from server_client.constants import *
from server_client.client import Client
from server_client.server import Server

class P2P:
    peers = ['0.0.0.0']

def main():
    msg = fileIO.convert_to_bytes()
    while True:
        try:
            print("-"*3+"Trying to connect"+"-"*3)
            time.sleep(randint(RAND_TIME_START,RAND_TIME_END))
            for peer in P2P.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
                
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass
        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()