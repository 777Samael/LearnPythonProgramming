parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

txt = 'we win'

for i in range(1, len(txt)):
    print(txt[i])

print('---')

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print('+' + parrot[9] + '+')

print('---')

print(parrot[10:])
print(parrot[10])

print('---')

print(parrot[:])

print('---')

print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-14:-8])

print('---')

print(parrot[0:6:2])
print(parrot[0:6:3])

print('---')

number1 = "9,223,372,036,854,775,807"
print(number1[1::4])

print('---')

number2 = "9,223;372:036 854,775;807"
print(number2[1::4])

separators = number2[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number2).split()
print([int(val) for val in values])
