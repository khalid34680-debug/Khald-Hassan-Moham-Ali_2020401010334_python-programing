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
