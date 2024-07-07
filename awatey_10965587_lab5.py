"""
    Name: Manasseh A. Awatey
    ID:   10965587
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")
print(data)


# ---------------- Exercise 1 ---------------- 
total_profits = data["total_profit"]
month_number = data["month_number"]


# re-assigning 
x = month_number
y = total_profits

# generating line plot 
plt.plot(x, y, label= "Company rofit per month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.xlim(1, 12)
plt.ylim(100000, 500000)
plt.title("Company rofit per month")
plt.show()



# ------------  Exercise 2 -------------
total_profits = data["total_profit"]
month_number = data["month_number"]

# re-assigning 
x = month_number
y = total_profits

# generating line plot 
plt.plot(x, y, linestyle=':', color='red', marker='o', markersize=8, markerfacecolor='black', linewidth=3, label= "Profit data of last year")
# plt.plot(df['Month'], df['Profit'], linestyle=':', color='red', marker='o', markersize=8, markerfacecolor='red', linewidth=3, label='Profit Data')

plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.xlim(1, 12)
plt.ylim(100000, 500000)
plt.title("Company rofit per month")
plt.legend(loc='lower right')
plt.show()



# ----------- Exercise 3 ----------- 
x = month_number
y1 = data["facecream"]
y2 = data["facewash"]
y3 = data["toothpaste"]
y4 = data["bathingsoap"]
y5 = data["shampoo"]
y6 = data["moisturizer"]


plt.plot(x, y1, label = "Facecream sales data", marker = "o")
plt.plot(x, y2, label= "Facewash sales data", marker= "s")
plt.plot(x, y3, label = "Toothpaste sales data", marker = "o")
plt.plot(x, y4, label= "Bathingsoap sales data", marker= "s")
plt.plot(x, y5, label = "Shampoo sales data", marker = "o")
plt.plot(x, y6, label= "moisturizer sales data", marker= "s")
plt.xlabel("Month Number")
plt.ylabel("Sales units in Number")
plt.title("Sales data")
plt.legend()
plt.show()



# ------------- Exercise 4 ------------- 
labels = ["facecream", "facewash", "toothpaste", "Bathingsoap", "shampoo", "moisturizer"]
sizes = [34480,	18515,	69910,	114010,	25410,	18515]
colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue", "red", "yellow"]
plt.pie(sizes, labels= labels, colors= colors, autopct="%1.1f%%")
plt.title("Sales data")
plt.legend(loc="lower right")
plt.show()



# ----------------- Exercise 5 ---------------
months = month_number
facecream = data["facecream"]
facewash = data["facewash"]
toothpaste = data["toothpaste"]
bathingsoap = data["bathingsoap"]
shampoo = data["shampoo"]
moisturizer = data["moisturizer"]

labels = ["facecream", "facewash", "toothpaste", "Bathingsoap", "shampoo", "moisturizer"]


# Creating the stack plot
plt.figure(figsize=(10, 6))
plt.stackplot(months, facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer, labels= labels)
plt.xlabel("Month Number") 
plt.ylabel('Sales units in Number')
plt.legend(loc='upper left')
plt.title("All products sales data using stack plot")

plt.show()



# ------------- Exercise 6 ------------
 
months = month_number
facewash = data["facewash"]
bathingsoap = data["bathingsoap"]

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot for Facewash
ax1.plot(months, facewash, marker='o', linestyle='-', color='black', label='Facewash')
ax1.set_title('Sales data of facewash')
ax1.grid(True)
ax1.legend()

# Plot for Bathing Soap
ax2.plot(months, bathingsoap, marker='o', linestyle='-', color='r', label='Bathing Soap')
ax2.set_title('Sales data of Bathingsoap')
ax2.set_xlabel('Months')
ax2.set_ylabel('Sales units in Number')
ax2.grid(True)
ax2.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
facewash = [18515, 19400, 20100, 20700, 21000, 21500, 22000, 22500, 23000, 23500, 24000, 24500]
bathingsoap = [114010, 118800, 121500, 125000, 129000, 134000, 137000, 140500, 144000, 147500, 151000, 154500]

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot for Facewash
ax1.plot(months, facewash, marker='o', linestyle='-', color='b', label='Facewash')
ax1.set_title('Facewash Sales Over Months')
ax1.set_xlabel('Months')
ax1.set_ylabel('Units Sold')
ax1.grid(True)
ax1.legend()

# Plot for Bathing Soap
ax2.plot(months, bathingsoap, marker='s', linestyle='--', color='r', label='Bathing Soap')
ax2.set_title('Bathing Soap Sales Over Months')
ax2.set_xlabel('Months')
ax2.set_ylabel('Units Sold')
ax2.grid(True)
ax2.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()