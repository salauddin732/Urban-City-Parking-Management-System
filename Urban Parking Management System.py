from abc import ABC, abstractmethod
from datetime import datetime

# ---------------- Vehicle ----------------
class Vehicle:
    def __init__(self, vehicle_type, license_plate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate


# ---------------- Parking Ticket ----------------
class ParkingTicket:
    def __init__(self, vehicle, entry_time, spot_id):
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.exit_time = None
        self.spot_id = spot_id


# ---------------- Pricing Strategy ----------------
class ParkingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, duration_hours, vehicle_type):
        pass


class WeekdayStrategy(ParkingStrategy):
    def calculate_fee(self, duration_hours, vehicle_type):
        rate = 5
        return duration_hours * rate


class WeekendStrategy(ParkingStrategy):
    def calculate_fee(self, duration_hours, vehicle_type):
        rate = 10
        return duration_hours * rate


# ---------------- Monthly Pass ----------------
class MonthlyPass:
    def __init__(self, pass_id, vehicle_license, valid_month):
        self.pass_id = pass_id
        self.vehicle_license = vehicle_license
        self.valid_month = valid_month

    def validate(self):
        current_month = datetime.now().month
        return self.valid_month == current_month


# ---------------- Parking Lot ----------------
class ParkingLot:
    def __init__(self, total_spots, pricing_strategy):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.pricing_strategy = pricing_strategy
        self.active_tickets = {}

    def park_vehicle(self, vehicle, entry_time):
        if self.available_spots <= 0:
            return "Error: Parking Lot is Full. Entry denied."

        spot_id = self.total_spots - self.available_spots + 1
        ticket = ParkingTicket(vehicle, entry_time, spot_id)
        self.active_tickets[vehicle.license_plate] = ticket
        self.available_spots -= 1

        return f"Vehicle {vehicle.license_plate} parked at spot {spot_id}"

    def exit_vehicle(self, vehicle, exit_time):
        ticket = self.active_tickets.get(vehicle.license_plate)

        if not ticket:
            return "Error: Vehicle not found."

        ticket.exit_time = exit_time
        duration = (ticket.exit_time - ticket.entry_time).seconds / 3600
        duration = int(duration)

        fee = self.pricing_strategy.calculate_fee(duration, vehicle.vehicle_type)

        del self.active_tickets[vehicle.license_plate]
        self.available_spots += 1

        return {
            "Duration": f"{duration} Hours",
            "Fee": f"${fee:.2f}"
        }

# ---------------- Main Input Program ----------------
if __name__ == "__main__":

    # Vehicle input
    vehicle_type = input("Vehicle type (car/bike/truck): ").lower()
    license_plate = input("License plate: ")

    if vehicle_type not in ["car", "bike", "truck"]:
        print("Invalid vehicle type!")
        exit()

    vehicle = Vehicle(vehicle_type, license_plate)

    # Time input
    entry_time_str = input("Entry time (HH:MM): ")
    exit_time_str = input("Exit time (HH:MM): ")

    entry_time = datetime.strptime(entry_time_str, "%H:%M")
    exit_time = datetime.strptime(exit_time_str, "%H:%M")

    # Strategy input
    strategy_input = input("Strategy (standard/weekend): ").lower()

    if strategy_input == "standard":
        strategy = WeekdayStrategy()
    elif strategy_input == "weekend":
        strategy = WeekendStrategy()
    else:
        print("Invalid strategy!")
        exit()

    # Create parking lot
    parking_lot = ParkingLot(300, strategy)

    # Park vehicle
    result = parking_lot.park_vehicle(vehicle, entry_time)
    print(result)

    # Exit vehicle
    output = parking_lot.exit_vehicle(vehicle, exit_time)

    print("\n"f"Duration : {output['Duration']}")
    print(f"Fee      : {output['Fee']}")