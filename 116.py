import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
        "Sun",
        (100,100),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (200,200,134)

         )
cv2.putText(img,
        "Mercury",
        (100,175),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (200,200,134)

         )
cv2.putText(img,
        "Venus",
        (200,300),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (200,200,134)

         )
cv2.putText(img,
        "Earth",
        (300,175),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (200,200,134)

         )
cv2.putText(img,
        "Mars",
        (400,201),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (200,200,134)

         )
cv2.putText(img,
        "Jupiter",
        (500,200),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (233,230,134)

         )
cv2.putText(img,
        "Saturn",
        (700,200),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (233,230,134)

         )
cv2.putText(img,
        "Uranus",
        (1000,150),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (233,230,134)

         )
cv2.putText(img,
        "Neptune",
        (1100,150),
        cv2.FONT_HERSHEY_COMPLEX,
        0.5,
        (233,230,134)

         )


cv2.imshow("Output",img)
cv2.waitKey(0)