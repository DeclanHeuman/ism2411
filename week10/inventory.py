# Module 10 - Lists and Tuples
# Reflection 1: I was surprised by how many ways Python lists can be changed after they are created. I expected lists to work more like fixed groups of information, but I learned that items can easily be added, removed, replaced, and rearranged.
#
# Reflection 2: A Python list could save time in a retail business by keeping track of product inventory and sales. Instead of manually calculating totals or searching through a spreadsheet, Python could quickly calculate averages, find the highest sale, and identify products or sales that meet certain conditions.


# Exercise 1: Create and Print Lists
products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]

print("Products:", products)


# Exercise 2: Access List Elements
print("First product:", products[0])
print("Last product:", products[-1])
print("Third product:", products[2])


# Exercise 3: Slice a List
print("First three products:", products[:3])
print("Last two products:", products[-2:])


# Exercise 4: Modify a List
products[1] = "Smartphone"
products.append("Mouse")
products.remove("Tablet")

print("Updated products:", products)


# Exercise 5: Tuples
product_prices = (999.99, 699.99, 399.99, 89.99, 49.99)

print("Product prices:", product_prices)

try:
    product_prices[0] = 899.99
except TypeError:
    print("Tuples cannot be changed after they are created.")


# Exercise 6: Sales Calculations
sales = [120, 450, 275, 600, 90, 350, 500, 200]

total = 0

for sale in sales:
    total += sale

average = total / len(sales)
highest = max(sales)
lowest = min(sales)

print("Total sales:", total)
print("Average sale:", average)
print("Highest sale:", highest)
print("Lowest sale:", lowest)


# Exercise 7: Accumulator with Discount
discounted_total = 0

for sale in sales:
    discounted_price = sale * 0.90
    discounted_total += discounted_price

print("Total after 10% discount:", round(discounted_total, 2))


# Exercise 8: Filter Sales
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_sales_count = len(high_sales)

if high_sales_count > 0:
    high_sales_average = sum(high_sales) / high_sales_count
else:
    high_sales_average = 0

print("Sales over $300:", high_sales)
print("Number of sales over $300:", high_sales_count)
print("Average of sales over $300:", round(high_sales_average, 2))