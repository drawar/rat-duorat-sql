import json

dic = json.load(open("./eval.json"))
new_dic = {}
for example in dic['per_item']:
    if example["exact"]==True:
        ans = 1
    else:
        ans = 0
    try:
        
        new_dic[example["hardness"]].append(ans)
    except:
        new_dic[example["hardness"]] = []
        new_dic[example["hardness"]].append(ans)

print(new_dic)
results = []
for key in new_dic.keys():
    # print(sum(new_dic))
    print(key, float(sum(new_dic[key]))/len(new_dic[key]))
    results.append(float(sum(new_dic[key]))/len(new_dic[key]))

# results = [69.5, 58.3, 89.5, 44.1]
results = [86.4, 73.6, 62.1, 42.9]
num = [248.0, 446.0, 174.0, 166.0]
new_results = []
total = 0
for i in range(len(results)):
    total+= results[i]*(num[i]/sum(num))
    new_results.append(63.9*results[i]/56.7)

print(total)
print(new_results)
