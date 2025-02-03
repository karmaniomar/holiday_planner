# Holiday Planner

The **Holiday Planner** is a Python-based application designed to help users plan their holidays by managing flight bookings, hotel stays, and car rentals. It collects user details, calculates costs, and saves transaction details to a local database. The application ensures data integrity by validating user inputs and generating unique transaction numbers for each booking.

---

## Features

- **User Details Collection**: Collects and validates user details such as name, email, and age.
- **Flight Booking**: Allows users to select a destination city from a predefined list and calculates the flight cost.
- **Hotel Booking**: Calculates the total cost of the hotel stay based on the number of nights.
- **Car Rental**: Calculates the total cost of renting a car based on the number of days.
- **Transaction Management**: Generates a unique 10-digit booking number and saves transaction details to a local database.
- **Receipt Generation**: Creates a personalized receipt for each booking.
- **Logging**: Logs all completed transactions for record-keeping.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/karmaniomar/holiday_planner.git
   cd holiday-planner
   ```

2. **Run the Application**:
   Ensure you have Python installed on your system. Then, run the following command:
   ```bash
   python holiday_planner.py
   ```

---

## Usage

1. **Start the Application**:
   Run the script, and you will be greeted with a welcome message.

2. **Enter User Details**:
   - Provide your first name, last name, email, and age.
   - The application will validate your inputs and ensure they meet the required criteria.

3. **Select Holiday Details**:
   - Choose a destination city from the available options.
   - Enter the number of nights you will stay at the hotel.
   - Enter the number of days you will rent a car.

4. **Review and Confirm**:
   - The application will display a summary of your holiday details, including costs.
   - Confirm your selection to proceed.

5. **Save and Exit**:
   - The application will save your transaction details to a local database and generate a personalized receipt.
   - A log entry will be created to record the completed transaction.

---

## File Structure

- **`holiday_planner.py`**: The main script containing the `HolidayPlanner` class and its methods.
- **`local_database/`**: A folder created by the application to store transaction and log files.
  - **`customer_transactions.txt`**: Stores all customer transactions, sorted alphabetically by last name.
  - **`log.txt`**: Logs all completed transactions with timestamps.
  - **`<firstname>_<lastname>_receipt.txt`**: Personalized receipt files for each booking.

---

## Code Overview

### Key Attributes

- **`DATABASE_FOLDER`**: The folder where transaction and log files are stored.
- **`TRANSACTION_FILE`**: The file path for storing customer transactions.
- **`LOG_FILE`**: The file path for logging booking activities.
- **`city_prices`**: A dictionary mapping cities to their respective flight prices.
- **`hotel_price_per_night`**: The cost of staying at a hotel per night.
- **`car_rental_per_day`**: The cost of renting a car per day.
- **`first_name`**, **`last_name`**, **`email`**, **`age`**: User details.
- **`city_flight`**: The city the user is flying to.
- **`transaction_number`**: A unique 10-digit booking number.
- **`transaction_time`**: The local date and time of the transaction.
- **`num_nights`**: The number of nights the user will stay at the hotel.
- **`rental_days`**: The number of days the user will rent a car.

### Key Methods

- **`generate_unique_transaction_number()`**: Generates a unique 10-digit booking number.
- **`get_existing_transaction_numbers()`**: Retrieves existing booking numbers to prevent duplicates.
- **`get_transaction_time()`**: Gets the local date and time of the transaction.
- **`get_valid_input(prompt)`**: Ensures user input is not empty.
- **`get_user_details()`**: Collects and validates user details.
- **`get_user_input()`**: Collects and validates user input for holiday details.
- **`display_holiday_details()`**: Displays holiday details for user confirmation.
- **`save_to_file()`**: Saves holiday details to a personalized receipt file and logs the transaction.
- **`save_transaction()`**: Saves and sorts transactions in the customer_transactions.txt file.
- **`save_log()`**: Logs all completed transactions in the log.txt file.

---

## Example Output

### Holiday Details
```
--- Holiday Details ---
Booking Number      : 1234567890
Booked On           : 2023-10-05 14h:30m:45s UTC

Name                : John Doe
Email               : john.doe@example.com
Destination         : New York
Flight Cost         : $500.00 USD
Hotel Cost          : $300.00 USD (3 nights)
Car Rental Cost     : $150.00 USD (3 days)
Total Holiday Cost  : $950.00 USD

If you need a refund or want to make changes, contact:
- Email             : support@holidayplanner.com
- Phone             : +1 (800) 123-4567

**Note:** Refunds cannot be issued after 24 hours.
```

### Receipt File (`john_doe_receipt.txt`)
The above details will be saved in a personalized receipt file within the `local_database` folder.

---

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any inquiries, please contact:
- **Email**: omar.karmani93@gmail.com

---

Thank you for using the **Holiday Planner**! We hope it makes your holiday planning experience seamless and enjoyable. 🌴✈️