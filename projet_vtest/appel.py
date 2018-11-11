import algo_genetique as ag
import gestion_cubes as g
import gestion_figure as gf
import mutation as Mut


liste=ag.gen(g.objets_cubes)

solution=[]
for i in liste:

	if not Mut.Pos_libre(i) :
		solution=i

if (solution):
	print('solution :')
	gf.afficher_fig(solution)
	print('cubes avec leur faces :')
	for i in range(len(solution)):
		for j in range(len(solution[0])):
			for k in range(len(solution[0][0])):
				L_vois=g.MAJ_L_voisins(g.objets_cubes, solution[i][j][k].num, solution)
				print("{0} : {1}" .format(solution[i][j][k].num, solution[i][j][k].L_faces))
				
else :
	print("pas de solution trouvee")
