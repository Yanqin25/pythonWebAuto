# coding=utf-8

import xlrd
import os
from xlutils.copy import copy
class ExcelUtil():

    def __init__(self,excel_path=os.path.join(os.getcwd(),"config/casedata.xls"),sheet_index=0):
        self.excel_path=excel_path
        self.sheet_index=sheet_index
        self.workbook=xlrd.open_workbook(excel_path)
        self.sheet=self.workbook.sheet_by_index(sheet_index)

    def get_data(self):
        rows=self.get_rows()
        return [self.sheet.row_values(i) for i in range(1,rows)] if rows>1 else None

    def get_rows(self):
        return self.sheet.nrows
    
    def get_cell_val(self,row,col):
        return self.sheet.cell(row,col).value if row<self.get_rows() else None

    def write_cell(self,row,val):
        workbook=xlrd.open_workbook(self.excel_path)
        write_data=copy(workbook)
        write_data.get_sheet(self.sheet_index).write(row,9,val)
        write_data.save(self.excel_path)

if __name__ == "__main__":
    ex=ExcelUtil(r"E:\coding\yangqin\pythonAuto\config\keyword.xls")
    result=ex.get_cell_val(10,4)
    print(result)
    ex.write_cell(2,'yanngqinqin222')
    ex.write_cell(3,'yanngqinqin333')