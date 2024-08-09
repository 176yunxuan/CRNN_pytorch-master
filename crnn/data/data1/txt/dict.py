'''
将chinese.txt文件中的字符，按照行号写入字典中，比如：’blank‘：‘1’，’0‘：’1‘.。。。。。
'''
def read_from_txt(txt_file):
    with open(txt_file, 'r',encoding='utf-8') as f:
        i = 1
        frame = {}
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n').split(' ')[0]
            frame[line] = i
            i += 1
        return frame

def read_from_txt_k_number(txt_file):
    with open(txt_file, 'r',encoding='utf-8') as f:
        i = 1
        frame = {}
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n').split(' ')[0]
            frame[i] = line
            i += 1
        return frame

