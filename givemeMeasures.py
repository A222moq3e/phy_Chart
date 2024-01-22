
# cheet height and width
height = 21
width = 17

# change this
# max_h = 360
# max_w = 100
# points = [[10, 360], [20, 240], [30, 180], [47, 170], [100, 62]]
# max_h = 290
# max_w = 100
# points = [[1, 290], [3.3, 280], [10, 170], [33, 76], [56, 48], [100, 30]]
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
# max_h = 160
# max_w = 100
# points = [[1, 160], [3.3, 114], [10, 57], [33, 21], [56, 13.2], [100, 7.8]]
# max_h = 126
# max_w = 100
# points = [[10, 126], [20, 86], [30, 66], [47, 57], [100, 30]]
# Exp7
max_h = 18.2
max_w = 9.1
points = [[1, 0], [5, 0], [8, 0], [8.93, 1], [
    8.96, 4.3], [9, 7.7], [9.03, 10.5], [9.1, 18.2]]


inc_h = round(max_h/height)
inc_w = round(max_w/width)
# inc_h = 1.5
inc_w = 0.55

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
