from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from config import work_dir

class iLearn:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://ilearn.fcu.edu.tw/login/index.php')
        self.driver.find_element(By.ID, 'username').send_keys(self.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginbtn').click()
    
    def go_to_grade_import_page(self, url):
        self.driver.get(url)
    
    def upload_csv(self):
        self.driver.find_element(By.NAME, 'userfilechoose').click()
        time.sleep(0.5)
        self.driver.find_element(By.NAME, 'repo_upload_file').send_keys(f'{work_dir}/storage/grade.csv')
        self.driver.find_element(By.CLASS_NAME, 'fp-upload-btn').click()
        Select(self.driver.find_element(By.ID, 'id_previewrows')).select_by_value('100')
        self.driver.find_element(By.ID, 'id_submitbutton').click()
    
    def map_csv_index(self, grade_cols):
        Select(self.driver.find_element(By.ID, 'id_mapto')).select_by_value('useridnumber')
        mapping_index = 1
        for cols in grade_cols[1:]:
            Select(self.driver.find_element(By.ID, f'id_mapping_{mapping_index}')).select_by_visible_text(cols)
            mapping_index += 1
            time.sleep(0.1)
    
    def submit_grade(self, url):
        self.driver.find_element(By.ID, 'id_submitbutton').click()
        while (self.driver.current_url != url):
            time.sleep(0.5)