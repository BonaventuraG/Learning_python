### while loop
i=0           #init
while i<10:   #condition
    print(i)
    i+=2      #update   

for i in range(0, 10, 1): #(init, cond, update)
    print(i,end=" ")
print("")

#_________________________________________ 
## while else vs flags

numbers=[4,3,2,4,6]
toolarge= False

i=0
while i<len(numbers):
    if numbers[i] **2>40:
        print("too large")
        toolarge=True #flag
        break
    print("ok for now")
    i+=1
else:
    print("ok everything") #esegue solo se il while viene concluso

if not toolarge:            #checking the flag
    print("ok everything")

#_________________________________________________
## do while

i=20  
print(i, end='')  
i+=1      
while i<10:   
    print(i,end='')
    i+=1 
print('')     

i=0
while True:
    print(i)
    i +=1
    if i>9:
        break

#____________________________________________
## indefinite loop lower and islower

print('do you want to coninue? Y/N')
response= input()
while response.lower()=='y': #lower is a method attached to a string (response in this case)
    print('do you want to coninue? Y/N')
    response=input()
if response.islower():
    print('hai dimenticato il maiuscolo')

while True:
    print('press Q to quit')
    response2=input()
    if response2=='Q' or response2=='q':
        break




