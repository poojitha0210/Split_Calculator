#A bill of X with a tip of Y is split among Z people

print("Welcome to tip calculator")
bill=float(input("bill\n:"))
tip=int(input("what percentage:\n"))
no_of_ppl=int(input("Total number of people:\n"))
tip_as_percent=(tip/100)
total_amount=(bill)*(tip_as_percent)
total_bill=bill+total_amount
split=total_bill/no_of_ppl
final_amt=round(split,2)
print(f"Each person should pay: ${final_amt}")