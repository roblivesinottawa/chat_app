import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import Client
from messenger import write, stop


class FrontEnd(Client):

    def __init__(self):
        super().__init__()

    def gui_loop(self):
        self.screen = tkinter.Tk()
        self.screen.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.screen, text="Chat: ", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.screen)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.screen, text="Message", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.screen, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.screen, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.screen.protocol("WM_DELETE_WINDOW", self.stop)

        self.screen.mainloop()
