def determine_life_stage(age):
    """Определяет жизненный этап по возрасту"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"


def main():
    # Приветствие и сбор основной информации
    print("Hello! Let's create your profile.")

    full_name = input("Please enter your full name: ")
    birth_year = int(input("Please enter your birth year: "))

    # Расчет возраста
    current_year = 2025
    age = current_year - birth_year

    # Определение жизненного этапа
    life_stage = determine_life_stage(age)

    # Сбор хобби
    print("\nNow let's list your favorite hobbies.")
    print("Enter one hobby at a time. Type 'stop' to finish.")

    hobbies = []
    while True:
        hobby = input("Enter a hobby: ").strip()
        if hobby.lower() == "stop":
            break
        if hobby:  # Проверяем, что введено не пустое значение
            hobbies.append(hobby)

    # Создание профиля
    profile = {
        "name": full_name,
        "birth_year": birth_year,
        "age": age,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

    # Вывод итогового профиля
    print("\n" + "=" * 50)
    print("YOUR PROFILE SUMMARY")
    print("=" * 50)
    print(f"Name: {profile['name']}")
    print(f"Birth Year: {profile['birth_year']}")
    print(f"Current Age: {profile['age']}")
    print(f"Life Stage: {profile['life_stage']}")

    # Вывод хобби
    if not profile['hobbies']:
        print("Hobbies: You didn't list any hobbies.")
    else:
        print(f"Hobbies: You have {len(profile['hobbies'])} hobby(ies):")
        for hobby in profile['hobbies']:
            print(f"  • {hobby}")

    print("=" * 50)


# Запуск программы
if __name__ == "__main__":
    main()
