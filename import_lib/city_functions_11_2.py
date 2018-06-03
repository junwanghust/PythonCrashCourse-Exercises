
def get_city_country(city, country, population=""):
    if population:
        res = city + ',' + country + ' - population ' + population
    else:
        res = city + ',' + country
    return res.title()
