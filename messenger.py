from client import Client
from server import HOST, PORT


class Messenger(Client):

    def __init__(self):
        super().__init__()

    
    def write(self):
        message = f"{self.nickname} : {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')


    def stop(self):
        self.running = False
        self.screen.destroy()
        self.sock.close()
        exit()


    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break
    
client = Client(HOST, PORT)