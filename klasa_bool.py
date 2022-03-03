class Car:

    def __init__(self, color, length):
        self.color = color
        self.length = length

    def __bool__(self):
        if self.color == "green":
            return False
        return True

    def __len__(self):
        print('len was called...')
        return self.length


class Test:
    def __bool__(self):
        return False


test = Test()

if test:
    print("Test is always True")
else:
    print("Test is always False")



green_car = Car("green", -100)
blue_car = Car("blue", 100)

print(bool(green_car))
if green_car.length:
    print(green_car.length)
print(bool(blue_car))
if blue_car.length:
    print(blue_car.length)