import json
from typing import Any
from abc import ABC, abstractmethod
from src.hh_api import Vacancy
import os


class AbstractJson(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def reed_vacancy(self, *args):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JSONSaver(AbstractJson):
    """
     Класс для сохранения вакансий в JSON-файл и получения вакансий из JSON-файл
    """

    def __init__(self, file_name='data/vacancies.json'):
        self.__path = os.path.abspath(file_name)

    # Функция для сохранения, вакансий в JSON-файл
    def add_vacancy(self, vacancies: list[Vacancy]):
        with open(self.__path, 'r', encoding='utf-8') as file:
            try:
                data: list[dict[str, Any]] = json.load(file)
            except json.JSONDecodeError:
                data = []

                # добавление вакансии в список
                for vacancy in vacancies:
                    data.append(vacancy.cast_to_object_list())

        # добавление список вакансий в JSON-файл
        with open(self.__path, 'w', encoding='utf-8') as file:
            return json.dump(data, file, indent=4, ensure_ascii=False)

    # Функция для получения вакансий по критериям пользователя
    def reed_vacancy(self) -> list:
        with open(self.__path, 'r', encoding='utf-8') as file:
            vacancy_list = json.load(file)
        return vacancy_list

    # Функция для удаления вакансии
    def del_vacancy(self):
        with open(self.__path, 'w', encoding='utf-8') as file:
            pass
