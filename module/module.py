def converter():
    FOOT = 30.48
    INCH = 2.54 
    MILE = 1609.34

    class PublicClass(object):
        def inches_to_centimeters(inches):
            return inches * INCH
        def feet_to_meters(feet): 
            return feet * FOOT
        def milesToKilometers( miles):
            return miles * MILE
    return PublicClass

module_converter = converter()
print(module_converter.feet_to_meters(12))