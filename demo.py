# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys

# try:
#     a=1/'Satya'
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e, sys) from e


# from us_visa.constants import DATABASE_NAME, COLLECTION_NAME
# print('Database name is:', DATABASE_NAME)
# print('Collection name is:', COLLECTION_NAME)


from us_visa.pipeline.training_pipeline import TrainPipeline
pipeline = TrainPipeline()

pipeline.run_pipeline()