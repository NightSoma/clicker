import os
import random
from typing import Any


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def allowed_input(allowed_keys: list[str]) -> str:
    key = None

    while key not in allowed_keys:
        key = input("> ")

    return key


upgrades: dict[int, dict[str, Any]] = {
    -1: {
        "text": "Більша винагорода за виграш",
        "code": -1,
        "level": 0,
        "preset": [[10, 2], [12, 3], [15, 4], [20, 5], [50, 10]],
    },
    -2: {
        "text": "Менший простір загадування",
        "code": -2,
        "level": 0,
        "preset": [
            [10, 9],
            [11, 8],
            [12, 7],
            [14, 6],
            [17, 5],
            [22, 4],
            [29, 3],
            [44, 2],
            [88, 1],
        ],
    },
    -3: {
        "text": "Шанс виграти навіть, якщо не вгадав",
        "code": -3,
        "level": 0,
        "preset": [
            [10, 10],
            [20, 20],
            [30, 30],
            [40, 40],
            [50, 50],
            [60, 60],
            [70, 70],
            [80, 80],
            [90, 90],
            [100, 100],
        ],
    },
}


random.seed(42)


def main(points: int = 0):
    number_min = 1
    number_max = 10
    points_for_correct_guess = 1
    random_chance_to_win = 0
    avaiable_upgrades = [-1, -2, -3]
    last_input_result: str = (
        f"Введіть будь яке число від {number_min} до {number_max} включно."
    )
    offset_description = 40
    # Game loop
    while points < 100:
        correct_number = random.randint(number_min, number_max)

        # Round loop
        while True:
            clear_screen()

            print(f"Кількість очок: {points:>32}")
            print(f"Винагорода за вгадування: {points_for_correct_guess:>22}")
            print(
                f"Загадене число може бути на проміжку від {number_min} до {number_max}"
            )
            print(f"Шанс виграти навіть коли не вгадав: {random_chance_to_win:>11}%")
            print()
            print("Ти можеш купити наступні апгрейди")
            print("(Щоб обрати один введи відповідне відємне значення)")
            print(f"Ціна|Код вибору|{'Опис':^{offset_description}}|    Зміна   ")
            for upgrade_code in avaiable_upgrades:
                upgrade = upgrades[upgrade_code]
                level = upgrade["level"]
                preset = upgrade["preset"]
                price, upgrade_value = preset[level][0], preset[level][1]
                if upgrade_code == -1:
                    print(
                        f"{price:^4}|{upgrade['code']:^10}|{upgrade['text']:^{offset_description}}|  {points_for_correct_guess} -> {upgrade_value}"
                    )
                elif upgrade_code == -2:
                    print(
                        f"{price:^4}|{upgrade['code']:^10}|{upgrade['text']:^{offset_description}}|  1-{number_max} -> 1-{upgrade_value}"
                    )
                elif upgrade_code == -3:
                    print(
                        f"{price:^4}|{upgrade['code']:^10}|{upgrade['text']:^{offset_description}}|  {random_chance_to_win}% -> {upgrade_value}%"
                    )

            print()
            print(last_input_result)
            print()

            key = allowed_input(
                [str(i) for i in range(number_min, number_max + 1)]
                + [str(uid) for uid in avaiable_upgrades]
            )
            key_int = int(key)

            if key_int in avaiable_upgrades:
                level = upgrades[key_int]["level"]
                preset = upgrades[key_int]["preset"]
                price, upgrade_value = preset[level][0], preset[level][1]

                if points < price:
                    last_input_result = f"Недостатньо очок для '{upgrades[key_int]['text']}', треба {upgrades[key_int]['price']}"
                    continue

                if key_int == -1:
                    points_for_correct_guess = upgrade_value
                    upgrades[key_int]["level"] += 1
                elif key_int == -2:
                    number_max = upgrade_value
                    upgrades[key_int]["level"] += 1
                elif key_int == -3:
                    random_chance_to_win = upgrade_value
                    upgrades[key_int]["level"] += 1

                if len(preset) <= upgrades[key_int]["level"]:
                    avaiable_upgrades.remove(key_int)

                points -= price
                last_input_result = (
                    f"Ви отримали покращення '{upgrades[key_int]['text']}'"
                )
            elif (
                key_int == correct_number
                or random.random() < random_chance_to_win / 100
            ):
                points += points_for_correct_guess
                last_input_result = f"Вірно, загадане число було {correct_number}!\nЯ загадв нове число, продовжуємо"
                break
            else:
                last_input_result = "Не вгадав, спробуй ще раз."


if __name__ == "__main__":
    while True:
        main()
        clear_screen()
        print("Ще раз? т (Так), н (Ні)")
        key = allowed_input(["т", "н"])
        if key == "н":
            break

    print("Дякую за гру!")
