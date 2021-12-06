from typing import Dict,List, Tuple
from math import atan2,degrees

def get_points(point: Dict[str, int])-> Tuple[int, int, int, int]:
    x1 = point["x1"]
    x2 = point["x2"]
    y1 = point["y1"]
    y2 = point["y2"]
    return x1, x2, y1, y2

def get_crosses(p_m: List[List[int]]) -> int:
    a=0
    for row in p_m:
        for i in row:
            if i > 1:
                a+=1
    return a

def create_points_matrix(points: List[Dict[str, int]]) -> List[List[int]]:
    points_matrix: List[List[int]] = []
    max_x = max_y = 0

    for point in points:
        x1,x2,y1,y2 = get_points(point)

        if x1 > max_x and x1 >= x2:
            max_x = x1
        if x2 > max_x and x2 >= x1:
            max_x = x2
        if y1 > max_y and y1 >= y2:
            max_y = y1
        if y2 > max_y and y2 >= y1:
            max_y = y2
    points_matrix = [ 
        [ 
            0 for x in range(max_x+1)
        ] for y in range(max_y+1)
    ]
    return points_matrix

def populate_points_matrix(points_matrix: List[List[int]], points: List[Dict[str, int]]) -> None:
    for point in points:
        x1,x2,y1,y2 = get_points(point)

        if x1 == x2:
            if (y2 < y1):
                y1,y2 = y2, y1
            for y in range(y1, y2+1):
                points_matrix[y][x1] += 1
        if y1 == y2:
            if (x2 < x1):
                x1,x2 = x2, x1
            for x in range(x1, x2+1):
                points_matrix[y1][x] += 1

        # if (x1 == y2 and x2 == y1) or (x1 == y1 and x2 == y2) or ():

        if degrees(atan2(abs(y2-y1),abs(x2-x1))) == 45:
            x_inc = 1
            y_inc = 1
            if x1 > x2:
                x_inc = -1
            if y1 > y2:
                y_inc = -1
            i=0
            for x in range(x1, x2+x_inc, x_inc):
                points_matrix[y1+i*y_inc][x] += 1
                i+=1
def main() -> None:

    with open("input.txt") as points_file:
        full_lines = [line.strip() for line in points_file.readlines()]
        lines = [line.split(" -> ") for line in full_lines]
        points = []
        for line in lines:
            x_1,y_1 = line[0].split(",")
            x_2,y_2 = line[1].split(",")
            points.append({"x1": int(x_1), "x2": int(x_2), "y1": int(y_1), "y2": int(y_2)})

    points_matrix = create_points_matrix(points)
    populate_points_matrix(points_matrix, points)
    amount_crosses = get_crosses(points_matrix)
    print(amount_crosses)

if __name__ == "__main__":
    main()