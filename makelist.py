file = open('list.txt' , 'w')

count = 0
while count < 10:
    user = input("What is your favorite animal?")
    file.write(user)
    count += 1

file.close()
