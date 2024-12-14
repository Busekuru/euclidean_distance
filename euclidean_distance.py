


points=[(1,2),(4,6),(7,8),(2,3)]
distances=[]

def euclideanDistance (point1 , point2):
    x1,y1= point1
    x2,y2= point2
    d= ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d
d = euclideanDistance(points[0], points[1])
print(d)


for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print("Hesaplanan mesafeler:", distances)

min_distance=min(distances)
print(f"En küçük mesafe: {min_distance}")
