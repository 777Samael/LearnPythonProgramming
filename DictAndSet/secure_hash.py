import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print(sorted(hashlib.algorithms_available))

python_program = """for i in range(10):
print(i)
"""
print(python_program)

# for b in python_program.encode('utf8'):
#     print(b, chr(b))

original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}")

python_program += "print('code change')"
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf8'))
print("---")
print(f"SHA256: {new_hash.hexdigest()}")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")
