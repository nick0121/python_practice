def get_formatted_city(city, country, population=None):
    if population:
        formatted = f"{city}, {country} and the population is {population}"
    else:
        formatted = f"{city}, {country}"
    return formatted.title()




