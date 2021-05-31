import random
def incepe_jocul():
    mat =[]
    for i in range(4):
        mat.append([0]*4)
        print("Comenzile sunt urmatoarele:")
        print("W sau w pentru a merge in sus")
        print("S sau s pentru a merge in jos")
        print("A sau a pentru a merge la stanga")
        print("D sau d pentru a merge la dreapta")
        adauga_nou_2(mat)
        return mat
def adauga_nou_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while(mat[r] !=0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        mat[r]=2
def status_joc(mat):
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'Ai castigat!'
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'Jocul nu s-a terminat'
    for i in  range(3):
        for j in range(3):
            if(mat[i][j]== mat[i+1][j] or mat[i][j]== mat[i][j+1]):
                return 'Jocul nu s-a terminat'
    for j in range(3):
        if(mat[3][j]== mat[3][j+1]):
            return 'Jocul nu s-a terminat'
    for i in range(3):
        if(mat[i][3]== mat[i+1][3]):
            return 'Jocul nu s-a terminat'
    return 'Ai pierdut'
def compresie(mat):
    changed = False
    nou_mat= []
    for i in range(4):
        nou_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            pos = 0
            for j in range(4):
                if(mat[i][j] !=0):
                    nou_mat[i][pos]=mat[i][j]
                    if(j != pos):
                        changed = True
                    pos += 1
    return nou_mat , changed
def schmb(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed
def inversare(mat):
    nou_mat =[]
    for i in range(4):
        nou_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return nou_mat
def transp(mat):
    nou_mat =[]
    for i in range(4):
        nou_mat.append([])
        for j in range(4):
            nou_mat[i].append(mat[j][i])
    return nou_mat
def mrg_stanga(grid):
    nou_mat, changed1 = compresie(grid)
    nou_mat, changed2 = schmb(nou_grid)
    changed = changed1 or changed2
    nou_grid, temp = compresie(nou_grid)
    return nou_grid, changed
def mrg_dreapta(grid):
    nou_grid = inversare(grid)
    nou_grid, changed = mrg_stanga(nou_grid)
    nou_grid = inversare(nou_grid)
    return nou_grid, chnaged
def mrg_sus(grid):
    nou_grid = transp(grid)
    nou_grid, changed = mrg_stanga(nou_grid)
    nou_grid = transp(nou_grid)
    return nou_grid, changed
def mrg_jos(grid):
    nou_grid = transp(grid)
    nou_grid, changed = mrg_dreapta(nou_grid)
    nou_grid = transp(nou_grid)
    return nou_grid, changed
