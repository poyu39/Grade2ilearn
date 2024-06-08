import time

from google_sheet import GoogleSheet
from ilearn import iLearn
from config import CONFIG


if __name__ == '__main__':
    google_sheet = GoogleSheet()
    google_sheet.open_gs(CONFIG.worksheet['url'])
    grade_df = google_sheet.get_grade_df(CONFIG.worksheet['title'], CONFIG.worksheet['start'], CONFIG.worksheet['end'])
    if grade_df is not None:
        google_sheet.export_to_csv(grade_df)
    
    ilearn = iLearn(**CONFIG.TA)
    ilearn.login()
    ilearn.go_to_grade_import_page(CONFIG.course['import_url'])
    time.sleep(1)
    ilearn.upload_csv()
    time.sleep(1)
    ilearn.map_csv_index(google_sheet.grade_cols)
    ilearn.submit_grade('https://ilearn.fcu.edu.tw/grade/import/csv/index.php')
    time.sleep(5)
    ilearn.driver.quit()