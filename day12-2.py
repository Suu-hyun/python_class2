# import requests
#
# response = requests.get("https://www.naver.com/")
# print(response.status_code)
# print(response.text)

import pandas as pd

# df = pd.read_csv("data.csv") # df는 변수 이름 datefile 준말로 만든 변수 다른거 써도 됨
# print(df)
# print(df.describe()) # 데이터 요약 분석

# """
# count - 해당 열의 데이터 갯수
# mean - 평균값
# std - 표준 편차 (데이터의 분산 정도)
# min - 최솟값
# 25% - 데이터의 25% 지정
# 50% - "
# 75% - "
# max - 최댓값
# """

# print(df["Age"])
# print(df[["Age", "Salary"]])

import matplotlib.pyplot as plt

# df.groupby("Age")["Salary"].mean().plot(kind="bar")
# plt.show()


import numpy as np

# arr1 = np.array([1,2,3,4,5]) # 일차원 배열
# print(arr1) # 리스트 아님, numpy에서 지원하는 배열
#
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

# 0으로 채운 다차원 배열
# zeros = np.zeros((3, 4)) # 3행 4열
# print(zeros)

# ones = np.ones((3, 4))
# print(ones)


# 특정한 값으로 채운 다차원 배열
# filled = np.full((3, 4), 5) # 3행 4열, 숫자 5로 채우겠다. 라는 의미
# print(filled)

# 연속된 값으로 채운 일차원 배열
# arr = np.arange(1, 10, 2)
# print(arr)

# random_arr = np.random.randint(1, 45, (6, 5))
# print(random_arr)

# arr1 = np.array([1,3,5])
# arr2 = np.array([2,5,8])
#
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)

import seaborn as sns

# df = pd.read_csv("tips.csv")
# plt.figure(figsize=(8,5))
# sns.scatterplot(x="total_bill", y= "tip", hue="sex", data=df, palette= "Set2")
# plt.xlabel("Total Bill ($)")
# plt.ylabel("Tip ($)")
# plt.show()