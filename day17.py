#playlist manager
song=['tere naam','ektara','zindagi hai tu','dheere dheere','agar tum kaho']
print("original list:",song)
song.append('tula apnar ahe')
print("after append:",song)
song.insert(2,'tere bin')
print("afetr insert:",song)
song.remove('tere naam')
print("After remove:",song)
r=song.reverse()
print("After reverse:",r)

#exam score
score=[10,90,30,96,32,11,78]
print("Original:",score)
print("Descending:",sorted(score,reverse=True))
print("Asending:",sorted(score))
c=0
for s in score:
    if(s>80):
        c=c+1
print("Score >80:",c)

#travel destinations
countries=('Japan','Italy','canada','Australia','brazil')
print("Destination:",countries)
#countries[0]='India'
c1,c2,c3,c4,c5=countries
print("Unpacked:",c1,c2,c3,c4,c5)

#Employee names
employee=['john','renuka','pragati']
print("Original:",employee)
employee.extend(['sujit','aniket','atul'])
print("Afetr extend:",employee)
print("Index of renuka",employee.index('renuka'))
print("Afetr pop:",employee.pop(2))

#product prices
price=[60,34,65,87,38,90]
print("Product original price:",print)
print("highest:",max(price))
print("Lowest",min(price))
Average=sum(price)/len(price)
print("Average:",Average)
print("after clear:",price.clear())

#weekkly tempratures
temp=(34,76,23,54,89,13,75)
print("Temprature:",temp)
weekend=temp[5::]
print("weekend temp:",weekend)
checkTemp=76
if(checkTemp in temp):
    print(f"Temprature {checkTemp} exist in temprature")
else:
    price(f"Temprature {checkTemp} not exist")


#shopping cart
items=['milk','bread','butter','eggs','cheese']
print("original items:",items)
items.extend(['apple','banana','chocolate'])
print("After extend:",items)
print("After sorting:",items.sort())
items_copy=items.copy()
print("Copied:",items_copy)
items.clear()
print("original items after clear:",items)