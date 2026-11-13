"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
Concepts used: dictionary, input/output, basic arithmetic, file handling
"""

# Hardcoded stock prices (dictionary)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_available_stocks():
    """Print all stocks and their prices."""
    print("\nAvailable stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    show_available_stocks()

    portfolio = {}  # stock name -> quantity the user owns

    print("\nEnter stock name and quantity. Type 'done' when finished.")

    while True:
        stock = input("\nStock name (or 'done'): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Please choose from the available list.")
            continue

        quantity_text = input(f"How many shares of {stock}? ").strip()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print("Please enter a valid whole number (like 5).")
            continue

        quantity = int(quantity_text)

        # If the stock is already added, increase its quantity
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"Added {quantity} share(s) of {stock}.")

    # Nothing entered
    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    # Calculate and display the total investment value
    print("\n=== YOUR PORTFOLIO ===")
    total = 0
    lines = []
    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        total += value
        line = f"{stock}: {quantity} x ${STOCK_PRICES[stock]} = ${value}"
        print(line)
        lines.append(line)

    print(f"\nTotal investment value: ${total}")

    # Optional: save result to a text file
    save = input("\nSave result to a file? (yes/no): ").lower().strip()
    if save == "yes" or save == "y":
        with open("portfolio.txt", "w") as file:
            file.write("=== STOCK PORTFOLIO ===\n")
            for line in lines:
                file.write(line + "\n")
            file.write(f"\nTotal investment value: ${total}\n")
        print("Saved to portfolio.txt")

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
