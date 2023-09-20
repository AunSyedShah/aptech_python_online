total = 0
while True:
    price = int(input("Enter price: "))
    if price < 1:
        break
    total += price

print(f"Total: {total}")


# You bought 12 products for 12000