'''
根据evaluate.py文件，编写脚本完成指定路径下的图片输出检测结果
'''

import os

import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import cv2
from tqdm import tqdm
import crnn.data.data1.txt.dict as dict
from crnn.config import opt
from crnn.models.crnn import CRNN
from crnn.data.dataset import TextDataset, ToTensor, ZeroMean, Rescale, Gray, CharClasses
from crnn.utils import ctc_decode, show_image
import data_set

def detect_image(image_path):
    '''
    :param image_path: ~str 图片路径
    :return: ~None
    读取图片，将图片转换为tensor，输入到模型中，输出预测结果
    '''
    dicts = dict.read_from_txt_k_number(opt.char_dict_file)
    crnn_model = torch.load(opt.load_path)
    crnn_model.eval()  # 记住一定要使用这个
    test_dataset = TextDataset(txt_file=opt.val_filename, root_dir=opt.root_dir,
                               max_label_length=10, transform=transforms.Compose([Rescale((32, 280)), Gray(), ZeroMean(), ToTensor()]))
    test_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    for batch in tqdm(test_dataloader):
        images, labels, label_length = batch['image'], batch['label'], batch['label_length']
        preds = crnn_model(images.to('cuda:0'))
        pred_labels = ctc_decode(preds)
        result = data_set.index2str(pred_labels[0], dicts)
        print(result)

if __name__ == '__main__':
    image_path = 'D:\idea\python\crnn\data\data1\\test\\'
    detect_image(image_path)
    pass

