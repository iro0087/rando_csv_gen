import csv, random, os

random_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

str_l = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

temp_l = []

add = 0

t = 0

t2 = 0

t3 = 0

t4 = 0

add_l = []

csv_file = str(input("What csv file do you want to create?"))

num_rows = int(input("How many rows do you want?"))

num_columns = int(input("How many columns do you want?"))

def touch(csv_file):

    with open(csv_file, "a"):

        os.utime(csv_file, None)

exclu = "?"

exclu_l = [exclu]

while exclu != -1:

        exclu = int(input("Which columns is a string (-1 to end)?"))

        exclu_l.append(exclu - 2)

exclu_l.pop(0)

exclu_l.pop(-1)

if len(exclu_l) == 0:

    exclu_l.append(-1)

print(exclu_l)

with open(csv_file, "w", encoding="UTF8") as csv_file:
    
    csv_writer = csv.writer(csv_file)

    while t < num_rows:

        temp_l.append(str(t))

        while t2 < num_columns - 1:

            if t2 != exclu_l[t4]:

                add = 0

                while t3 < random.choice(random_l):

                    add += random.choice(random_l)

                    t3 += 1

            else:

                add = ""

                while t3 < random.choice(random_l):

                    add += random.choice(str_l)

                    t3 += 1

                t4 += 1

            temp_l.append(add)

            t3 = 0

            t2 += 1

        t2 = 0
    
        csv_writer.writerow(temp_l)

        temp_l = []

        t4 = 0

        t += 1



