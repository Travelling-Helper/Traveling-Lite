# Traveling-Lite Algo

@author Yuqi Hu
@date Sep. 6th 2020
@version 0.0
@purpose This File serves as the main searching algorithm of this project.

### IMPORTANT NOTES:
1. Direction: From row to colum, each entry means the shortest time to travel from ith place to jth place.
2. Assumption:
    a. All points are connected.
    b. Each point can travel to other points within an exisited time span.
    c. We do not consider each point will be visited again based on time graph (even if in reality there exists B on the track from A to C, note as A-B-C. But A-C is consumes shorter time than A-B + B-C.)
    
### API
1. $shortest_path(matrix, start=None, end=None)$
  - $matrix$ is a 2D array which serves as a sqaure matrix.
  - $start$ and $end$ are both int type, serves as the starting and ending point.
  - Return Type is tuple as (<1D array>, int).
