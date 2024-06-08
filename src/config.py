import os
import yaml

work_dir = os.path.dirname(os.path.abspath(__file__))

class Config:
    def __init__(self):
        self.config = self.load_config()
        # key to self value
        self.worksheet = dict()
        self.TA = dict()
        
        for key, value in self.config.items():
            setattr(self, key, value)
        
    def load_config(self):
        with open(f'{work_dir}/storage/config.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

CONFIG = Config()