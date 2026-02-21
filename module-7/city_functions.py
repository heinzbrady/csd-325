def city_country(city, country, population=None, language=None):
    base = f"{city.title()}, {country.title()}"

    if population is not None and language is not None:
        return f"{base} - population {population}, {language.title()}"
    if population is not None:
        return f"{base} - population {population}"
    if language is not None:
        return f"{base}, {language.title()}"

    return base


print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 13960000))
print(city_country("santiago", "chile", 5000000, "spanish"))