def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'dk': 4, 'vk':6}
dict2 = {'ac': 7, 'bc':9}
dict3 = Merge(dict1, dict2)
print(dict3)
