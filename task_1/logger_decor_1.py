import logging


def log(func):
    """
    Логируем какая функция вызывается.
    """

    def wrap_log(*args, **kwargs):
        name_log = "logger_decor_1.log"
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Открываем файл логов для записи.
        fh = logging.FileHandler(name_log, encoding='UTF-8')
        fmt = '%(asctime)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info(f'Вызов функции: {func.__name__} с аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Результат: {result}')
        return func

    return wrap_log


@log
def multiply_function(a, b):
    return a * b


if __name__ == "__main__":
    value = multiply_function(2, 3)
