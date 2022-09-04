# tip calculator App
food_amount = float(input('enter food amount $: '))
tip_percentage = float(input('enter tip percentage %:')) / 100
tip_amount = food_amount * tip_percentage
total = food_amount + tip_amount
print('$' + str(total))