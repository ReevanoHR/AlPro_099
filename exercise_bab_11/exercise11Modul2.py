def city_country(
    kota,
    negara,
    populasi=""
):
    if populasi:
        return (
            f"{kota.title()}, "
            f"{negara.title()} - "
            f"population {populasi}"
        )

    return (
        f"{kota.title()}, "
        f"{negara.title()}"
    )