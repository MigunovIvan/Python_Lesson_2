# Задание 3:

raw = input("Введите текст на проверку:" ).strip().lower().capitalize()

valid_endings = (".", "!", "?", ";")

if not raw.endswith(valid_endings):
    raw = raw + "."
    print("Знак препинания в конце отсутствовал —  точка добавлена автоматически:", raw)
else:
    print(raw)
