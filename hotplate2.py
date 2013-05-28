import math
import sys

row_amount = int(raw_input("How many rows? "))
column_amount = int(raw_input("How many columns?" ))

plates = row_amount * column_amount

hot_plate = []
test = []

for i in range(0, plates):
    hot_plate.append(0.0)
    test.append(0.0)




middle_1 = (plates / 2) + (column_amount / 2) 
middle_2 = (plates / 2) + ((column_amount / 2) - 1) 

middle_3 = ((plates / 2) - column_amount) + (column_amount / 2)

middle_4 =((plates / 2) - column_amount) + ((column_amount / 2) - 1)

hot_plate[middle_1] = 100.0
hot_plate[middle_2] = 100.0
hot_plate[middle_3] = 100.0
hot_plate[middle_4] = 100.0


def heat_up(a):


    old_cell = hot_plate[a]

    count = 0
    total = 0

    if hot_plate[a - column_amount] is not None:
        total += hot_plate[a - column_amount]
        count += 1

    if hot_plate[a - column_amount] is not None:
        total += hot_plate[a - column_amount]
        count += 1

    if hot_plate[a - 1] is not None:
        total += hot_plate[a - 1]
        count += 1

    if hot_plate [a + 1] is not None:
        total += hot_plate [a + 1]
        count += 1


    avg = total / count

    new_cell = math.ceil(avg * 100) / 100
    hot_plate[a] = new_cell

    test_cell = new_cell - old_cell
    test[a] = test_cell
    stop = all(x == 0 for x in test)

    if r != 0 and stop == True:

        print "Turns:", r    
        for i, cell in enumerate(hot_plate):
            sys.stdout.write(" %r" % cell)
            if 0 == (i + 1) % column_amount:
                sys.stdout.write(" \n ")

        sys.exit(0)


for r in range(0, 1000):
    for a, i in enumerate(hot_plate):

        # The four cells in the center must stay at 100

        if a == middle_1 or \
       a == middle_2 or \
       a == middle_3 or \
       a == middle_4:
       
            continue

        # The four corner squares must stay at 0

        if a == 0  or \
       a == column_amount - 1  or \
       a == plates - column_amount or \
       a == plates - 1:
            
            continue

        heat_up(a)



        