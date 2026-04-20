import os
from pathlib import Path
import json
file_path = Path(__file__).parent/'a_new_file.txt'
file_name = Path(__file__).parent/'a_new_json.json'
file_xml  = Path(__file__).parent/'a_new_xml.xml'
with open(file_path,'+a') as f :
    f.write("第一行\n")   # 内容追加到末尾
    f.seek(0)            # 手动将指针移到开头才能读取已有内容
    content = f.read() 
print(content)
with open(file_name,'r',encoding="utf-8-sig")as fjson:
    json_data = json.load(fjson)
    print(json_data)
import xml.etree.ElementTree as ET
tree = ET.parse(file_xml)
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('字段: ', child.tag)
def coun_words (filename) :
    if not os.path.exists(filename):
        return -1
    try:
        with open(filename,'r',encoding='utf-8')as f:
            text = f.read()
            words = text.split()
            return len(words)
    except Exception as e:
        print(f'读取文件发生错误{e}')
        return -1

