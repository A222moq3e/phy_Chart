
# cheet height and width
height = 21
width = 17

# change this
# max_h = 360
# max_w = 100
# points = [[10, 360], [20, 240], [30, 180], [47, 170], [100, 62]]
max_h = 290
max_w = 100
points = [[1, 290], [3.3, 280], [10, 170], [33, 76], [56, 48], [100, 30]]
# max_h = 31
# max_w = 80
# points = [
#     [0, 0.043],
#     [0, 0.17],
#     [0, 0.256],
#     [0.01, 0.380],
#     [0.08, 0.48],
#     [1.44, 0.611],
#     [2.78, 0.643],
#     [4.28, 0.663],
#     [8.76, 0.696],
#     [12, 0.708],
#     [18.4, 0.727],
#     [25, 0.74],
#     [27.3, 0.743]]

inc_h = round(max_h/height)
inc_w = round(max_w/width)
# inc_h = 1.5
# inc_w = 0.05

print('increasing of height (Y-axis)')
for i in range(height+1):
    print(i*inc_h)
print('increasing of width (x-axis)')
for i in range(width+1):
    print(i*inc_w)


print('places:')
for i, point in enumerate(points):
    print(i, ' [', round(point[0]/inc_w, 2),
          'cm, ', round(point[1]/inc_h, 2), 'cm ]')
