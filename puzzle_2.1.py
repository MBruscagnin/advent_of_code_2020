'''
Set of passwords with a constraint.
Ex: "1-2 x: xpxc" meaning that in the password "xpxc"
must be at least one "x" and at most two "x" (out lower and upper bound in the code)

Return the number of passwords in the file data.txt that are comply with its constraint 
'''
array = []
ok = 0
with open('data.txt', 'r') as f:
    for line in f.readlines():
       # print(line)
        l = line.strip().split('\n')
        array.append(l)

for p in array:
    z = p.pop()
    x = z.split(':')
    pwd = x[1]
    y = x[0].split(' ')
    letter = y[1]
    range = y[0].split('-')

    lowerbound = int(range[0])
    upperbound = int(range[1])
    count = 0
    
    for chr in pwd:
        if chr == letter:
            count = count + 1

    if count >= lowerbound:
        if count <= upperbound:
            ok = ok + 1
print(ok)

