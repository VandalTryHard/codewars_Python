def main():
    print(valueYear("ADA", 1.36, 0.48, 29))


def valueYear(Name, price, percentYear, number):
    value = 0
    newNumber = number
    newValue =
    for i in range(365):
        dayValue = (price*number) * (percentYear / 365)
        value += dayValue
        newNumber += number * (percentYear/365)
        print(f"Value day: {dayValue}")
    yearValue = price * percentYear
    print(f"{Name} в количестве {number} приносит тебе в день {dayValue}$ или {yearValue} в год.\n"
          f"А Если ты будешь держать {Name} год и постоянно увеличивать 'Переводить автоматически':"
          f"{Name} принесет тебе в конце года {newNumber} и у тебя их будет {newNumber}")



if __name__ == "__main__":
    main()
