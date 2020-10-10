from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from maps import TimeMap, one_path_algo, clustering
# Create your views here.

# Robots.txt for crawler engines
def robots(request):
    return render(request, "robots.txt")
def err_404(request):
    return render(request, "err_404.html")

def gaodeMap(request):
    return render(request, "map.html")

def test(request):

    return render(request, "test.html") #测试
def tested(request):
    if request.method == 'POST':
        long_str = request.POST.get('positionsToReturn')
        lst_of_loc_str = [(str + '}') for str in long_str.split('}')]
        lst_of_loc_str.pop()
        lst_of_loc = [eval(str) for str in lst_of_loc_str]
        print(lst_of_loc)
        axes = [loc["location"] for loc in lst_of_loc]
        print(axes)
        a = TimeMap.TimeMap()
        time_list, guide_list = a.timeList(axes)
        print(time_list)
        cluster = request.POST.get('cluster')
        cluster = eval(cluster)
        if cluster == 0:
            paths = one_path_algo.one_path_algo.shortest_path(time_list)
            guides = []
            for i in range(len(paths[0]) - 1):
                guides.append(guide_list[paths[0][i]][paths[0][i + 1]])
            print(paths)
        else:
            paths = clustering.cluster.clustering(time_list, cluster)
            print(paths)
            locs = [[lst_of_loc[i] for i in group] for group in paths.values()]
            return render(request, "tested.html", {
                'positionsToReturn': request.POST.get('positionsToReturn'),
                'Paths': paths,
                'Locs': locs
            })

    return render(request, "tested.html", {
        'positionsToReturn': request.POST.get('positionsToReturn'),
        'Paths': paths[0],
        'Locs': [lst_of_loc[i] for i in paths[0]],
        'Time': paths[1],
        'Guides': guides
    })