print("Welcome to the tip calculator.")
print("===========================================================")
sub_total = float(input("Enter the bill amount $: "))
tip = float(input("Enter the tip percentage (10, 12, 15): "))
ppl_split = int(input("How many people to split the bill: "))
 
total = (sub_total * tip) / 100 + sub_total
split = round(total / ppl_split, 2)
 
print("=================================")
print(f"Total bill: ${total:.2f}")
print(f"Each person must pay: ${split:.2f}")
 
print("============================================================")
print("Thanks for dinner with us")
