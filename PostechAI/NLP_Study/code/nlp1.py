from bs4 import BeautifulSoup
import pandas as pd

"""
header =0 은 파일의 첫 번째 줄에 열 이름이 있음을 나타내며
delimiter = \t 는 필드가 탭으로 구분되는 것을 의미한다.
quoting =3 은 쌍따옴표를 무시하도록 한다.
"""
# QUOTE_MINIMAL (0), QUOTE_ALL (1),
# QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).

# 레이블인 sentiment 가 있는 학습 데이터
train = pd.read_csv('../data/labeledTrainData.tsv',header=0,delimiter='\t',quoting=3)

# 레이블이 없는 테스트 데이터
test = pd.read_csv('../data/testData.tsv',header=0,delimiter='\t',quoting=3)
example1 = BeautifulSoup(train['review'][0],"html5lib")
print(example1.get_text())