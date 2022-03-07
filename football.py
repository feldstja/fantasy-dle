import csv
import random

class Quarterback:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

class PositPlayer:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')
year = random.randrange(1970, 2020)
filename = 'data_v2/yearly/'+ str(year) +'.csv'
file = open(filename)

type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)
rows = []
quarterbacks = []
anonqb = []
runningbacks = []
anonrb = []
widerecievers = []
anonwr = []
tightends = []
anonte = []
for row in csvreader:
        player = [row[1], row[2], row[3], row[len(row) -1]]
        if row[3] == 'QB' and len(quarterbacks) <5:
            quarterbacks.append(player)
            anonqb.append([row[1]])
        elif row[3] == 'WR' and len(widerecievers) <10:
            widerecievers.append(player)
            anonwr.append([row[1]])
        elif row[3] == 'RB' and len(runningbacks) <10:
            runningbacks.append(player)
            anonrb.append([row[1]])
        elif row[3] == 'TE' and len(tightends) <5:
            tightends.append(player)
            anonte.append([row[1]])
        else:
            continue

quarterbacks = sorted(quarterbacks, key=lambda x:x[3], reverse = True)
widerecievers = sorted(widerecievers, key=lambda x:x[3], reverse = True)
runningbacks = sorted(runningbacks, key=lambda x:x[3], reverse = True)
tightends = sorted(tightends, key=lambda x:x[3], reverse = True)

roster = []
new_quarterbacks = random.sample(quarterbacks, len(quarterbacks))
new_widerecievers = random.sample(widerecievers, len(widerecievers))
new_runningbacks = random.sample(runningbacks, len(runningbacks))
new_tightends = random.sample(tightends, len(tightends))
def choose_team():
    print("\033c", end="")
    print('The year is ' + str(year) + '\n')
    print("Pick a Quarterback:")
    for i in range(len(new_quarterbacks)):
        print(str(i+1) + ': '+ new_quarterbacks[i][0] + ' (' + new_quarterbacks[i][1] + ')')
    qbselection = input()
    while int(qbselection) > 5:
        print('not valid selection')
        qbselection = input()
    print("\033c", end="")
    print('The year is ' + str(year) + '\n')
    print ('Youve selected ' + new_quarterbacks[int(qbselection) - 1][0] + '\n')
    roster.append(new_quarterbacks[int(qbselection) - 1])


    print("Pick a Wide Reciever:")
    for i in range(len(new_widerecievers)):
        print(str(i+1) + ': '+ new_widerecievers[i][0] + ' (' + new_widerecievers[i][1] + ')')
    wrselection = input()
    while int(wrselection) > 10:
        print('not valid selection')
        wrselection = input()
    print("\033c", end="")
    print('The year is ' + str(year) + '\n')
    print ('Youve selected ' + new_widerecievers[int(wrselection) - 1][0] + '\n')
    roster.append(new_widerecievers[int(wrselection) - 1])

    print("Pick a Running Back:")
    for i in range(len(new_runningbacks)):
        print(str(i+1) + ': '+ new_runningbacks[i][0] + ' (' + new_runningbacks[i][1] + ')')
    rbselection = input()
    while int(rbselection) > 10:
        print('not valid selection')
        rbselection = input()
    print("\033c", end="")
    print('The year is ' + str(year) + '\n')
    print ('Youve selected ' + new_runningbacks[int(rbselection) - 1][0] + '\n')
    roster.append(new_runningbacks[int(rbselection) - 1])

    print("Pick a Tight End:")
    for i in range(len(new_tightends)):
        print(str(i+1) + ': '+ new_tightends[i][0] + ' (' + new_tightends[i][1] + ')')
    teselection = input()
    while int(teselection) > 10:
        print('not valid selection')
        teselection = input()
    print("\033c", end="")
    print('The year is ' + str(year) + '\n')
    # print ('Youve selected ' + new_tightends[int(teselection) - 1][0] + '\n')
    roster.append(new_tightends[int(teselection) - 1])

choose_team()

print('Youre roster is: ')
for i in roster:
    print(i[2] + ': ' + i[0] + ' (' + i[1] + ')')

print('\nThe best roster was: ')
print(quarterbacks[0][2] + ': ' + quarterbacks[0][0] + ' (' + quarterbacks[0][1] + ')')
print(widerecievers[0][2] + ': ' + widerecievers[0][0] + ' (' + widerecievers[0][1] + ')')
print(runningbacks[0][2] + ': ' + runningbacks[0][0] + ' (' + runningbacks[0][1] + ')')
print(tightends[0][2] + ': ' + tightends[0][0] + ' (' + tightends[0][1] + ')')



# print(quarterbacks)
# print(runningbacks)
# print(widerecievers)
# print(tightends)
max_score =  float(quarterbacks[0][3]) + float(runningbacks[0][3]) + float(widerecievers[0][3]) + float(tightends[0][3])
min_score = float(quarterbacks[4][3]) + float(runningbacks[9][3]) + float(widerecievers[9][3]) + float(tightends[4][3])
team_score =  float(roster[0][3]) + float(roster[1][3]) + float(roster[2][3]) + float(roster[3][3])

print('\nThe maximum score is ' + str(round(max_score, 2)))
print('The minimum score is ' + str(round(min_score, 2)))
print('\nYour teams score is ' + str(round(team_score, 2)))

grade = ((team_score-min_score)/(max_score-min_score)) * 100
grade = round(grade, 2)
print('\nYour grade is ' + str(grade) + '%')





# # Create a new ComplexNumber object
# num1 = Quarterback(2, 3)
#
# # Call get_data() method
# # Output: 2+3j
# num1.get_data()
#
# # Create another ComplexNumber object
# # and create a new attribute 'attr'
# num2 = PositPlayer(5)
# num2.attr = 10
#
# # Output: (5, 0, 10)
# print((num2.real, num2.imag, num2.attr))
#
# # but c1 object doesn't have attribute 'attr'
# # AttributeError: 'ComplexNumber' object has no attribute 'attr'
# #print(num1.attr)
