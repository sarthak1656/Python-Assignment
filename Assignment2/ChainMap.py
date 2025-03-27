from collections import ChainMap

dict1 = {'101': 85, '102': 90}
dict2 = {'103': 78, '104': 88}
dict3 = {'105': 92, '106': 80}
dict4 = {'107': 75, '108': 89}

marks_chainmap = ChainMap(dict1,dict2,dict3,dict4)

print("Combined chainmap: ",marks_chainmap)

# Combined chainmap:  ChainMap({'101': 85, '102': 90}, {'103': 78, '104': 88}, {'105': 92, '106': 80}, {'107': 75, '108': 89})