def check_rows(grid): #Function that checks if a row is valid
    for i in grid:
        for j in i:
            if j != 0:
                contador = i.count(j)
                if contador != 1:
                    return False
    return True

def check_cols(grille): #Function that transforms a column into a row and calls the check_rows function to verify if it is valid
    coluna1 = []
    coluna2 = []
    coluna3 = []
    coluna4 = []
    coluna5 = []
    coluna6 = []
    coluna7 = []
    coluna8 = []
    coluna9 = []
    for i in grille:
        coluna1.append(i[0])
    for i in grille:
        coluna2.append(i[1])
    for i in grille:
        coluna3.append(i[2])
    for i in grille:
        coluna4.append(i[3])
    for i in grille:
        coluna5.append(i[4])
    for i in grille:
        coluna6.append(i[5])
    for i in grille:
        coluna7.append(i[6])
    for i in grille:
        coluna8.append(i[7])
    for i in grille:
        coluna9.append(i[8])
    matriz = [coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7, coluna8, coluna9]
    return check_rows(matriz)

def check_regions(grille): #Function that uses the previous functions to verify if a 3x3 region is valid
    region1 = [grille[0][0], grille[0][1], grille[0][2], grille[1][0], grille[1][1], grille[1][2], grille[2][0], grille[2][1], grille[2][2]]
    region2 = [grille[0][3], grille[0][4], grille[0][5], grille[1][3], grille[1][4], grille[1][5], grille[2][3], grille[2][4], grille[2][5]]
    region3 = [grille[0][6], grille[0][7], grille[0][8], grille[1][6], grille[1][7], grille[1][8], grille[2][6], grille[2][7], grille[2][8]]
    region4 = [grille[3][0], grille[3][1], grille[3][2], grille[4][0], grille[4][1], grille[4][2], grille[5][0], grille[5][1], grille[5][2]]
    region5 = [grille[3][3], grille[3][4], grille[3][5], grille[4][3], grille[4][4], grille[4][5], grille[5][3], grille[5][4], grille[5][5]]
    region6 = [grille[3][6], grille[3][7], grille[3][8], grille[4][6], grille[4][7], grille[4][8], grille[5][6], grille[5][7], grille[5][8]]
    region7 = [grille[6][0], grille[6][1], grille[6][2], grille[7][0], grille[7][1], grille[7][2], grille[8][0], grille[8][1], grille[8][2]]
    region8 = [grille[6][3], grille[6][4], grille[6][5], grille[7][3], grille[7][4], grille[7][5], grille[8][3], grille[8][4], grille[8][5]]
    region9 = [grille[6][6], grille[6][7], grille[6][8], grille[7][6], grille[7][7], grille[7][8], grille[8][6], grille[8][7], grille[8][8]]
    for j in region1:
        if j != 0:
            contador = region1.count(j)
            if contador != 1:
                return False
    for j in region2:
        if j != 0:
            contador = region2.count(j)
            if contador != 1:
                return False
    for j in region3:
        if j != 0:
            contador = region3.count(j)
            if contador != 1:
                return False
    for j in region4:
        if j != 0:
            contador = region4.count(j)
            if contador != 1:
                return False
    for j in region5:
        if j != 0:
            contador = region5.count(j)
            if contador != 1:
                return False
    for j in region6:
        if j != 0:
            contador = region6.count(j)
            if contador != 1:
                return False
    for j in region7:
        if j != 0:
            contador = region7.count(j)
            if contador != 1:
                return False
    for j in region8:
        if j != 0:
            contador = region8.count(j)
            if contador != 1:
                return False
    for j in region9:
        if j != 0:
            contador = region9.count(j)
            if contador != 1:
                return False
    return True

def check_sudoku(grille): # Function to check if a given soluction is valid
    if check_regions(grille) == True and check_cols(grille) == True and check_rows(grille) == True:
        return True
    return False

def naked_single(grid): # Function that iterates over itself solving the puzzle if possible
    nova_grille = grid.copy()
    dicionario = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if nova_grille[i][j] == 0:
                possibilidades = []
                for n in range(1, 10):
                    nova_grille[i][j] = n
                    if check_sudoku(nova_grille) == True:
                        possibilidades.append(n)
                if possibilidades != []:
                    dicionario.update({(i, j): possibilidades})
                nova_grille[i][j] = 0
    contador = 0
    for k in dicionario.keys():
        if len(dicionario[k]) != 1:
            contador += 1
    if contador == len(dicionario):
        return (False, None)
    for k in dicionario.keys():
        if len(dicionario[k]) == 1:
            nova_grille[k[0]][k[1]] = dicionario[k][0]
    for i in nova_grille:
        for j in i:
            if j == 0:
                naked_single(nova_grille)
    return (True, nova_grille)

grille = [[0, 0, 6, 0, 4, 0, 1, 0, 0],
              [0, 5, 0, 0, 9, 0, 0, 6, 0],
              [8, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 0, 0, 3, 0, 4, 0, 0, 0],
              [3, 1, 0, 0, 0, 0, 0, 4, 8],
              [0, 0, 0, 8, 0, 7, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 2, 0, 0, 3, 0, 0, 5, 0],
              [0, 0, 1, 0, 5, 0, 7, 0, 0]]

print(naked_single(grille))