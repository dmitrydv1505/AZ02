# AZ02
 AZ02. Загрузка данных. Обработка пропущенных значений и дубликатов. Преобразование данных и работа с типами.

ЗАДАНИЕ
Задание: Исследование оценок учеников

Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:

1. Самостоятельно создайте DataFrame с данными

2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно

3. Вычислите среднюю оценку по каждому предмету

4. Вычислите медианную оценку по каждому предмету

5. Вычислите Q1 и Q3 для оценок по математике:

Q1_math = df['Математика'].quantile(0.25)

Q3_math = df['Математика'].quantile(0.75)

- можно также попробовать рассчитать IQR

6. Вычислите стандартное отклонение

В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.


### Описание:
- **Шаг 1**: Используется `numpy` для генерации случайных оценок от 50 до 100 для 10 учеников по 5 предметам.
- **Шаг 2**: Выводятся первые несколько строк DataFrame с помощью `df.head()`.
- **Шаг 3**: Средние оценки вычисляются с помощью `df.mean()`.
- **Шаг 4**: Медианные оценки вычисляются с помощью `df.median()`.
- **Шаг 5**: Вычисляются первые и третьи квартильные значения для оценок по математике, а также интерквартильный размах (IQR).
- **Шаг 6**: Стандартное отклонение рассчитывается для каждого предмета с помощью `df.std()`.