import logging


def parametrized_decor_logger(path):
    def log(func):
        """
        Логируем какая функция вызывается.
        """

        def wrap_log(*args, **kwargs):
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)

            # Открываем файл логов для записи.
            fh = logging.FileHandler(path, encoding='UTF-8')
            fmt = '%(asctime)s - %(message)s'
            formatter = logging.Formatter(fmt)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            
            logger.info(f'Вызов функции: {func.__name__} с аргументами {args} и {kwargs}')
            result = func(*args, **kwargs)
            logger.info(f'Результат: {result}')

            return result

        return wrap_log

    return log


@parametrized_decor_logger(path='multiply_function.log')
def multiply_function(a, b):
    return a * b


if __name__ == "__main__":
    value = multiply_function(2, 3)
