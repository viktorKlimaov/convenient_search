import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def vacancy():
    return Vacancy("Frontend developer",
                   "https://hh.ru/vacancy/101939534", {
                       "from": 5000000,
                       "to": 15000000,
                       "currency": "UZS",
                       "gross": True
                   },
                   "Design, develop, and maintain user interfaces for Odoo applications using JavaScript, OWL (Odoo Web Library), and Vue.js. Ensure the technical...")


def test_cast_to_object_list(vacancy):
    assert Vacancy.cast_to_object_list(vacancy) == {
        "name": "Frontend developer",
        "url": "https://hh.ru/vacancy/101939534",
        "salary_from": 5000000,
        "salary_to": 15000000,
        "description": "Design, develop, and maintain user interfaces for Odoo applications using JavaScript, OWL (Odoo Web Library), and Vue.js. Ensure the technical..."
    }


def test_salary_from(vacancy):
    assert Vacancy.salary_from({
        "from": 5000000,
        "to": 15000000,
        "currency": "UZS",
        "gross": True
    }) == 5000000 or 0




def test_salary_to(vacancy):
    assert Vacancy.salary_to({
        "from": 5000000,
        "to": 15000000,
        "currency": "UZS",
        "gross": True
    }) == 15000000 or 0
