"""Randomly pick customer and print customer info"""

import random
import customer_info


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

pick_winner(customer_info.customers)