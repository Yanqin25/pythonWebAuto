# coding=utf-8

import xlrd
import os
class ExcelUtil():

    def __init__(self,excel_path=os.path.join(os.getcwd(),"config/casedata.xls"),sheet_index=0):
        self.workbook=xlrd.open_workbook(excel_path)
        self.sheet=self.workbook.sheet_by_index(sheet_index)
        self.rows=self.sheet.nrows

    def get_data(self):
        return [self.sheet.row_values(i) for i in range(1,self.rows)]

if __name__ == "__main__":
    ex=ExcelUtil()
    result=ex.get_data()
    print(result)