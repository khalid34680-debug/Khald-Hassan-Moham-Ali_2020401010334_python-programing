def calculate_total(coffee, tea, sandwich):
    total = coffee * 8.50 + tea * 6.00 + sandwich * 12.00
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    print("===== RECEIPT =====")
    print("Customer :", customer_name)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)
    print("-------------------")
    print(f"Total = RM {total:.2f}")
