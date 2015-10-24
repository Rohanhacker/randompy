import os
with open('r.txt') as f:
    r = f.readlines()
    print r
    r = ''.join(r)
    r = r.split('\n')
    print r
with open('r.txt','w+') as k:
    k.write('This place is a shithole how could I\'ve ended up here')
print os.listdir('/home/rohan')
os.makedirs('/home/rohan/rr')
print os.listdir('/home/rohan')
