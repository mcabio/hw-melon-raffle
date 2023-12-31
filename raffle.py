"""Read customer data from file and run a raffle."""

import random
# from random import choice was original line of code



class Customer:
    """A customer at Ubermelon."""

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode


def get_customers_from_file(customer_file_path):
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object
    containing customer information.
    """

    customers = []

    customer_file = open(customer_file_path)

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

    for line in customer_file:
        customer_data = line.strip().split("|")
        name, email, street, city, zipcode = customer_data

        new_customer = Customer(name, email, street, city, zipcode)
        customers.append(new_customer)

    return customers


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


# The code below is a common Python idiom. It checks whether the 
# Python script is being run as the main program or if it is being imported 
# as a module into another script. The special variable __name__ is a built-in variable in 
# Python, and when the script is executed, __name__ is set to "__main__" if the script is 
# the main program being run. If the script is imported as a module, __name__ is set to 
# the name of the module. Therefore, this condition ensures that the code block underneath 
# it will only be executed if the script is the main program.
if __name__ == "__main__":
    run_raffle() # If the condition if __name__ == "__main__": is true 
                 # (meaning the script is the main program), the function run_raffle() is called. 
                 # This is where the main logic or functionality of the script is expected to be defined. 
                 # The run_raffle() function will contain the code that should be executed when 
                 # the script is run.

