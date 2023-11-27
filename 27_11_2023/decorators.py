import time

def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


def make_breakfast():
    print("preparing breakfast")
    time.sleep(3)
    print("breakfast ready")
    
# @calculate_time
def make_coffee():
    print("preparing coffee")
    time.sleep(2)
    print("coffee ready")

make_coffee()
