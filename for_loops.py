for blah in "THIS SENTENCE IS AWESOME!":
    print(blah)

print("")

friends = ["Bob", "Sarah", "Amy", "Matthew"]

for index in friends:
    print(index)

print("")

for num in range(10):
    print(num)

print("")

'''
num = 0
for index in friends[num]:
    print(index)

print("")

'''
print(len(friends))
print("")
num = 0
while num < len(friends):
    for index in friends[num]:
        print(index)
    num += 1
    print("")

