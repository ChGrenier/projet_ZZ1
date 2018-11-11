import random as R
import gestion_cubes as g
import gestion_figure as gf
import ordres as o

#----liste des position libres---------------------------------------------------------------------------------------------------------------------------------------------------

def Pos_libre(figure):
	"""
	costitution de la liste des positions encore libre dans la figure
	pos_libres :	liste des positions encore libre dans la figure
	figure :	figure a obtenir, matrice 3D
	"""
	pos_libres=[]
	for i in range (len(figure)):
		for j in range (len(figure[0])):
			for k in range (len(figure[0][0])):
				if figure[i][j][k].num==0 :
					pos_libres.append((i, j, k))
	return pos_libres


#---ya il une figure pleine ?----------------------------------------------------------------------------------------------------------------------------------------------------

def est_pleine(liste_fig):
	"""
	definit si une liste de figure comprend une figure pleine
	liste_fig = liste des sous solutions
	"""
	plein=False
	cpt=0
	while (not plein and cpt<len(liste_fig)):
		plein=(len(Pos_libre(liste_fig[cpt]))==0)
		cpt+=1
	return plein
		

#----mutation--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mutation(figure, liste_fig, dico_cube):
	#print("mutation")
	"""
	fait une mutation sur la figure
	"""
	#print(gf.liste_cube_fig(figure))
	cube_m=R.choice(gf.liste_cube_fig(figure))#int
	g.retirer_cube_C(cube_m, figure, dico_cube)
	axe=R.choice(['X','Y','Z'])
	dico_cube[cube_m].rotation(axe,2)

	place=False
	cpt=0
	position=Pos_libre(figure)
	print(position)
	while (not place and cpt<len(position)):
		place=g.placer_cube(position[cpt], cube_m, figure, dico_cube)
		cpt+=1

	if (not place) :
		liste_fig.append(gf.init_fig(o.hauteur, o.largeur, o.longueur))
		#print(liste_fig)
		g.placer_cube((0, 0, 0), cube_m, liste_fig[-1], dico_cube)

	








	

