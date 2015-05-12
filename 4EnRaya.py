#!/usr/bin/python

class Casilla:
	fila=-1
	columna=-1
	def __init__(self,f,c):
		self.fila=f
		self.columna=c
	def __str__(self):
		return "[{}][{}]".format(self.fila,self.columna)
	def __repr__(self):
		return self.__str__()


class Linea:
	lin=None
	def __init__(self):
		self.lin=[]
	def aniadir(self,cas):
		self.lin.append(cas)
	def size(self):
		return len(self.lin)
	def getCasilla(self,i):
		return self.lin[i]
	def __str__(self):
		#Llamar a __str__() sobre un array, busca el método __repr__() en la clase a la que pertenece cada elemento del array
		return self.lin.__str__()
		


line=Linea()
#line.lin=[]
cas=Casilla(3,2)
#cas.setValue(3,2)
#print cas
line.aniadir(cas)
cas=Casilla(8,2)
line.aniadir(cas)

print line




def poner (filas,columnas,matriz,columnaElegida,elementoAPoner,vacio):
	if(columnaElegida>=columnas):
		return False
	else:
		encontrado=False
		fila_libre=filas-1
		while(not encontrado):
			if (matriz[fila_libre][columnaElegida]==vacio):
				encontrado=True
			else:
				fila_libre=fila_libre-1
			if(fila_libre==-1):
				encontrado=True
		if(fila_libre!=-1):
			matriz[fila_libre][columnaElegida]=elementoAPoner
			return True
		else:
			return False


def comprobarVictoria(filas,columnas,matriz,simbolo):
	estado_correcto=True
	resultado=False
	for i in range(filas):
		for j in range(columnas):
			if(matriz[i][j]==simbolo):
				longline=1
				#busqueda vertical
				filaBusqueda=i
				while(estado_correcto):
					if(filaBusqueda+1>=filas):
						estado_correcto=False
					else:
						filaBusqueda=filaBusqueda+1
						if(matriz[filaBusqueda][j]==simbolo):
							longline=longline+1
						else:
							estado_correcto=False
					if(longline==4):
						estado_correcto=False
						resultado=True		
						return resultado
				#busqueda horizontal
				longline=1
				estado_correcto=True
				colBusqueda=j
				while(estado_correcto):
					if(colBusqueda+1>=columnas):
						estado_correcto=False
					else:
						colBusqueda=colBusqueda+1
						if(matriz[i][colBusqueda]==simbolo):
							longline=longline+1
						else:
							estado_correcto=False
					if(longline==4):
						estado_correcto=False
						resultado=True
						return resultado
				#busqueda diagonal principal
				longline=1
				estado_correcto=True
				filaBusqueda=i
				colBusqueda=j
				while(estado_correcto):
					if(colBusqueda+1>=columnas or filaBusqueda+1>=filas):
						estado_correcto=False
					else:
						filaBusqueda=filaBusqueda+1
						colBusqueda=colBusqueda+1
						if(matriz[filaBusqueda][colBusqueda]==simbolo):
							longline=longline+1
						else:
							estado_correcto=False
					if(longline==4):
						estado_correcto=False
						resultado=True
						return resultado
				#busqueda diagonal secundaria
				longline=1
				estado_correcto=True
				filaBusqueda=i
				colBusqueda=j
				while(estado_correcto):
					if(colBusqueda-1<0 or filaBusqueda+1>=filas):
						estado_correcto=False
					else:
						filaBusqueda=filaBusqueda+1
						colBusqueda=colBusqueda-1
						if(matriz[filaBusqueda][colBusqueda]==simbolo):
							longline=longline+1
						else:
							estado_correcto=False
					if(longline==4):
						estado_correcto=False
						resultado=True
						return resultado
	return resultado

def comprobarTableroLleno(filas,columnas,matriz,vacio):
	for i in range(filas):
		for j in range(columnas):
			if(matriz[i][j]==vacio):
				return False;
	return True;

#main
vacio=u'\u2591'
tablero=[[vacio for x in xrange(7)] for y in xrange(7) ]

nombreP1=raw_input("Jugador 1, dime tu nombre: ")
nombreP2=raw_input("Jugador 2, dime tu nombre: ")

simboloP1='O'
simboloP2='X'

victoria=False
turno=False
columnaElegida=-1
turnoCorrecto=False;
ganador=""

print ""
print "Instrucciones:"
print "En cada turno debes indicar un numero del 0 al 6 para jugar en una columna, teniendo en cuenta la siguiente configuracion:"
for i in xrange(7):
			for j in xrange(7):
		 		print tablero[i][j],
			print ""
print"0 1 2 3 4 5 6"
print""

while(not comprobarTableroLleno(7,7,tablero,vacio) and not victoria):
	if (not turno):#Turno de J1
		print "Turno de {}".format(nombreP1)
		
		try:
			columnaElegida=input("En que columna quieres poner? (0-6): ")
			turnoCorrecto=poner (7,7,tablero,columnaElegida,simboloP1,vacio)
		except NameError:
			pass
		except SyntaxError:
			pass		
		while(not turnoCorrecto):
			print "La jugada no es valida"
			try:
				columnaElegida=input("En que columna quieres poner? (0-6): ")
				turnoCorrecto=poner (7,7,tablero,columnaElegida,simboloP1,vacio)
			except NameError:
				pass
			except SyntaxError:
				pass

		turnoCorrecto=False
		victoria=comprobarVictoria(7,7,tablero,simboloP1);
		if(victoria):
			ganador=nombreP1
		else:
			turno=True
		for i in xrange(7):
			for j in xrange(7):
		 		print tablero[i][j],
			print ""
		print"0 1 2 3 4 5 6"
		print""
	else:#Turno de J2
		print "Turno de {}".format(nombreP2)
		
		try:
			columnaElegida=input("En que columna quieres poner? (0-6): ")
			turnoCorrecto=poner (7,7,tablero,columnaElegida,simboloP2,vacio)
		except NameError:
			pass
		except SyntaxError:
			pass

		while(not turnoCorrecto):
			print "La jugada no es valida"
			try:
				columnaElegida=input("En que columna quieres poner? (0-6): ")
				turnoCorrecto=poner (7,7,tablero,columnaElegida,simboloP2,vacio)
			except NameError:
				pass
			except SyntaxError:
				pass
		
		turnoCorrecto=False
		victoria=comprobarVictoria(7,7,tablero,simboloP2);
		if(victoria):
			ganador=nombreP2
		else:
			turno=False
		for i in xrange(7):
			for j in xrange(7):
		 		print tablero[i][j],
			print ""
		print"0 1 2 3 4 5 6"
		print""
print "Enhorabuena {}, has hecho 4 en raya".format(ganador)