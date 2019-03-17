# coding=utf-8

import sys
sys.path.append("E:/coding/yangqin/pythonAuto")
import string
from util.excel_util import ExcelUtil
from keyword_selenium.action_method import ActionMethod

class KeywordCase:

    def run_main(self):
        self.actionMethod=ActionMethod()
        ex=ExcelUtil(r"E:\coding\yangqin\pythonAuto\config\keyword.xls")
        rows=ex.get_rows()
        if rows>1:
            for i in range(1,rows):
                is_run=ex.get_cell_val(i,3)
                if is_run and is_run.lower()=='yes':
                    method=ex.get_cell_val(i,4)
                    send_data=ex.get_cell_val(i,5)
                    handle_element=ex.get_cell_val(i,6)
                    except_result_method=ex.get_cell_val(i,7)
                    except_result_origin=ex.get_cell_val(i,8)
                    self.run_method(method,send_data,handle_element)
                    if except_result_origin:
                        except_result_tag=self.get_except_val(except_result_origin)[0]
                        except_result=self.get_except_val(except_result_origin)[1]
                        if except_result_tag=="text":
                            actual_result=self.run_method(except_result_method)
                            ex.write_cell(i,"pass") if except_result in actual_result else ex.write_cell(i,'fail')
                        elif except_result_tag=="element":
                            actual_result=self.run_method(except_result_method,except_result)
                            ex.write_cell(i,"pass") if actual_result else ex.write_cell(i,'fail')
                    else:
                        ex.write_cell(i,"pass")

    def get_except_val(self,data):
        return data.split("=")

    def run_method(self,method,send_data='',handle_el=''):
        method_name=getattr(self.actionMethod,method)
        if send_data and handle_el:
            result=method_name(send_data,handle_el)
        elif send_data and not handle_el:
            result=method_name(send_data)
        elif handle_el and not send_data:
            result=method_name(handle_el)
        else:
            result=method_name()
        return result
if __name__ == "__main__":
    KeywordCase().run_main()