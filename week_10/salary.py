OVERTIME_RATE = 25


def calculate_overtime(overtime_hours):
    return overtime_hours * OVERTIME_RATE


def calculate_gross_salary(basic_salary, allowance, overtime_pay):
    return basic_salary + allowance + overtime_pay


def calculate_epf(gross_salary):
    return gross_salary * 0.11


def calculate_socso(gross_salary):
    return gross_salary * 0.005


def calculate_net_salary(gross_salary, epf, socso):
    return gross_salary - epf - socso


def check_reward(years_of_service):
    if years_of_service > 3:
        return "Eligible for long-service reward"
    else:
        return "Not eligible for long-service reward"
