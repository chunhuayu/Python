### for Loops
>>> seq = [1,2,3,4,5]
>>> for item in seq:
        print(item)
1
2
3
4
5

>>> for item in seq:
        print('Yep')
Yep
Yep
Yep
Yep
Yep

>>> for jelly in seq:
        print(jelly+jelly)
2
4
6
8
10

### while Loops
>>> i = 1
    while i < 5:
        print('i is: {}'.format(i))
        i = i+1
i is: 1
i is: 2
i is: 3
i is: 4

### range()
>>> range(5)
range(0,5)

>>> for i in range(5):
         print(i)
0
1
2
3
4

>>> list(range(5))
[0, 1, 2, 3, 4]

### list comprehension
>>> x = [1,2,3,4]
>>> out = []
    for item in x:
        out.append(item**2)
    print(out)
[1,4,9,16]

>>> [item**2 for item in x]
[1,4,9,16]
