# Step 1: Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "Cocacola": 2500,
    "GOOGLE": 2700,
    "MICROSOFT": 300,
    "AMAZON": 3500
}

# Step 2: Get user input for stock holdings
portfolio = {}
print("Welcome to the Stock Portfolio Tracker!")
print("Enter the stock symbol and quantity you own (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Available: ", ', '.join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Step 3: Calculate total investment
total_investment = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\n Total Investment Value: ${total_investment}")

# Step 4 (Optional): Save to file
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio saved to 'portfolio_summary.txt'.")