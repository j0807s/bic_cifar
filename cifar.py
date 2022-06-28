import pickle
import numpy as np
import os

class Cifar100:
    def __init__(self):
        with open('cifar100/train','rb') as f:
            self.train = pickle.load(f, encoding='latin1')
        with open('cifar100/test','rb') as f:
            self.test = pickle.load(f, encoding='latin1')
        self.train_data = self.train['data']
        self.train_labels = self.train['fine_labels']
        self.test_data = self.test['data']
        self.test_labels = self.test['fine_labels']
        self.train_groups, self.val_groups, self.test_groups = self.initialize()
        self.batch_num = 5

    def initialize(self):
        train_groups = [[],[],[],[],[],[],[],[],[],[], [],[],[],[],[],[],[],[],[],[]]
        for train_data, train_label in zip(self.train_data, self.train_labels):
            # print(train_data.shape)
            train_data_r = train_data[:1024].reshape(32, 32)
            train_data_g = train_data[1024:2048].reshape(32, 32)
            train_data_b = train_data[2048:].reshape(32, 32)
            train_data = np.dstack((train_data_r, train_data_g, train_data_b))
            if train_label < 5:
                train_groups[0].append((train_data,train_label))
            elif 5 <= train_label < 10:
                train_groups[1].append((train_data,train_label))
            elif 10 <= train_label < 15:
                train_groups[2].append((train_data,train_label))
            elif 15 <= train_label < 20:
                train_groups[3].append((train_data,train_label))
            elif 20 <= train_label < 25:
                train_groups[4].append((train_data,train_label))
            elif 25 <= train_label < 30:
                train_groups[5].append((train_data,train_label))
            elif 30 <= train_label < 35:
                train_groups[6].append((train_data,train_label))
            elif 35 <= train_label < 40:
                train_groups[7].append((train_data,train_label))
            elif 40 <= train_label < 45:
                train_groups[8].append((train_data,train_label))
            elif 45 <= train_label < 50:
                train_groups[9].append((train_data,train_label))
            elif 50 <= train_label < 55:
                train_groups[10].append((train_data,train_label))
            elif 55 <= train_label < 60:
                train_groups[11].append((train_data,train_label))
            elif 60 <= train_label < 65:
                train_groups[12].append((train_data,train_label))
            elif 65 <= train_label < 70:
                train_groups[13].append((train_data,train_label))
            elif 70 <= train_label < 75:
                train_groups[14].append((train_data,train_label))
            elif 75 <= train_label < 80:
                train_groups[15].append((train_data,train_label))
            elif 80 <= train_label < 85:
                train_groups[16].append((train_data,train_label))
            elif 85 <= train_label < 90:
                train_groups[17].append((train_data,train_label))
            elif 90 <= train_label < 95:
                train_groups[18].append((train_data,train_label))
            elif 95 <= train_label < 100:
                train_groups[19].append((train_data,train_label))
        assert len(train_groups[0]) == 2500, len(train_groups[0])
        assert len(train_groups[1]) == 2500, len(train_groups[1])
        assert len(train_groups[2]) == 2500, len(train_groups[2])
        assert len(train_groups[3]) == 2500, len(train_groups[3])
        assert len(train_groups[4]) == 2500, len(train_groups[4])

        val_groups = [[],[],[],[],[],[],[],[],[],[], [],[],[],[],[],[],[],[],[],[]]
        for i, train_group in enumerate(train_groups):
            val_groups[i] = train_groups[i][2250:]
            train_groups[i] = train_groups[i][:2250]
        assert len(train_groups[0]) == 2250
        assert len(train_groups[1]) == 2250
        assert len(train_groups[2]) == 2250
        assert len(train_groups[3]) == 2250
        assert len(train_groups[4]) == 2250
        assert len(val_groups[0]) == 250
        assert len(val_groups[1]) == 250
        assert len(val_groups[2]) == 250
        assert len(val_groups[3]) == 250
        assert len(val_groups[4]) == 250

        test_groups = [[],[],[],[],[],[],[],[],[],[], [],[],[],[],[],[],[],[],[],[]]
        for test_data, test_label in zip(self.test_data, self.test_labels):
            test_data_r = test_data[:1024].reshape(32, 32)
            test_data_g = test_data[1024:2048].reshape(32, 32)
            test_data_b = test_data[2048:].reshape(32, 32)
            test_data = np.dstack((test_data_r, test_data_g, test_data_b))
            if test_label < 5:
                test_groups[0].append((test_data,test_label))
            elif 5 <= test_label < 10:
                test_groups[1].append((test_data,test_label))
            elif 10 <= test_label < 15:
                test_groups[2].append((test_data,test_label))
            elif 15 <= test_label < 20:
                test_groups[3].append((test_data,test_label))
            elif 20 <= test_label < 25:
                test_groups[4].append((test_data,test_label))
            elif 25 <= test_label < 30:
                test_groups[5].append((test_data,test_label))
            elif 30 <= test_label < 35:
                test_groups[6].append((test_data,test_label))
            elif 35 <= test_label < 40:
                test_groups[7].append((test_data,test_label))
            elif 40 <= test_label < 45:
                test_groups[8].append((test_data,test_label))
            elif 45 <= test_label < 50:
                test_groups[9].append((test_data,test_label))
            elif 50 <= test_label < 55:
                test_groups[10].append((test_data,test_label))
            elif 55 <= test_label < 60:
                test_groups[11].append((test_data,test_label))
            elif 60 <= test_label < 65:
                test_groups[12].append((test_data,test_label))
            elif 65 <= test_label < 70:
                test_groups[13].append((test_data,test_label))
            elif 70 <= test_label < 75:
                test_groups[14].append((test_data,test_label))
            elif 75 <= test_label < 80:
                test_groups[15].append((test_data,test_label))
            elif 80 <= test_label < 85:
                test_groups[16].append((test_data,test_label))
            elif 85 <= test_label < 90:
                test_groups[17].append((test_data,test_label))
            elif 90 <= test_label < 95:
                test_groups[18].append((test_data,test_label))
            elif 95 <= test_label < 100:
                test_groups[19].append((test_data,test_label))



        assert len(test_groups[0]) == 500
        assert len(test_groups[1]) == 500
        assert len(test_groups[2]) == 500
        assert len(test_groups[3]) == 500
        assert len(test_groups[4]) == 500

        return train_groups, val_groups, test_groups

    def getNextClasses(self, i):
        return self.train_groups[i], self.val_groups[i], self.test_groups[i]

if __name__ == "__main__":
    cifar = Cifar100()

    for i in range(20):
        print("train group samples : ", len(cifar.train_groups[i]))
        print("val group samples : ", len(cifar.val_groups[i]))
        print("test group samples : ", len(cifar.test_groups[i]))
    print(len(cifar.train_groups[9]))
    print(len(cifar.val_groups[9]))
    print(len(cifar.test_groups[9]))
