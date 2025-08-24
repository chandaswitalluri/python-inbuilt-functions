#string----> immutable

#case-conversions-builtin functions
#lower,upper,islower,isupper,swapcase,len,captlize
#len,count,index----for list and string common

#lower--->to convert from upper to lower
a="chandaswi"
print(a.lower())
#chandaswi    

#upper---->to convert from lower to upper
a="chandaswi"
print(a.upper()) 
#CHANDASWI  
#isupper---to check uppercase letter
a="chandaswi"
print(a.isupper())   
#False

#isupper--->to check lowercase letter
a="chandaswi"
print(a.islower())   
#True

#swapcase--->change upper to lower lower to upper
a="CHandaswi"
print(a.swapcase()) 
#chANDASWI   

#captilise--->only 1st letter of 1st word change to capital
#after space it wont change of every word---drawback
#to overcome that we use title
a="chandaswi"
print(a.capitalize())  
#Chandaswi

#title----->only 1st letter for every word after spaces capital
a="chandaswi"
print(a.title())  
#Chandaswi 

#trimming and replacing builtin fun
#strip,rstrip,lstrip,replace

#strip--->to remove extra spaces
#assign then print
a="      chandaswi    "
a=a.strip()
print(a)    
#chandaswi

#rstrip -----to remove space from right
a="      chandaswi    "
a=a.lstrip()
print(a)
#chandaswi         

#lstrip--to remove space from left
a="      chandaswi    "
a=a.rstrip()
print(a)  
#      chandaswi 

#replace---to replace old val with new value
#replace(old,"new")
#if we replace the word with other word which is not there in given string it wont give error
#but it just run the code without any op and error
a="chandaswi"   
a=a.replace("chandaswi","talluri")
print(a) 
#talluri  

a="chandaswi is"   
a=a.replace("talluri","talluri")
print(a)
#chandaswi is    

#find---where the elm is present in which index
str1="chandu"
print(str1.find('s')) 
#-1  

#startswith---we get true or false if the word starts with same
str1="chandu"
print(str1.startswith('c'))   
#True
print(str1.startswith('h'))    
#False

#endswith---we get true or false if the word starts with same
str1="chandu"
print(str1.endswith('ndu'))   
#True
print(str1.endswith('u'))    
#True

#split---it split each elem
num1=input("enter nums: ")
print(num1.split(','))   
#['1', '3', '5', '7']

#len()--->find the length of the string
a="chandaswi"
print(len(a))
#9

#count()--->it is used to count the number of occurances of a substring in the string.
a="chandaswi"
print(a.count("a"))
#2


#index()--->it is used to find the index of the first occurances of a substring in the string.
a="chandaswi"
print(a.index("s"))
#6


#map---->map(function,iterable)
def  square(x):
    return x**2
print(list(map(square,[2,3,4])))   
#[4, 9, 16]

#join
list1=["1","2","3","hello"]
encoded_str=','.join(list1)
print(encoded_str)  
#1,2,3,hello


#set--->collection of unordered finite unique
#1.add---->to add elem into set
a={1,2,3}
a.add(20)
print(a) 
 #{ 1, 2, 3,20}

#2.remove
#in remove if we give element from outside we get error
#
a={1,2,3}
a.remove(2)
print(a)   
#{1, 3}

#3.discard
#if we give element from outside also it print same input but wont give error
a={1,2,3}
a.discard(10)
print(a)   
#{1, 2, 3}

#4.pop---->which index to del
a={1,2,3}
print(a.pop()) 
#1
print(a)    
#{2, 3}

#5.clear---->remove everything
a={1,2,3}
print(a.clear())  
#none
a.clear()
print(a)   
#set()

#6.union--->combine both sets
a={1,2,3}
b={10,11,12}
print(a.union(b))   
#{1, 2, 3, 10, 11, 12}

#7.difference
#if a-b we get a elem which are not in b
#if b-a we get b elm which are not in a
a={3,4,5}
b={1,2,3,5,8,9}
print(a.difference(b)) 
#{4}  
print(b.difference(a))
# {8,1,2,9}

#intersection---->common elem from both
a={3,4,5}
b={1,2,3,5,8,9}
print(a.intersection(b))  
#{3,5}  

#symmetric_difference---->which are same that elem we wont get
a={3,4,5}
b={1,2,3,5,8,9}
print(a.symmetric_difference(b))
#{1,2,4,8,9} 


#isdisjoint--->no common elm we get true or false
a={3,4,5}
b={1,2,3,5,8,9}
print(a.isdisjoint(b))   
#False
a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))   
#True