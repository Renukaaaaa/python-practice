#square even numbers
numSquare=(n**2 for n in range(20)if n%2==0)
print(numSquare)
for num in numSquare:
    print(num)


#first letters extractor
words=['python','java','C','C++','PHP','Dot net','JavaScript']
wordsExtract=[w[0] for w in words]
print(wordsExtract)


#word lengths
sentence='python is fun to learn'
wordLenght=[len(word)for word in sentence.split()]
print(wordLenght)


#multiplication table
table=[[i*j for j in range(1,6)]for i in range(1,6)]
for row in table:
    print(row)


#fibonacci generator
def fibonacci(n):
    a,b=0,1
    count=0
    while count<n:
        yield a
        a,b=b,a+b
        count+=1
print(list(fibonacci(10)))


#prime number generator
primes=[n for n in range(2,51)if all(n % i!=0 for i in range(2,int(n**0.5)+1))]
print(primes)
    
