print("Welcome to the Tip Calculator")
Total_Bill = float(input("What was the total bill? ₹"))
Tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
No_of_people = int(input("How many people to split the bill: "))
# Calculates via formula and rounds up the number up to 2 decimal places.👇🏼
each_pay = round((Total_Bill + (Total_Bill * Tip) / 100) / No_of_people, 2)
print(f"Each person should pay: ₹{each_pay}")