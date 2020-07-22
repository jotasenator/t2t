import random
import time

class Criaturas():
	"""docstring for Criaturas"""
	def __init__(self,nombre,raza,defensa,ataque,vida,dodge):

		self.nombre = nombre
		self.raza = raza
		self.defensa = defensa
		self.ataque = ataque
		self.vida = vida
		self.dodge = dodge

#se puede instanciar con otros valores,
#teniendo en cuenta que lso golpes no le sumen vida al oponente
#para que hayan iguales oportunidades tienen lso mismos valores
#despues se pueda cambiar

maja = Criaturas('MAJÁ','Orco',1,5,15,1)
turi = Criaturas('TURI','Elfo',1,8,15,1)

#esto es solo para revisar
'''
print('raza maja:',maja.raza)
print('defensa maja:',maja.defensa)
print('ataque maja:',maja.ataque)
print('vida maja:',maja.vida)
print('dodge maja:',maja.dodge)

print('raza turi:',turi.raza)
print('defensa turi:',turi.defensa)
print('ataque turi:',turi.ataque)
print('vida turi:',turi.vida)
print('dodge turi:',turi.dodge)'''

#listas de ataques para cada quien

lista_ataque_turi = ['muerde',
					'vierte ron en los ojos',
					'quema con un cigarro',
					'lanza un plato de ensalada y golpea',
					'pone BAD BUNNY a todo volumen y destruye masivamente',
					'pregunta: Quien es el ultimo y frustra'
					]

lista_ataque_maja = ['escupe',
					'silva en los oidos muy fuerte',
					'se estira y pone un traspie ',
					'tira una piedra',
					'invoca a Felo y atemoriza',
					'grita Cuba si Yankis No y desguabina'
					]

print('Un elfo y un orco se encuentran y ocurre lo inevitable')
print()

while True:

	if maja.vida > 0 and turi.vida >0:

		at = lista_ataque_turi[random.choice(range(6))]
		am = lista_ataque_maja[random.choice(range(6))]

		turi_ataca = random.choice(range(1,turi.ataque))
		maja_ataca = random.choice(range(3,maja.ataque))

		time.sleep(1.5)
		print(maja.nombre,am,'a',turi.nombre)
		#esta formula se puede mejorar 
		turi.vida = turi.vida - maja_ataca + turi.dodge/2 + turi.defensa/2

		if turi.vida <0:

			break
			
		time.sleep(1.5)
		print(turi.nombre,at,'a',maja.nombre)
		#esta formula se puede mejorar 
		maja.vida = maja.vida - turi_ataca + maja.dodge/2 + maja.defensa

		if maja.vida < 0:

			break

if maja.vida > turi.vida:

	print('\nEl',turi.nombre,'cae de rodillas to pajareao...')
	print()
	print('Solo un',maja.raza,'de Santamaria podia salir victorioso jeje.')

else:

	print('\nLos',turi.raza+'s la echan buena con el regueton. Au voir!')
	print()
	print('El',maja.nombre,'veia como el',turi.nombre,'sacaba el pelt string...')





