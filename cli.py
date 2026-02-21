from storage import load_logs, save_logs
from analyzer import add_log, filter_by_category, total_spent, top_categories

# Вспомогательные функции
#_______________________________________________
def date_validation(date):   # YYYY-MM-DD

    if len(date) != 10:
        return False
    
    if date[4] != "-" and date[7] != "-":
        return False
    
    year = date[:4]
    month = date[5:7]
    day = date[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    
    if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
        return False

    return True


def menu_validation(action):
    try:
        action_int = int(action)
    except TypeError, ValueError:
        return False
    else:
        if action_int >= 1 and action_int <= 7:
            return action_int
        else:
            return False
        

def category_validation(category):
    if category == "":
        return False
    else:
        return True


def amount_validation(amount_str):
    try:
        amount_int = int(amount_str)
    except ValueError:
        return False
    else:
        if amount_int < 0:
            return False
        return True




# Функции действия / меню
#_______________________________________________
def print_menu():
    print(
        "Меню:\n"
        "1 - Показать логи\n"
        "2 - Добавить логи\n"
        "3 - Фильтр по категории\n"
        "4 - Общая сумма\n"
        "5 - ТОП-3 категории\n"
        "6 - Сохранить\n"
        "7 - Выход\n"   #autosave
        "________________________\n"
    )



#______________________________________________
def main():
    logs, status = load_logs()

    if logs == []:
        print("Файла нет/пустой. Создан пример логов.")
        logs = [
            {"date": "Example: 2026-02-01", "category": "food", "amount": 450, "user_data": False},
            {"date": "Example: 2026-02-02", "category": "transport", "amount": 120, "user_data": False},
        ]
        save_logs(logs)

    if logs is None:
        print(f"{status} \nФайл повреждён. Проверьте вручную прежде чем продолжить.")
        return 

    print("Логи загружены.\n")

    while True:
        
        print_menu()
        # Выбираем действие
        while True:
            action_str = input("Выберите действие: ")
            if menu_validation(action_str) is False:
                print("Введите целое число от 1 до 7")
                continue
            else:
                action = menu_validation(action_str)
                break
        
        # 1-e действие /// Показать логи
        if action == 1:
            print("Текущие логи:")
            for log in logs:
                idx = logs.index(log) + 1
                print(f"{idx}. Дата: {log["date"]} | Категория: {log["category"]} | Траты: {log["amount"]} | " )
            continue


        # 2-e действие /// Добавить логи
        if action == 2:
            print("Добавить лог:")
            while True:
                date = str(input("Введите дату (YYYY-MM-DD): "))
                if date_validation(date) is False:
                    print("Введите правильную дату (YYYY-MM-DD): ")
                    continue
                break
            while True:
                category = str(input("Ввердите категорию: "))
                category = category.strip().lower()
                if category_validation(category) is False:
                    print("Строка не может быть пустой.")
                    continue
                break
            while True:
                amount_str = str(input("Введите трату $:"))
                if amount_validation(amount_str) is False:
                    print("Введите сумму правильно (целое положителньое число)")
                    continue
                amount = int(amount_str)
                break
            
            while True:
                print(f"Вы уверены что хотите добавить лог: \nДата: {date}, категория: {category}, затраты: ${amount}?")
                answer = input("y/n:  ")
                if answer == "y":
                    add_log(logs, date, category, amount)
                    break
                elif answer == "n":
                    break
                else:
                    print("Введите ответ (y/n)")

        # 3-e действие /// Фильтр по категории
        if action == 3:                
            while True:
                category = str(input("Введите категорию для фильра: "))
                category.strip().lower()
                if category_validation(category) is False:
                    print("Строка не может быть пустой.")
                    continue
                break
            filtered = filter_by_category(logs, category)
            if filtered is False:
                print("Категория не найдена.")
            else:
                for log in filtered:
                    idx = filtered.index(log) + 1
                    print(f"{idx}. Дата: {log["date"]} | Категория: {log["category"]} | Траты: {log["amount"]} | " )
            continue

        # 4-e действие /// Общая сумма
        if action == 4:
            print("Итоговые затраты:")
            total = total_spent(logs)
            print(f"${total}")
            continue
    
        # 5-e действие /// Топ-3 категории
        if action == 5:
            print("3 самые затратные категории:")
            top = top_categories(logs)
            idx = 0
            for log in top:
                print(f"{idx + 1}. {log[0]}: ${log[1]}" ) 
                idx += 1
            continue

        # 6-e действие /// Сохранить логи
        if action == 6:
            save_logs(logs)
            print("Логи сохранены.")
            continue

        # 7-e действие
        if action == 7:
            save_logs(logs)
            print("Выход из программы...")
            break

if __name__ == "__main__":
    main()