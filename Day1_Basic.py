#%%

print("Hello World, I'm Aishah!")
#%%

#create new variable

first_int = 5
#1_int = 6 variable should not start with a number
# first int =6 #variable should not have a space
# first@%! = 2 #Identifiers cannot contain symbol


# %%

#Phyton Datatype : Boolean, Numbers, string, List, Dictionary, Tuple

first_num = 12345
#first_string = 'Let's take a guess'
second_string = "Let's take a guess"

# %% Number

#Integer
myint = 7
print(myint)
myint = 8
print(myint)

#Float
myfloat = 7.0
print("This is using the float method", float(myint))
print("This is using the int method", int(myfloat))

#Complex number
mycomplex =+ 2 + 3j #(real part + imaginary number)
print(mycomplex)

# %% Determine the type of variable

type(mycomplex)

# %%

5+3

a = 6
b = 7
print(a+b)

# %%
5 + 2 * 3
# %%

x = 9
x += 1
print(x)

# %% String

character = 's'


print(type(character))
# %% Operations on String
name = "tommy"
print(name[0]) #"t"
print(name[2]) #"m"
len(name)      #5

#Concatenate string

s = "tom and " + "jerry"
print(s) #"tom and jerry"

#slicing string
s[0:3]          #tom [start element : end element +1]
print(s[8:13])  #"jerry"
print(s[8:])    #"jerry"
print(s[-5:])   #negative indexing "jerry"

example = "Welcome"
print(example[:-1]) #welcom

# * is a repitition operator for string
s1 = 'spam' * 10
print(s1) #spamspamspamspamspamspamspamspamspamspam

# %% functions in string

birthdate = "980520-10-5595"
birthdate = birthdate[0:6]
len(birthdate)
print(max("abcdefghijkl")) #1
print(ord('1')) #49
print(min("abcdefghijkl"))
print(ord('a')) #97

# %% in and not in operators
#boolean :true and false

'a' in 'ncdekoef' #false
'come' not in 'welcome' #false

# %% String comparison

print('welcome' == 'welcome') #true
print("free" != 'freedom') #true
print("arrow" > 'arow') #true
print('pAsswOrd' == 'password') #false

# %% Testing Strings

password = "Aishahisawesome123"
print(password.isalnum()) #True
print(password.isupper()) #False isupper check All characters in uppercase
print(password.islower()) #False

password1 = "aishahisnotawesome"
print(password1.isdigit()) #False because no digit available

password2 = "123456789"
print(password2.isalpha()) #False

password3 = " "
print(password3.isspace()) #Return True if string contains only whitespace

# %% Search of substring

string1 = "Welcome to Python"
print(string1.endswith("thon")) #True
print(string1.startswith("thon")) #False

string2 = "Welcome to my class, come to study"
print(string2.count("come")) #2

print(string2.find("come")) #return lowest index where s1 starts in the string #3
print(string2.rfind("come")) #21

# %% Converting String

string3 = "Aman is a good student. Aman always repond to my class. Aman gets good marks in Python"

string4 = string3.replace("Aman", "Aiman")
print(string3)
print(string4)

string5 = "please clean your room!"
string5 = string5.capitalize() #Capitalize first letter
print(string5)

string6 = string5.upper() #Capitalize all letter
print(string6) #PLEASE CLEAN YOUR ROOM!

string7 = string6.lower() #lowercase all letter
print(string7)

string8 = "if iM FrOm gEn Z, i tYpE LiKe ThIs"
string9 = string8.swapcase() #IF Im fRoM GeN z, I TyPe lIkE tHiS
print(string9)

# %% LIST []

list1 = [10, 20, 30, 40, 50]
list2 = ["this is a string", 12, 40.0]
list3 = list()  #create an empty list
list4 = list(["tom", "jerry", 12345]) # create list with 3 items
list5 = list ("python")
print(list1,"\n", list2,"\n", list3,"\n", list4,"\n", list5)

# %% Accessing elements in the list

print(list1[2]) #access 3rd element in the list
print(len(list1)) #show how many elements in the list, 5
print(min(list1)) #show min value -> 10
print(max(list1)) #show max value -> 50
print(sum(list1)) #sum of values in list -> 150

#concatenate
print(list2*5) #repetition of the list by n times

# %% List Slicing

listofnames = ["Sherral", "Syamilah", "Aiman", "Azhar"]
print(listofnames[2:]) #print all names starts with an A
print(listofnames[:2]) #start index is optional, if omitted it will be 0
# + and * operators in list

list1 = ['11', '22']
list2 = ['33', '44']
list3 = list1 + list2
print(list3)
list3 = list1*2
print(list3)

# %%

a_tuple = (1,2,3)
a_list = [1,2,3]
a_list[2] = 4

#perform casting if want to change value in tuple
temp = list(a_tuple)
temp[2] = 4
a_tuple = tuple(temp)

# %% operations on tuple
# Use slicing operator, in and not in operators
# Tuple functions are simlar like list functions : sum(), max(), min(), len()

# %% Dictionary {key:value}

Azhar_friends = {
    "Sherral" : "60123456789",
    "Bathrisya" : "60987654321",
    "Aiman" : "6022222222"
}

print(Azhar_friends["Aiman"]) #6022222222
Azhar_friends["Aiman"] = "601111111"
len(Azhar_friends) #3

#print(Azhar_friends["Siti"]) #KeyError if key does not exist

print(Azhar_friends.keys()) #'Sherral', 'Bathrisya', 'Aiman'
print(Azhar_friends.values()) #'60123456789', '60987654321', '601111111'

#Two ways to retrieve the values

print(Azhar_friends["Sherral"])
print(Azhar_friends.get("Sherral"))

#Two ways to delete friends list
print(Azhar_friends.popitem()) #pick randomly and remove the
print(Azhar_friends.pop("Sherral"))

Azhar_friends.clear()
print(Azhar_friends)

# %% Math module
#Python Math
print(abs(-22)) # Returns the absolute value
print(max(9,1,2,3)) #Return the max number
print (min(8,7,6,5)) #Return the min number
print(pow(2,4)) #return 2**4 -> 2 to the power of 4
print(round(5.23456, 2)) #round to 2 digits after decimal point

#Import math module
import math
print(math.pi)
print(math.floor(24.9999)) # Round down to nearest integer #24
print(math.ceil)

#%% Control Statement : If-else, While, For loop