body_weight, height = map(float, input('Enter your body weight and your height separated by a space: ')
                          .replace(',', '.').split())
calculating = body_weight / (height ** 2)
print(f'Your body index {round(calculating, 1)}')
