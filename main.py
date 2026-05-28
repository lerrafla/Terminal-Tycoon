import random
import json
import os

SAVE_FILE = "savegame.json"


class Company:

    def __init__(self):

        self.month = 1
        self.cash = 5000
        self.employees = 3
        self.reputation = 50
        self.product = 40
        self.burnout = 10
        self.users = 0
        self.investors = 0

    def show_stats(self):

        print("\n==============================")
        print("      TERMINAL TYCOON")
        print("==============================")

        print(f"Month: {self.month}")
        print(f"Cash: ${self.cash}")
        print(f"Employees: {self.employees}")
        print(f"Reputation: {self.reputation}")
        print(f"Product Quality: {self.product}")
        print(f"Burnout: {self.burnout}")
        print(f"Users: {self.users}")
        print(f"Investors: {self.investors}")

        print("==============================\n")

    def hire_employee(self):

        cost = 1000

        if self.cash >= cost:

            self.cash -= cost
            self.employees += 1
            self.product += 3
            self.burnout -= 2

            print("\nHired a new employee.")

        else:
            print("\nNot enough cash.")

    def build_product(self):

        improvement = random.randint(4, 10)

        self.product += improvement
        self.burnout += random.randint(5, 10)

        print(f"\nYour team improved the product by {improvement} points.")

    def marketing(self):

        cost = 1500

        if self.cash >= cost:

            gained_users = random.randint(200, 1000)

            self.cash -= cost
            self.users += gained_users
            self.reputation += 5

            print(f"\nMarketing succeeded. +{gained_users} users.")

        else:
            print("\nNot enough cash.")

    def raise_funding(self):

        success = random.randint(1, 100)

        if success > 40:

            amount = random.randint(5000, 20000)

            self.cash += amount
            self.investors += 1
            self.burnout += 5

            print(f"\nInvestors gave you ${amount}!")

        else:

            self.reputation -= 5

            print("\nInvestors rejected your pitch.")

    def rest(self):

        self.burnout -= 10

        if self.burnout < 0:
            self.burnout = 0

        print("\nYour team rested.")

    def monthly_expenses(self):

        expense = self.employees * 400

        self.cash -= expense

        print(f"\nMonthly expenses: ${expense}")

    def random_event(self):

        events = [

            {
                "text": "A TikTok influencer promoted your app.",
                "users": 500,
                "cash": 0,
                "rep": 5
            },

            {
                "text": "Server crash during launch.",
                "users": -200,
                "cash": -1000,
                "rep": -10
            },

            {
                "text": "Your lead developer quit.",
                "users": 0,
                "cash": -500,
                "rep": -5
            },

            {
                "text": "Your app went viral overnight.",
                "users": 2000,
                "cash": 3000,
                "rep": 10
            },

            {
                "text": "Twitter roasted your startup.",
                "users": -100,
                "cash": 0,
                "rep": -8
            }
        ]

        event = random.choice(events)

        print("\nEVENT:")
        print(event["text"])

        self.users += event["users"]
        self.cash += event["cash"]
        self.reputation += event["rep"]

        if self.users < 0:
            self.users = 0

    def next_month(self):

        self.month += 1

        self.monthly_expenses()

        if random.randint(1, 100) < 60:
            self.random_event()

        if self.burnout >= 100:

            print("\nYour team burned out.")
            return False

        if self.cash <= -5000:

            print("\nYour startup went bankrupt.")
            return False

        return True

    def save_game(self):

        data = self.__dict__

        with open(SAVE_FILE, "w") as file:
            json.dump(data, file)

        print("\nGame saved.")

    def load_game(self):

        if not os.path.exists(SAVE_FILE):

            print("\nNo save file found.")
            return

        with open(SAVE_FILE, "r") as file:

            data = json.load(file)

        self.__dict__.update(data)

        print("\nGame loaded.")


def menu():

    print("\n==============================")
    print("         ACTIONS")
    print("==============================")

    print("1. Hire employee")
    print("2. Build product")
    print("3. Launch marketing")
    print("4. Raise funding")
    print("5. Rest")
    print("6. Save game")
    print("7. Load game")
    print("8. View stats")
    print("9. End month")
    print("0. Quit")


company = Company()

print("WELCOME TO TERMINAL TYCOON")
print("Build the next billion-dollar startup.")

running = True

while running:

    menu()

    choice = input("\nEnter choice: ")

    if choice == "1":

        company.hire_employee()

    elif choice == "2":

        company.build_product()

    elif choice == "3":

        company.marketing()

    elif choice == "4":

        company.raise_funding()

    elif choice == "5":

        company.rest()

    elif choice == "6":

        company.save_game()

    elif choice == "7":

        company.load_game()

    elif choice == "8":

        company.show_stats()

    elif choice == "9":

        alive = company.next_month()

        if not alive:

            print("\nGAME OVER")
            company.show_stats()

            break

    elif choice == "0":

        running = False

    else:

        print("\nInvalid choice.")
