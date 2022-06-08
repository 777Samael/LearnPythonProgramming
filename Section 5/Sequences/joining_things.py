flowers = [
    "Daffodil",
    "Evening Primrose",
    "hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    # 42,
]

for flower in flowers:
    print(flower)

separator = ", "
output = separator.join(flowers)
print(output)

print(",".join(flowers))
