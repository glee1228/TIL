import os
import tensorflow as tf
import numpy as np

from tensorflow.keras import preprocessing

samples = ['너 오늘 이뻐보인다',
          '나는 오늘 기분이 더러워',
          '끝내주는데, 좋은 일이 있나봐',
          '나 좋은 일이 생겼어',
          '환상적인데, 정말 좋은 것 같아']
label = [[1],[0],[1],[1],[0],[1]]

tokenizer = preprocessing.text.Tokenizer() # 객체 생성
tokenizer.fit_on_texts(samples) # 데이터 담기
sequences = tokenizer.texts_to_sequences(samples) # 숫자로 바뀐 데이터
word_index = tokenizer.word_index # 시퀀스 (딕셔너리) 생성 : 사전이 될 매핑이 된 딕셔너리

print('수치화된 텍스트 데이터 : \n',sequences)
print('각 단어의 인덱스 : \n',word_index)
print('라벨 :',label)