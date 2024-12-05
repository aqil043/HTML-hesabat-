# confest.py
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    """
    Bu hook test nəticələri cədvəlinin başlığını əldə etməyə kömək edir.
    Cədvəl başlığını "Test Name", "Status" və "Duration" ilə genişləndirir.

    :param cells: Test nəticələrinin başlıq hüceyrələri
    :return: Genişləndirilmiş başlıq hüceyrələri
    """
    cells.insert(1, html.th('Test Name'))
    cells.insert(2, html.th('Status'))
    cells.insert(3, html.th('Duration'))
    return cells
