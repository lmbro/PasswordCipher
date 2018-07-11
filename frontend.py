import tkinter as tk
import tkinter.ttk as ttk

from backend import Cipher
from constants import *


class PasswordCipher(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        self.parent = parent
        self.title = "Password Cipher"

        self._init_vars()
        self._init_widgets()

    def _init_vars(self):

        self.plaintext = tk.StringVar()
        self.ciphertext = tk.StringVar()
        self.method = tk.StringVar()
        self.key = tk.StringVar()

        self.method.set(METHOD_OPTS[0])

    def _init_widgets(self):

        tk.Label(self, text="Password")\
            .grid(row=0, column=0, sticky=tk.E)
        tk.Entry(self, textvariable=self.plaintext)\
            .grid(row=0, column=1, sticky=tk.EW)
        
        tk.Label(self, text="Website")\
            .grid(row=1, column=0, sticky=tk.E)
        tk.Entry(self, textvariable=self.key)\
            .grid(row=1, column=1, sticky=tk.EW)

        tk.Label(self, text="Method")\
            .grid(row=2, column=0, sticky=tk.E)
        tk.OptionMenu(self, self.method, *METHOD_OPTS)\
            .grid(row=2, column=1, sticky=tk.EW)

        tk.Button(self, text="Encrypt", command=self._encrypt)\
            .grid(row=3, column=0, columnspan=2)

        sub_frame = tk.Frame(self)
        sub_frame.grid(row=4, column=0, columnspan=2)
        tk.Entry(sub_frame, textvariable=self.ciphertext,  
            justify=tk.CENTER, state='readonly')\
            .grid(row=0, column=0, sticky=tk.EW)
        tk.Button(sub_frame, text="...", command=self._copy)\
            .grid(row=0, column=1, sticky=tk.EW)

    def _encrypt(self):

        method = self.method.get()

        if method == VIGENERE:
            ciphertext = Cipher.vigenere(self.plaintext, self.key)

        self.ciphertext.set(ciphertext)

    def _copy(self):

        self.clipboard_clear()
        self.clipboard_append(self.ciphertext.get())