# import math - would be needed for math.ceil. Round function works wihout math module

afloat = float(input('Enter a float number: '))

# round_afloat = math.ceil(afloat)  math.ceil always rounds up

round_afloat = round(afloat) # 1/1 round function - python uses Banker's rounding or "Half to Even" method 
# 2/1 where it rounds to the nearest EVEN number. I.e. 4.5 rounded to 4 and 5.5 is rounded to 6

print(f'{afloat} rounded is {round_afloat}')