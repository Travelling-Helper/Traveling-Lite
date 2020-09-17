import requests
import json


class TimeMap:

    def time(self, x1, x2):
        originPos = x1
        des_pos = x2
        dict_param = {"origin": originPos, "destination": des_pos, "key": "aea9020a2dd5f495d996dbcc58847536"}
        r = requests.get("https://restapi.amap.com/v3/direction/driving?", dict_param)
        response = r.json()
        routes = response['route']
        total_time = int(routes['paths'][0]['duration'])
        guide = routes['paths'][0]['steps']
        return total_time, guide

    def timeList(self, positions):
        time_list = [[] for _ in range(len(positions))]
        guide_list = [[] for _ in range(len(positions))]
        for indexi, i in enumerate(positions):
            for indexj, j in enumerate(positions):
                if indexi == indexj:
                    time_list[indexi].append(0)
                    guide_list[indexi].append('你tm搁着原地走呢')
                else:
                    time_guide = self.time(i, j)
                    time_list[indexi].append(time_guide[0])
                    guide_list[indexi].append(time_guide[1])
        return time_list, guide_list
