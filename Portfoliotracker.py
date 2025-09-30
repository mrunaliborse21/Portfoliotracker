stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 140
}

portfolio = {}
total_value = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Please choose from the available list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Calculate total investment
print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")

# Optional: Save to file
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_value}\n")
    print("✅ Summary saved to 'portfolio_summary.txt'")
