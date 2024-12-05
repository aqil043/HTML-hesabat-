# confest.py
import pytest
from pytest_html import extras

def add_test_description(report, item):
    """
    Bu funksiya testin təsvirini HTML hesabatına əlavə edir.
    Testin təsviri testin 'item' obyektindən əldə edilir və nəticəyə əlavə olunur.

    :param report: Test hesabatı
    :param item: Test obyekti
    :return: Test təsviri ilə hesabat
    """
    description = item.nodeid
    report.extra.append(extras.html(f"<p>Description: {description}</p>"))
