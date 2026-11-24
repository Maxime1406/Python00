def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets" or unit == "grams" or unit == "area":
        if unit == "packets":
            unit = "packets available"
        elif unit == "grams":
            unit = "grams total"
        elif unit == "area":
            unit = "square meters"
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit}")
    else:
        print("Unknown unit type")
