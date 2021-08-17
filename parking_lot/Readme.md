# Go-Jek Parking Lot Assignment (Python)

## 1. Problem Statment
Design a Parking lot which can hold `n` Cars. Every car been issued a ticket for a slot and the slot been assigned based on the nearest to the entry. The system should also return some queries such as:

- Registration numbers of all cars of a particular colour.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where a car of a particular colour is parked.



## 2. Supported Commands

- `create_parking_lot` <`n`>   
To create a Parking lot. Where `n` is the size of the parking lot

- `park` <`registration_number`> <`colour`>   
To park the car in the parking lot and prints the allocated slot in the parking lot. Where `registration_number` is given registration number for the car and `colour` is given colour for the car

- `leave` <`slot`>   
To leave the parking lot from desired slot and prints the leaving slot. given slot number. Where `slot` is given sloat number

- `status`   
To check the status of Parking Lot

- `slot_numbers_for_cars_with_colour` <`colour`>   
To prints the registration number of the cars for the given colour. Where `color` is given colour

- `slot_number_for_registration_number` <`registration_number`>   
prints the slot number of the cars for the given number. Where `registration_number` is given registration number.

- `registration_numbers_for_cars_with_colour` <`colour`>   
To prints the slot number of the cars for the given colour.  Where `colour` is given colour.

## 3. Running Application
#### 3.1 Running the application in File mode:

```
sh ./bin/parking_lot functional_spec/fixtures/file_input.txt```

#### 3.2 Running the application in Interactive mode:

```sh ./bin/parking_lot
```

## 4. Test Cases
- Total number of test cases - 8

#### 4.1 For running the tests

```
sh ./bin/setup
```





