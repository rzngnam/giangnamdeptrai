numbers = [1,1,2,3,4,2,3,4,5,6,7,8,1,2,3,41,2,3,41,2]
num = int(input("Enter a number ? "))
n = dict()
strnumber = ''
for i in range(len(numbers)):
    strnumber = strnumber + str(numbers[i])

for i in range(len(strnumber)):
    if strnumber[i] in n:
        n[strnumber[i]] += 1
    else:
        n[strnumber[i]] = 1

print("{0} appears {1} times in my list".format(num,n[str(num)]))