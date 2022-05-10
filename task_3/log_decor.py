import logging


def log(func):
    """
    Логируем какая функция вызывается.
    """

    def wrap_log(*args, **kwargs):
        name_log = func.__name__ + ".log"
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Открываем файл логов для записи.
        fh = logging.FileHandler(name_log, encoding='UTF-8')
        fmt = '%(asctime)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info(f'Путь к лог-файлу: {fh.stream.name}')
        logger.info(f'Вызов функции: {func.__name__} с аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        logger.info(f'Результат: {result}')

        return func

    return wrap_log
