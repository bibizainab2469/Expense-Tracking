import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("expense_data_1.csv")
data = df[["Date","Category","Note","Amount","Income/Expense"]]

# Function to add expense
def add_expense(date, category, note, amount, exp_type="Expense"):
    global data
    new_entry = {
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount,
        "Income/Expense": exp_type
    }
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    print(f"Added: {note} - {amount} ({category})")
    # Auto-save CSV
    data.to_csv("expense_data_1.csv", index=False)

# Function to view recent expenses
def view_expenses(n=5):
    return data.tail(n)

# Function to summarize expenses
def summarize_expenses(by="Category"):
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    return summary.sort_values(ascending=False)

# Main execution
if __name__ == "__main__":
    # Example additions
    add_expense("2025-08-22 19:30", "Food", "Shwarma", 2500)
    add_expense("2025-08-23 08:00", "Subscription", "Netflix Monthly Plan", 4500)
    add_expense("2025-08-24 14:00", "Entertainment", "Outdoor Games with friends", 7000)

    print("\nRecent Expenses:\n", view_expenses(5))
    print("\nSummary by Category:\n", summarize_expenses())

    # Pie Chart
    expense_summary = data[data['Category'] != 'Income'].groupby("Category")["Amount"].sum()
    plt.figure(figsize=(6,6))
    expense_summary.plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title("Expenses Breakdown by Category")
    plt.ylabel("")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8,5))
    expense_summary.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.show()
