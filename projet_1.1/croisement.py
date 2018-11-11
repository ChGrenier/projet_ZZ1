import gestion_cubes as g
import gestion_figure as gf
import mutation as Mut

#----croisement de deux figure---------------------------------------------

def croisement(porteuse_temp,donneuse_temp, dico_cube):
	#print("croisement")
	liste_cube_donn= gf.liste_cube_fig(donneuse_temp) #liste_cube_fig
	liste_pos_por=Mut.Pos_libre(porteuse_temp)
	ajouter=False
	cpt_c=0
	cpt_pos=0
	cpt_rot_x=0
	cpt_rot_y=0
	cpt_rot_z=0
	
	while (not ajouter and cpt_c<len(liste_cube_donn)):
		cube=dico_cube[liste_cube_donn[cpt_c]]
		while (not ajouter and cpt_pos<len(liste_pos_por)):
			while (not ajouter and cpt_rot_x<3):
				while (not ajouter and cpt_rot_y<3):
					while (not ajouter and cpt_rot_z<3):
						ajouter=g.placer_cube(liste_pos_por[cpt_pos], liste_cube_donn[cpt_c], porteuse_temp, dico_cube)
						cube.rotation('Z', 1)
						cpt_rot_z+=1
					cube.rotation('Y', 1)
					cpt_rot_y+=1
				cube.rotation('X', 1)
				cpt_rot_x+=1
			cpt_pos+=1
		cpt_c+=1
	return ajouter#croisement fait ou non ?


