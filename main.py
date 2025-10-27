"""
GBP/JPY Converter - A simple currency converter for GBP and JPY.
Will be developed later into something more advanced.

This script converts between British Pounds (GBP) and Japanese Yen (JPY)
using a fixed conversion rate for simplicity.
"""

# Define the fixed conversion rate (1 GBP = 202.56 JPY)
CONVERSION_RATE = 202.56

# Get the initial amount from user and validate it's positive
amount = float(input("Enter an amount: "))

# Input looped until a positive amount is provided
while amount <= 0:
    amount = float(input(
        "To use this correctly please enter an amount greater than 0: "
    ))

# Get the currency type and convert to uppercase for case-insensitive input
currency = input("What currency is that? (GBP/JPY): ").upper()

# Validate currency input - only accept GBP or JPY for now
while currency not in ["GBP", "JPY"]:
    currency = input("Please enter a valid currency (GBP/JPY): ").upper()

# Round the amount to 2 decimal places for proper currency display
amount = round(amount, 2)

# Perform conversion based on input currency
# Converting from GBP to JPY
if currency == "GBP":
    print(f"The amount £{round(amount, 2):,.2f}")
    amount = amount * CONVERSION_RATE
    print(f"Converted to JPY(Japanese Yen) is: ¥{round(amount, 2):,.2f}")
    
    # Converting from JPY to GBP
elif currency == "JPY":
    print(f"The amount ¥{amount:,.2f}")
    amount = amount / CONVERSION_RATE
    print(f"Converted to GBP(Pound Sterling) is: £{round(amount, 2):,.2f}")
else:
    # This case should never happen due to the validation loop above
    print(f"{currency} is not a valid currency.")
