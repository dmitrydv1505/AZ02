import pandas as pd
import numpy as np

try:
    # Создаем данные с оценками учеников
    data = {
        'Ученик': [f'Ученик {i}' for i in range(1, 11)],
        'Математика': np.random.randint(1, 6, size=10),
        'Физика': np.random.randint(1, 6, size=10),
        'Химия': np.random.randint(1, 6, size=10),
        'Литература': np.random.randint(1, 6, size=10),
        'История': np.random.randint(1, 6, size=10)
    }

    # Создаем DataFrame
    df = pd.DataFrame(data)

    # 1. Вывод первых нескольких строк DataFrame
    print("Первые несколько строк DataFrame:")
    print(df.head(), "\n")

    # 2. Вычислить среднюю оценку по каждому предмету
    print("Средняя оценка по каждому предмету:")
    print(df.mean(numeric_only=True), "\n")

    # 3. Вычислить медианную оценку по каждому предмету
    print("Медианная оценка по каждому предмету:")
    print(df.median(numeric_only=True), "\n")

    # 4. Вычислить Q1 и Q3 для оценок по математике
    Q1_math = df['Математика'].quantile(0.25)
    Q3_math = df['Математика'].quantile(0.75)
    IQR_math = Q3_math - Q1_math
    print(f"Q1 для Математики: {Q1_math}")
    print(f"Q3 для Математики: {Q3_math}")
    print(f"IQR для Математики: {IQR_math}\n")

    # 5. Вычислить стандартное отклонение
    print("Стандартное отклонение по каждому предмету:")
    print(df.std(numeric_only=True), "\n")

except Exception as e:
    print(f"Произошла ошибка: {e}")
