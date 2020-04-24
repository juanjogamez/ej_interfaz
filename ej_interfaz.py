#EJERCICIO INTERFAZ, JUAN JOSE GAMEZ
import tkinter as tk
from tkinter import ttk
from sense_emu import SenseHat
import time
class Aplicacion:
    def __init__(self):
        #Ventana
        self.ventana1=tk.Tk()
        self.ventana1.resizable(0,0)
        self.ventana1.title("SenseHat Interfaz")

        #Variables programa
        self.funcionar=0
        self.periodo=0
        self.medida=0
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.añadir=tk.IntVar()
        self.añadir.set(1)
        self.contador=0
        self.tipo="not_asigned"


        #Sensehat
        self.sense=SenseHat()

        #LABELFRAME1
        self.labelframe1=tk.LabelFrame(self.ventana1, text="Control")
        self.labelframe1.grid(row=1, column=1)
        self.btn_ctrl=tk.Button(self.labelframe1, text="Iniciar", command=self.boton, background="green")
        self.btn_ctrl.grid(row=1, column=1)
        self.label_periodo=tk.Label(self.labelframe1, text=("Periodo: "+ str(self.periodo)))
        self.label_periodo.grid(row=2, column=1)

        #LABELFRAME2
        self.labelframe2=tk.LabelFrame(self.ventana1, text="Medidas")
        self.labelframe2.grid(row=2, column=1)
        self.label_medida=tk.Label(self.labelframe2, text=str(self.medida))
        self.label_medida.grid(row=1, column=2)
        self.radio1=tk.Radiobutton(self.labelframe2 ,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(row=2, column=1)
        self.radio2=tk.Radiobutton(self.labelframe2 ,text="Presión", variable=self.seleccion, value=2)
        self.radio2.grid(row=2, column=2)
        self.radio3=tk.Radiobutton(self.labelframe2 ,text="Humedad", variable=self.seleccion, value=3)
        self.radio3.grid(row=2, column=3)

        
        #LABELFRAME3
        self.labelframe3=tk.LabelFrame(self.ventana1, text="Histórico")
        self.labelframe3.grid(row=3, column=1)
        self.scroll1 = tk.Scrollbar(self.labelframe3, orient=tk.VERTICAL)
            #TreeView
        self.tree = ttk.Treeview(self.labelframe3,yscrollcommand=self.scroll1.set)
        self.tree.grid(columnspan=3)
        self.scroll1.configure(command=self.tree.yview)
        self.scroll1.grid(row=0, column=3, sticky='NS')
        self.tree['columns'] = ('Valor', 'Fecha/Hora', 'Tipo')
        self.tree.heading('#0', text='#Num')
        self.tree.heading('Valor', text='Valor')
        self.tree.heading('Fecha/Hora', text='Fecha/Hora')
        self.tree.heading('Tipo', text='Tipo')        
            #Botones inferiores
        self.btn_clean=tk.Button(self.labelframe3, text="Limpiar", command=self.limpiar)
        self.btn_clean.grid(row=1, column=0)
        self.btn_med=tk.Button(self.labelframe3, text="Calcular Media", command=self.not_asigned)
        self.btn_med.grid(row=1,column=1)
        self.btn_exportar=tk.Button(self.labelframe3, text="Exportar", command=self.not_asigned)
        self.btn_exportar.grid(row=1, column=2)
        self.check_add=tk.Checkbutton(self.labelframe3, text="Añadir a lista", variable=self.añadir)
        self.check_add.grid(row=2, column=1)
        self.ventana1.mainloop()

    def programa(self):
        while (self.funcionar==1):
            self.periodo=self.periodo+1
            print("Periodo: ", self.periodo)                    #Debug
            self.label_periodo.configure(text=str(self.periodo))
            time.sleep(1)                                     
            #Lectura
            if(self.seleccion.get()==1):
                self.medida=self.sense.temp
                self.tipo="Temperatura"
            if(self.seleccion.get()==2):
                self.medida=self.sense.pressure
                self.tipo="Presión"
            if(self.seleccion.get()==3):
                self.medida=self.sense.humidity
                self.tipo="Humedad"

            print("Medida: ", self.medida)                      #Debug
            print('\n')
        
            #Escritura
            self.label_medida.config(text=str(self.medida))
            if(self.añadir.get()==1):
                self.contador=self.contador+1
                self.tree.insert('','end',text=str(self.contador), values=(str(self.medida),str(time.strftime("%c")), self.tipo))
            
            self.ventana1.update()


    def boton(self):
        if (self.funcionar==0):
            self.funcionar=1
            self.btn_ctrl.configure(text="Parar", background="red")
            self.programa()
            #Debug
        else:
            self.funcionar=0
            self.btn_ctrl.configure(text="Iniciar", background="green")
        print("Funcionar: "+str(self.funcionar)) #Debug

    
    def limpiar(self):
        if self.funcionar==1:
            self.boton()
        for i in self.tree.get_children():             #Fuente: https://stackoverflow.com/questions/22812134/how-to-clear-an-entire-treeview-with-tkinter
            self.tree.delete(i)
        self.periodo=0
        self.contador=0
        self.seleccion.set(1)
        self.medida=0
        self.label_periodo.configure(text=str(self.periodo))
        self.label_medida.config(text=str(self.medida))
        self.ventana1.update


    def not_asigned(self):
        print("Not implemented yet")


app=Aplicacion()