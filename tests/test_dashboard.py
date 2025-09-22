# tests/test_dashboard.py
from pages.dashboard_page import DashboardPage


def test_headers_are_visible(page):
    dashboard = DashboardPage(page)
    expected = [
        "PATIENT", "STUDY ID", "PACKAGE NAME", "PROVISIONAL DIAGNOSIS",
        "DATE OF SCAN", "FILES UPLOADED", "DATE OF UPLOAD", "PROCESS STATUS"
    ]
    headers = dashboard.get_headers()
    for e in expected:
        assert e in headers


def test_patient_and_study_id(page):
    dashboard = DashboardPage(page)
    row = dashboard.get_first_row()
    patient = row.locator("td").nth(0).inner_text()
    study_id = row.locator("td").nth(1).inner_text()

    assert patient.strip() != ""
    assert study_id.isdigit()


def test_process_status_and_download(page):
    dashboard = DashboardPage(page)
    row = dashboard.get_first_row()
    status = dashboard.get_status_text(row)
    download_btn = dashboard.get_download_button(row)

    if "Success" in status:
        assert download_btn.is_enabled()
        with page.expect_download() as download_info:
            download_btn.click()
        download = download_info.value
        download.save_as(f"downloads/{download.suggested_filename}")
    else:
        assert not download_btn.is_enabled()
