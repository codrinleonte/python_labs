#Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
#  Sa se scrie o functie care primeste ca parametru o lista de puncte si returneaza o lista
#  de tuple (a,b,c) unice care reprezinta dreptele unice determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).

def check_line_coefficients(point, a, b, c):
	if a * point[0] + b * point[1] + c == 0:
		return True
	return False

def getPointsRepresentation(listOfCoordinates):
    listOfLines = []
    search_interval = range(-100, 100)
    for point in listOfCoordinates:
        for a in search_interval:
            for b in search_interval:
                for c in search_interval:
                    if(check_line_coefficients(point,a,b,c) and (a, b, c) not in listOfLines):
                        listOfLines.append((a,b,c))

    return listOfLines

print(getPointsRepresentation([(1,2)]))