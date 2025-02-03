import datetime
import os
import random
import re


class HolidayPlanner:
    """
    A class to manage holiday planning, including user details, flight and hotel bookings,
    car rentals, and saving transaction details to a local database.

    Attributes:
        DATABASE_FOLDER (str): The folder name where transaction and log files are stored.
        TRANSACTION_FILE (str): The file path for storing customer transactions.
        LOG_FILE (str): The file path for logging booking activities.
        city_prices (dict): A dictionary mapping cities to their respective flight prices.
        hotel_price_per_night (int): The cost of staying at a hotel per night.
        car_rental_per_day (int): The cost of renting a car per day.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        age (int): The age of the user.
        city_flight (str): The city the user is flying to.
        transaction_number (str): A unique 10-digit booking number.
        transaction_time (str): The local date and time of the transaction.
        num_nights (int): The number of nights the user will stay at the hotel.
        rental_days (int): The number of days the user will rent a car.
    """

    DATABASE_FOLDER = "local_database"
    TRANSACTION_FILE = os.path.join(DATABASE_FOLDER, "customer_transactions.txt")
    LOG_FILE = os.path.join(DATABASE_FOLDER, "log.txt")

    def __init__(self):
        """
        Initializes the HolidayPlanner class with default values and ensures the database folder exists.
        """
        self.city_prices = {
            "New York": 500,
            "Paris": 400,
            "Tokyo": 600,
            "London": 450,
            "Dubai": 550,
        }
        self.hotel_price_per_night = 100
        self.car_rental_per_day = 50
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.age = 0
        self.city_flight = ""

        # Ensure the local database folder exists
        os.makedirs(self.DATABASE_FOLDER, exist_ok=True)

        self.transaction_number = self.generate_unique_transaction_number()
        self.transaction_time = self.get_transaction_time()

    def generate_unique_transaction_number(self):
        """
        Generates a unique 10-digit booking number and ensures no duplicates exist.

        :return: A unique 10-digit transaction number as a string.
        :rtype: str
        """
        existing_numbers = self.get_existing_transaction_numbers()
        while True:
            transaction_number = str(random.randint(1000000000, 9999999999))
            if transaction_number not in existing_numbers:
                return transaction_number

    def get_existing_transaction_numbers(self):
        """
        Retrieves existing booking numbers from the transaction file to prevent duplicates.

        :return: A set of existing transaction numbers.
        :rtype: set
        """
        existing_numbers = set()
        if os.path.exists(self.TRANSACTION_FILE):
            with open(self.TRANSACTION_FILE, "r") as file:
                for line in file:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        existing_numbers.add(parts[1])
        return existing_numbers

    def get_transaction_time(self):
        """
        Gets the local date and time based on the user's current timezone.

        :return: The current local date and time formatted as a string.
        :rtype: str
        """
        local_timezone = datetime.datetime.now().astimezone().tzinfo
        now = datetime.datetime.now(local_timezone)
        return now.strftime("%Y-%m-%d %Hh:%Mm:%Ss %Z")

    def get_valid_input(self, prompt):
        """
        Ensures that user input is not empty.

        :param prompt: The prompt message to display to the user.
        :type prompt: str
        :return: The user's input as a string.
        :rtype: str
        """
        while True:
            user_input = input(prompt).strip()
            if user_input:
                return user_input
            print("Input cannot be empty. Please try again.")

    def get_user_details(self):
        """
        Collects and validates user details including first name, last name, email, and age.
        """
        while True:
            try:
                self.first_name = self.get_valid_input(
                    "Enter your first name: "
                ).title()
                self.last_name = self.get_valid_input("Enter your last name: ").title()

                if not self.first_name.isalpha() or not self.last_name.isalpha():
                    raise ValueError(
                        "Names cannot contain numbers or special characters."
                    )

                print(f"\nYou entered: {self.first_name} {self.last_name}")
                confirm = self.get_valid_input("Is this correct? (yes/no): ").lower()
                if confirm == "yes":
                    break
                elif confirm == "no":
                    print("Please re-enter your name.")
                else:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                self.email = self.get_valid_input("Enter your email address: ").lower()
                if not re.match(r"^[^@]+@[^@]+\.[cC][oO][mM]$", self.email):
                    raise ValueError(
                        "Invalid email format. Must be something@something.com"
                    )
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                self.age = int(self.get_valid_input("Enter your age: "))
                if self.age < 18:
                    print(
                        "You must be supervised by a parent or guardian. Exiting program."
                    )
                    exit()
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for age.")

    def get_user_input(self):
        """
        Collects and validates user input for the city of flight, number of nights at the hotel,
        and number of days for car rental.
        """
        while True:
            try:
                print("\nAvailable cities: New York, Paris, Tokyo, London, Dubai")
                self.city_flight = self.get_valid_input(
                    "Enter the city you will be flying to: "
                ).title()
                if self.city_flight not in self.city_prices:
                    raise ValueError(
                        "Invalid city. Please choose from the available options."
                    )

                self.num_nights = int(
                    self.get_valid_input(
                        "Enter the number of nights you will stay at the hotel: "
                    )
                )
                if self.num_nights < 0:
                    raise ValueError("Number of nights cannot be negative.")

                self.rental_days = int(
                    self.get_valid_input(
                        "Enter the number of days you will hire a car: "
                    )
                )
                if self.rental_days < 0:
                    raise ValueError("Number of rental days cannot be negative.")

                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def display_holiday_details(self):
        """
        Displays holiday details for user confirmation with formatted alignment.

        :return: The formatted holiday details as a string.
        :rtype: str
        """
        flight_cost = f"${self.city_prices[self.city_flight]:,.2f} USD"
        hotel_cost = f"${self.num_nights * self.hotel_price_per_night:,.2f} USD"
        car_rental_cost = f"${self.rental_days * self.car_rental_per_day:,.2f} USD"
        total_cost = f"${self.hotel_price_per_night * self.num_nights + self.car_rental_per_day * self.rental_days + self.city_prices[self.city_flight]:,.2f} USD"

        details = (
            f"\n--- Holiday Details ---\n"
            f"{'Booking Number':<20}: {self.transaction_number}\n"
            f"{'Booked On':<20}: {self.transaction_time}\n"
            f"\n{'Name':<20}: {self.first_name} {self.last_name}\n"
            f"{'Email':<20}: {self.email}\n"
            f"{'Destination':<20}: {self.city_flight}\n"
            f"{'Flight Cost':<20}: {flight_cost}\n"
            f"{'Hotel Cost':<20}: {hotel_cost} ({self.num_nights} nights)\n"
            f"{'Car Rental Cost':<20}: {car_rental_cost} ({self.rental_days} days)\n"
            f"{'Total Holiday Cost':<20}: {total_cost}\n"
            f"\nIf you need a refund or want to make changes, contact:\n"
            f"{'- Email':<20}: support@holidayplanner.com\n"
            f"{'- Phone':<20}: +1 (800) 123-4567\n"
            f"\n**Note:** Refunds cannot be issued after 24 hours.\n"
        )

        print(details)
        confirm = self.get_valid_input(
            "Do you confirm your selection? (yes/no): "
        ).lower()
        if confirm == "yes":
            return details
        else:
            print("Restarting the booking process...")
            self.get_user_input()
            return self.display_holiday_details()

    def save_to_file(self):
        """
        Saves the holiday details to a personalized receipt file and logs the transaction.
        """
        details = self.display_holiday_details()
        receipt_filename = os.path.join(
            self.DATABASE_FOLDER,
            f"{self.first_name.lower()}_{self.last_name.lower()}_receipt.txt",
        )

        with open(receipt_filename, "w") as file:
            file.write(details)

        self.save_transaction()
        self.save_log()
        print(
            "\nThank you for confirming. Your quote is being shared with one of our representatives who will be in touch very soon! We appreciate your patience at this time."
        )

    def save_transaction(self):
        """
        Saves and sorts transactions in the customer_transactions.txt file.
        """
        transactions = []
        if os.path.exists(self.TRANSACTION_FILE):
            with open(self.TRANSACTION_FILE, "r") as file:
                transactions = file.readlines()

        transactions.append(
            f"{self.last_name}, {self.first_name}: {self.transaction_number}\n"
        )

        # Sort transactions alphabetically by last name
        transactions.sort()

        with open(self.TRANSACTION_FILE, "w") as file:
            file.writelines(transactions)

    def save_log(self):
        """
        Logs all completed transactions in the log.txt file.
        """
        with open(self.LOG_FILE, "a") as file:
            file.write(
                f"{self.transaction_time} - {self.first_name} {self.last_name} completed a booking ({self.city_flight} - {self.transaction_number})\n"
            )


if __name__ == "__main__":
    planner = HolidayPlanner()
    print("Welcome to the Holiday Planner!")
    planner.get_user_details()
    planner.get_user_input()
    planner.save_to_file()
