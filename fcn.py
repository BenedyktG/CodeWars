def tickets(people):
    bills = {
        25: 0,
        50: 0,
        100: 0
    }

    for bill in people:
        if bill == 25:
            bills[25] += 1
        elif bill == 50:
            bills[50] += 1
            bills[25] -= 1
        elif bill == 100:
            bills[100] += 1
            if bills[50] > 0:
                bills[50] -= 1
                bills[25] -= 1
            else:
                bils[25] -= 3

        print(bills)
    for value in bills.values():
        if value >= 0:
            print("YES")
        else:
            print("NO")


tickets([25, 50, 25, 100, 25, 25, 50, 100, 25, 50, 25, 100, 50, 25])
