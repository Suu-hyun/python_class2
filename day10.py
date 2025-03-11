# yolo 사용(미완성)
# import cv2
# from ultralytics import YOLO
#
# model = YOLO("yolov10n.net")
#
# cap = cv2.VideoCature(0)
#
# while cap.isOpened():
#     success, frame = cap.read()
#     if not success:
#         break
#
#     results = model(frame)
#
#     for r in results:
#     annotated_frame = r.plot()
#====================================================================
# 영어단어장 만들기
import json
import random


def study(level): #함수
    review_list = []


    with open("words.json", "r", encoding="utf-8") as file: # with로 파일을 열고 닫아줌
        word_list = list(json.load(file))
        filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))

        count = 0 # 단어10개까지
        while count < 10:
            select_index = random.randint(0, len(filtered_word_list)) #걸러진 단어갯수 만큼으로 len를 쓰는 것
            print("==========================")
            print(f"{filtered_word_list[select_index]["meaning"]}")

            input_eng = input("단어 : ")
            if input_eng == filtered_word_list[select_index]["word"]:
                print("정답입니다!!!")
            elif input_eng != filtered_word_list[select_index]["word"]:
                print("오답입니다!!!")
                print(f"정답 : {filtered_word_list[select_index]["word"]}")
                review_list.append(filtered_word_list[select_index])

            count += 1

        with open("review_not.json", "w", encoding="utf-8") as review_file:
            json.dump(review_list, review_file, indent=4, ensure_ascii=False)

def review():
    with open("review_not.json", "r", encoding="utf-8") as review_file:
        word_list = list(json.load(review_file))

        incorrect_count = 0
        for word_index in range(0, len(word_list)):
            print("==========================")
            print(f"{word_list[word_index]["meaning"]}")
            input_eng = input("단어 : ")
            if input_eng == word_list[word_index]["word"]:
                print("정답입니다!!")
            elif input_eng != word_list[word_index]["word"]:
                print("오답입니다!!")
                print(f"정답 : {word_list[word_index]["word"]}")
                incorrect_count += 1

        if incorrect_count == 0:
            print("오답노트를 전부 맞췄습니다!!")

while True: #메뉴판
    print("=======메뉴=======")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답노트
        5. 종료
    """)

    choice = input("메뉴를 선택하세요 : ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요.")
        continue