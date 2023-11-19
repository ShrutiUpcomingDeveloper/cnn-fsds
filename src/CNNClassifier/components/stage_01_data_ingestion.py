import os
import urllib.request as request
from zipfile import ZipFile
from CNNClassifier import logger
from pathlib import Path
from tqdm import tqdm
from CNNClassifier.entity import DataIngestionconfig
from CNNClassifier.utils import utils



class DataIngestion:
     def __init__(self,config:DataIngestionConfig):
          pass
     def  downlaod_file(self):
          pass
     def get_updated_list_of_files(self):
          pass
     def preprocess(self):
          pass
     def unzip_and_clean(self):
          pass