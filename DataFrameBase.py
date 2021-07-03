import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime, timedelta


class DataFrameBase:
    def __init__(self,path,sheet,columns):
        self.path = path
        self.sheet = sheet
        self.columns = columns          
        self.loadExcel()
        
    def loadExcel(self):        
        try:          
          self.data = pd.read_excel(self.path,sheet_name=self.sheet)           
          #self.data = self.data[self.columns]
          print(self.data)
        except Exception as e:
          print("No se pudo Cargar el Archivo", e)
        
        
        
             
