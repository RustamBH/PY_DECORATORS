from datetime import datetime


def parametrized_decor_logger(path):
    def decor_log(func):
        def wrap_log(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Дата и время запуска функции: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                file.write(f'Вызов функции: {func.__name__} с аргументами {args} и {kwargs}\n')
                file.write(f'Результат: {result}\n')
            return result

        return wrap_log

    return decor_log


@parametrized_decor_logger(path='logs/decor_logger_2.log')
def multiply_function(a, b):
    return a * b


if __name__ == "__main__":
    value = multiply_function(3, 4)
