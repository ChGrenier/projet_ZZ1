import random as R
import meilleur as Me
import gestion_cubes as g

def ponderation(liste_fig):
	"""
	retourne la liste ponderee et normee des sous solutions
	"""
	liste_pond=[]
	for i in range (len(liste_fig)):
		liste_pond.append(float(Me.nb_cube(liste_fig[i]))/float(len(g.objets_cubes)))
	return liste_pond


def choix_pond(liste_pond):
	#print("choix_pond")
	"""
	choix stochastique de la figure "porteuse"
	nb est initialise a 1-rnd car random() prends ses valeurs sur [0,1[ et on veut nos valeurs sur ]0,1]
	ceci ne change rien a la modelisation si on assimile les float a un interval continu
	"""
	i = 0
	cpt = 0
	nb = 1-R.random()
	while (nb>cpt and i<len(liste_pond)):
		#print(i, cpt, nb, liste_pond)
		cpt += liste_pond[i]
		i += 1
	return i-1

def choix_alea(liste_fig):
	#print("choix_alea")
	"""
	choix aleatoire de la figure "donneuse"
	"""
	nb = R.randint(0,len(liste_fig))-1
	return nb

