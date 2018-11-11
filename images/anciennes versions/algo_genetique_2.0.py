import gestion_cubes as g
import mutation as Mut
import meilleur as Me
import croisement as C
import random as R
import tirage as t
import ordres as o



nb_iter_max = 10000

def gen(dico_cube):
	"""
	applique l'algo gén à un dico pour construire la figure entrée en paramètres
	"""
	liste_fig=[]
	liste_c= gf.Cubes_libre_fig(figure)#liste_cube(dico_cube) a faire
	for i in range(len(liste_c)) :
		liste_fig.append(gf.init_fig(o.hauteur, o.largeur, o.longeur))
		placer_cube((0, 0, 0), dico_cube[liste_c[i]], liste_fig[i], dico_cube)

	i=0
	while (non(est_pleine(liste_fig)) and i<nb_iter_max): 

		liste_pond=t.ponderation(liste_fig)

		place_p=t.choix_pond(liste_pond)

		porteuse=liste_fig.pop([place])

		place_d=t.choix_alea(liste_fig)

		donneuse=liste_fig.pop([place_d])

		porteuse_temp=porteuse
		donneuse_temp=donneuse#matrice 3D

		C.croisement(porteuse_temp,donneuse_temp)#le croisement ne se fait pas toujourd (false si non fait), si non fait modifier critere elitise
		mut= Rnd.randint(1,100)

		if mut==1:
			Mut.muation(porteuse_temp)

		if Me. nb_cube(porteuse_temp)>Me. nb_cube(porteuse): #tester si il y a des figure vide dans la liste des figure
			liste_fig.append(porteuse_temp)
			liste_fig.append(donneuse_temp)

		else:
			liste_fig.append(porteuse)
			liste_fig.append(donneuse)
		
	return liste_fig

