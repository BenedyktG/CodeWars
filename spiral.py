import numpy as np


def createSpiral(n):
    output = []
    count = 1
    temp = np.zeros((n, n), dtype=int)
    i = 0
    j = 0
    if isinstance(n, int) and n > 1:

        while 0 in temp:
            temp[i][j] = count
            try:
                if temp[i][j + 1] == 0 or temp[i][j + 1] != 0:
                    if temp[i][j + 1] == 0:
                        j += 1
                        count += 1
                    if j == n - 1 or temp[i][j + 1] != 0:
                        i += 1
                    try:
                        if temp[i + 1][j] != 0:
                            j -= 1

                    except:
                        j -= 1
            except IndexError:
                i += 1





    else:
        return output


createSpiral(3)
