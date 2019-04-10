import xml.etree.ElementTree as ET
import os

class ReadXml(object):
	"""docstring for XmlParser"""
	def __init__(self,file_path=os.path.join(os.getcwd(), "sourceData/testcase.xml")):
		self.file_path=file_path
		self.tree=ET.parse(file_path)
		self.root = self.tree.getroot()
	def is_match(self,node,kv_map):
		'''判断节点是否包含属性'''
		for key in kv_map:
			if node.get(key)!=kv_map.get(key):
				return False
		return True
	def find_node_by_pathOrName(self,xpath_or_nodeName):
		'''根据xPath或者节点名字(第一级)获取节点'''
		return self.tree.findall(xpath_or_nodeName)

	def filter_node_by_keyVal(self,nodelist,kv_map):
		'''根据输入的attrMap过滤nodeList'''
		return [node for node in nodelist if self.is_match(node,kv_map)]

	def update_node_attr(self,nodelist,kv_map,delete=False):
		'''修改节点属性'''
		for node in nodelist:
			for key,val in kv_map.items():
				if delete:
					if key in node.attrib: 
						del node.attrib[key] 
				else:
				 	node.set(key,val)

	def update_node_val(self,nodelist,text,append=False,delete=False):
		'''修改节点值'''
		for node in nodelist:
			if append:
				node.text+=text
			elif delete:
				node.text=''
			else:
				print('update---------------',text)
				node.text=text


	def create_element(self,nodelist,tag,attrmap={},text=""):
		'''创建节点'''
		element=ET.Element(tag,attrmap)
		element.text=text
		for node in nodelist:
			node.append(element)

	def delete_node_by_keyval(self,nodelist,tag,kv_map):
		for node in nodelist:
			children=node.getchildren()
			for child in children:
				if child.tag==tag and self.is_match(child,kv_map):
					node.remove(child)

	def write_xml(self,out_path=os.path.join(os.getcwd(), "report/testcase_result.xml")):
		'''写入文件'''
		self.tree.write(out_path,encoding="utf-8",xml_declaration=True)

if __name__ == '__main__':
	xml=ReadXml()

	#根节点  应用
	xml.update_node_attr([xml.root],{"id":"20","name":"视频库"})
	xml.create_element([xml.root],"node_order",text="1")
	xml.create_element([xml.root],"details")
	
	# 模块 子模块
	xml.create_element([xml.root],"testsuite",attrmap={"id":"21","name":"title"})
	testsuite=xml.find_node_by_pathOrName("testsuite")
	xml.create_element(testsuite,"node_order",text="1")
	xml.create_element(testsuite,"details")

	# testcase
	xml.create_element(testsuite,"testcase",attrmap={"internalid":"22","name":"001.图片库应用信息显示正确"})
	testcase=xml.find_node_by_pathOrName("testsuite/testcase")

	xml.create_element(testcase,"node_order",text="0")
	xml.create_element(testcase,"externalid",text="1")
	xml.create_element(testcase,"version",text="1")
	xml.create_element(testcase,"summary")
	xml.create_element(testcase,"preconditions",text="已进入会员中心>内容&页面>图片库")
	xml.create_element(testcase,"execution_type",text="1")
	xml.create_element(testcase,"importance",text="1")
	xml.create_element(testcase,"estimated_exec_duration")
	xml.create_element(testcase,"status",text="1")
	xml.create_element(testcase,"is_open",text="1")
	xml.create_element(testcase,"active",text="1")

	# steps
	xml.create_element(testcase,"steps")
	steps=xml.find_node_by_pathOrName("testsuite/testcase/steps")

	for i in range(2):
		xml.create_element(steps,"step")
		step=xml.find_node_by_pathOrName("testsuite/testcase/steps/step")
		xml.create_element(step,"step_number",text=str(i+1))
		xml.create_element(step,"actions",text="进入图片库应用，查看title信息")
		xml.create_element(step,"expectedresults",text="title正确显示“图片库”")
		xml.create_element(step,"execution_type",text="1")
	
	# 写入
	xml.write_xml()



