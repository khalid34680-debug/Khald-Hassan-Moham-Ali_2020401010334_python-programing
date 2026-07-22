def create_ticket():
    print("--- IT Helpdesk Ticket ---")

    student_name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")

    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()

        if priority in ["High", "Medium", "Low"]:
            break
        else:
            print("Please enter High, Medium, or Low.")

    return student_name, student_id, issue, location, priority
