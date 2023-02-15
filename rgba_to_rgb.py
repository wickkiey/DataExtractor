# Convert RGBA images to RGB

import cv2
import os 

src_path = r"D:\data\cartoonset10k"
dst_path = "D:\data\cartoonset10k_rgb"

images = os.listdir(src_path)
images = [i for i in images if i.endswith(".png")]

# convert to RGB and save to file

for image in images:
    img = cv2.imread(os.path.join(src_path, image), cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    image = image.replace(".png", ".jpg")
    cv2.imwrite(os.path.join(dst_path, image), img)