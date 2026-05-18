import csv
import os

# File to store expenses
CSV_FILE = "expenses.csv"

def create_csv_if_not_exists():
    """Create expenses.csv with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["item", "amount"])


def add_expense():
    """Add a new expense to the CSV file."""
    print("\n--- Add Expense ---")
    
    # Get item name from user
    item = input("Enter item name: ").strip()
    if not item:
        print("Error: Item name cannot be empty!")
        return
    
    # Get amount from user
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Error: Amount must be greater than 0!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    # Append the expense to CSV file
    try:
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item, amount])
        print(f"✓ Expense added: {item} - ₹{amount}")
    except Exception as e:
        print(f"Error: Could not save expense. {e}")


def view_expenses():
    """Display all expenses from the CSV file."""
    print("\n--- View All Expenses ---")
    
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        
        # Check if file is empty or only has headers
        if len(expenses) <= 1:
            print("No expenses recorded yet!")
            return
        
        # Display header
        print(f"\n{'Item':<20} {'Amount':<10}")
        print("-" * 30)
        
        # Display all expenses (skip header row)
        for row in expenses[1:]:
            if len(row) >= 2:
                item, amount = row[0], row[1]
                print(f"{item:<20} ₹{amount:<10}")
    
    except FileNotFoundError:
        print("No expenses recorded yet!")
    except Exception as e:
        print(f"Error: Could not read expenses. {e}")


def show_total_spent():
    """Calculate and display the total amount spent."""
    print("\n--- Total Spent ---")
    
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        
        # Check if file is empty or only has headers
        if len(expenses) <= 1:
            print("No expenses recorded yet! Total: ₹0")
            return
        
        # Calculate total (skip header row)
        total = 0
        for row in expenses[1:]:
            if len(row) >= 2:
                try:
                    amount = float(row[1])
                    total += amount
                except ValueError:
                    pass  # Skip invalid amounts
        
        print(f"Total amount spent: ₹{total:.2f}")
    
    except FileNotFoundError:
        print("No expenses recorded yet! Total: ₹0")
    except Exception as e:
        print(f"Error: Could not calculate total. {e}")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*40)
    print("     EXPENSE TRACKER")
    print("="*40)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total spent")
    print("4. Exit")
    print("="*40)


def main():
    """Main program loop."""
    # Create CSV file if it doesn't exist
    create_csv_if_not_exists()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total_spent()
        elif choice == "4":
            print("\nThank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


# Run the program
if __name__ == "__main__":
    main()
