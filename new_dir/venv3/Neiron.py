import numpy as np
import cv2

img = cv2.imread('images/color_text.jpg')
black_bg = np.zeros_like(img, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 30, 30)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
upper_contours = []
middle_contours = []
lower_contours = []

for contour in con:
    x, y, w, h = cv2.boundingRect(contour)
    if y < img.shape[0] / 4.8:
        upper_contours.append(contour)
    elif  y < 2 * img.shape[0] / 4.8:
        middle_contours.append(contour)
    else:
        lower_contours.append(contour)

cv2.drawContours(black_bg, upper_contours, -1, (0, 255, 0), 1)
cv2.drawContours(black_bg, middle_contours, -1, (255, 255, 255), 1)
cv2.drawContours(black_bg, lower_contours, -1, (255, 0, 255), 1)

black_bg_rgb = cv2.cvtColor(black_bg, cv2.COLOR_BGR2RGB)
cv2.imshow( 'Result', black_bg_rgb)
cv2.waitKey(5000)
cv2.destroyAllWindows()
