from math import sqrt, inf
from statistics import mean

# this code was written in collaboration with marki, mksi and flmi
# Disclaimer: I would normally never write code with other people,
# But since learnit and the TA's REPEATLY stated that this was a group submission,
# I was purely following instructions.



n = int(input()) # Getting the input

# Class to keep track of the current points
class Point:
    def __init__(self, coords):
        self.coords = coords

    def __getitem__(self, index):
        return self.coords[index]
# A nested list of points. At first the lists look the same
# but they will be sorted differently later
x_points = []
y_points = []
for _ in range(n):
    point = Point([float(x) for x in input().split(" ")])
    x_points.append(point)
    y_points.append(point)

x_points.sort(key=lambda x: x[0]) # Sorting according to the x coordinate
y_points.sort(key=lambda x: x[1]) # Sorting accordin to the y coordinate

def compute_dist(a, b): # Helper function for computing the distance between the points
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def min_dist(x_points, y_points):
    if len(x_points) == 1: # If there is just one point we return nothing
        return inf, None
    if len(x_points) == 2: # Alse if there are two points in the "square", we compute the distance between the points
        return compute_dist(x_points[0], x_points[1]), (x_points[0], x_points[1])

    amount = len(x_points)
    first_half_x = x_points[:amount // 2] # Making the split to the left
    second_half_x = x_points[amount // 2:] # Making the split to the right

    first_set = set(first_half_x)
    first_half_y = [point for point in y_points if point in first_set]
    first_dist, first_points = min_dist(first_half_x, first_half_y) # Recursively making splits

    second_half_y = [point for point in y_points if point not in first_set]
    second_dist, second_points = min_dist(second_half_x, second_half_y) # Recursively keep making splits

    min_of_two_sides = min(first_dist, second_dist) # Getting the minimum distance of both side

    strip_dist, strip_points = strip(first_half_x, second_half_x, min_of_two_sides, y_points) # Defining the strip

    return min(((strip_dist, strip_points), (first_dist, first_points), (second_dist, second_points)), key=lambda x: x[0])


def strip(first_half, second_half, min_of_two_sides, y_points):


    middle_x_value = mean([first_half[-1][0], second_half[0][0]])

    relevant_points = set() # Defining the strip fromt the left hand side
    for point in first_half[::-1]:
        if middle_x_value - point[0] > min_of_two_sides:
            break
        relevant_points.add(point)

    for point in second_half: # defining the split from the right hand side
        if point[0] - middle_x_value > min_of_two_sides:
            break
        relevant_points.add(point)

    relevant_y_points = [point for point in y_points if point in relevant_points]

    strip_dist = inf
    strip_points = None

    for i in range(len(relevant_y_points)):
        current_point = relevant_y_points[i]
        for other_point in relevant_y_points[i:i+15]:
            if current_point == other_point:
                continue
            distance = compute_dist(current_point, other_point)
            if distance < strip_dist:
                strip_dist = distance
                strip_points = (current_point, other_point)

    return strip_dist, strip_points

    
min_distance, min_points = min_dist(x_points, y_points)

for point in min_points:
    print(*point.coords)


