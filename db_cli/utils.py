import random
from datetime import datetime, timedelta

from faker import Faker


def gerar_data_random(start: str = "2021-01-01 00:00:00",
                      end: str = "2022-02-28 23:59:59",
                      fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    start = datetime.strptime(start, fmt)
    end = datetime.strptime(end, fmt)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds

    random_second = random.randrange(int_delta)

    return start + timedelta(seconds=random_second)


def gerar_data():
    return Faker("pt_BR").date_time_between(start_date="-2y").strftime("%Y-%m-%d %H:%M:%S")


def gerar_nome_client() -> str:
    return Faker("pt_BR").name()


def gerar_endereco() -> str:
    return Faker("pt_BR").address()


def gerar_cidade() -> str:
    return Faker("pt_BR").city()


def gerar_estado_sigla() -> str:
    return Faker("pt_BR").estado_sigla()
