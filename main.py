def convert_length():
    value = float(input("Enter value in meters: "))
    print("\n--- Length Conversion ---")
    print(f"Kilometers: {value / 1000}")
    print(f"Miles: {value * 0.000621371}")
    print(f"Feet: {value * 3.28084}")

def convert_weight():
    Value = float(input("Enter value in grams: "))
    print("\n--- Weight Conversion ---")
    print(f"Kilograms: {Value / 1000}")
    print(f"Pounds: {Value * 0.00220462}")

def convert_temperature():
    value =  float(input("Enter value in Celsius: "))
    print("\n--- Temperature Conversion ---")
    print(f"Fahrenheit: {(value * 9/5) + 32}")
    print(f"Kelvin: {value + 273.15}")

def main():
    while True:
        print("\n=== Python Unit Converter ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()