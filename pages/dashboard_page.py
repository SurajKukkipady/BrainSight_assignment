# pages/dashboard_page.py
class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.table_rows = page.locator("tbody tr")

    def get_headers(self):
        return [h.inner_text() for h in self.page.locator("thead th").all()]

    def get_first_row(self):
        return self.table_rows.first

    def get_status_text(self, row):
        # Assuming 8th column is "PROCESS STATUS"
        return row.locator("td").nth(7).inner_text()

    def get_download_button(self, row):
        return row.get_by_text("Download")
