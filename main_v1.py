def deep_search(map_record,path,result,cnt):
    if(cnt > 7):
        return
    node = path[-1]
    if(node in map_record):
        for each_node in sorted(map_record[node]):
            if(each_node == path[0]):
                if(cnt > 2):
                    result[cnt].append(path)
            elif(each_node > path[0] and each_node not in path):
                deep_search(map_record,list(path)+[each_node],result,cnt + 1)
    return

#data = open("./test_data.txt", "r")
data = open("./data_test/77409/test_data.txt", "r")
#data = open("/data/test_data.txt", "r")
map_record = {}
for i in data:
    p1,p2,money = [int(k) for k in i.split(",")]
    if(p1 not in map_record):
        map_record[p1] = set()
    map_record[p1].add(p2)

result = {}
for i in range(3,8):
    result[i] = []

for key in sorted(map_record.keys()):
    print(key)
    deep_search(map_record,[key],result,1)

sum_len = 0
for i in range(3,8):
    sum_len = sum_len + len(result[i])

file = open("./result1.txt", "w")
file.write(str(sum_len)+"\n")
for i in range(3,8):
    for each_result in result[i]:
        for j in range(len(each_result)):
            if(j == 0):
                file.write(str(each_result[j]))
            else:
                file.write(","+str(each_result[j]))
        file.write("\n")
