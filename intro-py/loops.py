def total(l):
    s = 0
    for i in l:
        s += i
    return s

def average(t, l):
    return t / l

product_cart = [100, 200, 300, 400, 500]

t = total(product_cart)
a = average(t, len(product_cart))

print(f"The total is: {t}")
print(f"The average is: {a}")
