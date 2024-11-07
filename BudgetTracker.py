import time

total_expenses = 0
category_totals = {}
budget = 0

def set_budget(amount):
    global budget
    budget = amount
    print(f"\n Your budget is: ${amount}")
    
    

# function that adds your expenses and tells you if it is within or exceedimg your budget
def expense_adding(amount, item):
    global total_expenses, category_totals, budget
            
    total_expenses += amount
    
    if item in category_totals:
        category_totals[item] +=amount
    else:
        category_totals[item] = amount

    print("category total is " + str(category_totals))    
    
    print("\n" "Added " + item + " which cost " + str(amount)+ " and gave a total of " + str(total_expenses))
    
    if total_expenses > budget:
        print("you have exceeded the budget!")
    else:
        print("\n" "you are within the budget")    
    return total_expenses
    
    
# summary function that shows the categories, total expenses and the budget left after spending.
def show_summary():
    print("\n---Expense summary by category---\n")
        
        # Display each category and its corresponding total
    for category, amount in category_totals.items():
            print(f"\n The category is: {category} | the amount is: ${amount}") 

    print("\n--- Overall Summary ---")    
        # Display Total expenses and the budget left
    print(f"Total Expense: ${total_expenses}")
    print(f"\nRemaining budget: ${budget-total_expenses}\n")  
    print("-----------------------\n")


    # Example expenses
    expense_adding(500, "food" )
    expense_adding(300, "food" )
    expense_adding(800, "juice")
    expense_adding(200, "bags")
    expense_adding(500, "fruits")
    expense_adding(600, "toys")
    
    
def main_menu():
    while True:
        print("\n----MENU----\n")
        print("\nPlease select an option: ")
        print("1. Set your budget")
        print("2. Add your expense")
        print("3. Show Summary")
        print("4. Exit!")
       

        
        selection = input("Enter your choice: ")
        if selection == "1":
            budget = int(input("Enter your budget here: "))
            set_budget(budget)
        elif selection == "2":
            amount = int(input("Enter your amount: "))
            item = input("Enter a category: ")
            expense_adding(amount,item)
        elif selection == "3":
            show_summary()
            input("Press Enter to return to the menu...")
        elif selection == "4":
            print("Goodbye!")
            time.sleep(1)  # Adding a small delay before exiting
            break 
               
        else:
            print("Your selection is incorrect!")    
main_menu()            

                 
