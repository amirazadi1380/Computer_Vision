#تمرین امیر آزادی 
#برنامه ای بنویسید که یک عکس و یک عدد از ورودی گرفته و بر روی تصویر دریافت شده به همان میزان زوم کند
import cv2
import numpy as np

# دریافت مسیر تصویر و میزان زوم از کاربر
image_path = input("مسیر تصویر را وارد کنید: ")
zoom_number = float(input("میزان زوم را وارد کنید: "))

# خواندن تصویر از مسیر داده شده
image = cv2.imread(image_path)

# دریافت ابعاد تصویر
height = image.shape[0]  # ارتفاع تصویر
width = image.shape[1]   # عرض تصویر


# محاسبه ابعاد تصویر جدید بر اساس میزان زوم
new_width = int(width * zoom_number)
new_height = int(height * zoom_number)

# تغییر اندازه تصویر (زوم کردن)
zoomed_image = cv2.resize(image, (new_width, new_height))
x_start = (new_width - width) // 2
y_start = (new_height - height) // 2
new_image = zoomed_image[y_start:y_start + height, x_start:x_start + width]

# نمایش تصویر زوم‌شده
cv2.imshow("تصویر زوم شده", new_image)
cv2.waitKey(0)
