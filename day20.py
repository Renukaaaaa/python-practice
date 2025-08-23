#first and last character
str='PYTHON'
print("first character:",str[0],"last character:",str[-1])


#list reversal
colours=['yellow','green','orange','red','black','white','pink','violet']
print("Original list:",colours)
print("Revese list:",colours[::-1])


#extract middle element
numbers=[10,20,30,40,50,60,70]
print(numbers[2:5])


#odd indexed characters
str1='PYTHONPROGRAMMING'
print("letters at odd index",str1[0::2])


#sort words alphabetically
words=['python','is','the','important','java','world']
print("Asending",sorted(words))
print("descending",sorted(words,reverse=True))


#sort by string length
fruits=['apple','kiwi','banana']
sorted_words=sorted(fruits,key=len)
print(sorted_words)


#sort by second element
tuples=[(1,5),(3,1),(2,4)]
sorted_tuples=sorted(tuples,key=lambda x:x[1])
print(sorted_tuples)