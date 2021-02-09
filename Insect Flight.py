import InsectClass as i


def main():
    # Create an instance of the class
    flight = i.Insect()

    # Run the random length
    flight.flightlength()

    # Display the output
    print("The length of flight is:", flight.display(), "miles.")


# Call the main function
main()