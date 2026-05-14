task = input("Введите задачу: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("Задача сохранена")task = input("Введите задачу: ")

