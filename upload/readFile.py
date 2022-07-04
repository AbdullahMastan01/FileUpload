import pandas as pd
from .models import CSVfile_data
import csv

data_list = []

def process(file_name):
	base_dir = 'D:/Abdullah/Python/FileUpload/src/media/'
	with open(base_dir+file_name) as file:
		read			 = pd.read_csv(file)
		rm_duplicates	 = read.drop_duplicates(['sku'])

		for i,row in rm_duplicates.iterrows():
			tuple(row)
			(name,sku,description) = row
			data_list.append(
				CSVfile_data(name=name,sku=sku,description=description,)
		 		)
		CSVfile_data.objects.bulk_create(data_list)



		


