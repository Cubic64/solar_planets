import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
            
cv2.putText(img,
            "Mercury",
            (115,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (295,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (380,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (480,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (780,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (970,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1120,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("Output",img)
cv2.waitKey(0)