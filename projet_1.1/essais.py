#---liste des cubes dans la figure-----------------------------------------------------------------------------------------------------------------------------------------------

def liste_cube_fig(figure):
	cube=[]
	for i in range (len(figure)):
		for j in range (len(figure[0])):
			for k in range (len(figure[0][0])):
				if figure[i][j][k].num!=0 :
					cube.append(figure[i][j][k].num)
	return cube

#---suppresion des figure en double dans la liste des sous solution--------------------------------------------------------------------------------------------------------------

def en_double(liste_fig) :
	for i in liste_fig :
		if liste_fig.count(i)>1 :
			liste_fig.remouve(i)
	return(liste_fig)


#----supression des figure contenant des cubes en double-------------------------------------------------------------------------------------------------------------------------

def doublon(liste_fig):
	for i in liste_fig :
		lst=liste_cube_fig(i)
		dbl=False
		j=0
		while not dbl and j<len(lst) :
			dbl=not(lst.count(lst[j])==1 or lst[j]==0)
		if dbl :
			liste_fig.remouve(i)
	return(liste_fig)

L=[

en_double(L)
doublon(L)
print(L)

