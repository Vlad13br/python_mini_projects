from tkinter import *
from tkinter import filedialog as fd
from pdf2docx import parse
import pathlib


def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')


def convert():
    pdf_file = ePath.get()
    world_file = pathlib.Pat(pdf_file)
    world_file = world_file.stem + 'docx'
    parse(pdf_file, world_file)
    Label(root, text='Convert finish', font='Arial 15 bold',
          fg='lime', bg='black').pack(pady=10)


root = Tk()
root.title('Pdf to world')
root.geometry("400x300+300")
root.resizable(False, False)
root["bg"] = "black"

Button(root, text='select file', font='Arial 15 bold',
       fg='lime', bg='black', command=callback).pack(pady=10)
lbPath = Label(root, text='path to the file', fg='lime',
               bg='black', font='Arial 15 bold').pack()
ePath = Entry(root, width=50, state='readonly').pack(pady=10)

btnConvert = Button(root, text='Convert', fg='lime',
                    bg='black', font='Arial 15 bold', command=convert).pack(pady=10)


root.mainloop()
