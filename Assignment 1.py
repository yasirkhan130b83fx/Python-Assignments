# 1
print(f'''Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are''')


# 2
from platform import python_version
print(python_version())



# 3
import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)



# 4
import math
r = float(input("Please, enter radius: "))
print(f'Area = {math.pi * (r**2)} square unit/units')



# 5
ufn = "".join(reversed(input("Please, enter your first name: ")))
uln = "".join(reversed(input("Please, enter your last name: ")))
print(f'{ufn} {uln}')




# 6
a = int(input("Please, enter first value: "))
b = int(input("Please, enter second value: "))
print(f'Addition = {a + b}')





