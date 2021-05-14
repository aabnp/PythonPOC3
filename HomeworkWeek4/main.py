import random


def population():
    countries = ['Belgium', 'Roumania', 'France', 'Hungary', 'Netherlands', 'Germany']
    years = [2016, 2017, 2018, 2019, 2020]
    sexes = ['F', 'M']
    min_health_index = 1
    max_health_index = 10
    nr_of_cases = 100

    data = []

    for i in range(nr_of_cases):
        persons = (
            random.choice(countries),
            random.choice(years),
            random.choice(sexes),
            random.randint(min_health_index, max_health_index)
        )
        data.append(persons)
    return data


def get_countries_by_year(row_data, year_param):
    countries_by_year = {
        country: [sex, health_index]
        for (country, year, sex, health_index) in row_data
        if year == year_param
    }
    print(f'For {year_param} data per country is as follow: {countries_by_year}\n\n')


def get_data_by_year_for_germany(row_data):
    data_by_year_for_germany = {
        year: [sex, health_index]
        for (country, year, sex, health_index) in row_data
        if country == 'Germany'
    }
    print(f'Data for Germany is as follow: {data_by_year_for_germany}\n\n')


def get_data_by_country_and_year(raw_data):
    data_by_country_and_year = {
        country + '_' + str(year): [year, sex, health_index]
        for (country, year, sex, health_index) in raw_data
    }
    # print(data_by_country_and_year)
    return data_by_country_and_year


def get_data_with_health_index_bigger_that_5(raw_data):
    data_by_country_and_year_health_index_bigger_than_5 = {
        key: value for (key, value) in raw_data.items() if value[2] > 5
    }
    print(f'Data with health_index > 5 is as follow: {data_by_country_and_year_health_index_bigger_than_5}\n\n')


def get_data_with_health_index_bigger_that_5_and_sex_f(raw_data):
    data_with_health_index_bigger_that_5_and_sex_f = {
        key: value for (key, value) in raw_data.items() if value[1] == 'F' and value[2] > 5
    }
    print(f'Data with health_index > 5 and sex = 'F' is as follow: {data_with_health_index_bigger_that_5_and_sex_f}\n\n')


def sets():
    set1 = {2, 5, 11, 18, 23, 34, 37, 41, 47, 50}
    set2 = {1, 7, 14, 18, 24, 25, 37, 42, 43, 50}
    print(f'Intersection: {set1.intersection(set2)}\n')
    print(f'Union: {set1.union(set2)}\n')
    print(f'Symmetric Difference: {set1.symmetric_difference(set2)}\n')
    print(f'Difference: {set1.difference(set2)}\n')


if __name__ == "__main__":
    get_countries_by_year(population(), 2018)
    get_data_by_year_for_germany(population())
    print(f'Data for country_year is as follow: {get_data_by_country_and_year(population())}\n\n')
    get_data_with_health_index_bigger_that_5(get_data_by_country_and_year(population()))
    get_data_with_health_index_bigger_that_5_and_sex_f(get_data_by_country_and_year(population()))
    sets()