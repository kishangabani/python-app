'''
import math;
print("KI", end=' ')
print("Gabani")
print(3//2.0)
print(round(12.5))
print(2**3)
print(9//3)
print(          2*3)
print((1/10))
print(format(math.pi, '.48f'))

'''
#while True: print("Hello")
'''while True:
    try:
        x= int(input("Enter Numbr:"))
        break;
    except ValueError:
        print("Try Again.......")
'''
'''
user_ip = "Yogesh"
now = "16:20."
url = "http://petshop.com/pets/reptiles/pythons"

# TODO: print a log message incorporating the strings above.
# The message should be use the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

msg= user_ip+" accessed the site "+url+" at "+now
print(msg)
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)
print(log_message)
'''
'''
city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"
t=('gbbbgbrbttrrt....rrfffff.'
    '   gbebtt')
print(t)
print("\n")
word="KIshan"
print(word)
# print(word[3:]+word[:3])
print(word[:])
print(len(word))
abc=[11,22,33,44,55,66,77]
print(abc[-2:])
abc.append(88*2)
print(abc)
k=0
for i in range(5):
    k=k+i
    print(k)
'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#ask_ok('Do you really want to quit?')