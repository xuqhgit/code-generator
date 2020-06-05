import requests
import json
import base64
import zipfile


def get_data():
    res = requests.get("http://yun.gogohou.top:8091/shares/b")
    data = json.loads(res.text)
    data_str = base64.b64decode(data['data'])
    s_list = json.loads(data_str)
    for i in s_list:
        print("%s %s %s %s %s " % (i["p"],i["l"],i['h'],i['k'],i['z']))

class MZipFile(object):
    '''
    python zipfile 模块处理压缩文件并读取包里面的每个文件内容(行)
    '''

    def __init__(self, zip_path):
        '''
        :param zip_path: zip文件路径
        '''
        self.zip = zipfile.ZipFile(zip_path, 'r')  # 创建一个zipfile

    def get_filecount(self):
        '''
        :return: 返回压缩包里面的文件个数
        '''
        return len(self.zip.namelist())

    def get_one_file(self):
        '''
        :return: 创建一个generator ,每次返回一个文件的内容
        '''
        for name in self.zip.namelist():
            yield self.read_lines(name)  # 生成器

    def read_lines(self, name):
        '''
        :param name: 文件名
        :return: 整个文件所有行(列表:每一行作为一个元素)
        '''
        for line in self.zip.open(name).readlines():
            print(line)
        # return [line.decode() for line in self.zip.open(name).readlines()]

    def get_filenames(self):
        '''
        :return:  返回自拍zip文件里面的所有文件名(列表:每个文件名作为一个元素)
        '''
        return self.zip.namelist()

    def extract_to(self, path):
        '''
        解压zip 文件
        :param path: 解压路径
        '''
        self.zip.extractall(path)
        return path





'''
Examples
'''
if __name__ == "__main__":
    get_data()
    # zip = MZipFile(zip_path="/Users/apple/anchor/workplace/py_workplace/code-generator/gcode/web/static/workspace/00001/zip/sf_pass$20200529115119.zip")
    # print("文件个数:", zip.get_filecount())
    # print("文件名列表:", zip.zip.namelist())
    # print("各个文件内容:", str(list(zip.get_one_file())))
    # print("解压的路径:", zip.extract_to("./test"))

