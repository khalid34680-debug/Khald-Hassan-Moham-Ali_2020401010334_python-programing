from employee import get_employee
from salary import (
    calculate_overtime,
    calculate_gross_salary,
    calculate_epf,
    calculate_socso,
    calculate_net_salary,
    check_reward
)
from report import print_report


def main():
    (
        name,
        employee_id,
        basic_salary,
        allowance,
        overtime_hours,
        years_of_service
    ) = get_employee()

    overtime_pay = calculate_overtime(overtime_hours)

    gross_salary = calculate_gross_salary(
        basic_salary,
        allowance,
        overtime_pay
    )

    epf = calculate_epf(gross_salary)
    socso = calculate_socso(gross_salary)
    net_salary = calculate_net_salary(gross_salary, epf, socso)

    reward_status = check_reward(years_of_service)

    print_report(
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
    )


if __name__ == "__main__":
    main()
