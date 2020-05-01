import cv2
from lib import rect


def find_rects(image, min_ratio=0.5, max_ratio=1.7, min_width=50, max_width=150):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.adaptiveThreshold(image, 255, 1, 1, 11, 2)
    contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    rects = []
    for c in contours:
        x, y, width, height = cv2.boundingRect(c)
        ratio = abs(width / height)
        if (min_ratio < ratio < max_ratio) and (min_width < width < max_width):
            rects.append(rect.Rect(x, y, width, height))

    rects = sorted(rects)

    result = []
    for r1 in rects:
        include = False
        for idx, r2 in enumerate(rects):
            if r2.include(r1):
                include = True
                break
        if not include:
            result.append(r1)

    return result
