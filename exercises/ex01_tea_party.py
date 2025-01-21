"""Will show the quantity of tea bags, treats, and overall cost to plan the tea party."""

__author__: str = "730748060"


def main_planner(guests: int) -> None:
    """Brings all the functions together and calls each and produces printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People! ")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on number of guests."""
    return 2 * people


def treats(people: int) -> int:
    """A function to compute the number of treats needed based on the number of teas guests are expecting to drink."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
