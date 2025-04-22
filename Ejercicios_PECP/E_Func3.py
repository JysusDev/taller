def liters_100km_to_miles_gallon(liters):
    mile = 100000/1609.334
    galon = liters / 3.785411784
    return mile / galon

def miles_gallon_to_liters_100km(miles):
    km = miles * 1609.344 / 100000
    lt = 3.785411784
    return lt/km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))