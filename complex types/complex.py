def lists(lst):
    #вывод списка
    print(lst)
    #добавление элемента
    lst.append('Python')
    #вывод длины списка
    print(len(lst))
    #вывод 1-го элемента
    print(lst[0])
    #вывод последнего элемента
    print(lst[-1])
    #вывод со 2 по 4
    print(lst[1:4])
    #удаление строки
    lst.remove('Python')

def dicts(dct):
    #вывод по ключу
    print (dct.get('city'))
    #переопределение значения
    dct["temperature"]=float(dct.get("temperature"))-5   
    #Провреа наличие элемента и установка по умолчанию при его отсутствии
    if not dct.get('country'):
        dct['country']='Russia'
    #добавление даты
    dct['date']='27.05.2019'
    #вывод словаря
    print (dct)


lists([3, 5, 7, 9 ,10.5])

dicts({"city": "Москва", "temperature": "20"})