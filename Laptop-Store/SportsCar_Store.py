import random
from datetime import datetime, timedelta

def append_s(name):
    return name + 's'

print('Welcome to Apex Aura')
print('We have a huge collection of cars')
print('Please indicate your preferences.\n')

specs = ['Brand', 'Color', 'Transmission', 'Engine', 'DriveTrain', 'Interior', 'Wheel', 'Price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)

master_dict['Brands'] = ['Porsche', 'BMW', 'McLaren', 'Ferrari', 'Lamborghini']
master_dict['Colors'] = ['Red', 'Blue', 'Black', 'Silver']
master_dict['Transmissions'] = ['Manual', 'Automatic', 'Dual-Clutch', 'Sequential', 'Direct Drive']
master_dict['Engines'] = ['V6', 'V8', 'V10', 'Electric', 'Hybrid']
master_dict['DriveTrains'] = ['Rear-Wheel Drive', 'All-Wheel Drive', 'Front Wheel Drive', 'Four-Wheel Drive']
master_dict['Interiors'] = ['Leather', 'Alcantara', 'Carbon Fiber', 'Cloth', 'Synthetic']
master_dict['Wheels'] = ['Alloy', 'Carbon Fiber', 'Forged', 'Chrome']
master_dict['Prices'] = ['INR 1.5 Cr', 'INR 3 Cr', 'INR 5 Cr', 'INR 8.5 Cr', 'INR 10.5 Cr']

# Collect user preferences
user_choice = {}
for spec in specs:
    user_choice[spec] = input('Any preference for ' + spec + ' (These are the available options): ' + ', '.join(master_dict[append_s(spec)]) + '\n')

# Print user preferences for confirming choices
print('\n' + '='*30)
print('YOUR SELECTED PREFERENCES:')
print('='*30)
for spec in specs:
    print(spec + ': ' + user_choice[spec])

# 3. Ask for confirmation
confirm = input('\nAre you sure you want to proceed with these preferences? (yes/no): ')

if confirm.strip().lower() == 'yes':
    
    # 4. Generate 8 cars based on user preferences
    selected = []
    for i in range(random.randint(8, 11)):
        car = {}
        for spec in specs:
            pref = user_choice[spec].strip()
            if pref.lower() != 'no':
                car[spec] = pref
            else:
                car[spec] = random.choice(master_dict[append_s(spec)])
        selected.append(car)

    print('\nHere are ' + str(len(selected)) + ' cars that met your preference:\n')

    # 5. Output 
    print(f"{'No.':<6}", end='')
    for spec in specs:
        print(f'{spec:<18}', end='')
    print()

    print('-' * (6 + 18 * len(specs)))

    for idx, car in enumerate(selected, 1):
        print(f'{idx:<6}', end='')
        for spec in specs:
            print(f'{car[spec]:<18}', end='')
        print()

    # Simple selection and accessory dictionary
    pick = int(input('\nPick any car option number: ')) - 1
    chosen_car = selected[pick]
    brand = chosen_car['Brand']

    accessories = {
        'Porsche': ['Skull gear knob', 'Stickers', 'Sport mats'],
        'BMW': ['Blue headlights', 'Interior lights', 'Badges'],
        'McLaren': ['Telemetry kit', 'Wing mirrors', 'Steering wheel'],
        'Ferrari': ['Scuderia shields', 'Red belts', 'Titanium tips'],
        'Lamborghini': ['Underglow', 'Neon lights', 'Racing stripes']
    }

    print(f'Accessories for {brand}: {", ".join(accessories[brand])}')
    acc = input('Which accessory do you want? : ')
    print(f'Added {acc} to your {brand}!')

    # Interactive delivery announcement and payment prompt
    delivery_date = (datetime.now() + timedelta(days=8)).strftime('%A, %B %d, %Y')
    
    color = chosen_car['Color']
    engine = chosen_car['Engine']
    trans = chosen_car['Transmission']
    drivetrain = chosen_car['DriveTrain']
    interior = chosen_car['Interior']
    wheels = chosen_car['Wheel']
    price = chosen_car['Price']

    print("\n" + "🏁 " * 15)
    print("🔥 CONGRATULATIONS! YOUR DREAM MACHINE IS LOCKED IN! 🔥")
    print("=" * 45)
    print(f"Your beastly {color} {brand} with a roaring {engine} engine, {trans} transmission,")
    print(f"and {drivetrain} setup is officially in production!")
    print(f"✨ Custom Features:")
    print(f"   • Cabin: {interior} interior")
    print(f"   • Rims: {wheels} wheels")
    print(f"   • Extra Flex: Custom {acc}")
    print("-" * 45)
    print(f"📦 Get ready! It arrives at your doorstep in exactly 8 days on {delivery_date}.")
    print(f"💳 Total Investment: {price}")
    print(f"⚡ Please process the transfer of {price} by this week to finalize order. Welcome to Apex Aura! 🏎️💨")
    print("🏁 " * 15)

else:
    print('\nPreferences not confirmed. Try running it again :).')