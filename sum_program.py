#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a sum calculator


def main():
    # this function how the sum is calculated
    counter = 0
    sum_number = 0
    # input
    number_as_string = input("Enter a positive integer: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        while counter <= number_as_int:
            sum_number = sum_number + counter
            counter = counter + 1
    except Exception:
        print("That is not a integer.")
    finally:
        print("The sum is {0}".format(sum_number))
        print("\nDone.")


if __name__ == "__main__":
    main()
