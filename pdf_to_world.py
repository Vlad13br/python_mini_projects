from tkinter import *
from tkinter import filedialog as fd
from pdf2docx import Converter
import pathlib


def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')


def convert():
    pdf_file = ePath.get()
    docx_file = pathlib.Path(pdf_file).with_suffix('.docx')
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    Label(root, text='Convert finish', font='Arial 15 bold',
          fg='lime', bg='black').pack(pady=10)


root = Tk()
root.title('Pdf to Word')
root.geometry("400x300+300+300")  # Added missing '+300'
root.resizable(False, False)
root["bg"] = "black"

Button(root, text='Select File', font='Arial 15 bold',
       fg='lime', bg='black', command=callback).pack(pady=10)
lbPath = Label(root, text='Path to the File', fg='lime',
               bg='black', font='Arial 15 bold').pack()
ePath = Entry(root, width=50, state='readonly')
ePath.pack(pady=10)

btnConvert = Button(root, text='Convert', fg='lime',
                    bg='black', font='Arial 15 bold', command=convert).pack(pady=10)

root.mainloop()
