# Progressive Electricity Billing System

This is a complete Python ABL assignment for your `task2` folder. It includes the problem statement, objectives, assumptions, algorithm, flowchart, Python source code, sample input/output, and Mermaid flowchart code.

## 1. Problem statement

Develop a Python program to calculate household electricity bills for several months using progressive consumption slabs. The system must calculate energy charges, fixed charges, surcharges, and rebates. It should compare monthly bills and identify unusual increases when the current bill rises by more than 30% compared with the previous month.



## 4. Algorithm

1. Start the program.
2. Read the number of months.
3. For each month, input the electricity consumption in units.
4. Calculate energy charges using the progressive slabs:
   - If units are at most 100, charge ₹2 per unit.
   - If units are between 101 and 200, charge ₹2 for the first 100 units and ₹3 for the remaining units.
   - If units exceed 200, charge ₹2 for the first 100, ₹3 for the next 100, and ₹5 for the remaining units.
5. Add the fixed charge of ₹50.
6. If consumption exceeds 200 units, add a 5% surcharge on energy charges.
7. If consumption is below 100 units, subtract a 5% rebate on energy charges.
8. Calculate and store the final bill for each month.
9. Compare each month's bill with the previous month's bill.
10. If the increase exceeds 30%, mark it as an unusual increase.
11. Display the monthly bill details and comparison results.
12. Stop the program.

## 5. Flowchart
```mermaid

## 5. Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input number of months/]
    B --> C[/Input monthly consumption/]
    C --> D{Units <= 100?}

    D -- Yes --> E[Energy = Units * 2]
    D -- No --> F{Units <= 200?}

    F -- Yes --> G[Calculate first 100 units at Rs. 2 and remaining units at Rs. 3]
    F -- No --> H[Calculate first 200 units and remaining units at Rs. 5]

    E --> I[Add fixed charge]
    G --> I
    H --> I

    I --> J{Units > 200?}
    J -- Yes --> K[Add 5 percent surcharge]
    J -- No --> L{Units < 100?}

    L -- Yes --> M[Apply 5 percent rebate]
    L -- No --> N[Calculate final bill]
    K --> N
    M --> N

    N --> O[Store monthly bill]
    O --> P{More months?}
    P -- Yes --> C
    P -- No --> Q[Compare monthly bills]

    Q --> R{Increase > 30 percent?}
    R -- Yes --> S[Flag unusual increase]
    R -- No --> T[Normal increase]

    S --> U([End])
    T --> U
```

```

## 7. Sample input

Enter these values when you run the program:

```
Enter number of months: 4
Enter units for month 1: 80
Enter units for month 2: 150
Enter units for month 3: 230
Enter units for month 4: 310
```

## 8. Sample output

```
Month 1
Units consumed: 80
Energy charge: Rs. 160.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 0.00
Rebate: Rs. 8.00
Total bill: Rs. 202.00

Month 2
Units consumed: 150
Energy charge: Rs. 350.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Total bill: Rs. 400.00

Month 3
Units consumed: 230
Energy charge: Rs. 650.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 32.50
Rebate: Rs. 0.00
Total bill: Rs. 732.50

Month 4
Units consumed: 310
Energy charge: Rs. 1050.00
Fixed charge: Rs. 50.00
Surcharge: Rs. 52.50
Rebate: Rs. 0.00
Total bill: Rs. 1152.50

--- Monthly Bill Comparison ---
Month 1 to Month 2: 98.02% change
Warning: Unusual bill increase!
Month 2 to Month 3: 83.12% change
Warning: Unusual bill increase!
Month 3 to Month 4: 57.34% change
Warning: Unusual bill increase!

Billing process completed.
```


Important: Run the Python program first, check that the output matches the sample, and take a screenshot of the actual output. The sample output above is illustrative; `output.png` should be your own screenshot.
