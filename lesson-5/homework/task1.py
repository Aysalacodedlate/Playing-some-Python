#Write a script called temperature.py that defines two functions:
#oh, there exists similar problem on lesson 2, it was quite easier than this one. 

def convert_far_to_cel(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5 / 9


def convert_cel_to_far(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: F = C * 9/5 + 32
    """
    return celsius * 9 / 5 + 32

def main():
    fahrenheit = float(input("Write a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius:.2f} degrees C\n")

    celsius = float(input("Write a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit:.2f} degrees F")


if __name__ == "__main__":
    main()
