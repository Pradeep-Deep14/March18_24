#Nested List to flattened List

def flattened_list(Nested_List):
    flattened=[]
    for i in Nested_List:
        if isinstance(i,list):
            flattened.extend(flattened_list(i))
        else:
            flattened.append(i)
    return flattened

I=[1,2,[3,4,[5,6]],7]
result=flattened_list(I)

print("Flattend List:",result)