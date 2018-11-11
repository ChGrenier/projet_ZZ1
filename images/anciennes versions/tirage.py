
def ponderation(liste_fig):
	"""
	retourne la liste pondérée et normée des sous soulutions
	"""
	liste_pon=[]
	for i in range len(liste_fig):
		liste_pond.append(nb_cube(liste_fig[i])/27)
	return liste_pond


def choix_pond(liste_pond):
	"""
	choix stochastique de la figure "porteuse"
	nb est initialisé à 1-rnd car random() prends ses valeurs sur [0,1[ et on veut nos valeurs sur ]0,1]
	ceci ne change rien à la modélisation si on assimile les float à un interval continu
	"""
	i = 0
	cpt = 0
	nb = 1-Rnd.random()
	while nb>cpt:
		cpt += liste_pond[i]
		i += 1
	return i-1

def choix_alea(liste_fig):
	"""
	coix aléatoire de la figure "donneuse"
	"""
	nb = Rnd.randint(0,len(liste_fig))
	return nb

