
def set_budget(budget):
    total_expenses = 0
    category_totals = {}
    
    
    def expense_adding(amount, item):
        nonlocal total_expenses
        nonlocal category_totals
        
        total_expenses = 50
        total_expenses += amount
        
        if item in category_totals:
            category_totals[item] +=amount
        else:
            category_totals[item] = amount

        print("category total is" + str(category_totals))    
        
        print("\n" "Added " + item + " which cost " + str(amount)+ " and gave a total of " + str(total_expenses))
        
        if total_expenses > budget:
            print("you have exceeded the budget!")
        else:
            print("\n" "you are within the budget")    
        return total_expenses
        

    expense_adding(500, "food" )
    expense_adding(300, "food" )
    expense_adding(800, "juice")


set_budget(1000)  


