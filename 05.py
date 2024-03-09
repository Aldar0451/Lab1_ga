zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
# посадите медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear') 
print(zoo)
 
# добавьте птиц из списка birds в последние клетки зоопарка 
birds = ['rooster', 'ostrich', 'lark', ]
for item in birds:
    zoo.append(item)
print(zoo) 

# уберите слона
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
lion_position = zoo.index('lion')
print(f"Лев сидит в клетке  номер {lion_position +  1}")

lark_position = zoo.index('lark')
print(f"Жаворонок сидит в клетке  номер {lark_position +  1}") 
