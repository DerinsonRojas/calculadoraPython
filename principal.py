from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
numeroPantalla=StringVar()

print("-----------------------Funciones de Botones-----------------------------")

while numeroPantalla.get()=='':
    numeroPantalla.set('0')

def borrarPantalla():
    numeroPantalla.set('0')



def botonPresionado(num):
    numComas=0


    
    if  num==',' and numeroPantalla.get()=='0':
        numeroPantalla.set('0'+num)

    elif ',' in numeroPantalla.get() and num==',':
        numeroPantalla.set(numeroPantalla.get())

    elif numeroPantalla.get()=='0,' and num==',':
        numeroPantalla.set('0'+num)

    elif numeroPantalla.get()=='0':
        numeroPantalla.set(num)

    elif numeroPantalla.get()!='0':
        numeroPantalla.set(numeroPantalla.get()+num)    


#--------------Pantalla-----------------------
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
pantalla.config(fg="#4D1906", justify="right")

#--------------Fila 1---------------------------
boton7=Button(miFrame,text='7',width=3, command=lambda:botonPresionado('7'))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text='8',width=3, command=lambda:botonPresionado('8'))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text='9',width=3, command=lambda:botonPresionado('9'))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text='/',width=3, command=lambda:botonPresionado('indicar división'))
botonDiv.grid(row=2,column=4)

#--------------Fila 2---------------------------
boton4=Button(miFrame,text='4',width=3, command=lambda:botonPresionado('4'))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text='5',width=3, command=lambda:botonPresionado('5'))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text='6',width=3, command=lambda:botonPresionado('6'))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text='x',width=3, command=lambda:botonPresionado('indicar multi'))
botonMult.grid(row=3,column=4)

#--------------Fila 3---------------------------
boton1=Button(miFrame,text='1',width=3, command=lambda:botonPresionado('1'))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text='2',width=3, command=lambda:botonPresionado('2'))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text='3',width=3, command=lambda:botonPresionado('3'))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text='-',width=3, command=lambda:botonPresionado('indicar resta'))
botonRest.grid(row=4,column=4)

#--------------Fila 4---------------------------
botonComa=Button(miFrame,text=',',width=3, command=lambda:botonPresionado(','))
botonComa.grid(row=5,column=1)
boton0=Button(miFrame,text='0',width=3, command=lambda:botonPresionado('0'))
boton0.grid(row=5,column=2)
botonIgual=Button(miFrame,text='=',width=3, command=lambda:botonPresionado('ejecutar operacion'))
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text='+',width=3, command=lambda:botonPresionado('realizar suma'))
botonSuma.grid(row=5,column=4)

#--------------Fila 5--------------------------
botonBorrarUltimo=Button(miFrame,text='<-',width=3, command=lambda:botonPresionado('borrar el ultimo numero del entri'))
botonBorrarUltimo.grid(row=6,column=1)
botonBorrar=Button(miFrame,text='CE',width=3, command=borrarPantalla)
botonBorrar.grid(row=6,column=2)
botonSigno=Button(miFrame,text='+/-',width=3, command=lambda:botonPresionado('cambiar signo'))
botonSigno.grid(row=6,column=3)
botonPorcentaje=Button(miFrame,text='%',width=3, command=lambda:botonPresionado('calcula porcentaje'))
botonPorcentaje.grid(row=6,column=4)























raiz.mainloop()