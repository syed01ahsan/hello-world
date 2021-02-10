#Syed Ahsan
#1867491

import math

width = int(input("Enter wall width (feet):"))
height = int(input("Enter wall height (feet):"))
Area = width * height
print('Wall area:',Area)

paint = Area / 350
print('Wall area:',Area)
print('Paint needed : %f' % paint)

cans = math.ceil(paint)
print('Cans needed : ', cans)

color = input("Choose a color to paint the wall: ")

paint_colors = {'red': 35,'blue': 25,'green': 23}

cost = 0
for x in paint_colors.keys():
    if x == color.lower():
        cost = cans * paint_colors[x]
if (cost == 0):
    print("Wrong color selected. Color not available.")
else:
    print("Cost of purchasing red paint: $" + str(cost))