#Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.

#!/usr/bin/env python
#-*- coding: utf -8-*-

import tkinter as tk
from tkinter import ttk  #Carga ttk (para widgets nuevos 8.5+)
from tkinter import * # Carga módulo tk (widgets estándar)
from tkinter import ttk  #Carga ttk (para widgets nuevos 8.5+)

from tkinter import messagebox
from time import strftime
from tkcalendar import Calendar


#Importando gestor de DB y modulos que componen el paquete
#import Modulo_acceso
#import Modulo_administrador

#Interfaz UI
class appWidget(tk.Tk):

    def __init__(self, *args, **kwargs):
    
        super().__init__(*args, **kwargs)

        self.title ('Widget v-1.5')
        self.geometry('500x187+450+220') # Estableciendo tamano de la ventana
        self.config(bg='Black')
        self.resizable(0,0) # No permite modificar la dimensión de la ventana     
        self.update() # Actualiza la pantalla antes de cargar en sistema
        

        #Formato hora
        self.FORMATO_HORA= '%H: %M: %S %p'

        #Formato fecha
        self.FORMATO_FECHA= '%d-%m-%Y'
        self.FORMATO_DIA='%d'
        self.FORMATO_MES='%m'
        self.FORMATO_AÑO='%Y'
        self.FORMATO_NOMBRE_DIA='%A'

         #Formato n° día
        self.FORMATO_N_DIA= '%j'
        
        #Variables 
        self.fecha_hoy=strftime(self.FORMATO_FECHA)
        self.numero_del_dia= strftime(self.FORMATO_N_DIA)
        self.fecha_dia=strftime(self.FORMATO_DIA)
        self.fecha_mes=strftime(self.FORMATO_MES)
        self.fecha_año=strftime(self.FORMATO_AÑO)
        self.nombre_dia=strftime(self.FORMATO_NOMBRE_DIA)
       
        #Posicionamiento de elementos
        self.etiqueta_hora=ttk.Label(self, font=('Verdana', 20, 'bold'), background= 'black', foreground='White')
        self.etiqueta_hora.place(x=141, y=20)

        self.fecha_actual=ttk.Label(self, text= str(self.nombre_dia)+ ': ' +str(self.fecha_hoy) + ' | Día n°: ' + str(self.numero_del_dia), font=('Verdana', 10, 'bold'), background='Black', foreground='Yellow')
        self.fecha_actual.place(x=116, y=60)

        self.scroll=tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox=tk.Listbox(self, width=60, height= 4, background='Black', yscrollcommand= self.scroll.set,  font=('Verdana', 9))
        self.scroll.configure(command=self.listbox.yview)
        self.listbox.place(x=8, y=90)

        self.patente=ttk.Label(self, text='©2025 / By Vielmadev', font=('Comic', 8, 'bold'), background='Black', foreground='Green')
        self.patente.place(x=190, y=160)

        self.hora()


    #Método hora actual 
    def hora(self):

            self.hora_actual=strftime(self.FORMATO_HORA)
            self.etiqueta_hora.config(text=self.hora_actual)
            self.etiqueta_hora.after(1000, self.hora)

    #Método calendario 
    def calendarios(self): 

        self.calendario= Toplevel()
        self.calendario.geometry('250x180+574+230')
        self.calendario.resizable(0,0)
        self.calendario.title('Calendario')
        self.cal=Calendar(self.calendario, selectmode='day', year=int(self.fecha_año), month=int(self.fecha_mes), day=int(self.fecha_dia))
        self.cal.place(x=0, y=0)
        self.cal.focus_set()

        self.calendario.transient(master=self)
        self.calendario.grab_set()
        self.wait_window(self.calendario)

    #def acceso(self):
        #Modulo_acceso.acceso()


def main():
    # Instanciación de la appWidget
    widget= appWidget()
    widget.mainloop()
    return(0)

if (__name__ == '__main__'):
    main()
