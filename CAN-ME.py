#!/usr/bin/env python3
import sys
def print_banner():
    print(r" :'######:::::'###::::'##::: ##::::::::::'##::::'##:'########: ")
    print(r" '##... ##:::'## ##::: ###:: ##:::::::::: ###::'###: ##.....:: ")
    print(r"  ##:::..:::'##:. ##:: ####: ##:::::::::: ####'####: ##::::::: ")
    print(r"  ##:::::::'##:::. ##: ## ## ##:'#######: ## ### ##: ######::: ")
    print(r"  ##::::::: #########: ##. ####:........: ##. #: ##: ##...:::: ")
    print(r"  ##::: ##: ##.... ##: ##:. ###:::::::::: ##:.:: ##: ##::::::: ")
    print(r" . ######:: ##:::: ##: ##::. ##:::::::::: ##:::: ##: ########: ")
    print(r" :......:::..:::::..::..::::..:::::::::::..:::::..::........:: ")
    print(r"REDC2PORTAL: Just a simple python script used for quick CANDUMP raw data conversion to display speed")
    sys.stdout.flush()
def calculate_speed(data, speed_pos=3, kph_to_mph_factor=0.6213751):
    data_bytes = [data[i:i+2] for i in range(0, len(data), 2)]
    if len(data_bytes) < speed_pos + 2:
        print(f"Invalid data: {data} - Not enough bytes in the data string. LIGMA BALLZ")
        return None
    byte_3 = int(data_bytes[speed_pos], 16)
    byte_4 = int(data_bytes[speed_pos + 1], 16)
    speed_kph = (byte_3 << 8) + byte_4
    speed_kph = speed_kph / 100.0
    speed_mph = speed_kph * kph_to_mph_factor
    return round(speed_kph, 2), round(speed_mph, 2)
def main():
    print_banner()
    default_speed_pos = 3
    default_kph_to_mph_factor = 0.6213751
    change_defaults = input("Change the default values? (yes/no): ").strip().lower()
    if change_defaults == 'yes':
        speed_pos_input = input(f"Enter speed position (default is {default_speed_pos}): ").strip()
        speed_pos = int(speed_pos_input) if speed_pos_input.isdigit() else default_speed_pos
        kph_to_mph_input = input(f"Enter KPH to MPH conversion factor (default is {default_kph_to_mph_factor}): ").strip()
        kph_to_mph_factor = float(kph_to_mph_input) if kph_to_mph_input else default_kph_to_mph_factor
    else:
        speed_pos = default_speed_pos
        kph_to_mph_factor = default_kph_to_mph_factor
    print("Enter lines of raw CAN data in hexadecimal format type 'done' when you are obviously done:")
    data_lines = []
    max_speed_kph = 0
    max_speed_mph = 0
    while True:
        raw_data = input().strip()
        if raw_data.lower() == 'done':
            break
        data_lines.append(raw_data)
    for index, raw_data in enumerate(data_lines):
        result = calculate_speed(raw_data, speed_pos, kph_to_mph_factor)
        if result:
            speed_kph, speed_mph = result
            print(f"Data Line {index + 1}: Speed: {speed_kph} kph, {speed_mph} mph")
            if speed_kph > max_speed_kph:
                max_speed_kph = speed_kph
                max_speed_mph = speed_mph
        else:
            print(f"Data Line {index + 1}: Invalid data")
    print("CAN Done Taking A Big DUMP")
    print("\nFastest Speed Found:")
    print(f"{max_speed_kph} kph, {max_speed_mph} mph OH SO FAST! MUCH WOW!")
if __name__ == "__main__":
    main()
