# confest.py
import pytest
from pytest_html import extras
import time

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    """
    Test nəticələrinin cədvəlində hər bir testin adı, statusu və müddəti ilə bağlı sütunlar əlavə edir.

    :param report: Test hesabatı
    :param cells: Test nəticələrinin hüceyrələri
    :return: Yaradılmış cədvəl sırası
    """
    cells.insert(1, html.td(report.nodeid))
    cells.insert(2, html.td(report.outcome))
    cells.insert(3, html.td(str(report.duration)))
    return cells
