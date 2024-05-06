import fibonacci

def main():
    print("starting main...")
    number=int(input("enter the length of fibonacci series:"))

    series=fibonacci.get_fibonacci_series(number)

    print(series)


main()    