# lo primero es importar librerias
from tkinter import *

#creamos la raiz para el frame principal

raiz=Tk()
miFrame=Frame(raiz)

#empaquetamos el frame
#le dara el tamaño por defecto
miFrame.pack()

# creamos una variable global que sea accesible a todo el programa
# despues usaremos funciones para cada tipo de operacion 
# almacenaremos los datos de la funcion para poder concatenar operaciones y resetear
# se inicializa la operacion con cadena vacia para que empece con ningun valor
operacion=""

# declaro la variable de resultado inicializada en 0 para que al comienzo del programa o después del resteo salga 0
resultado=0

#------------------pantalla-----------------------------------------
#la pantalla representara la fila 1

#definimos una variable que se asocia a la pantalla con un string

numeroPantalla=StringVar() 

#construimos la pantalla con un entry para que haya un texto dinamico
#distribuimos los componentes de la calculadora con grid

pantalla=Entry(miFrame, textvariable=numeroPantalla)

#para colocar la pantalla alineada con botones usamos columnspan
#sirve para que usen 4 columnas de expansion

pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

#para el codigo del color de los numeros, busco el codigo del color

pantalla.config(background="black", fg="#03f943", justify="right")

#--------------pulsaciones teclado-------------------------

def numeroPulsado(num):

	global operacion

	if operacion!="":
		#si el usuario pulsa +, escribe el numero sin concatenar
		numeroPantalla.set(num) 

		operacion=""

	else:

	#decimos a la funcion que establezca un texto con set
	#para concatenar numeros usamos get
		numeroPantalla.set(numeroPantalla.get()+num)

#-----------------funcion suma---------------------------------
#en esta funcion hay que conseguir que se borre la pantalla cada vez que queramos introducir nuevos valores numericos
#pero a la vez estos valores tienen que irse almacenando, esto lo haremos en NumeroPulsado
def suma(num):
	global operacion

	global resultado

	resultado+=int(num) #resultado=resultado+int(num)

	operacion="suma"

	numeroPantalla.set(resultado)

#----------------funcion resta---------------------------------

def resta(num):

	global operacion

	global resultado

	resultado-=int(num)

	operacion="resta"

	numeroPantalla.set(resultado)

#-----------------funcion multiplicacion-----------------------

def multiplicacion(num):

	global operacion

	global resultado

	resultado*=int(num)

	numeroPantalla.set(resultado)

#------------------funcion division----------------------------

def division(num):

	global operacion

	global resultado

	resultado%=int(num)

	numeroPantalla.set(resultado)

#----------------funcion el_resultado--------------------------

def el_resultado():
	global resultado

	#configuramos para que nos sume los numeros almacenados+ultimo numero
	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	#reseteamos el resultado para que borre la cuenta anterior
	resultado=0

#---------------fila 2------------------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)


#---------------fila 3------------------------------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="*", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column=4)


#---------------fila 4------------------------------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

#---------------fila 5------------------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()