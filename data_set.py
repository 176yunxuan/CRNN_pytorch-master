'''
编写一个脚本，完成字符串和数字索引的转换，安装字典进行转换，比如 abc你 -> 1 2 3 13
'''

import crnn.data.data1.txt.dict as dict
def str2index(s: str, char_dict: dict):
    return [char_dict[char] for char in s]


def index2str(index: list, char_dict: dict):
    return ''.join([char_dict[i] for i in index])


def main():
    char_dict = dict.read_from_txt('crnn/data/data1/txt/chinese.txt')
    file = open('data1.txt', 'w', encoding='utf-8')
    with open('D:\\idea\\python\\crnn\\data\\data1\\test\\test.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n').split(' ')
            label = line[1]
            index = str2index(label, char_dict)
            file.write(line[0]+' '+' '.join([str(i) for i in index])+'\n')

if __name__ == '__main__':
    main()


