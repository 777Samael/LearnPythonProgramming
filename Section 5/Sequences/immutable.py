result = True
another_result = result
print(id(result))
print(id(another_result))

result = False

print(id(result))
print(id(another_result))

print("---")

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

print("---")

result += "ish"
print(id(result))
print(id(another_result))
