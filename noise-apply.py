import cv2 as cv
import numpy as np
import math

# آدرس تصویر
img_path = "dog.jpg"

# خواندن تصویر
img = cv.imread(img_path)
img_with_noise1 = img.copy()  # تصویر برای نویز اول
img_with_noise2 = img.copy()  # تصویر برای نویز دوم
final_img = img.copy()  # تصویر نهایی بدون نویز

# اندازه‌های تصویر
width = img.shape[1]
height = img.shape[0]

# درصد نویزها
noise_percentage1 = float(input("درصد نویز اول را وارد کنید: "))
noise_percentage2 = float(input("درصد نویز دوم را وارد کنید: "))

# تابع اعمال نویز
def apply_noise(img, width, height, noise_percentage):
    for y in range(height):
        for x in range(width):
            rand_value = rn.random()

            lower_bound = noise_percentage / 2 / 100
            higher_bound = 1 - lower_bound

            if rand_value < lower_bound:
                img[y][x] = [0, 0, 0]  # نویز سیاه
            elif rand_value > higher_bound:
                img[y][x] = [255, 255, 255]  # نویز سفید
            else:
                pass  
    return img

# اعمال دو نوع نویز
noise_image1 = apply_noise(img_with_noise1, width, height, noise_percentage1)
noise_image2 = apply_noise(img_with_noise2, width, height, noise_percentage2)

# تابع بررسی پیکسل صفر یا سفید
def check_zero_pixel(pixel):
    return (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0) or (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255)

# گرفتن همسایه‌های یک پیکسل
def get_neighbours(data, y, x, channel):
    neighbours = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            neighbours.append(data[y + dy][x + dx][channel])
    return neighbours

# پیدا کردن پیکسل‌های واقعی
def find_pixels(vector):
    return [val for val in vector if val != 0 and val != 255]

# حذف نویز برای هر دو تصویر
for y in range(1, height - 1):
    for x in range(1, width - 1):
        pixel1 = noise_image1[y][x]
        pixel2 = noise_image2[y][x]

        if check_zero_pixel(pixel1) or check_zero_pixel(pixel2):
            red_neighbours1 = get_neighbours(noise_image1, y, x, 2)
            green_neighbours1 = get_neighbours(noise_image1, y, x, 1)
            blue_neighbours1 = get_neighbours(noise_image1, y, x, 0)

            red_neighbours2 = get_neighbours(noise_image2, y, x, 2)
            green_neighbours2 = get_neighbours(noise_image2, y, x, 1)
            blue_neighbours2 = get_neighbours(noise_image2, y, x, 0)

            pixels_red = find_pixels(red_neighbours1 + red_neighbours2)
            pixels_green = find_pixels(green_neighbours1 + green_neighbours2)
            pixels_blue = find_pixels(blue_neighbours1 + blue_neighbours2)

            if len(pixels_red) == 0 or len(pixels_green) == 0 or len(pixels_blue) == 0:
                new_value_r = 0
                new_value_g = 0
                new_value_b = 0
            elif len(pixels_red) == 1 or len(pixels_green) == 1 or len(pixels_blue) == 1:
                new_value_r = pixels_red[0]
                new_value_g = pixels_green[0]
                new_value_b = pixels_blue[0]
            else:
                new_value_r = math.floor(pixels_red)
                new_value_g = math.floor(pixels_gree)
                new_value_b = math.floor(pixels_blue)

            final_img[y][x] = [new_value_b, new_value_g, new_value_r]

# نمایش تصاویر
cv.imshow("Original Image", img)
cv.imshow("Noise Image 1", noise_image1)
cv.imshow("Noise Image 2", noise_image2)
cv.imshow("Reduced Noise Image", final_img)
cv.waitKey(0)
cv.destroyAllWindows()
