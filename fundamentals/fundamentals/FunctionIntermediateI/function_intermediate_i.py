# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"]="Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]="Andres"
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30
print(z)


# Iterate Through a List of Dictionaries

def iterateDictionary(students):
    for i in range (0,len(students)):
        for key,value in students[i].items():
            print(f"{key} - {value},",end=" ")
        print("\n")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


# Get Values From a List of Dictionaries

def iterateDictionary2(key,students):
    for i in range (0,len(students)):
        students[i][key]
        print(students[i][key])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key,values in some_dict.items():
        print(f"{len(values)} {key}")
        print(*values, sep="\n")


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
