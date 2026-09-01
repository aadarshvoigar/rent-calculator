import time
print("=============================")
print("       Rent Calculator       ")
print(f"=============================\n")
while True:
    try:
        total_rent = int(input("Enter your hostel/flat rent: "))
        time.sleep(0.5)
        food = int(input("Enter the amount of food ordered:  "))
        time.sleep(0.5)
        electricity_spend = int(input("Enter the total of electricity spend: "))
        time.sleep(0.5)
        charge_per_unit = int(input("Enter charge per unit: "))
        time.sleep(0.5)
        total_person = int(input("Enter the number of persons living in room for rent: "))
        time.sleep(0.5)
    except ValueError:
        print("\nPlease enter a valid number")
        time.sleep(1.5)
        print("Restarting...\n")
        time.sleep(2)
    except Exception as e:
        print(f"An unknown problem occurs {e}")
        time.sleep(2)
        print("Restarting...")
        time.sleep(2)
    else:
        electricity_bill = electricity_spend * charge_per_unit
        per_person_rent = (total_rent + food + electricity_bill) // total_person
        print(f"\nRent for per person = {per_person_rent}")
        time.sleep(1.5)
        print("\nThanks! for using our platform.")
        time.sleep(1)
        break
