#Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.

#!/usr/bin/env python
#-*- coding: utf -8-*-

import tkinter as tk
from tkinter import ttk  #Módulo ttk para widgets nuevos 8.5+
from tkinter import * # Módulo tk widgets estándar

from time import strftime #Librería para formato hora

#Interfaz UI
class appWidget(tk.Tk):

    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)

        self.title ('TIME ⏰')
        self.geometry('350x180+450+220') # Estableciendo tamano de la ventana
        self.config(bg='Black')
        self.resizable(0,0) # No permite modificar la dimensión de la ventana 

        #Hora actual
        self.FORMATO_HORA= '%H:%M:%S %p'    

        #Formato fecha
        self.FORMATO_DIA='%d'
        self.FORMATO_MES='%m'
        self.FORMATO_AÑO='%Y'
        self.FORMATO_FECHA= '%d / %m / %Y'
        self.FORMATO_NOMBRE_DIA='%A'

         #Formato n° día
        self.FORMATO_N_DIA= '%j'
        
        #Variables 
        self.nombre_dia=strftime(self.FORMATO_NOMBRE_DIA)
        self.fecha_dia=strftime(self.FORMATO_DIA)
        self.fecha_mes=strftime(self.FORMATO_MES)
        self.fecha_año=strftime(self.FORMATO_AÑO)
        self.fecha_hoy=strftime(self.FORMATO_FECHA)
        self.numero_del_dia= strftime(self.FORMATO_N_DIA)
       
        #Posicionamiento de elementos
        self.etiqueta_hora=ttk.Label(self, font=('Comic Sans MS', 27, 'bold'), background= 'black', foreground='White')
        self.etiqueta_hora.place(x=55, y=18)

        self.dia_actual=ttk.Label(self, text= str(self.nombre_dia), font=('Verdana', 16, 'bold'), background='Black', 
        foreground='Blue')
        self.dia_actual.place(x=100, y=70)

        self.fecha_actual=ttk.Label(self, text= str(self.fecha_hoy), font=('Verdana', 14, 'bold'), background='Black', 
        foreground='Yellow')
        self.fecha_actual.place(x=91, y=105)

        self.n_dia=ttk.Label(self, text= 'Día n° : ' + str(self.numero_del_dia), font=('Verdana', 12, 'bold'), background='Black', 
        foreground='Yellow')
        self.n_dia.place(x=123, y=140)

        self.hora() #Llamanda a metodo hora

        #Método hora actual 
    def hora(self):
        self.hora_actual=strftime(self.FORMATO_HORA)
        self.etiqueta_hora.config(text=self.hora_actual)
        self.etiqueta_hora.after(1000, self.hora)

def main():
    # Instanciación de la appWidget
    widget= appWidget()
    widget.mainloop()
    return(0)

if (__name__ == '__main__'):
    main()
