"""
This is some code that solves killer sudoku puzzles
It was written when I was learning how to code and was still a teenager
I think I didn't even have a proper python editor when writing this but I'm unsure.
"""
# this is designed to solve killer sudoku
# square is a 1x1 grid and box is a 3x3 grid

# 123
# 456  #the number for each box
# 789
import copy
import datetime


def solve(supo, sums, sum2, sum3):  # supo=suduko possibilities, sums=list of lists which contain a list of loactions and what they add up to, sum2[x][y] = numbers that can be used to sum to x in y spaces
    global counter
    ri = []  # ri=row impossibilities, all numbers that no unknown square on that row can be
    bi = []  # bi=box impossibilities
    ci = []  # ci=column impossibilities
    for i in range(9):
        r = []
        b = []
        c = []
        for a in range(9):
            if type(supo[i][a]) == int:
                r.append(supo[i][a])
            if type(supo[int((a - (a % 3)) / 3 + (i - (i % 3)))][(a % 3) + 3 * (i % 3)]) == int:
                b.append(
                    supo[int((a - (a % 3)) / 3 + (i - (i % 3)))][(a % 3) + 3 * (i % 3)])  # gets each number in box i
            if type(supo[a][i]) == int:
                c.append(supo[a][i])  # finds all numbers in each row
        ri.append(r)
        bi.append(b)
        ci.append(c)
    sq_solved='true'
    while sq_solved=='true':  # while in last run, a square has been solved.
        sq_solved = 'false'
        # print('did')
        sq = 10
        for sum in sums:
            conb = 'true'  # is the sum contained in a box
            conr = 'true'  # is the sum contained in a row
            conc = 'true'  # is the sum contained in a col
            terms = len(sum[0])  # number of terms in the sum
            for sq in range(len(sum[0]) - 1):  # get each square in each sum
                if ((sum[0][sq][0] // 3) * 3) + (sum[0][sq][1] // 3) != ((sum[0][sq + 1][0] // 3) * 3) + (
                        sum[0][sq + 1][1] // 3):  # check if a square and the next aren't in te same box
                    conb = 'false'
                if sum[0][sq][0] != sum[0][sq + 1][0]:  # check if a square and the next aren't in te same row
                    conr = 'false'
                if sum[0][sq][1] != sum[0][sq + 1][1]:  # check if a square and the next aren't in te same column
                    conc = 'false'
            if conb == 'true' or conr == 'true' or conc == 'true':  # if the sum is in one box,row or col.
                num_in_all = sum3[terms]
                if len(num_in_all) != 0 and sq < terms:  # if there are numbers that must be there and valid square
                    if conb == 'true':  # if everything is in a box
                        # checks each square in the box the sum is contained, but not the sum.
                        # then remove any possibilities that must in the sum.
                        for row in range(3 * (sum[0][sq][0] // 3), 3 * (sum[0][sq][0] // 3) + 3):
                            for col in range(3 * (sum[0][sq][1] // 3), 3 * (sum[0][sq][1] // 3) + 3):
                                if ([row, col] not in sum[0]) and (type(supo[row][col]) != int):
                                    j = -1
                                    while j < len(supo[row][col]) - 1:  # for each possibility, if it must be in the sum, delete it
                                        j += 1
                                        if supo[row][col][j] in num_in_all:
                                            del (supo[row][col][j])
                                            j -= 1
                                    if len(supo[row][col]) == 0:  # if no valid possibilities exist
                                        return 'error'
                                    if len(supo[row][col]) == 1:  # if now solved
                                        sq_solved='true'
                                        supo[row][col] = supo[row][col][0]
                                        ci[col].append(supo[row][col])
                                        ri[row].append(supo[row][col])
                                        bi[int((row - (row % 3)) + (col - (col % 3)) / 3)].append(supo[row][col])
                                        for k in range(len(sums)):
                                            if [row, col] in sums[k][0]:
                                                sums[k][1] -= supo[row][col]
                                                if (sums[k][1] < 0):
                                                    return 'error'
                                                for m in range(len(sums[k][0])):
                                                    if sums[k][0][m] == [row, col]:
                                                        del (sums[k][0][m])
                                                        break
                    if conr=='true':  # if the sum is in row
                        row=sum[0][sq][0]
                        for col in range(9):
                            solves=0
                            if ([row,col] not in sum[0]) and (type(supo[row][col])==list):
                                for j in range(len(supo[row][col])):
                                    if supo[row][col][j-solves] in num_in_all:
                                        del (supo[row][col][j-solves])
                                        solves+=1
                                if len(supo[row][col]) == 0:  # if no possibilities
                                    return 'error'
                                if len(supo[row][col]) == 1:  # if now solved
                                    sq_solved='true'
                                    supo[row][col] = supo[row][col][0]
                                    ci[col].append(supo[row][col])
                                    ri[row].append(supo[row][col])
                                    bi[int((row - (row % 3)) + (col - (col % 3)) / 3)].append(supo[row][col])
                                    for k in range(len(sums)):
                                        if [row, col] in sums[k][0]:
                                            sums[k][1] -= supo[row][col]
                                            if (sums[k][1] < 0):
                                                return 'error'
                                            for m in range(len(sums[k][0])):
                                                if sums[k][0][m] == [row, col]:
                                                    del (sums[k][0][m])
                                                    break
                    if conc=='true':
                        col = sum[0][sq][1]
                        for row in range(3*(sum[0][sq][0]//3),3*(sum[0][sq][0]//3)+3):
                            solves=0
                            if ([row,col] not in sum[0]) and (type(supo[row][col])==list):
                                #print('hello')
                                for j in range(len(supo[row][col])):
                                    if supo[row][col][j-solves] in num_in_all:
                                        del (supo[row][col][j-solves])
                                        solves+=1
                                if len(supo[row][col]) == 0:  # if no possiblies
                                    return 'error'
                                if len(supo[row][col]) == 1:  # if now solved
                                    sq_solved='true'
                                    supo[row][col] = supo[row][col][0]
                                    ci[col].append(supo[row][col])
                                    ri[row].append(supo[row][col])
                                    bi[int((row - (row % 3)) + (col - (col % 3)) / 3)].append(supo[row][col])
                                    for k in range(len(sums)):
                                        if [row, col] in sums[k][0]:
                                            sums[k][1] -= supo[row][col]
                                            if (sums[k][1] < 0):
                                                return 'error'
                                            for m in range(len(sums[k][0])):
                                                if sums[k][0][m] == [row, col]:
                                                    del (sums[k][0][m])
                                                    break
        for row in range(9):
            for col in range(9):  # col for column
                bn = int((row - (row % 3)) + (col - (col % 3)) / 3)  # box number. bi[bn]=all the numbers that square can't be because of the box its in.
                sq = supo[row][col]  # sq is the square we want to deal with
                if type(sq) is list:
                    a = 0
                    sq = sq.copy()
                    si = []
                    for s in sums:
                        if [row, col] in s[0]:
                            si = sum2[len(s[0])][s[1]]  # sum impossiblities
                            break
                    for i in range(len(sq)):  # for each possibility in square
                        if (sq[i] in bi[bn]) or (sq[i] in ci[col]) or (
                                sq[i] in ri[row]) or (
                                sq[i] in si):  # if a possibility is in the row, col, box or cant be in section
                            del (supo[row][col][i - a])
                            a += 1
                    if len(supo[row][col]) == 0:  # if there are no soloutions
                        return 'error'
                    if len(supo[row][col]) == 1:  # if square is now solved
                        sq_solved='true'
                        supo[row][col] = supo[row][col][0]
                        ci[col].append(supo[row][col])
                        ri[row].append(supo[row][col])
                        bi[bn].append(supo[row][col])
                        s[1] = s[1] - supo[row][col]  # s is the index for where in sums sq is
                        for i in range(len(s[0])):  # remove sq from the sum it's in
                            if s[0][i] == [row, col]:
                                del (s[0][i])
                                if (s == [[], 0]) and (s != len(sums) - 1):  # last bit provides robustness
                                    for j in range(len(sums)):
                                        if sums[j] == [[], 0]:
                                            del (sums[j])
                                            break
                                break
    allsolved = 'true'
    for i in range(9):
        if len(ri[i]) != 9:  # if not all rows filled
            allsolved = 'false'
    if allsolved == 'true':
        return supo
    for np in range(2, 10):  # finds location of square with least uncertainty np=number of possibillities
        for row in range(9):
            for col in range(9):
                if type(supo[row][col]) == list:  # if unknown
                    if len(supo[row][col]) == np:  # if least unknowns
                        for i in range(np):  # for each possibility
                            for s in range(len(sums)):
                                if [row, col] in sums[s][0]:
                                    for m in range(len(sums[s][0])):  # removes square from sums2
                                        if [row, col] == sums[s][0][m]:
                                            sums2 = copy.deepcopy(sums)
                                            del (sums2[s][0][m])
                                            testsupo = copy.deepcopy(supo)
                                            sums2[s][1] -= supo[row][col][i]
                                            testsupo[row][col] = testsupo[row][col][i]
                                            test = solve(testsupo, sums2, sum2, sum3)  # test if it is a soloution
                                            if test == 'error':
                                                counter+=1
                                                break
                                            else:
                                                return test
                        return 'error'
    return 'error'


def solved_square(supo,row,col,sums,ci,ri,bi,sum):
    supo[row][col]=supo[row][col][0]
    supo[row][col] = supo[row][col][0]
    ci[col].append(supo[row][col])
    ri[row].append(supo[row][col])
    bi[int((row - (row % 3)) + (col - (col % 3)) / 3)].append(supo[row][col])
    sum[1] = sum[1] - supo[row][col]  # s is the index for where in sums sq is
    for i in range(len(sum[0])):  # remove sq from the sum it's in
        if sum[0][i] == [row, col]:
            del (sum[0][i])
            if (sum == [[], 0]) and (sum != len(sums) - 1):  # last bit provides robustness
                for j in range(len(sums)):
                    if sums[j] == [[], 0]:
                        del (sums[j])
                        break
            break
    return

def sum1(a):  # finds every way to sum a:9
    if a == 9:
        return [[[], 0], [[9], 9]]
    b = sum1(a + 1)  # finds every way to sum a+1:9
    for i in range(len(b)):
        c = b[i]
        c = c.copy()
        d = c[0]
        d = d.copy()
        d = [a] + d  # add another number
        c[1] += a  # increase total
        b.append([d, c[1]])  # add an extra way of summing which includes a
    return b


def sum2():
    a = sum1(1)
    length = len(a)
    sumto = []
    for total in range(46):
        b = []
        for i in range(length):
            if a[i][1] == total:
                b.append(a[i])
        sumto.append(b)
    # sumto[x] gives all ways to sum to x
    # print(sumto)
    sum2 = []
    for length in range(10):
        b = []
        for total in range(46):
            c = []
            for i in range(len(sumto[total])):
                if len(sumto[total][i][0]) == length:
                    c = c + sumto[total][i][0]
            d = []
            for i in range(1, 10):
                if i not in c:
                    d.append(i)
            b.append(d)
        sum2.append(b)
    # sum2[x][y] gives all numbers you cant be used to sum to y if you have x elements
    return sum2


def sum3():
    a = sum1(1)  # every possible sum
    sum3 = []
    for total in range(46):
        sum2total = []
        for length in range(10):  # the length of sums, eg 1+3+5=9 has len 3
            totlen = []
            numinall = []
            for i in a:
                if i[1] == total:
                    if len(i[0]) == length:
                        totlen.append(i[0])
            for num in range(1, 10):  # for each number 1 to 9:
                inall = 'true'
                for sum in totlen:  # for each of the sums, see if the num is in the sum
                    if num not in sum:
                        inall = 'false'
                if inall == 'true':
                    numinall.append(num)  # numbers in all the sums
            sum2total.append(numinall)
        sum3.append(sum2total)
    return sum3


# [sum2,sum3]=sum23()# sum2[x][y] = all the numbers that cant sum to y in x numbers  sum3[x][y]=all combinations to sum to y in x numbers
sum2 = sum2()  # sum2[x][y] gives all numbers you cant use to sum to y if you have x elements
sum3 = sum3()  # sum3[x][y] gives all numbers that must be used to sum to y if you have x elements
#print(sum3[17])
supo = []
for row in range(9):
    d = []
    for col in range(9):
        d.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    supo.append(d)  # gets supo to have every number 1:9 as options in every square
a = datetime.datetime.now()
sums = [[[[0, 0], [1, 0]], 16], [[[0, 1], [1, 1]], 5], [[[0, 2], [0, 3]], 11], [[[0, 4], [1, 4]], 9],
        [[[0, 5], [0, 6]], 7], [[[0, 7], [0, 8], [1, 7]], 13], [[[1, 2], [2, 2]], 13], [[[1, 3], [2, 3]], 6],
        [[[1, 5], [1, 6]], 8], [[[1, 8], [2, 8]], 17], [[[2, 0], [3, 0]], 4], [[[2, 1], [3, 1], [3, 2]], 18],
        [[[2, 4], [2, 5]], 16], [[[2, 6], [3, 6]], 4], [[[2, 7], [3, 7]], 14],
        [[[3, 3], [4, 3], [4, 4], [4, 5], [5, 5]], 26], [[[3, 4], [3, 5]], 8], [[[3, 8], [4, 8]], 7],
        [[[4, 0], [5, 0]], 10], [[[4, 1], [4, 2]], 15], [[[4, 6], [4, 7]], 8], [[[5, 1], [6, 1]], 8],
        [[[5, 2], [6, 2]], 5], [[[5, 3], [5, 4]], 11], [[[5, 6], [5, 7], [6, 7]], 17], [[[5, 8], [6, 8]], 7],
        [[[6, 0], [7, 0]], 13], [[[6, 3], [6, 4]], 10], [[[6, 5], [7, 5]], 9], [[[6, 6], [7, 6]], 14],
        [[[7, 1], [8, 1], [8, 0]], 17], [[[7, 2], [7, 3]], 13], [[[7, 4], [8, 4]], 7], [[[7, 7], [8, 7]], 7],
        [[[7, 8], [8, 8]], 13], [[[8, 2], [8, 3]], 4], [[[8, 5], [8, 6]], 15]]
counter = 0
#for i in sums:
#    i[0], i[1] = i[1], i[0]
c = solve(supo, sums, sum2, sum3)  # solve it
b = datetime.datetime.now()
print('it took:', b - a)
print(counter)
for i in range(9):
    print(c[i])
# [[[[1,1]],5]]
# [[[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]], 45], [[[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1]], 45], [[[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]], 45], [[[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]], 45], [[[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4]], 45], [[[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5]], 45], [[[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6]], 45], [[[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]], 45], [[[0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8]], 45]]
# [[9, [1, 2, 3, 4], [2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]],[[7, 9], [1, 2, 3, 4], [4, 5, 6, 7, 8, 9], [1, 2, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9],[[1, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [1, 2, 4, 5], [7, 9], [7, 9], [1, 3], [5, 6, 8, 9], [8, 9]],[[1, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [1, 3], [5, 6, 8, 9], [1, 2, 3, 4, 5, 6]],[[1, 2, 3, 4, 6, 7, 8, 9], [6, 7, 8, 9], [6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 6]],[[1, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4], [2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6]],[[4, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4], [1, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6]],[[4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 8, 9], [1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]],[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3], [1, 3], [1, 2, 3, 4, 5, 6], [6, 7, 8, 9], [6, 7, 8, 9], [1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]]]
# [[[[0,0],[1,0]],16],[[[0,1],[1,1]],5],[[[0,2],[0,3]],11],[[[0,4],[1,4]],9],[[[0,5],[0,6]],7],[[[0,7],[0,8],[1,7]],13],[[[1,2],[2,2]],13],[[[1,3],[2,3]],6],[[[1,5],[1,6]],8],[[[1,8],[2,8]],17],[[[2,0],[3,0]],4],[[[2,1],[3,1],[3,2]],18],[[[2,4],[2,5]],16],[[[2,6],[3,6]],4],[[[2,7],[3,7]],14],[[[3,3],[4,3],[4,4],[4,5],[5,5]],26],[[[3,4],[3,5]],8],[[[3,8],[4,8]],7],[[[4,0],[5,0]],10],[[[4,1],[4,2]],15],[[[4,6],[4,7]],8],[[[5,1],[6,1]],8],[[[5,2],[6,2]],5],[[[5,3],[5,4]],11],[[[5,6],[5,7],[6,7]],17],[[[5,8],[6,8]],7],[[[6,0],[7,0]],13],[[[6,3],[6,4]],10],[[[6,5],[7,5]],9],[[[6,6],[7,6]],14],[[[7,1],[8,1],[8,0]],17],[[[7,2],[7,3]],13],[[[7,4],[8,4]],7],[[[7,7],[8,7]],7],[[[7,8],[8,8]],13],[[[8,2],[8,3]],4],[[[8,5],[8,6]],15]]
