import csv, random, os

from os.path import exists

random_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

str_l = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

temp_l = []

add = 0

t = 0

t2 = 0

t3 = 0

t4 = 0

add_l = []

temp_l2 = []

csv_file = str(input("What is the csv file? "))

existing = 0

if exists(csv_file) == True:

    print("Existing file")

    with open(csv_file, "r", encoding="UTF8") as csv_file2:

        csv_reader = csv.reader(csv_file2)

        for i in csv_reader:

            temp_l2.append(i)

    csv_file2.close()

    existing = 1

num_rows = int(input("How many rows do you want? "))

if num_rows >= len(temp_l2):

    num_rows_f = num_rows

else:

    num_rows_f = len(temp_l2)

num_columns = int(input("How many columns do you want? "))

gaus = float(input("What disparity multiplicator do you want? (1 is default) "))

print("")

print("Increasing the randomness can neglect the impact of the disparity factor ")

print("")

gaus2 = str(input("Do you want to increase the randomness? (y/n) "))

ri_l = [1]

add = 0

if gaus2 == "y":

    ri_l = []

    min_ = float(input("Min value of the interval countaining the random factor "))

    max_ = float(input("Max value of the interval containing the random factor "))

    step = float(input("What is the step? "))

    ri_l.append(min_)

    while min_ + add <= max_:

        ri_l.append(min_ + add)

        add += step

def touch(csv_file):

    with open(csv_file, "a"):

        os.utime(csv_file, None)

exclu = "?"

exclu_l = [exclu]

while exclu != -1:

        exclu = int(input("Which column(s), in numeric order, is a string (-1 to end)? "))

        exclu_l.append(exclu - 1)

exclu_l.pop(0)

exclu_l.pop(-1)

if len(exclu_l) == 0:

    exclu_l.append(-1)

with open(csv_file, "w", encoding="UTF8") as csv_file:
    
    csv_writer = csv.writer(csv_file)

    while t < num_rows_f:

        while t2 < num_columns and t < num_rows:

            if t2 != exclu_l[t4]:

                add = 0

                while t3 < random.choice(random_l) * gaus * random.choice(ri_l):

                    add += random.choice(random_l) * gaus 

                    t3 += 1

            else:

                add = "a"

                while t3 < random.choice(random_l) * gaus * random.choice(ri_l):

                    add += random.choice(str_l)

                    t3 += 1

                if t4 + 1 < len(exclu_l):

                    t4 += 1

            temp_l.append(add)

            t3 = 0

            t2 += 1

        t2 = 0

        t4 = 0

        if t < len(temp_l2): 

            while t2 < len(temp_l2[t]):

                while t4 < len(temp_l2[t - 1]) - len(temp_l2[t]):

                    temp_l2[t].append(" ") 

                    t4 += 1

                t4 = 0

                temp_l.insert(t2, temp_l2[t][t2])

                t2 += 1

        else:

            if existing == 1:

                while t2 < len(temp_l2[0]):

                    temp_l.insert(0, " ")

                    t2 += 1

        t2 = 0

        csv_writer.writerow(temp_l)

        temp_l = []

        t4 = 0

        t += 1

csv_file.close()
