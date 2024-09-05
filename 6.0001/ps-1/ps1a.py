def House_hunting_calculator(
    annual_salary, portion_saved,total_cost):
    portion_down_payment = .25* total_cost
    current_savings=0
    monthly_salary=annual_salary/12
    intrest_rate=.04
    month_count = 0 
    while (portion_down_payment - current_savings) > 0 :
        month_count += 1
        current_savings += (monthly_salary*portion_saved) + (current_savings*intrest_rate/12)
    return month_count


if __name__ == "__main__":
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    try:
        print("Number of months:", House_hunting_calculator(annual_salary, portion_saved, total_cost))
    except Exception as e:
        print("Error has occured:", e )

