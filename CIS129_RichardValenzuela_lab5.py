def main():
    totalBottles = 0
    totalPayout = 0.10  # 10 cents per bottle

    for day in range(1, 8):
        todayBottles = int(input(f"Enter the number of bottles returned for day {day}: "))
        while todayBottles < 0:
            print("ERROR: The number of bottles cannot be negative.")
            todayBottles = int(input(f"Enter the correct number of bottles for day {day}: "))

        totalBottles += todayBottles

    totalPayout = totalBottles * 0.10

    print("\nSummary:")
    print(f"Total bottles collected for the week: {totalBottles}")
    print(f"Total payout for the week: ${totalPayout:.2f}")

    # Ask if the user wants to enter data for another week
    keepGoing = input("Do you want to enter data for another week? (yes/no): ")
    if keepGoing == "yes":
        main()
    else:
        print("Thank you for using the bottle tracking program!")
main()