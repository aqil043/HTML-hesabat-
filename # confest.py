# confest.py
import pytest
from pytest_html import extras

def add_table_header(report):
    """
    Bu funksiya HTML hesabatına cədvəl başlığını əlavə edir.
    Əlavə edilən başlıq 'Test Result' olacaq.

    :param report: Test hesabatı
    :return: Yaradılmış başlıq ilə hesabat
    """
    report.extra.append(extras.html("<h3>Test Results</h3>"))
