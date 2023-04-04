# CONTDOWN

def contdown(n):
    list=[]
    for i in range (n,-1,-1):
        list.append(i)
    return list

print(contdown(10))



# PRINT AND RETURN

def print_and_return(list):
    print(list[0])
    return(list[1])

print(print_and_return([5,9]))


# FIRST PLUS LENGTH

def first_plus_length(list):
    sum=list[0]+len(list)
    return(sum)

print(first_plus_length([10,7,5,4,6,9,8,2,1,4]))


# VALUES GRATER THAN SECOND
list2=[]
def values_greater_than_second(list):
    for i in range (0,len(list)):
        if len(list)<2:
            return False
        if list[i]>list[1]:
            list2.append(list[i])
    print(len(list2))
    return list2
    
print(values_greater_than_second([5,2,3,2,1,4]))


# THIS LENGTH, THAT VALUE

def return_list(a,b):
    list=[]
    for i in range(0,a):
        list.append(b)
    return list
    
print(return_list(5,7))
    