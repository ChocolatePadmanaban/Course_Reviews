def SavingsAmountCalculator(salary, portion_saved):
    monthly_salary = salary/12
    semi_annual_raise = .07
    intrest_rate = .04
    current_savings, month_count = 0,0
    while month_count <= 36:
        month_count += 1
        if month_count %6== 0:
            monthly_salary +=  monthly_salary*semi_annual_raise
        current_savings += (monthly_salary*portion_saved) + (current_savings*intrest_rate/12)
    return current_savings


def SavingsPercentCalculator(salary, low=0, high=10000, steps=0):
    def CheckHelper(salary, intrest_rate):
        return 249900 < SavingsAmountCalculator(salary,intrest_rate/10000) < 250100
    steps += 1
    if high == low:
        if CheckHelper(salary, high):
            return high/10000 , steps
        else:
            return None,steps
    mid = (high+low)//2 
    if CheckHelper(salary, mid):
        return mid/10000 , steps
    elif SavingsAmountCalculator(salary, mid/10000) > 250000 :
        if low==mid:
            return None, steps
        else:
            return SavingsPercentCalculator(salary, low, mid-1, steps)
    else:
        return SavingsPercentCalculator(salary, mid+1 , high, steps)
    
    
if __name__ =="__main__":
    salary = float(input("Enter the starting salary: "))
    savings_percent , steps = SavingsPercentCalculator(salary)
    if savings_percent == None:
        print("It is not possible to pay the down payment in three years")
    else:
        print("Best savings rate:", savings_percent)
        print("Steps in bisection search:", steps)