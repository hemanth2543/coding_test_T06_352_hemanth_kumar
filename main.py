'''
1. Implement palindrome using iterator(for loop) and generator mechanism.'''
print("\n=======palindrome means reverse of that thing  should be same is called palindrome=====")
print(" \n------- 1.a. List Comprehension ------ ")
word=input(" enter a string: ")#static input MALAYALAM
palindrome = [w for w in word if w == w[::-1]]
k=''.join(palindrome)# to join the spilted letters into one and assining to the variable k
if word==k: # for checking the word is a palindrome or not
    print(word,"is a palindrome")
else:
    print(word, "is not a palindrome")

print("\n-------------------------------1.1.palindrome using iterator(for loop)-------------------------------------------")
print("\npalindrome using iterator(for loop)")
S=input(" enter a string: ")#static input MALAYALAM
for i in S:#for loop
    if S==S[::-1]:#s=MALAYALAM and S[::-1] means revers of S that is malayalam
        print(S,"is a palindrome")
        break# to break the loop
    else:
        print('It is a palindrome')
        break

print("\n-------------------------------1.2.palindrome using generator mechanism-------------------------------------------")
print("\nrange is genaretor soo i am using the range function for numbers to check palindrome or not")
N=input("enter a number: ")# static input 12321

i=0# intialy declaring the i=0

for i in range(len(N)):# for loop
    if N[i]!=N[-1-i]:# n[i]=0 and n[-1-0]=-1 so 1 will store in -1 position like that the loop will itrate
        # untill the length of the N
        print('It is not a palindrome')
        break# here break the loop
    else:
        print('It is a palindrome')
        break # if dont give brak it will continue that is infinate loop


print("\n---------------------------------------------------------------------------------------------------------------------------------")

'''
2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46'''
print("\n------------------------2.Sum of 2 digits into output------------------------- ")
n1=int(input("enter n1 number: "))
n2=int(input("enter n2 number: "))
cou=0
N1=[]
temp=n1
while temp>0:  # i am retiving the each number from the given number n1
    k=temp%10   #123%10=3
    N1.append(k) # appending to N1
    cou=cou+k  # adding count
    temp=temp//10
sum=0
N2=[]
num=n2
while num>0:   # i am retiving the each number from the given number n2
    s=num%10     #456%10=6
    N2.append(s)  # appending to N2
    sum=sum+s
    num=num//10
N3 = [] # declaration of the empyt list
for x in range (0, len (N1)): #for loop
    N3.append( N1[x] + N2[x]) #again appending
sum=0
for i in N3:
    sum=sum+i # adding each and every element inthe list N3
print("sum of two numbers output",sum)


'''
		
3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba
   '''
def rev_str(s): # function declaration
    x = list(filter(str.isalpha, s[::-1])) # reversing the alphagets
    for i,s_ in enumerate(s):
        if not s_.isalpha():
            x.insert(i, s_)
    return ''.join(x)

instr = "ab@#cd!ef"
outstr = ' '.join(rev_str(s) for s in instr.split())

print("Reverse string considering only alphabets. Symobls should not be reversed",outstr)

'''

4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
# '''
print("\n---------4.elements duplicate count output in  dict format-----------")
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
      #this is navie method
d={}#crestion of  empty dict
for i in some_list:#for loop
    if i in d: #if condition for checking i is presint inside the dict d or not
        d[i]+=1
    else:
        d[i]=1
print("duplicate count output in  dict format",d)
'''
		
		
5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
   
   '''
print("\n------------5.adding of two tuples-----------")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)

#in t1 supprating the strings and integers and store into n1 and n2
n1=[]
n2=[]
for i in t1:
    if type(i)==int:
        n1.append(i)
    else:
        n2.append(i)


#in t2 supprating the strings and integers and store into l1 and l2
l1=[]
l2=[]
for i in t2:
    if type(i)==int:
        l1.append(i)
    else:
        l2.append(i)


# adding n1 l1 lists becouse thouse elements are integers
k=[]
for i in range(0,len(n1)):
    k.append(n1[i]+l1[i])


# adding n2 l3 lists becouse thouse elements are strings
m=[]
for i in range(0,len(n2)):
    m.append(n2[i]+l2[i])


##adding k m lists becouse thouse elements to one single list
output=k+m
#converting list into tuple
print("adding of two tuples output is",tuple(output))


'''

6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
# '''
print("---------------------6.""remove leading zeros from an IP address.----------------------")
input="216.08.094.196" #input
for i in input: # for loop
    if i=='0': #checking condection
        del(i)
    else:
        print("remove leading zeros from an IP address",i,end="")
'''
			
	
   
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
'''

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] # this is input
print(list(map(lambda x:int(x),str(l).replace('[','').replace(']','').split(', '))))
             #in this i am repalcing the [ ] with space by using map and lambda functions placing into the list
'''

8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
	
'''

print("\n--------------------8.Load sample content in text file----------------------------")
def counter(khk1): # function declaration khk1 is a file name
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_vowels=0
    num_spaces = 0
    with open(khk1, 'r') as f: #context manager it will resposible for open and close the file in read mode
        for line in f: # f is variable which will store the obj
            num_lines += 1# increment
            word = 'Y'#declaring a variable word and assigning its value as Y because every file is
                        # supposed to start with a word or a characte loop to iterate ever line letter by letter
            for letter in line:

                # condition to check that the encountered character is not white space and a word
                if (letter != ' ' and word == 'Y'):

                    # incrementing the word count by 1
                    num_words += 1

                    # assigning value N to variable word because until space will not encounter a word can not be completed
                    word = 'N'

                # condition to check that the encountered character is a white space
                elif (letter == ' '):

                    # incrementing the space count by 1
                    num_spaces += 1

                    # assigning value Y to variable word because after white space a wor is supposed to occur
                    word = 'Y'
                elif (letter in ["a",'e','i','o','u']):

                    num_vowels+=1
                    word='Y'

                # loop to iterate every letter character by character
                for i in letter:

                    # condition to check that the encountered character is not white space and not a newline character
                    if (i != " " and i != "\n"):
                        # incrementing character count by 1
                        num_charc += 1

    # printing total word count
    print("\n------------------------------8.2. No of words in a file ------------------------------------")
    print("Number of words in text file: ",
          num_words)

    # printing total line count
    print("\n----------------------------8,1. No of lines in file-----------------------------")
    print("Number of lines in text file: ",
          num_lines)

    # printing total character count
    print("\n--------------------------------8.3. No of chars --------------------------------------------")
    print('Number of characters in text file: ',
          num_charc)

    # printing total space count
    print("\n----------------------------8.	5. No of special chars ---------------------------------------------")
    print('Number of spaces in text file: ',
          num_spaces)

    # printing total vowels count
    print("\n----------------------------8.	4. No of  vowels ---------------------------------------------")
    print('Number of vowels in text file: ',
          num_vowels)


# Driver Code:
if __name__ == '__main__':
    fname = 'khk1.txt'
    try:
        counter(fname)
    except:
        print('File not found')
