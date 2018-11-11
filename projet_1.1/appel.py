import algo_genetique as ag
import gestion_cubes as g
import gestion_figure as gf
import mutation as Mut

print (g.objets_cubes)
liste=ag.gen(g.objets_cubes)


#print(liste)
#for i in liste :
#	print(len(gf.liste_cube_fig(i)))

for i in liste:
	gf.afficher_fig(i)
	if not Mut.Pos_libre(i) :
		solution=i

gf.afficher_fig(solution)
for i in range(len(solution)):
	for j in range(len(solution[0])):
		for k in range(len(solution[0][0])):
			print("{0} : {1}, {2}" .format(solution[i][j][k].num, solution[i][j][k].L_faces, solution[i][j][k].L_voisins))
			#print("{0} : {1}, ({2}, {3}, {4})" .format(solution[i][j][k].num, solution[i][j][k].L_faces, solution[i][j][k].X, solution[i][j][k].Y, solution[i][j][k].Z))
