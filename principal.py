from tkinter import *
from turtle import title


raiz=Tk()
raiz.config(padx=30, pady=30, background="green")
raiz.title('Calculadora')
miFrame=Frame(raiz)

miFrame.pack()
numeroPantalla=StringVar()
operacion=''
resultado=0
resultadoMultiplicacion=1
resultadoResta=0


indicadorDeOperacion=''
print("-----------------------Inicio de la calculadora-----------------------------")

if numeroPantalla.get()=='':
    numeroPantalla.set('0')

#---------Funcion el resultado-----------------------

def operacionResultado():
    global resultado
    
    global operacion

    global indicadorDeOperacion

    global resultadoMultiplicacion



    print("observando al indicador de operacion: ", indicadorDeOperacion)
    if numeroPantalla.get()=='0' and resultado ==0:
        return '0'


    if numeroPantalla.get()=='':
        return '0'
    if indicadorDeOperacion=='s':
        #print("Resultado: ",type(resultado))
        #print("Numero en pantalla: ",type(numeroPantalla.get()))
        a=float(numeroPantalla.get())#Lineas del codigo
        #print("tipo de dato de a: ",type(a))
        numeroPantalla.set(resultado+a)#Lineas del codigo
        indicadorDeOperacion=''

    elif indicadorDeOperacion=='r':
        a=float(numeroPantalla.get())#Lineas del codigo
        numeroPantalla.set(resultado-a)#Lineas del codigo
        indicadorDeOperacion=''
    
    elif indicadorDeOperacion=='m':
        a=float(numeroPantalla.get())#Lineas del codigo
        numeroPantalla.set(resultadoMultiplicacion*a)#Lineas del codigo
        indicadorDeOperacion=''
    
    elif indicadorDeOperacion=='d':
        a=float(numeroPantalla.get())#Lineas del codigo
        try:
            numeroPantalla.set(resultado/a)#Lineas del codigo
        
        except:
            numeroPantalla.set('NoDivEntreCero')
        
        indicadorDeOperacion=''
    

    resultadoMultiplicacion=1
    resultado=0

    return ""

def borrarPantalla():
    global resultado 
    global resultadoMultiplicacion

    numeroPantalla.set('0')

    resultado=0
    resultadoMultiplicacion=1

def botonPresionado(num):

    global operacion

    if operacion!='':
        numeroPantalla.set(num)

        operacion='' 
    else:
        if  num==',' and numeroPantalla.get()=='0':
            numeroPantalla.set('0'+num)

        elif ',' in numeroPantalla.get() and num==',':
            numeroPantalla.set(numeroPantalla.get())

        elif numeroPantalla.get()=='0,' and num==',':
            numeroPantalla.set('0'+num)

        elif numeroPantalla.get()=='0':
            numeroPantalla.set(num)

        elif numeroPantalla.get()!='0':
            numeroPantalla.set(numeroPantalla.get()+str(num))

#----------------Operaciones aritmeticas---------
def suma(num):

    global indicadorDeOperacion
    global operacion

    global resultado

    global resultadoMultiplicacion

    resultadoMultiplicacion=1

    resultado+=float(num)

    operacion='suma'
    indicadorDeOperacion='s'
    numeroPantalla.set(resultado)

def resta(num):
    global operacion

    global resultado

    global resultadoResta

    global indicadorDeOperacion

    operacion='resta'

    indicadorDeOperacion='r'

    num2=float(num)

    if resultado==0:
        resultado=num2-resultado

    else:
        resultado=resultado-num2

    numeroPantalla.set(resultado)

def multiplicacion(num):
    global operacion
    global indicadorDeOperacion
    global resultadoMultiplicacion
    
    operacion='multiplicacion'

    indicadorDeOperacion='m'

    resultadoMultiplicacion*=float(num)
    
    numeroPantalla.set(resultadoMultiplicacion)
#Falta arreglar la vivision entre cero cuando no se agrega nada a la calculadora
def division(num):
    global operacion

    global indicadorDeOperacion

    global resultado

    global resultadoMultiplicacion

    operacion='division'

    indicadorDeOperacion='d'
    
    try:
        if float(num)==0:
            resultado=float(num)/resultadoMultiplicacion
        if resultado==0 and float(num)!=0:
            resultado=float(num)/resultadoMultiplicacion
        elif resultado!=0:
            resultado=resultado/float(num)

        numeroPantalla.set(resultado)

    except ZeroDivisionError:
        numeroPantalla.set("NoDivEntreCero")

def cambiaSigno(num):
    if num=='0' or num=='0.0':
        return '0'
    if num!='0':
        numeroNuevo=-1*float(num)
        a=str(numeroNuevo)
        numeroPantalla.set(a)
        return ''
#Mejorar el borrado de numeros
def borrarUltimo(num):

    a=num[:-1]
    str(a)
    numeroPantalla.set(a)

    return ''

#--------------Pantalla-----------------------
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=5,pady=5, columnspan=4)
pantalla.config(fg="#4D1906", justify="right", width=25, font=40)

#--------------Fila 1---------------------------
boton7=Button(miFrame,text='7',width=7, height=3, command=lambda:botonPresionado('7'))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text='8',width=7, height=3, command=lambda:botonPresionado('8'))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text='9',width=7, height=3, command=lambda:botonPresionado('9'))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text='/',width=7, height=3, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)

#--------------Fila 2---------------------------
boton4=Button(miFrame,text='4',width=7, height=3, command=lambda:botonPresionado('4'))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text='5',width=7, height=3, command=lambda:botonPresionado('5'))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text='6',width=7, height=3, command=lambda:botonPresionado('6'))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text='x',width=7, height=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3,column=4)

#--------------Fila 3---------------------------
boton1=Button(miFrame,text='1',width=7, height=3, command=lambda:botonPresionado('1'))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text='2',width=7, height=3, command=lambda:botonPresionado('2'))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text='3',width=7, height=3, command=lambda:botonPresionado('3'))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text='-',width=7, height=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4,column=4)

#--------------Fila 4---------------------------
botonComa=Button(miFrame,text='.',width=7, height=3, command=lambda:botonPresionado('.'))
botonComa.grid(row=5,column=1)
boton0=Button(miFrame,text='0',width=7, height=3, command=lambda:botonPresionado('0'))
boton0.grid(row=5,column=2)
botonCambiaSigno=Button(miFrame,text='+/-',width=7, height=3, command=lambda:botonPresionado(cambiaSigno(numeroPantalla.get())))
botonCambiaSigno.grid(row=5,column=3)
botonSuma=Button(miFrame,text='+',width=7, height=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)

#--------------Fila 5--------------------------
botonBorrarUltimo=Button(miFrame,text='<-',width=7, height=3, command=lambda:botonPresionado(borrarUltimo(numeroPantalla.get())))
botonBorrarUltimo.grid(row=6,column=1)
botonBorrar=Button(miFrame,text='CE',width=7, height=3, command=borrarPantalla)
botonBorrar.grid(row=6,column=2)
botonIgual=Button(miFrame,text='=',width=15,height=3, command=lambda:botonPresionado(operacionResultado()))
botonIgual.grid(row=6,column=3, columnspan=2)

raiz.mainloop()