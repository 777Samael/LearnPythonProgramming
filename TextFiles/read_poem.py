# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     # print(line, end='')
#     # print(line.strip())
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()
# ----------------
# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.strip())
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
#
# for line in reversed(lines):
#     print(line, end='')
# ----------------
# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()
#
# print(text)
# for character in reversed(text):
#     print(character, end='')
# ----------------
# with open('Jabberwocky.txt') as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
#
# print("---")

with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
