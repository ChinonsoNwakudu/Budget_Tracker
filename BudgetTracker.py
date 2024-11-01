
def set_budget(budget):
    total_expenses = 0
    
    
    def expense_adding(amount, item):
        nonlocal total_expenses
        
        total_expenses = 50
        total_expenses += amount
        
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


