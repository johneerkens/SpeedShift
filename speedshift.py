#!/usr/bin/env python3

from speedshift_core import kmh_to_mph, mph_to_kmh


def main():
    print("=== SpeedShift ===")
    print("1) km/h → mph")
    print("2) mph → km/h")
    print("0) Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        kmh = float(input("Enter speed in km/h: "))
        mph = kmh_to_mph(kmh)
        print(f"{kmh:.2f} km/h = {mph:.2f} mph")

    elif choice == "2":
        mph = float(input("Enter speed in mph: "))
        kmh = mph_to_kmh(mph)
        print(f"{mph:.2f} mph = {kmh:.2f} km/h")

    elif choice == "0":
        print("Goodbye 👋")
        exit()

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
