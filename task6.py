def convert_length(value, from_unit, to_unit):
    length_units = {
        'm': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001,
        'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254
    }
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit.")
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kg': 1, 'g': 0.001, 'mg': 1e-6, 'lb': 0.453592, 'oz': 0.0283495
    }
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit.")
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'l': 1, 'ml': 0.001, 'm3': 1000, 'ft3': 28.3168, 'in3': 0.0163871
    }
    if from_unit not in volume_units or to_unit not in volume_units:
        raise ValueError("Invalid volume unit.")
    return value * volume_units[from_unit] / volume_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'C':
        return value * 9/5 + 32 if to_unit == 'F' else value + 273.15
    if from_unit == 'F':
        return (value - 32) * 5/9 if to_unit == 'C' else (value - 32) * 5/9 + 273.15
    if from_unit == 'K':
        return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9/5 + 32
    raise ValueError("Invalid temperature unit.")

def main():
    print("Welcome to the Measurement Converter!")
    print("Available conversion types: length, weight, volume, temperature")
    
    while True:
        conversion_type = input("\nEnter the type of conversion (or 'exit' to quit): ").lower()
        if conversion_type == 'exit':
            break
        
        if conversion_type not in ['length', 'weight', 'volume', 'temperature']:
            print("Invalid conversion type. Please try again.")
            continue
        
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit: ").lower()
        to_unit = input("Enter the to unit: ").lower()
        
        try:
            if conversion_type == 'length':
                result = convert_length(value, from_unit, to_unit)
            elif conversion_type == 'weight':
                result = convert_weight(value, from_unit, to_unit)
            elif conversion_type == 'volume':
                result = convert_volume(value, from_unit, to_unit)
            elif conversion_type == 'temperature':
                result = convert_temperature(value, from_unit, to_unit)
            print(f"Converted value: {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
