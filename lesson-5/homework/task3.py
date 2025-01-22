#A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.

def main():
    
    try:
        n = int(input("Write a positive integer: "))
        if n <= 0:
            print("I said, write a positive integer.")
            return

        for i in range(1, n + 1):
            if n % i == 0:  
                print(f"{i} is a factor of {n}")

    except ValueError:
        print("You are dump.")


if __name__ == "__main__":
    main()