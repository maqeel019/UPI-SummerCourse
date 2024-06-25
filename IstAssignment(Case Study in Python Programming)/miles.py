# Initialize variables to store total miles and total gallons
total_miles = 0
total_gallons = 0

# Initialize a flag to indicate whether to continue inputting data
continue_input = True

while continue_input:
    # Prompt user to input miles driven and gallons used for each tankful
    miles_driven = float(input("Enter miles driven (-1 to quit): "))
    if miles_driven == -1:
        break
    gallons_used = float(input("Enter gallons used: "))

    # Calculate and display miles per gallon for each tankful
    mpg = miles_driven / gallons_used
    print(f"Miles per gallon for this tankful: {mpg:.2f}")

    # Update total miles and total gallons
    total_miles += miles_driven
    total_gallons += gallons_used

# Calculate and display combined miles per gallon for all tankfuls
if total_gallons > 0:
    combined_mpg = total_miles / total_gallons
    print(f"\nCombined miles per gallon for all tankfuls: {combined_mpg:.2f}")
else:
    print("No data entered.")