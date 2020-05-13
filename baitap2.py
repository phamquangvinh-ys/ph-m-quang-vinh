import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import numpy
df = pandas.read_csv("C:/dshs.csv")


d = {'a': 0, 'b': 1, 'c': 2,'d': 3}
df['TTHN'] = df['TTHN'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['NN ME'] = df['NN ME'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['NN BO'] = df['NN BO'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['TRUONG THCS'] = df['TRUONG THCS'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['LY DO CHON TRUONG'] = df['LY DO CHON TRUONG'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['NGUOI QT  HT'] = df['NGUOI QT  HT'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['DH TL'] = df['DH TL'].map(d)
d = {'a': 0, 'b': 1, 'c': 2,'d': 3,'e': 4,'g': 5}
df['CT TI VI'] = df['CT TI VI'].map(d)
d = {'TB': 0, 'K': 1, 'G': 2}
df['Class'] = df['Class'].map(d)
print(df)

xeploai = ['TS-VAN','TS-TO HOP','TS-TOAN','M','15P','V1']
X_testing = df[xeploai]
y_testing = df['Class']
print(X_testing)
print(y_testing)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_testing, y_testing)
print ("phân loại")
#print(clf.predict([[6.25,7.25,7.5,2,6,7.8]]))
#print(clf.predict([[6.5,7.25,7.25,9,6,7.3]]))
print(clf.predict([[8,8,8,8,8,7]]))

#y dự báo
y_dubao= clf.predict(X_testing)
#y thực tế
y_thucte = numpy.array(y_testing)
#ma trận nhầm lẫn
from sklearn.metrics import accuracy_score
print('accuracy = ',accuracy_score(y_thucte, y_dubao))
from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(y_thucte, y_dubao)
print('Ma trận nhầm lẫn:')
print(cnf_matrix)
normalized_confusion_matrix = cnf_matrix/cnf_matrix.sum(axis = 1, keepdims = True)
print('\nMa trận nhầm lẫn chuẩn hóa:')
print(normalized_confusion_matrix)

