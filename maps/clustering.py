"""
@author Yuqi Hu
@date Sep. 13th 2020
@version 1.0
@purpose This File serves as the main clustering algorithm of this project.
## IMPORTANT NOTES:
* Direction: From row to colum, each entry means the shortest time to travel from ith place to jth place.
* Assumption:
    - All points are connected.
    - Each point can travel to other points within an exisited time span.
    - We do not consider each point will be visited again based on time graph (Even if in reality there exists `B` on the track from `A` to `C`, note as `A-B-C`, but `time(A-C)` is less than `time(A-B) + time(B-C)`.)
## APIs
* `clustering(matrix, cluster_N)`
    * `matrix` is a 2D array which serves as a sqaure matrix.
    * `cluster_N` is an integer that the user wants to divide the points set into.
    * Return Type is a diction in the form of `{index : point_indices_list_correponding_to_the_centroids}`. `index` is an integer, and `point_indices_list_correponding_to_the_centroids` is a list of integer indices of points.
"""

import copy
from collections import defaultdict

class cluster:
    """
    #################
    ### APIs FUNC ###
    #################
    """

    # API func.
    def clustering(matrix, cluster_N):
        # Validation
        if cluster_N > len(matrix) or cluster_N <= 0:
            print("Ilegal input!")
            return {}

        # Separation
        result = cluster.categorization(matrix, cluster_N)
        for i in range(len(result)):
            if len(result[i]) == 0:
                return cluster.categorization(matrix, cluster_N, True)
        return result

    """
    #################
    ### MAIN ALGO ###
    #################
    """

    def categorization(point_lst, N, centroid_zero_flag=False, iter_time=1000):
        """
        ######################
        ### HELPERS ###
        ######################
        """

        def dist(a, b):
            sum = 0
            for i in range(0, len(a)):
                sum += (a[i] - b[i]) ** 2
            return sum ** (1 / 2)

        def mid_point(point_lst):
            total_num = len(point_lst)
            if total_num == 0:
                return None
            len_element = len(point_lst[0])
            a = []
            for i in range(0, len_element):
                a.append(0)
            for i in range(0, total_num):
                for j in range(0, len_element):
                    a[j] += point_lst[i][j]
            for i in range(0, len_element):
                a[i] = a[i] / total_num
            return a

        def closer_to(s, centroids_lst):
            centroids_num = len(centroids_lst)
            dict_closer_to = {}
            for i in range(0, centroids_num):
                dict_closer_to.update({dist(s, centroids_lst[i]): i})
            return dict_closer_to[min(dict_closer_to)]

        def get_centroids_lst(point_lst, N):
            centroids_lst = [mid_point(point_lst)]
            point_lst = copy.deepcopy(point_lst)
            N -= 1
            while N != 0:
                dict_get_centroids_lst = {}
                for i in range(len(point_lst)):
                    sum = [0]
                    for centroid in centroids_lst:
                        sum[0] += dist(centroid, point_lst[i])
                    dict_get_centroids_lst.update({sum[0] : i})
                centroids_lst.append(point_lst.pop(dict_get_centroids_lst[max(dict_get_centroids_lst)]))
                N -= 1
            return centroids_lst

        def get_centroids_lst_zero(point_lst, N):
            zero_centroids_lst = []
            for i in range(N):
                zero_centroids_lst.append(point_lst[i])
            return zero_centroids_lst

        """
        #################
        ### CORE ALGO ###
        #################
        """

        centroids_lst = None
        if centroid_zero_flag:
            centroids_lst = get_centroids_lst_zero(point_lst, N)
        else:
            centroids_lst = get_centroids_lst(point_lst, N)

        dict = None
        inter_count = 0
        previous_centroids_lst = copy.deepcopy(centroids_lst)
        while inter_count < iter_time:
            dict = defaultdict(list)
            for i in range(len(point_lst)):
                closest_centroid_pos = closer_to(point_lst[i], centroids_lst)
                dict[closest_centroid_pos].append(i)
            for i in range(N):
                temp_centroid = mid_point([point_lst[x] for x in dict[i]])
                if temp_centroid:
                    centroids_lst[i] = temp_centroid
            inter_count += 1
            if previous_centroids_lst == centroids_lst:
                break
            previous_centroids_lst = copy.deepcopy(centroids_lst)
        return dict
