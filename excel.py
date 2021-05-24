import numpy as np
import pandas as pd

import xlrd
import openpyxl
path = "C:\\Users\\artur.rakhmanov\\Projects\\DBMagic\\try_to_import.xlsx"
workbook = pd.read_excel(path)
workbook.as_matrix()
