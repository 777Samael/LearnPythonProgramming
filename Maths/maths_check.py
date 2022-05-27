# x% * y == y% * x
# x/100 * y == y/100 * x

for x in range(1, 100):
    for y in range(1, 100):
        lewa = round(x/100 * y, 2)
        prawa = round(y/100 * x, 2)
        if not lewa == prawa:
            print(f"{x}% * {y} ({lewa}) <> {y}% * {x} ({prawa})")
        # else:
        #     print(f"{x}% * {y} ({lewa}) = {y}% * {x} ({prawa})")
