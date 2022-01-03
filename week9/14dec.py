"""
День 2. Неделя 9. 14 декабря
Тема: QuerySet Django

QuerySet - это набор объектов из базы данных, который может использовать фильтры для ограничения результатов.

QuerySet позволяет читать данные из базы данных, фильтровать и изменять их порядок и т.д.

Каждая модель содержит как минимум один Manager, и он называется objects по умолчанию. Обратиться к нему можно непосредственно через класс модели.
ClassName.objects

- all() - возвращает все объекты
        ClassName.objects.all()


- get(), first() - возвращают один объект
    ClassName.objects.get(condition)


- filter() - фильтрует QuerySet
    ClassName.objects.filter(condition)

- count() - подсчитывает количество объектов в QuerySet
        ClassName.objects.count()



Начало разбора:

objects.filter(column__startswith=condition)



"""


"""


"""





