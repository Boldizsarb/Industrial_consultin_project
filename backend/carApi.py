import requests




def vehicle_enquiry(registration_number):

    co2_emissionCar = ""
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-api-key": "w2aWXWc3BKsQnR74vUzJ5KUzjsUSdLe8FlMAbMLi",
        "X-Correlation-Id": "string"
    }
    data = {
        "registrationNumber": registration_number
    }

    response = requests.post(url, json=data, headers=headers)
    json_data = response.json() ## the whole json response if needed

    if 'co2Emissions' in json_data:
        co2_emissionCar = json_data['co2Emissions']  # Update the global variable
    else:
        co2_emissionCar = ""  # Handle the case where 'co2Emissions' is not present

    return co2_emissionCar


def miles_to_kilometers(miles):
    return miles * 1.60934



def final_emition(reg,miles, people =1): ### this gives you the final g/km -> grams per kilometer ## by default the number of people is 1

    gram_per_km = vehicle_enquiry(reg)
    kilometer = miles_to_kilometers(miles)
    total_emmission = gram_per_km * kilometer
    total_emmission_in_miles = gkm_to_gm(total_emmission) / people
    return total_emmission_in_miles,total_emmission


def gkm_to_gm(g_per_km): ## changing it to miles
    return g_per_km / 0.621371


# in_km = final_emition("GV08OWH",20) ## this would be the function call with 2 parameters, the reg and the miles
# in_miles = gkm_to_gm(in_km)
# print(f"The emmited Co2 is {in_km} g/km , or {in_miles} g/mile shame on you!")

print(final_emition("gv08owh",20,1))