# i wrote the commments for better undertstanding if you stuck in any line of code.
def main():
    print("Miles Per Gallon Calculation")  # Starting off by informing the user about the program
    total_miles = 0  # This will keep track of the total miles driven
    total_gallons = 0  # This will keep track of the total gallons used

    while True:  # We'll keep asking for input until the user decides to stop
        try:
            # Asking the user how many gallons were used. They can type -1 to end the input process.
            gallons = float(input("Enter the gallons used (-1 to end): "))
            if gallons == -1:  # If the user types -1, we'll break out of the loop
                break
            
            # Now we ask for the miles driven
            miles = float(input("Enter the miles driven: "))

            if gallons == 0:  # We can't divide by zero, so we need to handle this case
                print("Gallons used cannot be zero. Please enter a valid number.")
                continue  # Skip the rest of the loop and start over

            # Calculate miles per gallon for this particular tank
            mpg = miles / gallons
            # Display the result to the user with 6 decimal places
            print(f"The miles/gallon for this tank was {mpg:.6f}")

            # Add the current miles and gallons to our total
            total_miles += miles
            total_gallons += gallons
        except ValueError:  # If the user enters something that isn't a number, we'll end up here
            print("Invalid input. Please enter numerical values.")

    if total_gallons > 0:  # If we've collected any valid data, we'll calculate the overall mpg
        combined_mpg = total_miles / total_gallons
        # Display the overall average miles per gallon
        print(f"\nThe overall average miles/gallon was {combined_mpg:.6f}")
    else:  # If no valid data was entered, we'll let the user know
        print("No valid input received.")

if __name__ == "__main__":
    main()  # This makes sure the script runs when we execute the file
'''
     Output of the program is:
     
Miles Per Gallon Calculation
Enter the gallons used (-1 to end): 9
Enter the miles driven: 129.48
The miles/gallon for this tank was 14.386667
Enter the gallons used (-1 to end): 3
Enter the miles driven: 70
The miles/gallon for this tank was 23.333333
Enter the gallons used (-1 to end): -1

The overall average miles/gallon was 16.623333

'''