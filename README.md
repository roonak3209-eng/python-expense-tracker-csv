# Expense Tracker with CSV Storage

A beginner-friendly Python CLI application that helps you track your daily expenses by storing data in a CSV file.

## Description

This is a simple command-line expense tracker that allows you to:
- Add new expenses with item names and amounts
- View all recorded expenses
- Calculate and display the total amount spent
- Store all data persistently in a CSV file

Perfect for learning Python basics like file I/O, CSV handling, and building interactive CLI applications!

## Technology Used

- **Python 3** - Programming language
- **CSV Module** - For reading and writing expense data
- **File I/O** - For data persistence

## How to Run

1. Make sure you have Python 3 installed
2. Open terminal/command prompt in the project folder
3. Run the following command:

```bash
python main.py
```

4. Follow the menu prompts to add, view, or manage your expenses

## Features

✓ **Add Expense** - Add new expenses with item name and amount  
✓ **View Expenses** - Display all recorded expenses in a formatted table  
✓ **Show Total Spent** - Calculate total amount spent across all expenses  
✓ **Data Persistence** - All expenses are saved to `expenses.csv`  
✓ **Error Handling** - Gracefully handles missing files and invalid inputs  
✓ **Beginner-Friendly** - Well-commented code and simple structure  

## What I Learned

Through building this project, I learned:

1. **CSV Module** - How to read from and write to CSV files using Python's `csv` module
2. **File I/O** - Working with file operations like opening, reading, and appending data
3. **Data Persistence** - Storing and retrieving data from files for long-term storage
4. **Error Handling** - Using try-except blocks to handle file-related errors gracefully
5. **CLI Development** - Building simple command-line interface with menus and user input
6. **Data Processing** - Reading CSV data and performing calculations like summing amounts
7. **Code Organization** - Structuring code into functions for better maintainability

## Sample Terminal Output

```
========================================
     EXPENSE TRACKER
========================================
1. Add expense
2. View all expenses
3. Show total spent
4. Exit
========================================
Enter your choice (1-4): 2

--- View All Expenses ---

Item                 Amount    
------------------------------
Coffee               ₹80       
Notebook             ₹120      
Bus Ticket           ₹40       
Lunch                ₹180      
Pen                  ₹20       

========================================
     EXPENSE TRACKER
========================================
1. Add expense
2. View all expenses
3. Show total spent
4. Exit
========================================
Enter your choice (1-4): 3

--- Total Spent ---
Total amount spent: ₹440.00

========================================
     EXPENSE TRACKER
========================================
1. Add expense
2. View all expenses
3. Show total spent
4. Exit
========================================
Enter your choice (1-4): 1

--- Add Expense ---
Enter item name: Pizza
Enter amount: 250
✓ Expense added: Pizza - ₹250

========================================
     EXPENSE TRACKER
========================================
1. Add expense
2. View all expenses
3. Show total spent
4. Exit
========================================
Enter your choice (1-4): 4

Thank you for using Expense Tracker. Goodbye!
```

## Project Structure

```
python-expense-tracker-csv/
├── main.py              # Main program with all functionality
├── expenses.csv         # CSV file storing expense data
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Future Enhancements

Possible improvements for learning:
- Add expense categories (Food, Transport, etc.)
- Filter expenses by date or category
- Delete or edit existing expenses
- Generate monthly reports
- Export data to other formats (JSON, Excel)
