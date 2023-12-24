
# cheet height and width
height = 21
width = 17

# change this
# max_h = 360
# max_w = 100
max_h = 290
max_w = 100

inc_h = round(max_h/height)
inc_w = round(max_w/width)

print('increasing of height (Y-axis)')
for i in range(height+1):
    print(i*inc_h)
print('increasing of width (x-axis)')
for i in range(width+1):
    print(i*inc_w)


points = [[1, 290], [3.3, 280], [10, 170], [33, 76], [56, 48], [100, 30]]
print('places:')
for i, point in enumerate(points):
    print(i, ' [', round(point[0]/inc_w, 2),
          'cm, ', round(point[1]/inc_h, 2), 'cm ]')
