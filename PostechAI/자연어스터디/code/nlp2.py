import pandas as pd
from bs4 import BeautifulSoup
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
stemmer = nltk.stem.PorterStemmer()

def review_to_words(raw_review):
    #1. HTML 제거
    review_text = BeautifulSoup(raw_review,'html.parser').get_text()
    #2. 영문자가 아닌 문자는 공백으로 변환
    letters_only = re.sub('[^a-zA-Z]',' ',review_text)
    #3. 소문자 변환
    words = letters_only.lower().split()
    #4. 파이썬에서는 리스트보다 세트로 찾는게 훨씬 빠르다.
    # stopwords 를 세트로 변환한다.
    stops = set(stopwords.words('english'))
    # 5. Stopwords 불용어 제거
    meaningful_words = [w for w in words if not w in stops]
    # 6. 어간 추출
    stemming_words = [stemmer.stem(w) for w in meaningful_words]
    # 7. 공백으로 구분된 문자열로 결합하여 결과를 반환
    return( ' '.join(stemming_words))
"""
header =0 은 파일의 첫 번째 줄에 열 이름이 있음을 나타내며
delimiter = \t 는 필드가 탭으로 구분되는 것을 의미한다.
quoting =3 은 쌍따옴표를 무시하도록 한다.
"""
# QUOTE_MINIMAL (0), QUOTE_ALL (1),
# QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).



from multiprocessing import Pool
import numpy as np

def _apply_df(args):
    df, func, kwargs = args
    return df.apply(func, **kwargs)

def apply_by_multiprocessing(df, func, **kwargs):
    #키워드 항목 중 workers 파라미터를 꺼냄
    workers = kwargs.pop('workers')
    # 위에서 가져온 workers 수로 프로세스 풀을 정의
    pool = Pool(processes=workers)
    # 실행할 함수와 데이터프레임을 워커의 수 만큼 나눠 작업
    result = pool.map(_apply_df, [(d, func, kwargs) for d in np.array_split(df, workers)])
    pool.close()
    return pd.concat(list(result))

if __name__ == '__main__':
    #clean_train_reviews = apply_by_multiprocessing(train['review'][0:5], review_to_words, workers=4)
    #print(clean_train_reviews[:10])
    # 레이블인 sentiment 가 있는 학습 데이터
    train = pd.read_csv('../data/labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
    #print(train)
    # 레이블이 없는 테스트 데이터
    test = pd.read_csv('../data/testData.tsv', header=0, delimiter='\t', quoting=3)

    num_reviews = train['review'].size
    #print(num_reviews)
    clean_review = review_to_words(train['review'][0])
    #print(clean_review)
    clean_train_reviews = []

    for i in range(0, 10):
        train['review_clean'] = train['review'].apply(review_to_words)
    print(train['review_clean'])