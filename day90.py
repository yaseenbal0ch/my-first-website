print("===== *args EXAMPLE =====")

def add(*numbers):
    total = 0
 
    for num in numbers:
                total += num

    print("Total:", total)

    add(10, 20)
    add(5, 10, 15)
    add(1, 2, 3, 4, 5)