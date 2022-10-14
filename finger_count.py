import cv2
import HandTrackingModule as htm
import jarvis
import time


def main():
    global lmList
    totalFingers = 0
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)


    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]

    temp_finger_count = []
    t_end = time.time() + 8
    while time.time() < t_end:
    # while True:
        success, img1 = cap.read()
        img = cv2.flip(img1,1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)

        if len(lmList) != 0:
            fingers = []
            if lmList[8][2] < lmList[6][2]:
                # print("Index Finger")
                fingers.append(1)
            else:
                fingers.append(0)
            if lmList[12][2] < lmList[10][2]:
                # print("Middle Finger")
                fingers.append(1)
            else:
                fingers.append(0)
            if lmList[16][2] < lmList[14][2]:
                # print("Ring Finger")
                fingers.append(1)
            else:
                fingers.append(0)
            if lmList[20][2] < lmList[18][2]:
                # print("pinky Finger")
                fingers.append(1)
            else:
                fingers.append(0)
            if lmList[17][1] > lmList[4][1]:
                # print('sidha')
                if lmList[4][1] < lmList[3][1]:
                    # print("Thumb Finger")
                    # print(lmList[4])
                    # print(lmList[3])
                    fingers.append(1)
                else:
                    # print(lmList[4])
                    # print(lmList[3])
                    fingers.append(0)
            if lmList[17][1] < lmList[4][1]:
                # print("ulta")
                if lmList[4][1] > lmList[3][1]:
                    # print("Thumb Finger")
                    # print(lmList[4])
                    # print(lmList[3])
                    fingers.append(1)
                else:
                    # print(lmList[4])
                    # print(lmList[3])
                    fingers.append(0)


            # print(fingers)


            # print("lmList[tipIds[id]]",lmList[tipIds[id]])
            totalFingers = fingers.count(1)
            print(totalFingers)
            temp_finger_count.append(totalFingers)




            # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 255), 10)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    return (lmList,temp_finger_count)



if __name__ == "__main__":
    main()