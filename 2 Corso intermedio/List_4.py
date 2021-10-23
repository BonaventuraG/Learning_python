# from 2.16.16 to 2.37.25

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## List of list (2D List)

print()
print('list of lists')

grades=[[25,24,30,21],[20,28,29,27],[26]]
print(grades)
print('grades[1][0]',grades[1][0])

grades[1].append(27)

print(grades)

def print_2d(list_2d):
    for inner_list in list_2d:
        for grade in inner_list:
            print(grade, end=' ')
        print()

print_2d(grades)

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## list into string: join

data='just a string'
d=' '
appoggio=data.split(d)
print(appoggio)
print(data) 
print(d.join(appoggio))
print(appoggio) #appoggio è rimasta splittata dopo il join: le liste non vengono cancellate nè modificate dal join

data=['hello', 'you', 'all', 10, 11]

print(" ".join(str(i) for i in data))

#______________________________________________________________________________________________________________________
#**********************************************************************************************************************
## sorting list 2D


data=[[4,5,2,7,1],[10,11,4,2,34,23],[10],[4,88]]

print(sorted(data))

print(sorted(data, key=sum)) #ordina in base alla somma 

def avg(list):
    return sum(list)/len(list)

print(sorted(data, key=avg)) #ordina in base alla media


