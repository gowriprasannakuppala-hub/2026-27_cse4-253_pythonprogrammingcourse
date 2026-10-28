## Case Study: Multi-Plan Telecommunications Cost Optimization
## 1. Problem Statement
Develop a Python program to compare multiple mobile recharge plans based on a user's data usage, call minutes, validity requirements, and budget. The program should calculate excess usage charges, determine the total cost of each plan, check whether the plan satisfies all user requirements, and identify the most economical eligible plan.

Assumptions for this project:

Each mobile plan has:
- Monthly plan price
- Included data in GB
- Included call minutes
- Validity in days
- Extra data charge per GB
- Extra call charge per minute
A plan is eligible only if its validity meets the user's requirement and its total cost is within the user's budget. Among eligible plans, the program selects the one with the lowest total cost.
## 2. Algorithm
1. Start.
2. Input the user's data usage, call minutes, minimum validity, and budget.
3. Input the number of mobile plans.
4. For each plan, input its price, included data, included call minutes, validity, and excess usage rates.
5. Calculate excess data and excess call minutes.
6. Calculate extra data and call charges.
7. Calculate the total cost of each plan.
8. Check whether the plan meets the validity and budget constraints.
9. Store all eligible plans.
10. Select the eligible plan with the lowest total cost.
11. Display the cost comparison and the most economical eligible plan.
12. If no plan is eligible, display a suitable message.
13. Stop.
## 3. Flowchart
```mermaid


flowchart TD
    A([Start]) --> B[/Input data usage, call minutes, budget and minimum validity/]
    B --> C[/Input number of mobile plans/]
    C --> D[/Input plan price, included data, calls, validity and extra charges/]
    D --> E[Calculate excess data and excess calls]
    E --> F[Calculate extra data and call charges]
    F --> G[Calculate total plan cost]
    G --> H{Cost within budget and validity sufficient?}
    H -- Yes --> I[Store eligible plan]
    H -- No --> J[Mark plan as not eligible]
    I --> K{More plans to evaluate?}
    J --> K
    K -- Yes --> D
    K -- No --> L{Any eligible plans?}
    L -- Yes --> M[Select eligible plan with lowest total cost]
    L -- No --> N[Display no eligible plan found]
    M --> O[/Display plan comparison and best plan/]
    N --> P([Stop])
    O --> P

  ```
## 5. Sample Input
Enter required data usage (GB): 5
Enter required call minutes: 300
Enter minimum validity (days): 28
Enter your budget (Rs.): 500
Enter number of mobile plans: 3

Enter details for Plan 1
Plan name: Plan A
Plan price (Rs.): 299
Included data (GB): 3
Included call minutes: 200
Validity (days): 28
Extra data charge per GB: 50
Extra call charge per minute: 0.5

Enter details for Plan 2
Plan name: Plan B
Plan price (Rs.): 399
Included data (GB): 6
Included call minutes: 500
Validity (days): 56
Extra data charge per GB: 40
Extra call charge per minute: 0.5

Enter details for Plan 3
Plan name: Plan C
Plan price (Rs.): 249
Included data (GB): 2
Included call minutes: 250
Validity (days): 28
Extra data charge per GB: 60
Extra call charge per minute: 0.75


## 6. Sample Output
========== PLAN COST COMPARISON ==========

Plan: Plan A
Base price: Rs. 299.00
Extra data charge: Rs. 100.00
Extra call charge: Rs. 50.00
Total cost: Rs. 449.00
Validity: 28 days
Status: Eligible

Plan: Plan B
Base price: Rs. 399.00
Extra data charge: Rs. 0.00
Extra call charge: Rs. 0.00
Total cost: Rs. 399.00
Validity: 56 days
Status: Eligible

Plan: Plan C
Base price: Rs. 249.00
Extra data charge: Rs. 180.00
Extra call charge: Rs. 37.50
Total cost: Rs. 466.50
Validity: 28 days
Status: Eligible

========== BEST PLAN ==========
Most economical plan: Plan B
Total cost: Rs. 399.00
Validity: 56 days
==========================================


