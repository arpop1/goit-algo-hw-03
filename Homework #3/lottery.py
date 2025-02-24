import random

def get_numbers_ticket(min, max, quantity):
        try:
            numbers_set = set()
            limit = max - min #є ідея написати таку формулу: (max - min)+1. Уявімо що нам потрібно 5 чисел від 1 до 5 (вийде 1, 2, 3, 4, 5.), тоді формула max - min не підійде?
            if min >= 1 and min < max <= 1000 and quantity <= limit:
                while len(numbers_set) < quantity:
                     number = random.randrange(min, max)
                     numbers_set.add(number)
            numbers_list = list(numbers_set)
            numbers_list.sort()
            return numbers_list 
        except (TypeError, ValueError, NameError):
            print("Неправильно введені дані. Використувуйте числа")
            return numbers_list

result = get_numbers_ticket(10, 14, 6)
print(result) #Повертає тільки 1, 2, 3, 4, оскільки інших комбінацій бути не може
