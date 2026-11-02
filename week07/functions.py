
# Self-Assessment
#
# 1. In Exercise 5, the first bug I spotted was __________.
#    I found it by __________. This tells me that my current
#    debugging instincts are __________.
#
# 2. apply_discount(price, tier) takes a price and a discount
#    tier as inputs. It checks which tier was given, applies
#    the correct discount, and returns the discounted price.
#    A colleague could use it without reading the body because
#    the function name and inputs explain what it does.
#
# 3. AI Disclosure:
#    I used AI to assisnt me with the exercise 5 assignment.



# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


price = 200

print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


result = final_price(200, "gold", 0.07)
print(f"final_price(200, \"gold\", 0.07) = ${result:.2f}")


# --- Exercise 4 ---
orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 5 explanation:
# The first error was that total = sale replaced the total with each
# individual sale instead of adding them together. I changed it to
# total += sale so all the sales are added together.
# The second error was a missing colon after "for sale in sales".
# I added the colon because Python requires one after a for loop.
# The third error was using <= in the while loop. This caused the
# program to try accessing an index that does not exist. I changed
# it to < so the loop stops before reaching an invalid index.


# --- Exercise 6 ---
x = 100   # global variable


def double_it():
    x = 999   # local variable
    return x * 2


print(x)
print(double_it())
print(x)

# Scope explanation:
# The x outside the function is a global variable, while the x
# inside double_it() is a local variable. The local x only exists
# inside the function, so changing or creating it does not change
# the global x. Therefore, the output is 100, 1998, and 100.