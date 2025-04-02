from random import *


# read file with roster -> in list
# rand'ly pick 2 at a time
#   if odd #, last group has 3
# groups number 1 - N

roster = []

infile = open("roster.txt", 'r')

for name in infile:
    name = name.rstrip()

    roster.append(name)

infile.close()

# display roster
##for each in roster:
##    print(each)

length = len(roster)

shuffle(roster)

odd = False

# if length is odd, add 1 to make final group
if length % 2 != 0:
    #length += 1
    odd = True

groupNum = length // 2

groups = []

count = 0

for each in range(0, groupNum):

    group = []

    group.append(roster[count])   

    count += 1

    if count != len(roster):
        group.append(roster[count])   

    count += 1

    if odd and count == len(roster) - 1:            # only append if name exists
        group.append(roster[count])
         
    
    groups.append(group)    # add pair to 2D list


outfile = open("groups.txt",'w')

count = 1

for row in groups:
    outfile.write("{0:<3s} ".format(str(count) + "."))
    
    for col in row:
        outfile.write("{0:<20s}".format(col))

    outfile.write("\n")
    count += 1


outfile.close()











    
