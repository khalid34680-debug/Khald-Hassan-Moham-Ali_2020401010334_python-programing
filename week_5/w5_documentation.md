# Week 5 Tutorial 5 Documentation

## 1. Problem Statement
A small cafe needs a simple program to calculate customer bills automatically.

## 2. Inputs
The program needs these inputs:
- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity

## 3. Outputs
The program will print a receipt showing:
- Customer name
- Quantity of each item
- Total bill amount in RM

## 4. Process Flow
1. Ask the user to enter customer name.
2. Ask the user to enter coffee quantity.
3. Ask the user to enter tea quantity.
4. Ask the user to enter sandwich quantity.
5. Calculate the total price.
6. Print the receipt.

## 5. Constraints
- Coffee price is RM 8.50
- Tea price is RM 6.00
- Sandwich price is RM 12.00
- Quantities should be whole numbers.
- Quantities should not be negative.

## 6. Decomposition
The problem can be divided into smaller tasks:
1. Get customer information.
2. Get item quantities.
3. Calculate total bill.
4. Print receipt.

## 7. Pseudocode
START

SET coffee price = 8.50  
SET tea price = 6.00  
SET sandwich price = 12.00  

INPUT customer name  
INPUT coffee quantity  
INPUT tea quantity  
INPUT sandwich quantity  

CALCULATE total = coffee quantity * coffee price + tea quantity * tea price + sandwich quantity * sandwich price  

PRINT receipt  
PRINT customer name  
PRINT coffee quantity  
PRINT tea quantity  
PRINT sandwich quantity  
PRINT total  

END
