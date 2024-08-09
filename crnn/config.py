from pprint import pprint
class Config:
    # data

    # 300w
    train_filename = '/crnn/data/data1\\train.txt'
    val_filename = '/crnn/data/data1\\test1.txt'
    root_dir = 'D:\\idea\\python\\crnn\\data\\data1\\images\\'
    # part 300w
    # train_filename = '/home/liumihan/Desktop/OCR/CRNN/data/data1/txt/train.txt'
    # val_filename = '/home/liumihan/Desktop/OCR/CRNN/data/data1/txt/test.txt'
    # root_dir = '/home/liumihan/Desktop/OCR/CRNN/data/data1/img'

    # char_dict_file = 'D:\\idea\\python\\crnn\\data\\data1\\chinese.txt'
    char_dict_file = '/crnn/data/data1\\txt\chinese.txt'
    image_size = (32, 280)
    max_label_length = 7

    # cuda
    device = 'cuda:0'

    # network
    nclasses = 66

    # training
    epoch = 50

    # model
    # load_path = "./crnn/trained_weights/2.pt"
    # trained_weights = './crnn/trained_weights/0.pt'
    load_path = './crnn/trained_weights/epoch_49_epoch_loss0.00486.pt'
    trained_weights = './crnn/trained_weights/epoch_9_epoch_loss0.50449.pt'
    def _parse(self, kwargs):
        state_dict = self._state_dict()
        for k, v in kwargs.items():
            if k not in state_dict:
                raise ValueError('Unknow Option: "--%s"' % k)
            setattr(self, k, v)
        print('**********************************user config*************************')
        pprint(self._state_dict())
        print('*************************************end******************************')

    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in Config.__dict__.items() if not k.startswith('_')}

opt = Config()
