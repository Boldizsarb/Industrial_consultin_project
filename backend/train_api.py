

def calculate_train_emissions_standardized(distance_miles, co2_per_mile_per_person=35):
    total_co2_per_person = distance_miles * co2_per_mile_per_person
    return total_co2_per_person

## acoording to srouces the avarage co2 emited by a bus per pserson is 100g/mile
distance_miles = 10  # example distance in miles

emission_per_passenger = calculate_train_emissions_standardized(distance_miles)
print(f"CO2 Emissions per passenger for the trip: {emission_per_passenger:.1f} grams")