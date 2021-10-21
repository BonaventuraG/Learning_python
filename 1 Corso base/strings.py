###string 
## excape strings \

msg= "hello\nJohn   \"\x41\" \\n"
print(msg)

#____________________________________
##single quotes and double (are almost the same)

msg2 ='hello'
print(msg2)

msg3 = "l'imbuto" #devi usare i double quotes 
#per poter usare liberamente i single come 
#apostrofi
print(msg3)

msg4 = 'disse:"che vergogna!"'
# devi usare i singles per usare liberamente
# i double come virgolette
print(msg4)

#in alternativa usare l'escape \

#______________________________________
##concatenation
full_message = msg3 + " " + msg4
print(full_message)
print(msg3, msg4) #this also works, but are two arg

print("hey" "there") #this is one argument concatenated

msg5 = ("this is a long string..."
"so long that I had to start a new line")
#concatenated literals
print(msg5)

#_______________________________________
##Multiline strings
very_long_string = """aaaaaaaaa \ 
aaaaa
bbbbbbbbbbbbbbbbbbbbbb
ccccccccccccccccccc"""
#i tre doubleq rendono attivo lo \n implicito
# il backslash annulla lo \n
print(very_long_string)

#_____________________________________
## Indexes

str1 = "abcde fg"

print(str1[0]+str1[5]+str1[3])

#____________________________________
## Slicing strings

print(str1[3:])
print(str1[3:7]) #l'intervallo in effetti è
         # [x;y[ col secondo escluso

#_____________________________________
## negative Indexes (indicies)

print(str1[-1])
print(str1[-3:]) 
print(str1[:-4])
print(str1[2:-4])

#_____________________________________
## id : allocation

task="miao"
print(id(task))
task="quaqua"
print(id(task)) 
#the strings cannot be changed
# task[0]="Q" questo non funziona
task= task +"!"
print(task)
print(id(task)) 
#la memoria è stata liberata
#e poi riallocata

different = task
different= different +"?!"
print(id(task), task)
#l'allocazione di task non è cambiata perchè 
# è stato modificato different ma non task

#________________________________________
# length

print(len(task))
print(task[len(task)-1]," ", task[-1])

#_______________________________________
#numbers to string

#print("the length is " + len(task) + " !!")
#non puoi concatenare direttamente degli int

print("the length is " + str(len(task)) + " !!")
#così hai concatenato le stringhe (convertendo int in str)

print("the length is" , len(task), "!!")
#così hai passato tre argomenti diversi, int è rimasto int



