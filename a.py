import json
a = {'a':'rohan','r':4,'bool':True}
with open('r.txt','w+') as f:
    json.dump(a,f,indent=2)
with open('r.txt','r') as f:
    a = json.load(f)
    print a['r']
