# Gets a collection of birthdays from the user and checks if
# each person is at least 21 years of age
from datetime import date


def main():
    today = date.today()
    print(today.year)

    user_prompt = get_date()
    print(user_prompt)
    try:
        while date is not None:
            if int(today.year) - int(user_prompt.year) < 21:
                print("Person is less than 21 years of age")
            elif int(today.year) - int(user_prompt.year) > 21:
                print("Person is older than 21 years of age")
            elif int(today.year) - int(user_prompt.year) == 21 and \
                    int(today.month) - int(user_prompt.month) == 0 and \
                    int(today.day) - int(user_prompt.day) == 0:
                print("Person turned 21 years old today")
            else:
                print("Person is less than 21 years of age")

            user_prompt = get_date()
    except:
        print("Invalid date")


def get_date():
    """

    :rtype: date
    """
    print("Enter a birth date: ")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return date(year, month, day)


if __name__ == '__main__':
    main()
