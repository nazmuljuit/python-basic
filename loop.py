colors = [11, 34, 98, 43, 45, 54, 54]
#print all item
for item in colors:
    print(item)
# print only greater 50
for item in colors:
    if item > 50:
        print(item)
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
#print only integer 
for color in colors:
    if isinstance(color, int):
        print(color)
#print only integer and greater than 50
for item in colors:
    if item > 50 and isinstance(item,int):
        print(item)
