import random

def append_s(name):
    return name + 's'

print('Welcome to Apex Aura')
print('We have a huge collection of cars')
print('Please indicate your preferences.\n')

specs = ['Brand', 'Color', 'Transmission', 'Engine', 'DriveTrain', 'Interior', 'Wheels', 'Price']

specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)

master_dict['Brands'] = ['Porsche', 'BMW', 'McLaren', 'Ferrari', 'Lamborghini']
master_dict['Colors'] = ['Red', 'Blue', 'Black', 'Silver']
master_dict['Transmissions'] = ['Manual', 'Automatic', 'Dual-Clutch', 'Sequential', 'Direct Drive']
master_dict['Engines'] = ['V6', 'V8', 'V10', 'Electric', 'Hybrid']
master_dict['DriveTrains'] = ['Rear-Wheel Drive', 'All-Wheel Drive', 'Front Wheel Drive', 'Four-Wheel Drive']
master_dict['Interiors'] = ['Leather', 'Alcantara', 'Carbon Fiber', 'Cloth', 'Synthetic']
master_dict['Wheelss'] = ['Alloy', 'Carbon Fiber', 'Forged', 'Chrome']
master_dict['Prices'] = ['INR 1.5 Cr', 'INR 3 Cr', 'INR 5 Cr', 'INR 8.5 Cr', 'INR 10.5 Cr']

#  Collect user preferences
user_choice = {}
for kk in specs:
    user_choice[kk] = input('Any preference for ' + kk + ' (Enter no for no preference):\n')

# Print user preferences for confirming choices
print('\n' + '='*30)
print('YOUR SELECTED PREFERENCES:')
print('='*30)
for kk in specs:
    print(kk + ': ' + user_choice[kk])

# 3. Ask for confirmation
confirm = input('\nAre you sure you want to proceed with these preferences? (yes/no): ')

if confirm.strip().lower() == 'yes':
    
    # 4. Generate 8 cars based on user preferences
    selected = []
    for i in range(random.randint(8, 11)):
        car = {}
        for kk in specs:
            pref = user_choice[kk].strip()
            if pref.lower() != 'no':
                car[kk] = pref
            else:
                car[kk] = random.choice(master_dict[append_s(kk)])
        selected.append(car)

    print('\nHere are ' + str(len(selected)) + ' cars that met your preference:\n')

    # 5. Output 
    for kk in specs:
        print(f'{kk:<13}', end='')
    print()

    print('-' * (13 * len(specs)))

    for car in selected:
        for kk in specs:
            print(f'{car[kk]:<13}', end='')
        print()

else:
    print('\nPreferences not confirmed. Run the program again to restart.')