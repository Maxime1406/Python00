def ft_harvest_total() -> None:
    i: int = 1
    total_harvest: int = 0
    while i < 4:
        weight: int = int(input(f"Day {i} harvest: "))
        total_harvest = total_harvest + weight
        i += 1
    print(f"Total harvest: {total_harvest}")
