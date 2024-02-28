import random
import pyttsx3


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


speak_engine = pyttsx3.init()


user_age = True

while user_age != 0:
    print("#############--НАЧАЛО--###################")
    user_age = int(input("Введите ваш возраст: "))
    age = random.randint(365, 366)  # Day
    hour = 24  # Hour
    minute = 60  # Minutes
    second = 60  # Second

    days = age * user_age  # count days in age
    hours = days * hour  # count hour in age
    minutes = hours * minute  # count minutes in age
    seconds = minutes * second  # count second in age

    if user_age not in range(0, 101):
        user_age = int(input("Попробуйте еще раз: "))

    elif user_age == 0:
        break
    
    else:
        print(f"Вы указали, что вам {user_age} лет")
        print(f"Это {days} дней, если в году {age} дней.")
        print(f"Это {hours} часов.")
        print(f"Это {minutes} минут.")
        print(f"Это {seconds} секунд.")
    
    print("##############--КОНЕЦ--###################")
    


# speak(f"Вы указали, что вам {user_age} лет")
# speak(f"Это {days} дней, если в году {age} дней.")
# speak(f"Это {hours} часов.")
# speak(f"Это {minutes} минут.")
# speak(f"Это {seconds} секунд.")
