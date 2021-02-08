
def describe_city(city_name, country_name="japan"):
    print(f"{city_name.title()} is in {country_name.title()}. ")

describe_city('Okinawa') # Gonna use a positional argument here
describe_city(city_name='Tokyo') # Using a keyword argument here
describe_city(city_name="Reno", country_name="United States") # Using keyword arguments to bypass the default.

