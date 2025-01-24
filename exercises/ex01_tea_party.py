"""Planning a tea party that uses number of guests to calculate how many tea bags needed, number of treats, and expected cost."""

__author__: str = "730549091"


def main_planner(guests: int) -> None:
    """Brings together all defined funtions into a printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """takes the number of guests and figures out how many tea bags are needed."""
    return 2 * people


def treats(people: int) -> int:
    """takes the number of guests and figures out how many treats are needed."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """figures out the cost of the tea party based on the number of tea bags and number of treats."""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
