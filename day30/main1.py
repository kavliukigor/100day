try:
    file=open('file.txt')
    dictionary={'key':'value'}
    print(dictionary['key'])
except FileNotFoundError:
    file = open('file.txt','w')
    print('File error')
except KeyError as error_message:
    print(f"Key {error_message} don't exist")
else:
    inside=file.read()
    print(inside)
finally:
    height = float(input('Your height'))
    weight =int(input('Your weight'))

if height>3:
    raise ValueError("Nihuya ti shpala")
    
bmi=weight/height**2
print(bmi)