
#1
def add_number(num1: int, num2: int) :
    return num1 + num2
print("The answer is", add_number(4,5))

#2
def is_even(number):
    return number % 2 == 0

print(is_even(0))




#3
def reverse_string(text):
    return text[::-1]

print(reverse_string("Zack"))




#4
def count_vowels(text):
    vowels = 'aeiou'
    
    text = text.lower()
    
    count = sum(1 for char in text if char in vowels)
    
    return count

print(count_vowels("Zack Njine"))


#5
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper


#6
def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func


@apply_decorator
def my_function():
    print("Original Function Called")

my_function()


#7

def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# Example usage
people = [("Zack", 50), ("Njine", 25), ("John", 15)]
print(sort_by_age(people))


#8

def merge_dicts(dict1, dict2):
    
    merged = dict1.copy() 
    
    
    for key, value in dict2.items():
        if key in merged:
    
            merged[key] += value
        else:
    
            merged[key] = value
            
    return merged


dict1 = {'a': 4, 'b': 7, 'c': 17}
dict2 = {'b': 44, 'c': 48, 'd': 51}
result = merge_dicts(dict1, dict2)
print(result)

#9
class Smartphone:
    def __init__(self, brand, model, release_year):
        self.brand = brand
        self.model = model
        self.release_year = release_year

    def display_info(self):
        print(f"Smartphone Brand: {self.brand}")
        print(f"Smartphone Model: {self.model}")
        print(f"Release Year: {self.release_year}")


my_phone = Smartphone("Apple", "iPhone 13", 2021)
my_phone.display_info()



























