"""
contient la definition de l'objet cube et toutes les fonctions associees.
"""

import sys

class Cube () :
    def __init__(self,  position,  L_faces,  numero,  angle):
	"""
    position : 	tuple (triplet) corresonpant a la position (X, Y, Z) dans la forme a obtenir
	orientation : 	identifiant de la face tournee vers le bas
	L_faces : 	liste de la position de chaque face (forme)
	numero : 	identifiant du cube
	L_voisins : 	liste des voisins du cube 
	angle :		forme du bas 'horizontale' ou 'verticale'
	"""
        self.X = 		position[0]
        self.Y = 		position[1]
        self.Z = 		position[2]
        self.L_faces = 		L_faces
        self.num = 		numero
	self.angle = 		angle
        
    def rotation(self,  axe,  nb_rot):
	"""
	definit le mouvement des face lors de la rotation du cube selon les axes X, Y ou Z dans le sens direct; gere egalement la modification de l'angle de la forme 
	nb_rot : 	nombre de rotation de 90 deg a faire : 1 = 1/4 de tour, 2 = 1/2 tour, 3 = -1/4 de tour
	axe : 		axe autour duquel aura lieu la rotation : "X", "Y", ou "Z"
	"""
        if axe == "X" :
            for i in range (nb_rot):
                temp=self.L_faces[0] #permutation circulaire
                self.L_faces[0] = self.L_faces[1]
                self.L_faces[1] = self.L_faces[5]
                self.L_faces[5] = self.L_faces[3]
                self.L_faces[3] = temp
		#2 et 4 ne font que tourner
                self.angle*=-1

                
        elif axe == "Y":
            for i in range (nb_rot):
                temp=self.L_faces[1] #permutation circulaire
                self.L_faces[1] = self.L_faces[4]
                self.L_faces[4] = self.L_faces[3]
                self.L_faces[3] = self.L_faces[2]
                self.L_faces[2] = temp
		#0 et 5 ne font que tourner
                self.angle*=-1
                
        elif axe == "Z":
            for i in range (nb_rot):
                temp=self.L_faces[0] #permutation circulaire
                self.L_faces[0] = self.L_faces[4]
                self.L_faces[4] = self.L_faces[5]
                self.L_faces[5] = self.L_faces[2]
                self.L_faces[2] = temp
		#1 et 3 ne font que tourner
                self.angle*=-1

    
    
    def deplacement(self,  axe,  nb_depl,  longueur,  largeur,  hauteur):
	"""
	definit la modification de la position d'un cube lors de sont deplacement selon X, Y ou Z; gere egalement les eventuelles sorties du cube
	nb_depl : 	nombre de deplacement de 1 souhaite
	longueur : 	longueur de la forme a obtenir, dimension selon X, a recuperer dans la figure
	largeur : 	largeur de la forme a obtenir, dimension selon Y, a recuperer dans la figure
	hauteur : 	hauteur de la forme a obtenir, dimension selon Z, a recuperer dans le figure
	"""
        if axe == "X":
            self.X += nb_depl
            if self.X > longueur : sys.exit ("X hors cube")
        
        elif axe == "Y":
            self.Y += nb_depl
            if self.Y > largeur : sys.exit ("Y hors cube")
        
        elif axe == "Z":
            self.Z += nb_depl
            if self.Z > hauteur : sys.exit ("Z hors cube")
        

