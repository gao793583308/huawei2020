import functools
def custom_sort(x,y):
    for i in range(len(x)):
        if(x[i] < y[i]):
            return -1
        elif(x[i] > y[i]):
            return 1
    return 1

#data = open("./data_test/77409/test_data.txt", "r")
#data = open("./test_data.txt", "r")
data = open("/data/test_data.txt", "r")
map_record = {}
for i in data:
    p1,p2,money = [int(k) for k in i.split(",")]
    if(p1 not in map_record):
        map_record[p1] = set()
    map_record[p1].add(p2)

result = {}
for i in range(2,7):
    result[i] = []
sum_len = 0

for key in sorted(map_record.keys()):
    que = set()
    path = {}
    position = {}

    que.add(key)
    path[0] = [key]
    position[key] = [0]

    for i in range(7):
        cnt = 0
        new_node = set()
        new_path = {}
        new_position = {}
        for each_node in sorted(list(que)):
            if(each_node in map_record):
                for add_node in sorted(map_record[each_node]):
                    if(add_node == key):
                        if(i > 1):
                            for each_poisiton in position[each_node]:
                                sum_len = sum_len + 1
                                result[i].append(path[each_poisiton])
                    elif(add_node > key):
                        if(add_node not in new_node):
                            new_node.add(add_node)
                            new_position[add_node] = []
                            for each_poisiton in position[each_node]:
                                if(add_node not in path[each_poisiton]):
                                    new_path[cnt] = path[each_poisiton]+[add_node]
                                    new_position[add_node].append(cnt)
                                    cnt = cnt + 1
                        else:
                            for each_poisiton in position[each_node]:
                                if (add_node not in path[each_poisiton]):
                                    new_path[cnt] = path[each_poisiton] + [add_node]
                                    new_position[add_node].append(cnt)
                                    cnt = cnt + 1
        #print(sorted(que))
        #print(sorted(new_node))
        #a = input()
        que = new_node
        position = new_position
        path = new_path

#file = open("result1.txt", "w")
file = open("/projects/student/result.txt", "w")
file.write(str(sum_len)+"\n")
for i in range(2,7):
    result[i] = sorted(result[i],key=functools.cmp_to_key(custom_sort))
    for each_result in result[i]:
        for j in range(len(each_result)):
            if(j == 0):
                file.write(str(each_result[j]))
            else:
                file.write(","+str(each_result[j]))
        file.write("\n")