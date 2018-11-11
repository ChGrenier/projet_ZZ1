import definition_cube as d
import ordres as o
import gestion_cubes as g
import tirage as ti

import meilleur as me
import mutation as mu

import random as R

L_S = [i for i in range(1,28)]	#initialisation de la liste des sous solutions
L_P = [1 for i in range(1,28)]	#initialisation de la liste des ponderations
cpt_it = 0			#compteur d'iteration
N = 2000			#nombre d'iteration maximal


while not conforme(solution) and cpt_it < N :		#tant que la solution ne convient pas 			(encore a ecrire)

	sous_sol_1 = ti.selection_stoch(L_S, L_P)	#tirage stochastique de la sous solution 1 		(encore a ecrire)
	pond1 = L_P[L_S.index(sous_sol_1)]
	L_P.remove(pond1)				#on supprime sa ponderation
	L_S.remove(sous_sol_1)				#on la retire de la liste des sous solutions

	id = R.randint(len(L_S))
	sous_sol_2 = L_S[id]				#tirage aleatoire de la sous solution 2
	pond2 = L_P[L_S.index(sous_sol_2)]
	L_P.remove(pond2)				#on supprime sa ponderation
	L_S.remove(sous_sol_2)				#on la retire de la liste

	nouv_SS = croisement(sous_sol_1, sous_sol_2)	#croisement des deux sous solutions 			(encore a ecrire)
	mu.mutation(nouv_SS)				#mutation de la nouvelle sous solution obtenue 		(encore a ecrire), faire un tirage aleatoire avant ?
	
	if me.meilleur(nouv_SS, sous_sol_1) :		#on compare la nouvelle sous solution a la sous solution 1 (tiree par ponderation)
		L_S.append(nouv_SS)			#ajouter la nouvelle sous solution
		L_P.append(ponderation(nouv_SS))	#on ajoute la ponderation de la nouvelle sous solution
	else :
		L_S.append(sous_sol_1)			#si ca ne convient pas on remet les deux sous solutions initiale dans la liste
		L_S.append(sous_sol_2)
		L_P.append(pond1)
		L_P.append(pond2)
	
	cpt_it+=1					#incrementation du compteur d'iteration
