import sys
sys.path.append(r"K:\TEST-DOCUMENT\09.自动化小工具\UIFunctionAuto")
from util.read_xml import ReadXml
from util.read_excel import ExcelUtil
import re



class Excel2Xml:
    def __init__(self, excel_path, index=0, xml_path=None):
        self.excel = ExcelUtil(excel_path, index)
        self.xml = ReadXml(xml_path) if xml_path else ReadXml()
        self.root = [self.xml.root]

    def create_root_el(self, id, name):
        '''修改根节点'''
        self.xml.update_node_attr(self.root, {"id": id, "name": name})
        self.xml.create_element(self.root, "node_order", text="1")
        self.xml.create_element(self.root, "details")

    def create_module_el(self, id, name):
        '''创建模块节点'''
        self.xml.create_element(self.root, "testsuite", attrmap={
                                "id": id, "name": name})
        testsuite = self.xml.find_node_by_pathOrName("testsuite[last()]")
        self.xml.create_element(testsuite, "node_order", text="1")
        self.xml.create_element(testsuite, "details")
        return testsuite

    def create_case_el(self, testsuite, internalid, caseId, caseTitle, precondition, isAuto, importance, status):
        '''创建用例，不包括步骤'''
        self.xml.create_element(testsuite, "testcase", attrmap={
                                "internalid": internalid, "name": caseTitle})
        testcase = self.xml.find_node_by_pathOrName(
            "testsuite[last()]/testcase[last()]")
        self.xml.create_element(testcase, "node_order", text="0")
        # 用例编号
        self.xml.create_element(testcase, "externalid", text=caseId)
        self.xml.create_element(testcase, "version", text="1")
        self.xml.create_element(testcase, "summary")
        self.xml.create_element(testcase, "preconditions", text=self.replace_tag_p(precondition))
        self.xml.create_element(testcase, "execution_type", text=isAuto)
        self.xml.create_element(testcase, "importance", text=importance)
        self.xml.create_element(testcase, "estimated_exec_duration")
        self.xml.create_element(testcase, "status", text=status)
        self.xml.create_element(testcase, "is_open", text="1")
        self.xml.create_element(testcase, "active", text="1")
        return testcase

    def create_case_step(self, testcase, testStep, expectResult):
        '''创建用例步骤'''
        self.xml.create_element(testcase, "steps")
        steps = self.xml.find_node_by_pathOrName(
            "testsuite[last()]/testcase[last()]/steps[last()]")
        if len(expectResult) == 1:
            val = expectResult.get("1")
            expectResult.clear()
            expectResult[str(len(testStep))] = val
        for key in testStep.keys():
            self.xml.create_element(steps, "step")
            step = self.xml.find_node_by_pathOrName(
                "testsuite[last()]/testcase[last()]/steps[last()]/step[last()]")
            self.xml.create_element(step, "step_number", text=key)
            self.xml.create_element(step, "actions", text=testStep.get(key))
            self.xml.create_element(
                step, "expectedresults", text=expectResult.get(key))
            self.xml.create_element(step, "execution_type", text='1')

    def write_xml(self, out_path=None):
        self.xml.write_xml(out_path) if out_path else self.xml.write_xml()

    def replace_tag_p(self,string):
        '''将字符串中的\n替换成P标签，以便在testLink正常显示换行'''
        return re.sub(r'(\S*)\n',r'<p>\1</p>',string)

    def format_case(self, case):
        '''将用例中的自动化，重要性，状态转为xml中对应的数字'''
        isAuto = ["no", "yes"]
        importance = ["低", "中", "高"]
        status = ["草稿", "待评审", "评审中", "重做", "废弃", "Future", "终稿"]
        case[9] = str(isAuto.index(case[9])+1)
        case[7] = str(importance.index(case[7])+1)
        case[8] = str(status.index(case[8])+1)
        return [re.sub('<','&lt;',a) for a in case]

    def get_dict(self, stepDesc):
        '''将操作步骤，预期结果转为字典格式，如{'1': '检查图片库列表视图默认排序', '2': '切换到图示视图，查看排序'} {'1': '均按照添加时间倒序排序（新添加的在后面）'}'''
        stepDesc=stepDesc.strip()
        lines=stepDesc.count("\n")+1
        stepDict = {}
        if lines==1:
            result=stepDesc.split('.')
            stepDict['1'] = result[1] if len(result)>1 else result[0]
        else:
            steps=re.split(r'\n\d+\.',stepDesc)
            for i in range(len(steps)):
                result = steps[i].split('.', 1)
                stepDict[str(i+1)] = result[1] if len(result)>1 else result[0]
        for key,val in stepDict.items():
            stepDict[key]=self.replace_tag_p(val)
        return stepDict

    def get_module(self, index):
        '''得到用例子模块列表，index代表子模块字段在excel中的列数，从0开始'''
        module = []
        for i in range(1, self.excel.get_rows()):
            subModule = self.excel.get_cell_val(i, index)
            if subModule not in module:
                module.append(subModule)
        return module

    def __main__(self, out_path=None):
        '''主方法，输出xml结果文件，out_path指定输出结果路径'''
        application = self.excel.get_cell_val(1, 2)
        id = 10
        print(id)
        self.create_root_el(str(id), application)
        id += 1
        module = self.get_module(3)
        for i in range(len(module)):
            moduleCases = self.excel.get_data_by_colname(module[i], 3, 13)
            testsuit = self.create_module_el(str(id), module[i])
            id += 1
            for j in range(len(moduleCases)):
                case = self.format_case(moduleCases[j])
                testcase = self.create_case_el(testsuit, str(
                    id), case[0], case[1], case[4], case[9], case[7], case[8])
                id += 1
                stepsDict = self.get_dict(case[5])
                expectDict = self.get_dict(case[6])
                self.create_case_step(testcase, stepsDict, expectDict)
        self.write_xml(out_path)


if __name__ == "__main__":
    # ex = Excel2Xml(excel_path=r"K:\测试用例-企业图册-待评审-杨勤test.xlsx", index=1)
    ex=Excel2Xml(excel_path=r"K:\TEST-DOCUMENT\04.测试用例\后台Vue改造\测试用例-企业图册-待评审-杨勤.xlsx",index=1)
    ex.__main__()
