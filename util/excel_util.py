# coding=utf-8

import xlrd
import os
from xlutils.copy import copy
class ExcelUtil():

    def __init__(self, excel_path=os.path.join(os.getcwd(), "sourceData/registerCase.xls"), sheet_index=0):
        self.excel_path = excel_path
        self.sheet_index = sheet_index
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_index(sheet_index)

    # 获取需要执行的用例
    def get_data(self):
        rows = self.get_rows()
        return [self.sheet.row_values(i)[:-1] for i in range(1, rows) if self.get_cell_val(i, -1).lower() == 'yes'] if rows > 1 else None

    def get_rows(self):
        return self.sheet.nrows

    def get_cell_val(self, row, col):
        return self.sheet.cell(row, col).value if row < self.get_rows() else None

    def write_cell(self, row, col, val):
        workbook = xlrd.open_workbook(self.excel_path)
        write_data = copy(workbook)
        write_data.get_sheet(self.sheet_index).write(row, col, val)
        write_data.save(self.excel_path)


class ExcelUtilXls():

    def __init__(self, file_path, index=0):
        self.file_path = file_path
        self.wb = load_workbook(self.file_path)
        self.ws = self.__get_sheet(index)

    # 获取sheet页
    def __get_sheet(self, index):
        sheet_name = self.wb.get_sheet_names()[index]
        return self.wb.get_sheet_by_name(sheet_name)
    # 获取行数

    def get_rows(self):
        return self.ws.max_row
    # 获取单元格值

    def get_cell_val(self, row, col):
        return self.ws.cell(row=row, column=col).value

    # 写入单元格值
    def write_cell(self, row, col, val):
        self.ws.cell(row=row, column=col).value = val

    # 写完后再同一保存，节省时间
    def save_file(self):
        self.wb.save(self.file_path)

    # 最后写入一行值
    def write_last_lines(self, listVal):
        self.ws.append(listVal)
        self.wb.save(self.file_path)


if __name__ == "__main__":
    # 统一用例编号，仅支持xls格式
    # ex=ExcelUtil(r"K:\测试用例-企业图册-待评审-杨勤.xlsx",1)
    # for i in range(1,ex.get_rows()):
    #     sourceVal=ex.get_cell_val(i,1)
    #     index=sourceVal.find('.')
    #     num=ex.get_cell_val(i,0)[-3:]
    #     if num!=sourceVal[:index]:
    #         val=num+'.'+sourceVal[index+1:]
    #         ex.write_cell(i,1,val)

    # 写入xlsx
    ex = ExcelUtilXls(r"K:\TEST-DOCUMENT\04.测试用例\后台Vue改造\测试用例-企业图册-待评审-杨勤.xlsx", 1)

    for i in range(2, ex.get_rows()+1):
        sourceVal = ex.get_cell_val(i, 2)
        index = sourceVal.find('.')
        num = ex.get_cell_val(i, 1)[-3:]
        if num != sourceVal[:index]:
            val = num+'.'+sourceVal[index+1:]
            ex.write_cell(i, 2, val)
    ex.save_file()