# Kylee Gordon Final Exam 05/10/2022

# This program allows the user to select the vehicle type and car wash service for each vehicle.
# It then calculates the cost of each car was and displays the total cost of all car washes.

# Initialize Constant Variable
SEDAN_STANDARD_FEE = 16.99
SEDAN_PREMIUM_FEE = 21.99
SEDAN_ULTIMATE_FEE = 27.99

TRUCK_STANDARD_FEE = 19.99
TRUCK_PREMIUM_FEE = 25.99
TRUCK_ULTIMATE_FEE = 33.99


def main():
    total_cost = 0
    # Input
    num_washes = getCarWashes()

    # Processing
    for x in range(1, num_washes + 1):
        vehicle_type = getVehicleType(x)
        selected_service = getCarWashService(x)
        current_car_wash_fee = calculateCarWashFee(vehicle_type, selected_service)
        total_cost += current_car_wash_fee

    # Output
    print("The total of all car washes is: $" + format(total_cost, '.2f'))


def getCarWashes():
    num_washes = 0
    while num_washes > 5 or num_washes < 1:
        try:
            num_washes = int(input("Enter number of car washes (Min: 1 - Max: 5): "))
        except ValueError:
            print("Input must be a numeric integer")

    return num_washes


def getVehicleType(current_car):
    print("Select from one of the following types of vehicles: ")
    print("1. Compact/Sedan")
    print("2. Truck/SUV")
    vehicle_type = 0

    while vehicle_type > 2 or vehicle_type < 1:
        try:
            vehicle_type = int(input("Please choose the vehicle type for car wash #" + str(current_car) + ": "))
        except ValueError:
            print("Input must be a numeric integer")

    return vehicle_type


def getCarWashService(current_car):
    print("Select from one of the following services: ")
    print("1. Standard")
    print("2. Premium")
    print("3. Ultimate")
    selected_service = 0

    while selected_service > 3 or selected_service < 1:
        try:
            selected_service = int(input("Please choose the car wash service for vehicle #" + str(current_car) + ": "))
        except ValueError:
            print("Input must be a numeric integer")

    return selected_service


def calculateCarWashFee(vehicle_type, selected_service):
    global SEDAN_STANDARD_FEE, SEDAN_PREMIUM_FEE, SEDAN_ULTIMATE_FEE, TRUCK_STANDARD_FEE, TRUCK_PREMIUM_FEE, TRUCK_ULTIMATE_FEE
    if vehicle_type == 1:
        if selected_service == 1:
            return SEDAN_STANDARD_FEE
        elif selected_service == 2:
            return SEDAN_PREMIUM_FEE
        elif selected_service == 3:
            return SEDAN_ULTIMATE_FEE
    elif vehicle_type == 2:
        if selected_service == 1:
            return TRUCK_STANDARD_FEE
        elif selected_service == 2:
            return TRUCK_PREMIUM_FEE
        elif selected_service == 3:
            return TRUCK_ULTIMATE_FEE

    return "Invalid Selection"


main()
