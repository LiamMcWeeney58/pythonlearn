# test comment
print ('hello world')
#3.1.1 Numbers 
2+2
17/3 #normal division
17//3 #floor division  (gets rid of fraction part)
17%3  #remainder of division
50+2*4 #order of operations is used 
5*2 #One star symbol '*' is used for multiplication (5*2=10)
5**2 #Two stars '**' is used to calculate powers (ex: 5**2 = 25 because 5x5=25)
length = 100 #example of how to assign a variable 
height = 9*3 #note for variables: they use order of operations so the order the variables in equation are assigned could change answer
5.25*10**3 #Floating point math is supported (5.25*10**3= 525.0)
#the underscore symbol '_' is used to define the last number used. For example: 5.25*10**3= 525.0, the 525.0 now is the '_' so if you were to do _/2 you would get 262.5
tax = 17.5/47
price = 58
price * tax
price + _ #use of previous number ex: the '_' will be 21.59574 as that is the previous number
round(_,2) #rounding rounds a decimal to a certain amount of decimal places (of your choice!) How it works: round(x,y)  x= the decimal you want to round  y= how many places you want to round
#3.1.2 Strings
'hello' #output is 'hello'
'won\'t you be my neighbor' #for words with the "'" symbol you will need to put a "\" before the "'" this will make the output have double quotes '""' 
"won't you be my neighbor" #same output as above however you don't need the '\' symbol as double quotes '""' are used
'"Won\'t you be my neighbor?" said Mr.Rodgers'#A quote inside a quote, this is the breaking point. The output of this line is '"Won\'t you be my neighbor?" said Mr.Rodgers' THIS IS NOT WHAT YOU WANT!
print('"Won\'t you be my neighbor?" said Mr.Rodgers') #This is what you want, the 'print()' function gets you a working output that you want 
qwerty = '1st\n2nd' #the 'n\' creates a new line for the text after it. Making h = print('text\nhere') will result in the output being 'none'
print(qwerty)
print('william\nathan\james') #this output cuts off the letter n
print(r'william\nathan\james') #the 'r' before the printed text 
print("""L1
L2
L3""")  #triple quotation marks can expand accross multiple lines
'Teddy likes to say ' + 65 * 'sorry! ' + 'a lot!' #Words can be multiplied to be spammed multiple times!
'Li' 'am' #output is 'Liam' as both were combined 
abcd = 'word1'
efg = 'word2'
abcd + efg #output is 'word1word2' putting the two variables together with no '+' symbol results in an error
LMfavDino = 'stegosaurus'
LMfavDino[5] #defines what character is in certain space 
LMfavDino[1:3] #definds characters inbetween chosen space. Output is 'et' if you made the '1' a '0' then the output would be 'ste'
LMfavDino[5:] #output is the last 6 characters: 'saurus'
LMfavDino[:5] #output is the first 5 characters
LMfavDino[-3] #negative number counts from the right as opposed from positives counting from the left
LMfavDino[5:] + LMfavDino[5:] #output is 'stegosaurus' (in a nutshell this is how the print went: 'stego' + 'saurus' = 'stegosaurus')
#first letter is 0 
'R' + LMfavDino[2:] #output is 'Regosaurus'
len(LMfavDino) #the function known as 'Len()' determines 
#3.1.3 Lists
MultiplesOf9 = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
MultiplesOf9 #lists the variables 
MultiplesOf9[6] #output is 63
MultiplesOf9[-5] #output is 54
MultiplesOf9[:]
#Lists are akin to strings 
MultiplesOf9 + [99, 108, 117, 126, 135, 144, 153] #output is [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153]
