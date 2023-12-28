
let height = 21
let width = 17

let max_h = 290
let max_w = 100
let points = [[1, 290], [3.3, 280], [10, 170], [33, 76], [56, 48], [100, 30]]

inc_h = Math.round(max_h/height)
inc_w = Math.round(max_w/width)

console.log('increasing of height (Y-axis)')

// for i in range(height+1):
for(let i=0;i<height;i++)
console.log(i*inc_h)
console.log('increasing of width (x-axis)')
// for i in range(width+1):
for(let i=0;i<width;i++)
console.log(i*inc_w)


console.log('places:')
for(let i=0;i<points.length;i++){
    console.log(i, ' [', (points[i][0]/inc_w).toFixed(2),'cm, ', (points[i][1]/inc_h).toFixed(2), 'cm ]');
}
// for i, point in enumerate(points):
//     print(i, ' [', round(point[0]/inc_w, 2),
//           'cm, ', round(point[1]/inc_h, 2), 'cm ]')
