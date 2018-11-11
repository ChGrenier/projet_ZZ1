import gestion_cubes as g
import mutation as Mut
import meilleur as Me
import croisement as C
import random as R
import tirage as t
import ordres as o
import gestion_figure as gf



nb_iter_max = 10000

def gen(dico_cube):
	"""
	applique l'algo gen a un dico pour construire la figure entree en parametres
	"""
	liste_fig=[]
	liste_c= g.liste_cube(dico_cube)
	#print(liste_c)
	for i in range(len(liste_c)) :
		#print("ici")
		liste_fig.append(gf.init_fig(o.hauteur, o.largeur, o.longueur))
		#print(dico_cube[liste_c[i]])
		g.placer_cube((0, 0, 0), liste_c[i], liste_fig[i], dico_cube)
		#gf.afficher_fig(liste_fig[i])

	i=0
	while (not(Mut.est_pleine(liste_fig)) and i<nb_iter_max and len(liste_fig)>=2): 
		#print("s")
		#print(i)
		#for j in liste_fig : 
		#	gf.afficher_fig(j)

		
		liste_pond=t.ponderation(liste_fig)

		place_p=t.choix_pond(liste_pond)

		porteuse=liste_fig.pop(place_p)

		place_d=t.choix_alea(liste_fig)

		donneuse=liste_fig.pop(place_d)

		porteuse_temp=porteuse
		donneuse_temp=donneuse#matrice 3D

		
		#gf.afficher_fig(porteuse_temp)
		#gf.afficher_fig(donneuse_temp)


		croismnt=C.croisement(porteuse_temp,donneuse_temp, dico_cube)
		mut= R.randint(1,10)

		if (mut==1 and Me.nb_cube(donneuse_temp)):
			Mut.mutation(porteuse_temp, liste_fig, dico_cube)

		if (Me.nb_cube(porteuse_temp)>=Me.nb_cube(porteuse) and croismnt):
			liste_fig.append(porteuse_temp)
		else:
			liste_fig.append(porteuse)

		if (Me.nb_cube(donneuse_temp)!=0):#on rement la donneuse dans la liste que si elle est non vide
			liste_fig.append(donneuse_temp)
		else:
			liste_fig.append(donneuse)

		if not(i%100):
			print(i)
			#print(len(liste_fig))
		#	gf.afficher_fig(porteuse_temp)
		#	gf.afficher_fig(donneuse_temp)
		liste_fig=gf.en_double(liste_fig)
		liste_fig=gf.doublon(liste_fig)
		i+=1
		
#a chaque tour il faudrai enlever les figures en double et celle qui ont plusieur fois le meme cube
	return liste_fig

