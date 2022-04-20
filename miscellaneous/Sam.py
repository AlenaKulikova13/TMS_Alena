

# s = "песни по 7 минут самые классные"
# s1 = s.encode("utf-8")
# print(s1)
#
# t = b'\xd0\xbf\xd0\xb5\xd1\x81\xd0\xbd\xd0\xb8 \xd0\xbf\xd0\xbe 7 \xd0\xbc\xd0\xb8\xd0\xbd\xd1\x83\xd1\x82 \xd1\x81\xd0\xb0\xd0\xbc\xd1\x8b\xd0\xb5 \xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xbd\xd1\x8b\xd0\xb5'
# t1 = t.decode("utf-8")
# print(t1)

# s = "да"
# s1 = s.encode("utf-8")
# print(s1)
#
# t = b'\xd0\xb4\xd0\xb0'
# t1 = t.decode("utf-8")
# print(t1)

# f = open('Sample.txt','r')
# k = 0
# for line in f:
#     k += 1
#     print(line,f"Строка {k}")
#
# f.close()

import json
with open("data.json", "w"):
    json.dump(data,jsonFile)
