#تمرین امیر آزادی 
#شیب خط بین دو نقطه را پیدا کرده و بر اساس شیب خط به دست آمده طیف رنگی یا گرادیان آن محسابه و نمایش داده شود 
import cv2
import numpy as np

# تعریف دو نقطه دلخواه 
x1 = 50; y1 = 50;
x2 = 200; y2 = 150;

# محاسبه شیب
#فرمول شیب خط برابر است با تغییرات عمودی تقسیم بر تغییات افقی بین دو نقطه 
m = (y2 - y1) / (x2 - x1);

# تعریف ابعاد تصویر و انتخاب عدد 256 در جهت استفاده از طیف رنگی 0 تا 255
width = 256;
height = 256;
n_channels = 3;

# ایجاد یک تصویر خالی مشکی
image = np.zeros(shape=(height, width, n_channels), dtype=np.uint8);

#  ایجاد تصویر طیف رنگی بر اساس شیب به دست آورده شده
for i in range(width):
    for j in range(height):
        color_num = int(j * m) % 256  # شدت رنگ بر اساس شیب
        #برای تست و جلوگیر از خروج عدد به دست آمده از بازه موجود که 0 تا 255 است
        image[j, i] = [color_num, color_num, color_num]; 

# نمایش تصویر
cv2.imshow("طیف رنگی بر اساس شیب خط", image);
cv2.waitKey(0);
