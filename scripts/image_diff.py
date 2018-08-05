import os
import subprocess
import tempfile

import tkFileDialog
import tkMessageBox

from Tkconstants import *
from Tkinter import Frame, Button, Tk, Label, Entry, StringVar


class ImageDiffGui(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        root.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid(row=0, column=0, sticky=N+S+E+W)

        # define buttons
        Label(self, text='Image file 1:').grid(row=0, column=0)
        self.file1 = StringVar()
        Entry(self, textvariable=self.file1).grid(row=0, column=1, sticky=W+E+N+S)
        Button(self, text='Open file', command=self.open_file1).grid(row=0, column=2)

        Label(self, text='Image file 2:').grid(row=1, column=0)
        self.file2 = StringVar()
        Entry(self, textvariable=self.file2).grid(row=1, column=1, sticky=W+E+N+S)
        Button(self, text='Open file', command=self.open_file2).grid(row=1, column=2)

        self.file_out = StringVar()
        entry = Entry(self, textvariable=self.file_out, state='readonly')
        entry.grid(row=2, column=0, columnspan=2, sticky=W + E + N + S)
        Button(self, text='Convert', command=self.convert).grid(row=2, column=2)

    def convert(self):
        # options = self.option_value.get()
        tmpfile = tempfile.mktemp('.gif', 'imagediff')
        file1 = self.file1.get()
        file2 = self.file2.get()
        if os.path.exists(file1) and os.path.exists(file2):
            # print tmpfile
            args = ['convert', '-delay', '50', file1, file2, '-loop', '0', tmpfile]
            # print args
            status = subprocess.Popen(args)
            # print status
            self.file_out.set(tmpfile)
        else:
            tkMessageBox.showwarning(
                "Error",
                "Files are not specified"
            )

    def open_file1(self):
        self.__open_file(self.file1)

    def open_file2(self):
        self.__open_file(self.file2)

    def __open_file(self, txt_field):
        home = os.path.expanduser('~')
        pictures = os.path.join(home, 'Pictures')
        filename = tkFileDialog.askopenfilename(initialdir=pictures if os.path.exists(pictures) else home)
        if filename and os.path.exists(filename):
            txt_field.set(filename)
            self.file_out.set('')


if __name__ == '__main__':
    tk = Tk()
    ImageDiffGui(tk)
    tk.mainloop()
