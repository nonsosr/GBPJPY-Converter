# GBP/JPY Converter
# Will be developed later into something more advanced using

Amount = float(input("Enter an amount:"))
currency = input("What currency is that? (GBP/JPY): ")

Amount = round(Amount, 2)
if currency == "GBP":
    print(f"The amount £{Amount}")
    Amount = Amount * 202.56
    print(f"Converted to: ¥",round(Amount, 2))
elif currency == "JPY":
    print(f"The amount ¥{Amount}")
    Amount = Amount / 202.56
    print("Converted to: £",round(Amount, 2))
