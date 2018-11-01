#!/user/bin/env python
#!encoding=utf-8
'''封装xml操作方法'''
from xml.etree import ElementTree as ET
from Common import PathTools

class XmlTools:
    '''操作xml文件的公共方法'''

    def _get_rootnode(self):
        '''获取根目录节点'''
        self.xml_file=ET.parse(PathTools.data_path)
        root_node=self.xml_file.getroot()
        return root_node

    def get_node(self,node_path):
        '''定位单个指定节点'''
        root_node=self._get_rootnode()
        return root_node.find(node_path)

    def get_node_text(self, node_path):
        '''获取指定节点的text'''
        get_node=self.get_node(node_path)
        return get_node.text

    def get_node_tag(self,node_path):
        '''获取指定节点的tag'''
        get_node=self.get_node(node_path)
        return get_node.tag

    def get_node_attribute(self,node_path,attribute):
        '''获取指定节点的atrribute'''
        get_node=self.get_node(node_path)
        get_node_attribute=get_node.get(attribute)
        return get_node_attribute

    def get_nodes(self,nodeinfo,node_path=None):
        '''定位多个相同nodeinfo的节点集合'''
        root_node=self._get_rootnode()
        if node_path==None:
            '''没有指定子节点，则获取根目录下的节点集合'''
            get_nodes_list=root_node.findall(nodeinfo)
            return get_nodes_list
        elif node_path!=None:
            '''指定子节点，则获取指定节点路径下的节点集合'''
            set_node=root_node.find(node_path)
            get_nodes_list=set_node.findall(nodeinfo)
            return get_nodes_list

    def get_childs(self,father_nodepath):
        '''获取父节点下面的子节点的集合'''
        child_list=[]
        father_node=self.get_node(father_nodepath)
        for child in father_node:
            child_list.append(child)
        return child_list

    def make_child_data(self,father_nodepath):
        '''将父节点下单个子节点的tag和text获取并生成键值对'''
        set_dict = {}
        father_node=self.get_node(father_nodepath)
        for child in father_node:
            set_dict[child.tag]=child.text
        return set_dict


# if __name__=="__main__":
#     aaa=XmlTools()
#     # print(aaa.get_node_text('Common/email/email_sender'))
#     # print(aaa.get_childs('LoginPage/test1'))
#     bbb=aaa.make_child_data('LoginPage/test1')
#     print(bbb)
