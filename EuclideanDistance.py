points = [(5,6),(4,19),(45,1),(13, 24)]
distances = []

def euclideanDistance(point1, point2):
    x, y=point1
    a, b=point2
    return ((x-a)**2 + (y-b)**2)**0.5

def distances_of_points():
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if  i != j:
                distance = euclideanDistance(points[i], points[j])
                print(f"Distance between {points[i]} and {points[j]} is {distance}")
                distances.append(distance)
            else:
                continue
    return distances

def min_distance(distance):
    min = distance[0]
    for i in range(1,len(distance)):
        if distance[i]<min:
            min = distance[i]
    print(f"Minimum distance is {min}")
    return None

distances_of_points()
min_distance(distances)
