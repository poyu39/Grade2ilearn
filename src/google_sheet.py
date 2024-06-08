import pygsheets
from pygsheets import Worksheet
from pandas import DataFrame
from config import work_dir

class GoogleSheet:
    def __init__(self):
        self.google_certificate = pygsheets.authorize(service_file=f'{work_dir}/storage/certificate.json')
        
    def open_gs(self, url: str):
        self.google_sheet = self.google_certificate.open_by_url(url)

    def get_grade_df(self, title: str, start: str, end: str):
        grade_wks = self.google_sheet.worksheet_by_title(title)
        grade_wks: Worksheet
        grade_df = grade_wks.get_as_df(start=start, end=end)
        return grade_df
    
    def export_to_csv(self, grade_df: DataFrame):
        grade_df = grade_df.drop('姓名', axis=1)
        self.grade_cols = grade_df.columns
        grade_df.to_csv(f'{work_dir}/storage/grade.csv', index=False)