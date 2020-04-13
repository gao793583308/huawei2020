def deep_search(map_record,path,result,cnt, visited):
    if(cnt > 7):
        return
    node = path[-1]
    if(node in map_record):
        for each_node in sorted(map_record[node]):
            if(each_node == path[0]):
                if(cnt > 2):
                    result[cnt].append(path)
            elif(each_node > path[0] and each_node not in path):
                if(cnt > 3 and each_node not in visited[path[0]]):
                    continue
                deep_search(map_record,list(path)+[each_node],result,cnt + 1, visited)
    return

def search_all(map_record,visited):
    for key in map_record.keys():
        #print(1,key)
        que = set()
        que.add(key)
        for i in range(3):
            que_new = set()
            for node in que:
                if (node in map_record):
                    for each_node in sorted(map_record[node]):
                        que_new.add(each_node)
                        visited[each_node].add(key)
            que = que_new

#data = open("./test_data.txt", "r")
#data = open("./data_test/1004812/test_data.txt", "r")
data = open("/data/test_data.txt", "r")
map_record = {}
visited = {}
for i in data:
    p1,p2,money = [int(k) for k in i.split(",")]
    if(p1 not in map_record):
        map_record[p1] = set()
    map_record[p1].add(p2)
    if(p1 not in visited):
        visited[p1] = set()
    if(p2 not in visited):
        visited[p2] = set()

result = {}
for i in range(3,8):
    result[i] = []

search_all(map_record,visited)
#print(visited)
for key in sorted(map_record.keys()):
    #print(key)
    deep_search(map_record,[key],result,1, visited)

sum_len = 0
for i in range(3,8):
    sum_len = sum_len + len(result[i])

#file = open("./result1.txt", "w")
file = open("/projects/student/result.txt", "w")
file.write(str(sum_len)+"\n")
for i in range(3,8):
    for each_result in result[i]:
        for j in range(len(each_result)):
            if(j == 0):
                file.write(str(each_result[j]))
            else:
                file.write(","+str(each_result[j]))
        file.write("\n")
