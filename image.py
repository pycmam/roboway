import cv2
import imutils
from lib import transform as tr, grid

source = cv2.imread("samples/sample11.jpg")
source = imutils.resize(source, width=600)
image = tr.auto_transform(source, 5)
rects = grid.find_rects(image)

padding = 7
for idx, r in enumerate(rects):
    new_img= image[r.y + padding:r.y + r.height - padding, r.x + padding:r.x + r.width - padding]
    cv2.rectangle(image, (r.x + padding, r.y + padding), (r.x + r.width - padding, r.y + r.height - padding), (0, 255, 0), 2)
    cv2.imwrite('result/' + str(idx+1) + '.png', new_img)

print(idx+1)
cv2.imshow("Source", source)
cv2.imshow("Image", image)

# cv2.imwrite('result.jpg', image)
# cv2.imshow("Source Image", imutils.resize(source, height = 650))
# cv2.imshow("Final Image", imutils.resize(image, height = 650))
cv2.waitKey(0)
cv2.destroyAllWindows()
