# GBP/JPY Converter
# Will be developed later into something more advanced

Amount = float(input("Enter an amount:"))
currency = input("What currency is that? (GBP/JPY): ")

Amount = round(Amount, 2)
if currency == "GBP":
    print(f"The amount £{Amount}")
    Amount = Amount * 202.56
    print(f"Converted to JPY is: ¥{round(Amount, 2):,.2f}")
elif currency == "JPY":
    print(f"The amount ¥{Amount:,.2f}")
    Amount = Amount / 202.56
    print(f"Converted to GBP is: £{round(Amount, 2):,.2f}")
else:
    print(f"{currency} is not a valid currency.")
