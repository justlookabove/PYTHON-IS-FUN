from math import *


name1 = "python app"
name2 = "internships"

print("My " + name1 + " brings all the " + name2 + " to the yard, and they're "
                                                   "like its better than yours.")

print("")

print("Holla!\nWe dem boyz!")

print("")

print("\"Holla! We makin noise!\"")

print("")

text = "THIS POST IS DOES NOT SOUND SERIOUS!"

print(text.lower().islower()) # Should return true
print(text[11]) # Should return S
print(text.replace("NOT", "HELLA"))

print("")

num = 36.6
print(sqrt( num))

theOffice = ["Michael", "Jim", "Pam", "Dwight", "Kevin", "Kevin", "Kelly"]
theOffice[4] = "Vance Refrigeration"
print(theOffice[1:5])

breakingBad = ["Walter White", "Jesse", "Hank", "Pollos Los Hermanos","That one gangster guy"]
theOffice.extend(breakingBad)

print(theOffice)

theOffice.append("Saul Goodman")
print(theOffice)

theOffice.insert(3, "Creed")
print(theOffice)

theOffice.remove("Pollos Los Hermanos")
print(theOffice)

theOffice.sort()
print(theOffice)

print("")

# Copying a list
anotherOffice = theOffice
print(anotherOffice)

coordinates = (4, 5)
print(coordinates[0])

i = 1
while i <= 10:
    print(i)
    i = i + 1

