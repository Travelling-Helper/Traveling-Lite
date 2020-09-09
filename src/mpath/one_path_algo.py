"""
@author Yuqi Hu
@date Sep. 9th 2020
@version 1.0
@purpose This File serves as the main searching algorithm of this project.
## IMPORTANT NOTES:
* Direction: From row to colum, each entry means the shortest time to travel from ith place to jth place.
* Assumption:
    - All points are connected.
    - Each point can travel to other points within an exisited time span.
    - We do not consider each point will be visited again based on time graph (Even if in reality there exists `B` on the track from `A` to `C`, note as `A-B-C`, but `time(A-C)` is less than `time(A-B) + time(B-C)`.)
## APIs
* `shortest_path(matrix, start=None, end=None)`
    * `matrix` is a 2D array which serves as a sqaure matrix.
    * `start` and `end` are both int type, serving as the start and end point.
    * Return Type is a tuple in the form of `(shortest_path, the_time_of_shortest_path)`. `shortest path` is an 1D int array, and `the_time_of_shortest_path` is a double type number.
"""


class one_path_algo:
    """
    #################
    ### APIs FUNC ###
    #################
    """
    # Main algo.
    # Separate to later algo.
    def shortest_path(matrix, start=None, end=None):
        if not validate_matrix(matrix):
            return [] # No solution

        # Case 1: No start and no end
        if start == None and end == None:
            print("Shortest with no start nor end point.")
            return shortest_path_no_se(matrix)

        # Checks if start or end point is valid, return false if it is not valid, true if it is valid
        def start_end_validation(start, end):
            if not start == None and (start < 0 or start >= len(matrix)):
                print("Invalid start point.")
                return False
            elif not end == None and (end < 0 or end >= len(matrix)):
                print("Invalid end point.")
                return False
            else:
                return True
        if not start_end_validation(start, end):
            return []

        # Case 2: Has start Xor end
        if end == None or start == None:
            if end == None:
                # Case 2.1: Only has a start
                print("Shortest with with only start point.")
                return shortest_path_only_start(matrix, start)
            else:
                # Case 2.2: Only has an end
                print("Shortest with with only end point.")
                return shortest_path_only_end(matrix, end)

        # Case 3: Contains both start and end
        print("Shortest with with both start and end points.")
        return shortest_path_with_se(matrix, start, end)

    """
    #################
    ### CORE ALGO ###
    #################
    """

    # Find out the shortest path that visit all the points with no start nor end by shortest_path_with_se, and the total time
    def shortest_path_no_se(matrix):
        dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp_tuple = shortest_path_with_se(matrix, i, j)
                dict.update({temp_tuple[1] : temp_tuple[0]})
        min_val = min(dict)
        return dict[min_val], min_val

    # Find out the shortest path that visit all the points with only a start point by BFS, and the total time
    def shortest_path_only_start(matrix, start):
        dict = {str(start) : 0}
        finish = {}
        lst = []

        def next_vertices(cur_path):
            lst = []
            for cur in range(0, len(matrix)):
                if str(cur) not in cur_path:
                    lst.append(cur)
            return lst

        while len(dict) != 0:
            cur_path = list(dict.keys())[0]
            if len(cur_path) == len(matrix):
                finish.update({cur_path : dict.pop(cur_path)})
            else:
                cur_value = dict.pop(cur_path)
                cur_vertex = eval(cur_path[-1:])
                next_list = next_vertices(cur_path)
                for i in next_list:
                    new_path = cur_path + str(i)
                    new_value = cur_value + matrix[cur_vertex][i]
                    dict.update({new_path : new_value})

        shortest_path, min_val = argmin(finish)

        for i in shortest_path:
            lst.append(eval(i))

        return lst, min_val

    # Find out the shortest path that visit all the points with only an end point by BFS, and the total time
    def shortest_path_only_end(matrix, end):
        dict = {str(end) : 0}
        finish = {}
        lst = []

        def next_vertices(cur_path):
            lst = []
            for cur in range(0, len(matrix)):
                if str(cur) not in cur_path:
                    lst.append(cur)
            return lst

        while len(dict) != 0:
            cur_path = list(dict.keys())[0]
            if len(cur_path) == len(matrix):
                finish.update({cur_path : dict.pop(cur_path)})
            else:
                cur_value = dict.pop(cur_path)
                cur_vertex = eval(cur_path[-1:])
                next_list = next_vertices(cur_path)
                for i in next_list:
                    new_path = cur_path + str(i)
                    new_value = cur_value + matrix[i][cur_vertex]
                    dict.update({new_path : new_value})

        shortest_path, min_val= argmin(finish)
        for i in shortest_path:
            lst.append(eval(i))
        lst.reverse()
        return lst, min_val

    # Find out the shortest path that visit all the points with both start and end, and the total time
    def shortest_path_with_se(matrix, start, end):
        start_is_end_flag = (start == end)

        copy_matrix = matrix
        if start_is_end_flag:
            copy_matrix = []
            for i in matrix:
                copy_matrix.append(i.copy())
            for i in range(len(copy_matrix)):
                copy_matrix[i].append(copy_matrix[i][start])
            end_to_all_row = copy_matrix[start].copy()
            copy_matrix.append(end_to_all_row)
            end = len(copy_matrix) - 1
        matrix = copy_matrix

        dict = {str(start) : 0}
        finish = {}
        lst = []

        def next_vertices(cur_path):
            lst = []
            for cur in range(0, len(matrix)):
                if str(cur) not in cur_path:
                    lst.append(cur)
            return lst

        while len(dict) != 0:
            cur_path = list(dict.keys())[0]
            if len(cur_path) == len(matrix):
                finish.update({cur_path : dict.pop(cur_path)})
            else:
                cur_value = dict.pop(cur_path)
                cur_vertex = eval(cur_path[-1:])
                if cur_vertex != end:
                    next_list = next_vertices(cur_path)
                    for i in next_list:
                        new_path = cur_path + str(i)
                        new_value = cur_value + matrix[cur_vertex][i]
                        dict.update({new_path : new_value})


        shortest_path, min_val = argmin(finish)

        if start_is_end_flag:
            for i in shortest_path:
                temp_value = eval(i)
                if temp_value == len(matrix) - 1:
                    lst.append(start)
                else:
                    lst.append(temp_value)
        else:
            for i in shortest_path:
                lst.append(eval(i))

        return lst, min_val

    """
    ###############
    ### HELPERS ###
    ###############
    """

    # Takes in 2-D array such that cannot be empty. Also, it validates that it is a regularized matrix.
    def validate_matrix(matrix):
        # return true if the input mat has another layer inside
        """
        Doc Test:
        a = [] # False Empty
        b = [0] # False 1D
        c = [[0]] # True
        d = [[1, 0], [1]] # False Bizarre
        e = [[1, 0], [1, 0]] # True
        """
        def has_layer(mat):
            try:
                mat[0]
                return True
            except:
                return False

        row_num = len(matrix)

        if row_num == 0 :
            print("Input matrix is empty.")
            return False

        if not has_layer(matrix[0]):
            print("Input matrix is just 1D, expected 2D.")
            return False

        for i in range(row_num):
            if len(matrix[i]) != row_num:
                print("Input matrix is not an square matrix, bizarre.")
                return False

        return True

    # Takes in a 1-D diction, and return the argument that makes the value minimized the value, and output the smallest value
    def argmin(d):
        if not d: return None
        min_val = min(d.values())
        return [k for k in d if d[k] == min_val][0], min_val
