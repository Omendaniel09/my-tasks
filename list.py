name = input("what is your name?: ")

foods = []

food1 = input("enter your favourite food: ").strip()
foods.append(food1)

food2 = input("enter your second favourite food: ").strip()
foods.append(food2)

food3 = input("enter your third favourite food: ").strip()
foods.append(food3)

print('\nHello' , name + "!  Your favourite foods are:")
for i in range(len(foods)):
    print(f"{i + 1}. {foods[i]}")