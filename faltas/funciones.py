#                                                        #
#              Eleazar Sánchez Arbelo                    #
#								             12/11/18	 #
##########################################################

import crayons

def Falta(profesores):	#Funcion que sustituye a los profesores.
	print('')
	print(crayons.white('Profesores guardados :'))
	for t in range (0,len(profesores)):
		print(crayons.green(profesores[t].nombre))
	print('')
	aux=str(input(crayons.green('Nombre ')))
	aux='$'+aux
	for k in range (0,len(profesores)):
		if aux == profesores[k].nombre:
			aux2=k
			break
	dia= int(input(crayons.green('Día de la falta [L(1),M(2),X(3),J(4),V(5)]    ')))
	hora=int(input(crayons.green('Hora falta [1,2,3,4,5,6]                      ')))
	hora-=1
	materia = profesores[aux2].hour[dia][hora]
	for i in range (0,len(profesores)):	#Busca si un profesor tiene clase ese dia con ese curso
		for j in range (0,6):
			if profesores[i].hour[dia][j]== materia:
				profesores[i].d = True
	print('')
	for ii in range (0,len(profesores)):
		if profesores[ii].d and profesores[ii].hour[dia][hora] == 'LIBRE':
			print (crayons.blue(profesores[ii].nombre) ,crayons.blue( 'puede sustitur'))

def Mostrar(profesores):	#Muestra los horarios
	print('')
	print (crayons.white('Profesores guardados: '))
	for i in range (0,len(profesores)):
		print(crayons.green(profesores[i].nombre))
	print('')
	aux=str(input(crayons.green('Nombre ')))
	aux='$'+aux
	for k in range (0,len(profesores)):
		if aux == profesores[k].nombre:
			aux2=k
			break
	print('')
	for j in range(0,5):
		print(crayons.blue(profesores[aux2].hour[0][j]))
		print(crayons.green(profesores[aux2].hour[j+1]))

def Ver(i,j):	#Ver dias en la recogida de datos
	if i==1:
		print (' LUNES     ' ,j+1, 'h')
	if i==2:
		print (' MARTES    ' ,j+1, 'h')
	if i==3:
		print (' MIERCOLES ' ,j+1, 'h')
	if i==4:
		print (' JUEVES    ' ,j+1, 'h')
	if i==5:
		print (' VIERNES   ' ,j+1, 'h')

def Crear_profesor(f,Profesor):	#Guarda el profesor en fichero
	f.write('$')
	prof=Profesor()
	prof.nombre=input('Nombre : ')
	f.write(prof.nombre)
	Crear_horario(f,prof)

def Crear_horario (f,profesora):	#Guarda horario en fichero
	print('')
	print(crayons.green('Introduzca el horario : '))
	for i in range (1,6):
		for j in range (0,6):
			Ver(i,j)
			profesora.hour[i][j]= input()
			f.write(','+profesora.hour[i][j])
	f.write('\n')

def Conver(aux,a):	#de array a profesor.hour
	n=1
	for i in range (1,6):
		for j in range(0,6):
			aux.hour[i][j]=a[n]
			n+=1

def Manual():
	print('')
	print(crayons.green('El programa carga automáticamente los profesores del fichero faltas.txt'))
	print(crayons.green('Siempre ha de llamar a la misma asignatura de la misma forma y con la misma cantidad de mayusculas y minusculas.'))
	print(crayons.green('Las horas que tenga libres debe escribirlas como LIBRE en mayusculas.'))
	print(crayons.green('Si quiere eliminar un profesor, eliminelo del archivo faltas.txt y no deje ninguna linea entre el resto de los profesores guardados.'))
	print(crayons.green('Si añade profesor/es nuevo/s, antes de realizar operaciones con este/os nuevo/s profesor/es debe reiniciar el programa.'))
	print('')
