# from 30.20 to 37.40

#>>>>>>>>>>>>>> SETS <<<<<<<<<<<<<<<#

# Avoiding duplicates. Sets are unordered, unchangable, unindexed

napoli_set = {'sole','mare', 'mandolino', 'pasta', 'pizza','pizza','San Gennaro'}
print(napoli_set) #il duplicato non dà errore, ma viene ignorato
# da notare come vengano stampati in ordine sparso

napoli_list= ['sole','mare', 'mandolino', 'pasta', 'pizza','pizza','San Gennaro']

counts=[napoli_list.count(item) for item in napoli_list]
print(counts)

counts=[[napoli_list.count(item), item] for item in set(napoli_list)]
print(counts)

from collections import Counter

print(Counter(napoli_list)) #ha costruito un dizionario

#>>>>>>>>>>>>>> TUPLE <<<<<<<<<<<<<<<#

books=[('a',1),('b',2),('c',3),('a',2)]
print(books[1][0])
print(books[0]==books[3])