import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
import pandas as pd
##from PIL import Image, ImageTk
##import skimage.data
import numpy as np
##import keras

def graficas():
    global window
    self.destroy()
    window=tk.Tk()
    window.title("Heineken")
    window.minsize(600, 400)
    button4 = tk.Button(window, text='Examinar', width=25, command=Archivo)
    button4.pack()
    button4.place(x=50, y=150)
    button2 = tk.Button(window, text='Graficar', width=25)
    button2.pack()
    button2.place(x=200, y=200)
    window.textbox = tk.Entry(window, width = 40)
    window.textbox.place(x=250, y=150)
    window.mainloop()

def Archivo():
    global fileName 
    fileName = askopenfilename( filetypes = [( "xlsx", ".xlsx")])
    #print(letras)
    window.textbox.insert(0,fileName)

def Archivo2():
    global fileName1 
    fileName1 = askopenfilename( filetypes = [( "xlsx", ".xlsx")])
    #print(letras)
    window3.textbox.insert(0,fileName1)    

def Tabla():
    global window2
    window3.destroy()
    window2=tk.Tk()
    window2.title("Heineken")
    window2.geometry("1920x1080")
    button = tk.Button(window2, text='Regresar', width=10, command= Button33)
    button.pack()
    button.place(x=600, y=600)
    txt = scrolledtext.ScrolledText(window2, width=150, height = 30)
    txt.pack()
    txt.place(x=20, y=50)
    pd.options.display.width = None
    
    #pd.set_option('display.precision', 2)
    #scroll = Scrollbar(window2)
    #scroll.pack(side=RIGHT)
    #window2.textbox = tk.Entry(window2, width = 40)
    #window2.textbox.place(x=50, y=150)
    #pd.options.display.float_format = '{:.2f}'.format
    #pd.set_option('display.max_rows', None, 'display.max_columns', None)
    #df = pd.read_excel(fileName, sheet_name='PRINCIPAL', header=[5], index_col="Aviso").dropna(how='all')

    df = pd.read_excel(fileName1, sheet_name='PRINCIPAL').dropna(how='all')
    Completo = df[df[('Estatus Refacción')] == 'Completo']
    cosa = Completo[['Ubicación Técnica','# de Sap.','Descripción', 'Cantidad', 'Ots', 'Costo en SAP Refacción','Estatus Refacción']]
    txt.insert(1.0, cosa)
    window2.mainloop()


def Tabla2():
    global window4
    window3.destroy()
    window4=tk.Tk()
    window4.title("Heineken")
    window4.geometry("1920x1080")
    
    button = tk.Button(window4, text='Regresar', width=10, command= Button32)
    button.pack()
    button.place(x=600, y=600)
    
    frame = tk.Frame(window4, height = 30, width=180)
    frame.pack()
    frame.place(x=20, y=50)
    sBar = tk.Scrollbar(frame)
    sBar.pack(side=tk.RIGHT, fill ="y")
    sBar2 = tk.Scrollbar(frame, orient = tk.HORIZONTAL)
    sBar2.pack(side = tk.BOTTOM, fill="x")
    Txtbox = tk.Text(frame, height = 30, width = 180, yscrollcommand = sBar.set, xscrollcommand = sBar2.set, wrap = "none")
    Txtbox.pack()
    sBar.config(command=Txtbox.yview)
    sBar2.config(command=Txtbox.xview)
    
    #window4.minsize(1600, 600)
    #window4.maxsize(1920, 1800)
    #frame = tk.Frame(window4, height = 1600, width=1800)
    #frame.pack()
    #frame.place(x=0, y=50)
    #sbar = tk.Scrollbar(window4, orient = tk.HORIZONTAL)
    #txt = scrolledtext.ScrolledText(window4, width=125, height = 30, xscrollcommand = sbar.set, wrap = "none" )
    #txt.pack()
    #txt.place(x=0, y=0)
    
    pd.options.display.width = None
    df = pd.read_excel(fileName1, sheet_name='PRINCIPAL').dropna(how='all')
    Completo = df[df[('Estatus Refacción')] == 'Parcial']
    cosa = Completo[['Ubicación Técnica','# de Sap.','Descripción', 'Cantidad', 'Ots','# Pedido', 'Fe. Entrega', 'Proveedor', 'Costo en SAP Refacción','Estatus Refacción']]
    Txtbox.insert(1.0, cosa)
    window4.mainloop()

def Tabla3():
    global window5
    window3.destroy()
    window5=tk.Tk()
    window5.title("Heineken")
    window5.geometry("1920x1080")

    button = tk.Button(window5, text='Regresar', width=10, command= Button31)
    button.pack()
    button.place(x=600, y=600)
    
    frame = tk.Frame(window5, height = 30, width=180)
    frame.pack()
    frame.place(x=20, y=50)
    sBar = tk.Scrollbar(frame)
    sBar.pack(side=tk.RIGHT, fill ="y")
    sBar2 = tk.Scrollbar(frame, orient = tk.HORIZONTAL)
    sBar2.pack(side = tk.BOTTOM, fill="x")
    Txtbox = tk.Text(frame, height = 30, width = 180, yscrollcommand = sBar.set, xscrollcommand = sBar2.set, wrap = "none")
    Txtbox.pack()
    sBar.config(command=Txtbox.yview)
    sBar2.config(command=Txtbox.xview)
    
    pd.options.display.width = None
    df = pd.read_excel(fileName1, sheet_name='PRINCIPAL').dropna(how='all')
    Completo = df[df[('Estatus Refacción')] == 'Transito']
    cosa = Completo[['Ubicación Técnica','# de Sap.','Descripción', 'Cantidad', 'Ots','# Pedido', 'Fe. Entrega', 'Proveedor', 'Costo en SAP Refacción','Estatus Refacción']]
    Txtbox.insert(1.0, cosa)
    window5.mainloop()


def Pantalla():
    global window3
    self.destroy()
    window3=tk.Tk()
    window3.title("Heineken")
    window3.minsize(600, 400)
    button5 = tk.Button(window3, text='Examinar', width=25, command=Archivo2)
    button5.pack()
    button5.place(x=50, y=150)
    button6 = tk.Button(window3, text='Completo', width=10, command=Tabla)
    button6.pack()
    button6.place(x=200, y=200)
    button7 = tk.Button(window3, text='Parcial', width=10, command= Tabla2)
    button7.pack()
    button7.place(x=300, y=200)
    button8 = tk.Button(window3, text='Transito', width=10, command= Tabla3)
    button8.pack()
    button8.place(x=400, y=200)
    window3.textbox = tk.Entry(window3, width = 40)
    window3.textbox.place(x=250, y=150)
    window3.mainloop()

def Button33():
    window2.destroy()
    Inicio()

def Button32():
    window4.destroy()
    Inicio()
    
def Button31():
    window5.destroy()
    Inicio()
    
def Inicio():
    global self
    self= tk.Tk()
    self.title("Heiniken")
    self.minsize(600, 400)

    button = tk.Button(self, text='Grafica', width=25, command=graficas)
    button.pack()
    button.place(x=200, y=150)

    button3 = tk.Button(self, text='Tabla', width=25, command=Pantalla)
    button3.pack()
    button3.place(x=200, y=200)



    self.mainloop()

pd.options.display.float_format = '{:.2f}'.format
pd.set_option('display.max_rows', None, 'display.max_columns', None)
Inicio()


