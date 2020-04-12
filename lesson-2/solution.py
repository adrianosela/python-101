symptoms = 0

print("What is your name?")
name = input()

print("What is your age?")
age = input()

print("Do you have a cough?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have excessive fatigue?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have a phlegm?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have a shortness of breath?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have bodyaches?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have a sore throat?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print("Do you have a lack of appetite?")
if (input() == 'yes'):
    symptoms = symptoms + 1

print()
print("Name: " + name)
print("Age: " + age)

if (symptoms >= 4):
	print("You present symptoms of the novel virus and you must seek medical attention.")
else:
	print("You do not present enough symptoms to merit seeking medical attention.")
