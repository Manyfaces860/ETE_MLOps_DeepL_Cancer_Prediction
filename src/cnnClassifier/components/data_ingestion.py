import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.utils.common import create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        try:
            dataset_url = self.config.source_URL
            zip_download_name = self.config.local_data_file
            
            create_directories([self.config.root_dir])
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_name}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_name)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_name}")
            
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        
        unzip_path = self.config.unzip_dir
        create_directories([unzip_path])
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
            