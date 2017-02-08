Fam = ["David", "Ann", "Joe", "Meg", "Dottie", "Rosie", "Daisey"]

#print(Fam[0])
#print(Fam[0].lower()) 

#print(Fam[-1]) #Returns last Element

#message = "Why is " + Fam[-1] + " always so bad."

#print(message)

#Fam.append("Chris")
#print(Fam)

Friends = []

Friends.append('Joe')
Friends.append('John')
Friends.append('Mike')
Friends.append('Matt')
Friends.insert(0, 'Zach')
Friends.append('Jake')

print(Friends)

del Friends[3]
print(Friends)

Friends.pop()

#first_friend = Friends.pop(1) #you can pop any list item

#print("My first friend was: " + first_friend)

#Fam.remove('Dottie')
#print(Fam)
Friends.append('Mike')

Friends.sort()
print("Sorted friends list: " + str(Friends))
Friends.sort(reverse=True)
print("Reverse alphabetical of friends list: " + str(Friends)) #reverse() just puts the list in reverse order

print("Length of List: " + str(len(Friends)))


