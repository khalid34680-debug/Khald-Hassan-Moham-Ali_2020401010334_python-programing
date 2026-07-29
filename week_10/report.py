def print_report(
    name,
    employee_id,
    basic_salary,
    allowance,
    overtime_hours,
    overtime_pay,
    years_of_service,
    reward_status,
    gross_salary,
    epf,
    socso,
    net_salary
):
    print("\n---------- SALARY REPORT ------------")

    print(f"Employee Name     : {name}")
    print(f"Employee ID       : {employee_id}")
    print(f"Basic Salary      : RM {basic_salary:.2f}")
    print(f"Allowance         : RM {allowance:.2f}")
    print(f"Overtime Hours    : {overtime_hours:.2f}")
    print(f"Overtime Payment  : RM {overtime_pay:.2f}")
    print(f"Years of Service  : {years_of_service}")
    print(f"Reward Status     : {reward_status}")

    print("-----------------------------------")
    print(f"Gross Salary      : RM {gross_salary:.2f}")
    print(f"EPF (11%)         : RM {epf:.2f}")
    print(f"SOCSO (0.5%)      : RM {socso:.2f}")
    print("-----------------------------------")
    print(f"Net Salary        : RM {net_salary:.2f}")
    print("------------------------------------------")
