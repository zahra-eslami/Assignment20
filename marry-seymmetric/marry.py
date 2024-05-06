import random

boys = ['Ali', 'Reza', 'Hassan', 'Mehdi', 'Amir', 'Kourosh', 'Babak', 'Farhad']
girls = ['Maryam', 'Sara', 'Leila', 'Zahra', 'Narges', 'Parisa', 'Sepideh', 'Fatemeh', 'Sanaz']

min_length = min(len(boys), len(girls))

random.shuffle(boys)
random.shuffle(girls)

results = []
for i in range(min_length):
    results.append((boys[i], girls[i]))

print("marry list:")
for boy, girl in results:
    print(f"{boy} &  {girl}")
