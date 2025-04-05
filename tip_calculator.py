print ("Welcome to the tip Calculator!")
total_bill= float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10,12,15? "))
no_of_people=int(input("How many people to split the bill? "))
tip_given= total_bill *(tip_percent/100)
total_payment= total_bill+tip_given
pay=(total_bill+tip_given)/no_of_people
print(f"total tip calculated {round(tip_given,2)}")
print(f"Total bill is {round(total_payment,2)}")
print(f"Each person should pay {round(pay,2)}")