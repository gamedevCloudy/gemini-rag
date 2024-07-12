import google.generativeai as genai

from Unstructured_dls import UnstructuredDataLoader
from split_segments import split_into_segments

loader = UnstructuredDataLoader()

external_database = loader.get_data(folder_name='data')

embedded_data = None

for i in range(0,5): 
    file_path = "out{i}.txt"
    with open(file_path, "r") as file:
        external_data = file.readlines()
        