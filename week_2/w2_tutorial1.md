# Week 2 Tutorial 2

## Scenario

A person can enter the movie theater if:

- Age is 13 or above
- OR the person is with an adult
- AND the person has a valid ticket

## 1. Components

### Inputs

- Age
- With adult
- Valid ticket

### Process

Check the age, adult companion, and ticket.

### Output

- Allowed to enter
- Not allowed to enter

Age>=13  Adult  Ticket  Result

F         F       F       F
F         F       T       F
F         T       F       F
F         T       T       T
T         F       F       F
T         F       T       T
T         T       F       F
T         T       T       T

## 2.3 Algorithm

Start

Input age
Input adult
Input ticket

If (age >= 13 OR adult = True) AND ticket = True
    Display "Allowed to enter"
Else
    Display "Not allowed to enter"

End

## 2.4 Pseudocode

BEGIN

INPUT age
INPUT adult
INPUT ticket

IF ((age >= 13 OR adult = TRUE) AND ticket = TRUE) THEN
    PRINT "Allowed to enter"
ELSE
    PRINT "Not allowed to enter"
END IF

END

## 3.1 Test Cases

Test Case 1

Age = 15
Adult = False
Ticket = True

Result:
Allowed to enter


Test Case 2

Age = 10
Adult = False
Ticket = True

Result:
Not allowed to enter


Test Case 3

Age = 10
Adult = True
Ticket = True

Result:
Allowed to enter

## Logic Diagram
<img width="441" height="638" alt="logic_drawio" src="https://github.com/user-attachments/assets/749cd2a5-fe31-4317-be62-d7344ffb7699" />
