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
from mypackage.review.review import review
from mypackage.study.study import study

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