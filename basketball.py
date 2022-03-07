import csv
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')


year = random.randrange(1951, 2018)
# year = 1994
filename = 'archive 2/Seasons_Stats.csv'
file = open(filename)

type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)

# print(year)

rows = []
# for i in range(len(header)):
#     print(str(i) + ': ' + header[i])


for row in csvreader:
    if row[1] == str(year):
        fantasypts = int(row[52])+ 2*int(row[47])+int(row[46])
        player = [row[2], row[3], row[5], row[6], row[46], row[47], row[48], row[49], row[52], fantasypts]
        if(len(rows) > 0 and player[0] == rows[-1][0]):
            continue
        rows.append(player)
    elif(row[1] > str(year) and len(rows) > 1):
        break
    else:
        continue

rows = sorted(rows, key=lambda x:x[9], reverse=True)
# rows = sorted(rows, key=lambda x:round(x[9]/float(x[3])), reverse=True)

playerTiers = [[], [], [], [], []]
for i in range(len(rows)):
    # if i == 0: print('A TIER:')
    # if i == 5: print('\nB TIER:')
    # if i == 10: print('\nC TIER:')
    # if i == 15: print('\nD TIER:')
    # if i == 20: print('\nE TIER:')
    if i < 25:
        # print(rows[i][0])
        # playerTiers[int(i/5)].append(rows[i][0])

        if(rows[i][0][-1] == '*'):
            rows[i][0] = rows[i][0][0:(len(rows[i][0]) - 1)]
        playerTiers[int(i/5)].append(rows[i])


newATier = random.sample(playerTiers[0], len(playerTiers[0]))
newBTier = random.sample(playerTiers[1], len(playerTiers[0]))
newCTier = random.sample(playerTiers[2], len(playerTiers[0]))
newDTier = random.sample(playerTiers[3], len(playerTiers[0]))
newETier = random.sample(playerTiers[4], len(playerTiers[0]))

newPlayerTier = [newATier, newBTier, newCTier, newDTier, newETier]
# print('\n')
# print(playerTiers)

from prettytable import PrettyTable
t = PrettyTable([str(year), 'Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5'])




num = 5
char = "a"
for tier in newPlayerTier:
    i = ord(char[0])
    ctrl = ['$' + str(num)]
    for j in range (5):
        # ctrl.append(chr(i + j) + ': ' + tier[j][0] + ' ' + str(tier[j][9]))
        # ctrl.append(chr(i + j) + ': ' + tier[j][0] + ' ' + str(round(tier[j][9]/float(tier[j][3]), 2)))
        ctrl.append(chr(i + j) + ': ' + tier[j][0] +' | ' + str(tier[j][3]) +' games')
    t.add_row(ctrl)
    i += 5
    char = chr(i)
    num = num -1
print(t)



# import pynput
selection = ''
# selection = input()

from pynput.keyboard import Key, Listener

# print('\r you have $15 remaining')
cash = 15
letters = '     '
space = 5
prevlet = ''
print('\t' + letters + '\t\tyou have $'+ str(cash) +' remaining',  end="\r")

def show(key):
    global cash, letters, space, prevlet, selection
    # global letters
    # global space
    # global prevlet
    char = str(key)[1]
    space = space - 1

    letters = prevlet + (space * ' ')


    if key == Key.enter:
        print('\nyoure selection is')
        for let in letters:
            print('\t(' + let + ')', end="\t")
        selection = letters


        return False
    prevlet = prevlet + char
    # char = str(key)[1]
    # if key.isalpha():

        # Stop listener
        # print('\r')
        # return False


    i = ord(char[0])
    i = int(6-((i-96)/5))
    cash = cash-i

    if(cash >=10):
        print('\t' + letters + '\t\tyou have $'+ str(cash) +' remaining\t',  end="\r")
    else:
        print('\t'+ letters + '\t\tyou have $'+ str(cash) +' remaining ',  end="\r")

    #
    # print(num)
    # print('You Entered {0}\n'.format( key))


# Collect all event until released
with Listener(on_press = show) as listener:
    listener.join()

# if len(selection) != 5:
#     return False
    # print ('invalid selection. please pick again')

    # selection = input()

team = []
for i in selection:
    # print (type(ord(i[0])))
    # print
    num = int(ord(i[0])) - 97
    #
    # print (int(num/5))
    # print(int(num%5))
    team.append(newPlayerTier[int(num/5)][int(num%5)])
score = 0
print('\n')
for player in team:
    score += player[9]
    print(player[0], end="\t")
print ('\n')
print('your score is: '+ str(score))
# print ('\n')



combos = []

def findCombinationsUtil(arr, index, num,reducedNum):
    global playerTiers
    # Base condition
    if (reducedNum < 0):
        return

    # If combination is
    # found, print it
    if (reducedNum == 0):
        if(index == 5 and arr[index - 1] <= 5):
            track = [0, 0, 0, 0, 0]
            sum = 0
            for i in range(index):
                fpoints = int(playerTiers[5 - arr[i]][track[arr[i] - 1]][9])
                print(arr[i], end = ", ")
                print(playerTiers[5 - arr[i]][track[arr[i] - 1]][0]+ ', ' + str(fpoints))
                sum = sum + fpoints
                track[arr[i] - 1] = track[arr[i] - 1] + 1
            print(track)
            print(sum)
            combos.append([sum, track])
            print("")

        return

    # Find the previous number stored in arr[].
    # It helps in maintaining increasing order
    prev = 1 if(index == 0) else arr[index - 1]

    # note loop starts from previous
    # number i.e. at array location
    # index - 1
    for k in range(prev, num + 1):

        # next element of array is k
        arr[index] = k

        # call recursively with
        # reduced number
        findCombinationsUtil(arr, index + 1, num,
                                 reducedNum - k)

# Function to find out all
# combinations of positive numbers
# that add upto given number.
# It uses findCombinationsUtil()
def findCombinations(n):

    # array to store the combinations
    # It can contain max n elements
    arr = [0] * n

    # find all combinations
    findCombinationsUtil(arr, 0, n, n)

# Driver code
n = 15;
# findCombinations(n);

combos =[[2, 0, 1, 0, 2], #11355
[2, 0, 0, 2, 1],  #11445
[1, 2, 0, 0, 2],  #12255
[1, 1, 1, 1, 1],  #12345
[1, 1, 0, 3, 0],  #12444
[1, 0, 3, 0, 1],  #13335
[1, 0, 2, 2, 0],  #13344
[0, 3, 0, 1, 1],  #22245
[0, 2, 2, 0, 1],  #22335
[0, 2, 1, 2, 0],  #22344
[0, 1, 3, 1, 0],  #23334
[0, 0, 5, 0, 0]]  #33333

class combination:
    def __init__(self, r=[], i=0, j = []):
        self.arr = r
        self.score = i
        self.roster = j

    def get_data(self):
        print(f'{self.arr} {self.score} {self.roster}')

    def get_score(self):
        return self.score

    def get_roster(self):
        return self.roster

listcombos = []

for comb in combos:
    sum = 0
    savearr = []
    for j in comb:
        savearr.append(j)
    ros = []
    for i in range(len(comb)):
        fpoints = 0
        while (comb[i]> 0):
            fpoints = int(playerTiers[i][comb[i] - 1][9])
            ros.append(playerTiers[i][comb[i] - 1][0])
            # print(comb[i], end = ", ")
            # print(playerTiers[i][comb[i] - 1][0]+ ', ' + str(fpoints))
            sum = sum + fpoints
            comb[i] = comb[i] - 1

    listcombos.append(combination(savearr, sum, ros))
    # print('\n')


listcombos = sorted(listcombos, key=lambda x:x.get_score(), reverse=True)


for thing in listcombos:
    thing.get_data()
#
# sum = 0
# for i in range(index):
#     fpoints = int(playerTiers[5 - arr[i]][track[arr[i] - 1]][9])
#     print(arr[i], end = ", ")
#     print(playerTiers[5 - arr[i]][track[arr[i] - 1]][0]+ ', ' + str(fpoints))
#     sum = sum + fpoints
#     track[arr[i] - 1] = track[arr[i] - 1] + 1
# print(track)
# print(sum)
# combos.append([sum, track])
# print("")

# for comb in combos:
#     print(comb[2])
# # print(min(combos))
# # print(max(combos))
#
# highest = max(combos)[1]
#
# index = 4
# while (index >= 0):
#     if(highest[index] > 0):
#         for j in range(0, highest[index]):
#             guy = playerTiers[5 - index - 1][j]
#             print(guy[0] + ', ' + str(guy[9]))
#     index  = index - 1
