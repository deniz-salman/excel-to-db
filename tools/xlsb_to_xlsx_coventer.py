

import pandas as pd
from pyxlsb import open_workbook
import openpyxl

def convert_xlsb_to_xlsx(xlsb_path, xlsx_path):
    with open_workbook(xlsb_path) as wb:
        with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
            for sheetname in wb.sheets:
                df = pd.read_excel(xlsb_path, sheet_name=sheetname, engine='pyxlsb')
                df.to_excel(writer, sheet_name=sheetname, index=False)
convert_xlsb_to_xlsx('excel_files/10 - 2023 EK?M -?TH-1-2.xlsb', 'excel_files/10 - 2023 EK?M -?TH-1-2.xlsx')