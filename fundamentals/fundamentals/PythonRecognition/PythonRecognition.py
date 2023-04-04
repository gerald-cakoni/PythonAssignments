num1 = 42 #variable declaration, initialize int
num2 = 2.3  #variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #variable declaration, initialize tuple
print(type(fruit))  #type check, print to console
print(pizza_toppings[1])    #acces value of the list, print to console
pizza_toppings.append('Mushrooms')  #add value
print(person['name'])   #acces value, print to console
person['name'] = 'George'   #change value
person['eye_color'] = 'blue'    #change value
print(fruit[2]) #acces value, print to console

if num1 > 45:   #if condition
    print("It's greater")    #print to console
else:   #else condition
    print("It's lower") #print to console

if len(string) < 5: #length check, if condition
    print("It's a short word!") #print to console
elif len(string) > 15:  #length check, else if condition
    print("It's a long word!")  #print to console
else:   #length check, else condition
    print("Just right!")  #print to console

for x in range(5):  #for loop, start=0, stop=5, increnent=1
    print(x)  #print to console
for x in range(2,5):  #for loop, start=2, stop=5, increnent=1
    print(x)  #print to console
for x in range(2,10,3):  #for loop, start=2, stop=10, increnent=3
    print(x)  #print to console
x = 0   #Variable declaration
while(x < 5):   #while loop, start=0, stop=4
    print(x)  #print to console
    x += 1  #increnent=1

pizza_toppings.pop() #delete value at the end of the list
pizza_toppings.pop(1)   #delete value at index 1 of the list

print(person) #print to console
person.pop('eye_color') #delete value from dictionary
print(person) #print to console

for topping in pizza_toppings:  # for loop
    if topping == 'Pepperoni':  #if condition
        continue    #continue anyway, even if the condition is fulfilled
    print('After 1st if statement') #IndentationError: unexpected indent
    if topping == 'Olives': #if condition
        break   #break, stop execution

def print_hello_ten_times():    #declarate the function
    for num in range(10):   #for loop, starts at 0 till 10, increment 1
        print('Hello')  #print to console

print_hello_ten_times() #call the function

def print_hello_x_times(x): #declarate the function with parameter
    for num in range(x): #for loop, starts at 0 till x, increment 1
        print('Hello')  #print to console

print_hello_x_times(4)  #call the function, give 4 as parameter

def print_hello_x_or_ten_times(x = 10): #declarate the function with parameter 10
    for num in range(x):    #for loop, starts at 0 till x, increment 1
        print('Hello')  ##print to console

print_hello_x_or_ten_times()    #call the function, it takes 10 as parameter because we defined before
print_hello_x_or_ten_times(4)   #call the function, give 4 as parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
# print(boolean)
# fruit.append('raspberry')