"""
contient les appels de test des fonctions
"""

import definition_cube as d
import ordres as o
import gestion_cubes as g

print g.faces_cubes
print g.objets_cubes
print g.objets_cubes[2].L_faces
print g.Figure

g.objets_cubes[2].rotation("X", 1)

print g.objets_cubes[2].L_faces
print g.objets_cubes[2].angle


g.placer_cube((1,1,1), 24, g.Figure, g.objets_cubes)

print ('coordonnees de 24 : ', g.objets_cubes[24].X, g.objets_cubes[24].Y, g.objets_cubes[24].Z)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
g.afficher_fig(g.Figure)


g.placer_cube((1,1,0), 20, g.Figure, g.objets_cubes)

print ('coordonnees de 20 : ', g.objets_cubes[20].X, g.objets_cubes[20].Y, g.objets_cubes[20].Z)
print ('voisins de 20 : ', g.objets_cubes[20].L_voisins)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
g.afficher_fig(g.Figure)

g.placer_cube((1,2,0), 7, g.Figure, g.objets_cubes)

print ('coordonnees de 7 : ', g.objets_cubes[7].X, g.objets_cubes[7].Y, g.objets_cubes[7].Z)
print ('voisins de 7 : ', g.objets_cubes[7].L_voisins)
print ('voisins de 20 : ', g.objets_cubes[20].L_voisins)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
g.afficher_fig(g.Figure)

g.placer_cube((1,2,1), 7, g.Figure, g.objets_cubes)

print ('coordonnees de 7 : ', g.objets_cubes[7].X, g.objets_cubes[7].Y, g.objets_cubes[7].Z)
print ('voisins de 7 : ', g.objets_cubes[7].L_voisins)
print ('voisins de 20 : ', g.objets_cubes[20].L_voisins)
print ('voisins de 24 : ', g.objets_cubes[24].L_voisins)
g.afficher_fig(g.Figure)
