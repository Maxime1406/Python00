def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    helper(days, 1)


def helper(days: int, i: int) -> None:
    if i < days + 1:
        print(f"Day {i}")
        i += 1
        helper(days, i)
    else:
        print("Harvest time!")
