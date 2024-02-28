import random
import pyttsx3

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

speak_engine = pyttsx3.init()

user_age = int(input('Введите ваш ворзраст: '))
age = random.randint(365, 366) # Day
hour = 24 # Hour
minute = 60 # Minutes
second = 60 # Second


days = age * user_age # count days in age
hours = days * hour # count hour in age
minutes = hours * minute # count minutes in age
seconds = minutes * second # count second in age


speak(f"Вы указали, что вам {user_age} лет")
speak(f"Это {days} дней, если в году {age} дней.")
speak(f"Это {hours} часов.")
speak(f"Это {minutes} минут.")
speak(f"Это {seconds} секунд.")
