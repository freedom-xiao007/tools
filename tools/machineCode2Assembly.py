"""
机器码转汇编码
python处理二进制文件（.bin):https://blog.csdn.net/and_then111/article/details/86744938
5.4 读写字节数据:https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p04_read_write_binary_data.html
用Python玩玩反汇编:https://zhuanlan.zhihu.com/p/28238335
Compile & install Capstone:http://www.capstone-engine.org/documentation.html
Python tutorial for Capstone:http://www.capstone-engine.org/lang_python.html
"""
import os

from capstone import *

def read_iso_file(file_path):
    res = b""
    size = os.path.getsize(file_path)  # 获得文件大小
    with open(file_path, 'rb') as f:
        for i in range(size):
            data = f.read(1)
            # print(data)
            res += data
    return res

if __name__ == '__main__':
    CODE = read_iso_file('E:\code\other\self\operating-system\myOS.img')
    # CODE = b"\xEB\x63"
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    for i in md.disasm(CODE, 0x1000):
        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
