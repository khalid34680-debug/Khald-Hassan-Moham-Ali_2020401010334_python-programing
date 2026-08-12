from lab_monitor import check_computers, count_available, display_status


while True:
    computers = check_computers()

    available = count_available(computers)

    display_status(computers, available)

    choice = input(
        "\nPerform another monitoring cycle? (Y/N): "
    ).upper()

    if choice == "N":
        print("Monitoring stopped.")
        break
