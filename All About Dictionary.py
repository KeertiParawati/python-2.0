student_data = {
    "id1": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara",  "class": "V", "subject_integration": "english, math, science"},  # duplicate of id1
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
    }
result = {}
seen__keys = [] # using a list instead of set


for student__id, detalis in student_data.items():
    unique__keys = (detalis["name"],detalis["class"],detalis["subject__integration"])


    if unique__keys not in seen__keys:
        seen__keys.append(unique__keys)
        result[student__id] = detalis

for k, v in result.items():
    print(k,":",v) 

tesr__dict = {'codingal':2,'is':2,'best':2,'for':2,'codingal':1}

print("the orginal dictionary:",+ str (tesr__dict))

k = 2

res = 0
for key in tesr__dict:
    if tesr__dict[key] == k:
        res = res + 1


print("Frequency of k is:" + str (res))