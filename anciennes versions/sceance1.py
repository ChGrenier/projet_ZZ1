import sys

class Cube :
    def __init__(self,  position,  L_faces,  numero,  L_voisins):
        self.X=position[0] #X #position dans le cube 3x3x3
        self.Y=position[1] #Y
        self.Z=position[2] #Z
        self.orientation=L_faces[0] #id de la face en bas
        self.L_faces=L_faces #liste de la position de chaque face
        self.num=numero #identifiant du cube
        self.L_voisins=L_voisins #liste des voisins du cube
        
    def rotation(self,  axe,  nb_rot):
        if axe=="X" : #rotation du cube autour de l'axe X dans le sens direct
            for i in range (nb_rot): #nombre de rotation : 1 = 1/4 de tour, 2 = 1/2 tour, 3 = -1/4 de tour
                temp=self.L_faces[0] #permutaion circulaire
                self.L_faces[0]=self.L_faces[1]
                self.L_faces[1]=self.L_faces[5]
                self.L_faces[5]=self.L_faces[3]
                self.L_faces[3]=temp
                self.face.rotation(self.L_face[2]) #rotation de 90deg des faces qui ne bouge pas
                self.face.rotation(self.L_face[4])
                
        elif axe=="Y": #rotation du cube autour de l'axe Y dans le sens direct
            for i in range (nb_rot): #nombre de rotation : 1 = 1/4 de tour, 2 = 1/2 tour, 3 = -1/4 de tour
                temp=self.L_faces[1] #permutaion circulaire
                self.L_faces[1]=self.L_faces[4]
                self.L_faces[4]=self.L_faces[3]
                self.L_faces[3]=self.L_faces[2]
                self.L_faces[2]=temp
                self.face.rotation(self.L_face[0]) #rotation de 90deg des faces qui ne bouge pas
                self.face.rotation(self.L_face[5])
                
        elif axe=="Z": #rotation du cube autour de l'axe Z dans le sens direct
            for i in range (nb_rot): #nombre de rotation : 1 = 1/4 de tour, 2 = 1/2 tour, 3 = -1/4 de tour
                temp=self.L_faces[0] #permutaion circulaire
                self.L_faces[0]=self.L_faces[4]
                self.L_faces[4]=self.L_faces[5]
                self.L_faces[5]=self.L_faces[2]
                self.L_faces[2]=temp
                self.face.rotation(self.L_face[1]) #rotation de 90deg des faces qui ne bouge pas
                self.face.rotation(self.L_face[3])
    
    
    def deplacement(self,  axe,  nb_depl,  longueur,  largeur,  hauteur):
        if axe=="X": #deplacement du cube selon l'axe X
            self.X+=nb_depl #nb de deplacement de 1
            if self.X>longueur : sys.exit ("X hors cube") #si on sort du cube le programme s'arrete
        
        elif axe=="Y": #deplacement du cube selon l'axe Y
            self.Y+=nb_depl #nb de deplacement de 1
            if self.Y>largeur : sys.exit ("Y hors cube") #si on sort du cube le programme s'arrete
        
        elif axe=="Z": #deplacement du cube selon l'axe Z
            self.Z+=nb_depl #nb de deplacement de 1
            if self.Z>hauteur : sys.exit ("Z hors cube") #si on sort du cube le programme s'arrete
        
        
        
    
    #def compatibilite(self):
        #if #comparaison des faces et angle des faces pour chacun des voisins
        
        
        


class Face :
    def __init__(self,  forme, orientation_face):
        self.forme=forme #positif = bosse, negatif = creux
        self.orientation=orientaion_face #1 ou -1 pour 0 et 90°
    
    def comparaison(self,  face_aj): #vrai si meme orientation et faces complementaires
        return (self.orientation==face_aj.orientation and self.forme + face_aj.forme == 0):


    def rotation(self):
        return(self.orientation*=-1) # * -1 = rotation de 90°
    
    

class Figure : #gerer la figure finale (longeur, largeur, hauteur) à obtenir et les voisins de chaque cubes
    def __init__(self,  dimension):
        self.longueur=dimension[0] #X
        self.largeur=dimension[1] #Y
        self.hauteur=dimension[2] #Z
        
    def init_fig (self,  longueur,  largeur,  hauteur): #liste de liste de liste, lol
        [[[0 for i in range(longueur)] for j in range(largeur)]for k in range(hauteur)] #initialisee à 0




