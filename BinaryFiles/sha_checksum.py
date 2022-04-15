import hashlib

published_hash = '9f47eda37229f68eee03b24b9748937c7dc3868f906e8ba69fbcbdd3bc5dc3e2'

filename = 'colorama-0.4.4-py2.py3-none-any.whl'

with open(filename, 'rb') as downloaded_file:
    contents = downloaded_file.read()

file_hash = hashlib.sha256(contents).hexdigest()
print(file_hash)

if file_hash != published_hash:
    print(f'The file {filename} has been modified')
else:
    print(f'File {filename} hash is correct')
