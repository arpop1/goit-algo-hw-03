import random

def get_numbers_ticket(min, max, quantity):
        try:
            numbers_set = set()
            if min >= 1 and max <= 1000:
                while len(numbers_set) < quantity:
                     number = random.randrange(min, max)
                     numbers_set.add(number)
            else:
                print("Числа повинні бути від 1 до 1000")
            numbers_list = list(numbers_set)
            numbers_list.sort()
            return numbers_list 
        except (TypeError, ValueError, NameError):
            print("Неправильно введені дані. Використувуйте числа")

result = get_numbers_ticket(1, 5, 4)
print(result) #Повертає тільки 1, 2, 3, 4, оскільки інших комбінацій бути не може