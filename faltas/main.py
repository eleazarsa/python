#                                                        #
#              Eleazar Sánchez Arbelo                    #
#													     #
##########################################################

import os
import crayons
from funciones import *
 
f=open("faltas.txt",'r+')

profesores=[]
menu=88

class Profesor():
	nombre=('')
	hour=[['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]
	d = False 							#dato booleano que marcara si un profesor tiene clase ese dia con esa determianda materia

print('')
print(crayons.white(' Bienvenido a iFaltas1.0 ')) 
for linea in f.readlines():	#Lee del fichero y crea array profesores
	a=linea.split(',')
	aux=Profesor()
	aux.hour=[['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]
	aux.nombre=a[0]
	Conver(aux,a)	
	profesores.append(aux)
while menu !=0:
	print('')
	print(crayons.white('#########################'))
	print(crayons.green(' 1. Crear nuevo profesor '))	
	print(crayons.green(' 2. Ejecutar sustitución '))
	print(crayons.green(' 3. Mostrar horarios     '))
	print(crayons.green(' 4. Manual               '))
	print(crayons.green(' 0. Salir                '))
	print(crayons.white('#########################'))
	print('')
	menu=int(input(crayons.green('Seleccione una opción: ')))
	if(menu==1):
		Crear_profesor(f,Profesor)
		os.system("clear")
	if(menu==2):
		Falta(profesores)
	if(menu==3):
		Mostrar(profesores)
	if(menu==4):
		Manual()
	
f.close()
