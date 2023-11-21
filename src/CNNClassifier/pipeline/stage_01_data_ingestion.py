from CNNClassifier.components import stage_01_data_ingestion
from CNNClassifier.config import ConfigurationManager
from CNNClassifier import logger

logger.info("data ingestion stage started")

config= ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()

data_ingestion= DataIngestion(config=data_ingestion_config)
data_ingestion.download_file()
data_ingestion.unzip_and_clean()

logger.info("data ingetsion stage completed")