
def set_budget(budget):
    total_expenses = 0
    category_totals = {}
    

    # function that adds your expenses and tells you if it is within or exceedimg your budget
    def expense_adding(amount, item):
        nonlocal total_expenses
        nonlocal category_totals
        
        
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

        # Display Total expenses and the budget left
        print(f"\nTotal Expense: ${total_expenses}")
        print(f"\nRemaining budget: ${budget-total_expenses}\n")  
        print("-----------------------\n")


    # Example expenses
    expense_adding(500, "food" )
    expense_adding(300, "food" )
    expense_adding(800, "juice")
    expense_adding(200, "bags")
    expense_adding(500, "fruits")
    expense_adding(600, "toys")
    
    show_summary()

    
set_budget(15000)  


