# from 2.00.11 to 2.16.16

#___________________________________________________________________________________________________________________
#*******************************************************************************************************************
## Stacks (LIFO)

stack =[]
stack.append('plate A')
stack.append('plate B')
print(stack.pop())
print(stack.pop())

print('insert any thing to the stack by typing and pressing enter')
print('press r to remove an element or q to quit')

while True:
    
    data=input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'r':
        print('removing:', stack.pop())
    else:
        stack.append(data)
    print(stack)

for stuff in stack:
    print('->', stuff)

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## Queue

myqueue=[]
myqueue.append('data1')
myqueue.append('data2')

print(myqueue.pop(0))
print(myqueue.pop(0))

print('insert any thing to the queue by typing and pressing enter')
print('press r to remove an element or q to quit')

while True:
    
    data=input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'r':
        print('removing:', myqueue.pop(0))
    else:
        myqueue.append(data)
    print(myqueue)

for stuff in myqueue:
    print('->', stuff)


