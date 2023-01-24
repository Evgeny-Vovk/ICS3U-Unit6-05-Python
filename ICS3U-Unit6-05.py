# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: January 2023
# ICS3U-Unit6-05.py File, learning functions with parameters in python.


def grade_process(grades):
    sum = 0
    for mark in grades:
        sum += mark
    average = sum / len(grades)
    return average


def main():

    grades = []

    try:
        print("Please enter one mark at a time. Enter -1 to end.")

        mark = int(input("What is your mark? (as %): "))
        while mark != -1:
            grades.append(mark)
            mark = int(input("What is your mark? (as %): "))

        average = grade_process(grades)

        print("\nThe average of all grades is {0:,.0f}.".format(average))
        print("")

    except (ValueError):
        print("Invalid input, please try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
