def python_food():
    width = 80
    text = "Spam and egg"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centred", mode='w') as centred_file:

# call the function
# print(center_text("spam and eggs"))
# print(center_text("spam, spam and eggs"))
# print(center_text(12))
# print(center_text("spam, spam, spam and spam"))
# print(center_text("first", "second", 3, 4, "spam", sep=":"))

with open("menu", "w") as menu:
    s1 = center_text("spam and eggs")
    s2 = center_text("spam, spam and eggs")
    s3 = center_text(12)
    s4 = center_text("spam, spam, spam and spam")
    s5 = center_text("first", "second", 3, 4, "spam", sep=":")
    print(s1, file=menu)
    print(s2, file=menu)
    print(s3, file=menu)
    print(s4, file=menu)
    print(s5, file=menu)
