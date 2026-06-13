# ============================================
# GEE252: Basic Python Programming Assignment
# Name: OBHAKHAN ISE USIFO
# Matric Number: ENV2404599
# ============================================

# ============================================
# Problem 1: Variables and Data Types
# ============================================
print("========== Problem 1: Variables and Data Types ==========")

# Stores and displays information about an African market
market_name = "Balogun market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False
total_revenue = 25000000

print("Market:", market_name, ", Type:", type(market_name))
print("Traders:", num_traders, ", Type:", type(num_traders))
print("Coordinates:", location_coords, ", Type:", type(location_coords))
print("Open Sundays:", is_open_sundays, ", Type:", type(is_open_sundays))
print("Average Daily Revenue per Trader:" , str(float(total_revenue/num_traders)) + " Naira")

print("")
print("========== Problem 2: Lists and Basic Operations ==========")

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]
print("")
#Add "Ivory Coast" to the end of the list
host_countries.append("Ivory coast")
print(host_countries)

print("")
#Insert "Morocco" at position 1
host_countries[1] = "Morocco"
print(host_countries)

print("")
#Remove "Senegal" from the list
host_countries.pop(3)
print(host_countries)

print("")
#Print the total number of countries in the list
print(len(host_countries))

print("")
#Countries in alphabetical order
host_countries = sorted(host_countries)
print(host_countries)

print("")
#every second country in the list using slicing
print(host_countries[::2])


print("========== Problem 3: Dictionaries ==========")
print("")
river_data= {
    
    "Nile": {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
 "Niger": {"length_km": 4180, "countries": 5}
}

print("")
#Add a new river Zambezi
river_data["Zambezi"] = {"length_km" : 2574, "countries" : 6}
print(river_data)
print("")

#Update the Niger river's countries value to 6
river_data["Niger"]["countries"] = 6
print(river_data)
print("")

#Print all river names
for river in river_data.keys():
    print(river)

print("")

#No of Congo river flow countries
print(river_data["Congo"]["countries"])
print("")

#Total combined length of all rivers
total = river_data["Nile"]["length_km"] + river_data["Congo"]["length_km"] + river_data["Niger"]["length_km"] + river_data["Zambezi"]["length_km"]
print(total)
print("")

print("========== Problem 4: Loops ==========")
print("")
#For loop: Multiplication table of 7 (from 7x1 to 7x10)
for i in range(1,11):
    print("7 x " + str(i) + "= " + str(7 * i))
print("")

#For loops: Each letter in the word "AFRICA"
word = "AFRICA"
for i in word: 
    print(i)

print("")
#For loop: Calculate the sum of all even numbers from 1 to 50
total = 0
for i in range(1,51):
    if i % 2 == 0:
        total = total + i
print(total)

print("")
print("=====PART B: WHILE LOOP=====")
#Count down from 20 to 1 and print each number
i = 20
while i >= 1:
    print(i)
    i = i - 1

print("")
#First number greater than 500 that is divisible by both 3 and 7
i = 500
while i % 3 != 0 or i % 7 != 0:
    i += 1
print(i)

print("")
print("========== Problem 5: Conditional Statements ==========")
#Monthly rainfall levels for West African weather monitoring
def classify_rainfall (mm):
    if mm > 300:
        return "Flood Risk"
    elif mm >= 200 and mm <= 300:
        return "Heavy Rain"
    elif mm >= 100 and mm <= 199:
        return "Moderate Rain"
    elif mm >= 1 and mm <= 99:
        return "Light Rain"
    else:
        return "Dry"
print("350 mm :" + classify_rainfall(350))
print("250 mm :" + classify_rainfall(250))
print("150 mm :" + classify_rainfall(150))
print("50 mm :" + classify_rainfall(50))
print("0 mm :" + classify_rainfall(0))

print("")
print("========== Problem 6: Functions ==========")
#Converts an amount in US Dollars to Nigerian Naira
def calculate_exchange (amount, rate):
    result = float(amount * rate)
    return result 
print(calculate_exchange(100,1580))
print("")
# This function formats a price with a currency code
# The currency parameter is optional, it defaults to "NGN" if not provided
def format_price (amount, currency = "NGN"):
    formatted = "{:,}".format(amount)
    return currency + " " + formatted
print(format_price(5000))
print(format_price(200, "GHS"))
print("")
#This function takes a list of sudent scores and returns the highest, lowest and class average scores
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores)/ len(scores)
    return lowest, highest, average 
#Test with: [55, 72, 88, 61, 94, 47, 79]
print(analyze_scores ([55, 72, 88, 61, 94, 47, 79]))