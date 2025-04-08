"""This function handles the deposit process for the user."""

# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.

def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    # TODO: Prompt the user to select an account and make a deposit.
    # TODO: If the user chooses to quit, return from the function.
    option = input("Enter 1 for Checking, 2 for Savings, or 'q' to quit: ")
    if option == 'q':
        print("Exiting the deposit process.")
        return

    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if option in ['1', '2']:
            try:
                # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                amount = float(input("Enter the amount to deposit: "))
            # Use the ValueError as an exception.
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.
                print("Invalid amount. Please enter a valid number.")
                # TODO: Call the handle_deposit function recursively for an invalid amount.
                handle_deposit(checking, savings)
                # TODO: Ensure the function returns after the recursive call.
                return
            # TODO: Add an if/else conditional statement to check the account choice,
            if option == '1':
                # TODO: Call the withdraw method on the appropriate account.
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
                checking.deposit(amount)
                print(f"Updated Checking Account Balance: ${checking.get_balance():,.2f}")
            else:
                # TODO: Call the deposit methods on the appropriate account.
                # TODO: Add a print statement to display the updated balance after the deposit
                # TODO: Format the balance to two decimal places and thousands.
                savings.deposit(amount)
                print(f"Updated Savings Account Balance: ${savings.get_balance():,.2f}")
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid choice. Please select either 1 or 2.")
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
