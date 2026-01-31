
# Urban City Parking Management System

Overview

Urban City Parking Management System is a Python based, object oriented application designed to manage a parking building with 300 parking spaces.
The system automates vehicle entry and exit tracking, parking fee calculation, space availability, and pricing strategies.

This project demonstrates clean OOP design.

**Problem Statement**

Urban City Parking owns a multi level parking building with a fixed capacity of 300 vehicles.

This system solves the problem by:

- Tracking vehicle entry and exit time.

- Automatically calculating parking fees.

- Managing parking capacity.

- Supporting different pricing strategies.

**Key Features**

- Vehicle entry and exit tracking with timestamps.

- Automated fee calculation.

- Capacity management with maximum 300 slots.

- Space allocation and availability tracking.

- Pricing strategies for weekday and weekend.

- Monthly pass validation support.

- Command line based input system.

**System Design**

The system follows Object Oriented Programming principles.

**Main Components**
1. **Vehicle**

Represents a vehicle entering the parking lot.

Attributes:

- vehicle_type, car, bike, truck

- license_plate

2. **ParkingTicket**

Stores parking session details.

Attributes:

- vehicle

- entry_time

- exit_time

- spot_id

3. **ParkingStrategy, Abstract Class**

Defines a common interface for pricing strategies.

Method:

- calculate_fee(duration_hours, vehicle_type)

4. **WeekdayStrategy**

Implements weekday pricing logic.

- Flat rate of 5 per hour.

5. **WeekendStrategy**

Implements weekend pricing logic.

- Flat rate of 10 per hour.

6. **MonthlyPass**

Handles monthly pass validation.

Method:

- validate(), checks if pass is valid for the current month.

7. **ParkingLot**

Core class that manages the parking system.

Responsibilities:

- Track available parking spaces.

- Assign parking spots.

- Generate parking tickets.

- Calculate parking fees.

- Release spots on exit.

Key methods:

- park_vehicle(vehicle, entry_time)

- exit_vehicle(vehicle, exit_time)

**Capacity Management**

- Total capacity is fixed at 300 parking spots.

- Entry is denied automatically when the lot is full.

- Available spots update in real time.

**Pricing Logic**

Pricing is calculated based on:

- Duration of stay.

- Selected pricing strategy.

Current strategies:

- Weekday pricing.

- Weekend pricing.

The Strategy pattern allows easy future expansion.

**How to Run the Project**

You have two options.

**Option 1. Run in Google Colab**

1. Open the .ipynb file in Google Colab.

2. Run all cells.

3. Follow the input prompts in the output section.

This option requires no local setup.

**Option 2. Run Locally Using Python File**

1. Download the Python source file.

2. Make sure Python 3.8 or later is installed.

3. Open any IDE and run.

4. Enter inputs when prompted:

- Vehicle type.

- License plate.

- Entry time.

- Exit time.

- Pricing strategy.

**Sample Input**

- Vehicle type: car

- License plate: ABC-123

- Entry time: 09:00

- Exit time: 13:00

- Strategy: standard

**Sample Output**

- Duration: 4 Hours

- Fee: $20.00

**Technologies Used**

- Python

- Object Oriented Programming

- Strategy Design Pattern

- datetime module

**Author:** 67732@student.vit.edu.au
