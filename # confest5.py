# confest.py
from pytest_html import extras

def pytest_report_teststatus(report, result):
    """
    Testin nəticəsini HTML hesabatına daxil edir. 
    Testin statusunu və təsvirini hesabatda göstərir.

    :param report: Test hesabatı
    :param result: Test nəticəsi
    :return: Test statusunun nəticəsi
    """
    result.append(extras.html(f"<p>Status: {report.outcome}</p>"))
    return result
