def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("Temperature Converter")
    c = float(input("Enter Celsius: "))
    print(f"Fahrenheit: {c_to_f(c)}")
