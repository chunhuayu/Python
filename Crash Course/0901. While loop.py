### Python Loops, Python has two primitive loop commands:
# while loops
# for loops

# The while Loop : With the while loop we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:
>>> i = 1
>>> while i < 6:
      print(i)
      i += 1
1
2
3
4
5
        
        
# Note: remember to increment i, or else the loop will continue forever.

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
# The break Statement : With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:

>>> i = 1
>>> while i < 6:
      print(i)
      if i == 3:
        break
      i += 1

1
2
3

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# Continue to the next iteration if i is 3:
>>> i = 0
>>> while i < 6:
      i += 1 
      if i == 3:
        continue
      print(i)
1
2
4
5
6

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
