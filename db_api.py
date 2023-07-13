import sqlite3

db_path = 'database.db'
c = sqlite3.connect(db_path).cursor()

def func_get(table: str = 'users', **kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    request_kwargs = "("
    for arg in keys:
        request_kwargs += f"{arg},"
    request_kwargs = request_kwargs[:-1] + ") = (" + "?," * (len(keys)-1) + '?' + ")"
    try:
        return c.execute(f"SELECT * FROM '{table}' WHERE {request_kwargs}", values)
    except TypeError:
        return None


def func_get_one(table: str = 'users', parametrs: list = None, **kwargs) -> dict:
    """

    :param table: Название таблицы в БД
    :param parametrs: Параметры, которые нужно вытащить со строчки, по дефолту ВСЕ
    :param kwargs: Критерии по которым идет отбор
    :return: Словарь с данными
    """
    data = func_get(table, **kwargs).fetchone()
    return {x: data[x] for x in parametrs} if parametrs else dict(data)


def func_get_all(table: str = 'users', parametrs: list = None, **kwargs) -> list[dict]:
    """
    БД, получить все строчки по критериям.

    :param table: Название таблицы в БД
    :param parametrs: Параметры, которые нужно вытащить с каждый строчки, по дефолту ВСЕ
    :param kwargs: Критерии по которым идет отбор
    :return: Список словарей с данными
    """
    data = func_get(table, **kwargs).fetchall()
    return [{x: elem[x] for x in parametrs} if parametrs else dict(elem) for elem in data]
