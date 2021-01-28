import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from frontend import FrontEnd
from messenger import Messenger

HOST = '127.0.0.1'
PORT = 9090

class Client:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "please choose a nickname", parent=msg)
        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

        self.frontend = FrontEnd()
        self.messenger = Messenger()