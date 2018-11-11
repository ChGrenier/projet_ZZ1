import sys

class Cube () :
    def __init__(self,  position,  L_faces,  numero,  L_voisins, angle):
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
        self.orientation = 	L_faces[0]
        self.L_faces = 		L_faces
        self.num = 		numero
        self.L_voisins = 	L_voisins
	self.angle = 		angle
        
    def rotation(self,  axe,  nb_rot):
	"""
	definit le mouvement des face lors de la rotation du cube selon les axes X, Y ou Z dans le sens direct; gere egalement la modification de l'angle de la forme 
	nb_rot : 	nombre de rotation de 90 deg a faire : 1 = 1/4 de tour, 2 = 1/2 tour, 3 = -1/4 de tour
	axe : 		axe autour duquel aura lieu la rotation : "X", "Y", ou "Z"
	"""
        if axe == "X" :
            for i in range (nb_rot):
                temp=self.L_faces[0] #permutaion circulaire
                self.L_faces[0] = self.L_faces[1]
                self.L_faces[1] = self.L_faces[5]
                self.L_faces[5] = self.L_faces[3]
                self.L_faces[3] = temp
		#2 et 4 ne font que tourner
                self.angle*=-1

                
        elif axe == "Y":
            for i in range (nb_rot):
                temp=self.L_faces[1] #permutaion circulaire
                self.L_faces[1] = self.L_faces[4]
                self.L_faces[4] = self.L_faces[3]
                self.L_faces[3] = self.L_faces[2]
                self.L_faces[2] = temp
		#0 et 5 ne font que tourner
                self.angle*=-1
                
        elif axe == "Z":
            for i in range (nb_rot):
                temp=self.L_faces[0] #permutaion circulaire
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
	longueur : 	longueur de la forme a obtenir, dimension selon X, a recuperer dans Figure
	largeur : 	largeur de la forme a obtenir, dimension selon Y, a recuperer dans Figure
	hauteur : 	hauteur de la forme a obtenir, dimension selon Z, a recuperer dans Figure
	"""
        if axe == "X": #deplacement du cube selon l'axe X
            self.X += nb_depl
            if self.X > longueur : sys.exit ("X hors cube")
        
        elif axe == "Y": #deplacement du cube selon l'axe Y
            self.Y += nb_depl
            if self.Y > largeur : sys.exit ("Y hors cube")
        
        elif axe == "Z": #deplacement du cube selon l'axe Z
            self.Z += nb_depl
            if self.Z > hauteur : sys.exit ("Z hors cube")
        
        
        

#    def compatibilite(self):
#	"""
#	retourne True si un cube peu bien etre place a l'endroi designe et False sinon
#	compare les faces en contacte (forme, complementarite) et verifie que les cubes sont sous le meme angle entre un cube et chacun de ses voisins
#	"""
#        if
        
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Face () : #vraiment utile ???
    def __init__(self,  forme, orientation_face):
	"""
	forme : 	identifiant de la forme presente sur la face, positif pour les males, negatif pour les femmelles
	orientation : 	forme horizontale ou verticale
	"""
        self.forme =		forme
        #self.orientation =	orientaion_face
    
    def comparaison(self,  face_aj): #ARP?
	"""
	retourn True si deux faces sont compatible et False sinon
	compare la forme, la compementarite et l'angle des faces designee
	face_aj : 	face avec laquelle est faite la comparaison
	"""
        return (self.forme + face_aj.forme == 0) #ne necessite de verifier l'orientation que d'une seul face (ex : celle du bas)
#orientaition a verifier dans le cube


#    def rotation(self):
#	"""
#	modifi l'orientation des faces lors de la rotation du cube
#	*-1 = rotation de 90 deg
#	"""
#        return(self.orientation * -1)#toutes les faces change d'orientation lors de la rotation... -> mettre la rotation dans "Cube" ?

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Figure () : #gerer la figure finale (longeur, largeur, hauteur) a obtenir et les voisins de chaque cubes
    def __init__(self,  dimension):
	"""
	longueur : 	longeur de la forme a obtenir, dimension selon X
	largeur : 	largeur de la forme a obtenir, dimension selon Y
	hauteur : 	hauteur de la forme a obtenir, dimension selon Z
	"""
        self.longueur =		dimension[0]
        self.largeur =		dimension[1]
        self.hauteur =		dimension[2]
        
    def init_fig (self):
	"""
	initialise a 0 la matrice 3D de la forme a realiser
	forme de type parallellepipede rectangle : longeur, largeur, hauteur
	longueur : 	longeur de la forme a obtenir, dimension selon X
	largeur : 	largeur de la forme a obtenir, dimension selon Y
	hauteur : 	hauteur de la forme a obtenir, dimension selon Z
	"""
	return([[[0 for k in range(self.hauteur)] for j in range(self.largeur)]for i in range(self.longueur)])

    def placer_cube(self, position, cube, figure):
	"""
	place un cube dans la matrice de la forme et met a jour la liste des voisins de ce cube et de ceux autour
	position :	coordonnees ou l'on veux placer le cube dans la forme, triplet
	cube :		cube a placer, de type Cube
	figure :	figure a obtenir, matrice 3D
	"""
	#penser a verifer que position est dans la figure
	if position[0] < longueur and position[1] < largeur and position[2] < hauteur :
		figure[position[0]][position[1]][position[2]] = cube
		

"""
placer pas a metre ici... figure pas besoin d'etre une classe...
a metre dans le programme principale
"""

