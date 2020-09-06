# Traveling-Lite Algo

 - Author: Yuqi Hu
 - Date: Sep. 6th 2020
 - Version: 0.0
 - Purpose: This File serves as the main searching algorithm of this project.

## IMPORTANT NOTES:
1. Direction: From row to colum, each entry means the shortest time to travel from ith place to jth place.
2. Assumption:
    a. All points are connected.
    b. Each point can travel to other points within an exisited time span.
    c. We do not consider each point will be visited again based on time graph (Even if in reality there exists 'B' on the track from 'A' to 'C', note as 'A-B-C', but 'time(A-C)' is less than 'time(A-B) + time(B-C)'.)
    
### APIs
1. 'shortest_path(matrix, start=None, end=None)'
  - 'matrix' is a 2D array which serves as a sqaure matrix.
  - 'start' and 'end' are both int type, serving as the start and end point.
  - Return Type is a tuple in the form of '(shortest_path, the_time_of_shortest_path)'. 'shortest path' is an 1D int array, and 'the_time_of_shortest_path' is a double type number.
