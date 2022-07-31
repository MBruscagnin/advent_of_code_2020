'''
Each policy actually describes two positions in the password, 
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''
array = []
ok = 0
sol = 0
with open('advent_of_code/data2.txt', 'r') as f:
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
    count = -1
    temp = 0
    
    for chr in pwd:
        count = count + 1
        if chr == letter:
            if count == lowerbound:
                ok = ok + 1
                temp = 1
            if count == upperbound:
                if temp == 0:
                    ok = ok + 1
                else:
                    ok = ok - 1
print(ok)
