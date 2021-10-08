# Century from year
year_in = int(input("Enter the year: "))

if (year_in % 100) > 0 :
    century = (year_in // 100) + 1
else :
    century = year_in // 100

print(f"The century is: {century}")