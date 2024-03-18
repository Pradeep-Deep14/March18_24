#Print Duplicates in the list


L=[1,2,2,3,4,4,5]

Duplicates=list(set([x for x in L if L.count(x)>1]))

print("Duplicates in the list:" , Duplicates)