from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    def __init__(self):
        self.__ventana= Tk()
        self.__cantidad=[StringVar,StringVar,StringVar]
        self.__preciobase=[StringVar,StringVar,StringVar]
        self.__precioactual=[StringVar,StringVar,StringVar]
        self.__total=StringVar()
        self.__ventana.title('Calculadora IPC')
        mainframe=ttk.Frame(self.__ventana,padding="3 3 12 12")
        ttk.Label(mainframe,text='Item').grid(column=0,row=0,padx=20,pady=8,sticky="w")
        ttk.Label(mainframe,text='Cantidad').grid(column=1,row=0,padx=20)
        ttk.Label(mainframe,text='Precio Año Base').grid(column=2,row=0)
        ttk.Label(mainframe,text='Precio Año Actual').grid(column=3,row=0,padx=10)
        ttk.Label(mainframe,text='Vestimenta').grid(column=0,row=1,padx=20,sticky="w")
        ttk.Label(mainframe,text='Alimentos').grid(column=0,row=2,padx=20,sticky="w")
        ttk.Label(mainframe,text='Educación').grid(column=0,row=3,padx=20,sticky="w")
        self.cant1Entry= ttk.Entry(mainframe, width=10,textvariable=self.__cantidad[0])
        self.cant1Entry.grid(column=1,row=1,pady=8)
        self.cant2Entry= ttk.Entry(mainframe, width=10,textvariable=self.__cantidad[1])
        self.cant2Entry.grid(column=1,row=2,pady=8)
        self.cant3Entry= ttk.Entry(mainframe, width=10,textvariable=self.__cantidad[2])
        self.cant3Entry.grid(column=1,row=3,pady=8)
        self.base1Entry= ttk.Entry(mainframe, width=10,textvariable=self.__preciobase[0])
        self.base1Entry.grid(column=2,row=1,padx=8)
        self.base2Entry= ttk.Entry(mainframe, width=10,textvariable=self.__preciobase[1])
        self.base2Entry.grid(column=2,row=2,padx=8)
        self.base3Entry= ttk.Entry(mainframe, width=10,textvariable=self.__preciobase[2])
        self.base3Entry.grid(column=2,row=3,padx=8)
        self.actual1Entry= ttk.Entry(mainframe, width=10,textvariable=self.__precioactual[0])
        self.actual1Entry.grid(column=3,row=2)
        self.actual2Entry= ttk.Entry(mainframe, width=10,textvariable=self.__precioactual[1])
        self.actual2Entry.grid(column=3,row=1)
        self.actual3Entry= ttk.Entry(mainframe, width=10,textvariable=self.__precioactual[2])
        self.actual3Entry.grid(column=3,row=3)
        mainframe.pack(padx=20,pady=20)
        midframe=ttk.Frame(self.__ventana)
        ttk.Button(midframe,text='Calcular IPC',command=self.calcular).grid(column=1,row=0,padx=50,sticky="s")
        ttk.Button(midframe,text='Salir',command=self.__ventana.destroy).grid(column=2,row=0)
        midframe.pack()
        lowframe=ttk.Frame(self.__ventana)
        ttk.Label(lowframe,text='IPC %').grid(column=0,row=0,padx=20,sticky="w")
        ttk.Label(lowframe,textvariable=self.__total).grid(column=1,row=0)
        ttk.Label(lowframe,text='%').grid(column=2,row=0,sticky="w")
        lowframe.pack(side=LEFT,padx=20, pady=25)
        self.__ventana.mainloop()
    def calcular (self):
        try:
            cantidad=[float(self.cant1Entry.get()),float(self.cant2Entry.get()),float(self.cant3Entry.get())]
            base=[float(self.base1Entry.get()),float(self.base2Entry.get()),float(self.base3Entry.get())]
            actual=[float(self.actual1Entry.get()),float(self.actual2Entry.get()),float(self.actual3Entry.get())]
            valor1=cantidad[0]*(actual[0]/base[0])
            valor2=cantidad[1]*(actual[1]/base[1])
            valor3=cantidad[2]*(actual[2]/base[2])
            total=valor1+valor2+valor3
            total=int(total)*100
            self.__total.set(total)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos en todas las casilla')