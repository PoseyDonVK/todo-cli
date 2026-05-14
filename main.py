while True:
    print("\n1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выход")

    choice = input("> ")

    if choice == "1":
        task = input("Введите задачу: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")

        except FileNotFoundError:
            print("Задач пока нет")

    elif choice == "3":
        break
