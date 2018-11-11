"""
contient les appels de test des fonctions
"""

#import definition_cube as d
import ordres as o
import gestion_cubes as g
import gestion_figure as gf
import meilleur as Me
import mutation as Mut

figure=gf.init_fig(o.hauteur, o.largeur, o.longueur)
#print (g.faces_cubes)
#print (g.objets_cubes)
#print (g.objets_cubes[2].L_faces)
#print (gf.Figure)

#g.objets_cubes[2].rotation("X", 1)

#print (g.objets_cubes[2].L_faces)
#print (g.objets_cubes[2].angle)

print(Mut.Pos_libre(figure))

g.placer_cube((0,0,0), 24, figure, g.objets_cubes)

print ('coordonnees de 24 : ', g.objets_cubes[24].X, g.objets_cubes[24].Y, g.objets_cubes[24].Z)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
gf.afficher_fig(figure)

print(Mut.Pos_libre(figure))

g.placer_cube((1,1,0), 20, figure, g.objets_cubes)

print ('coordonnees de 20 : ', g.objets_cubes[20].X, g.objets_cubes[20].Y, g.objets_cubes[20].Z)
print ('coordonnees de 24 : ', g.objets_cubes[24].X, g.objets_cubes[24].Y, g.objets_cubes[24].Z)
print ('voisins de 20 : ', g.objets_cubes[20].L_voisins)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
g.MAJ_L_voisins(g.objets_cubes, 24, figure)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
gf.afficher_fig(figure)
print(Me.nb_cube(figure))

print(Mut.Pos_libre(figure))
