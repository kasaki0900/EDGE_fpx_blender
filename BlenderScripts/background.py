import cv2
import os
import numpy as np


def gen(ori_w, ori_h):
    bg = cv2.imread('F:\\BlenderPro\\ast\\bg.png')
    bg = cv2.resize(bg, (ori_w, ori_h))
    bg = bg.astype(float)

    path = 'F:\\BlenderPro\\ast\\render'  # 图片流
    output_path = 'F:\\BlenderPro\\ast\\exp.mp4'  # 输出

    files = os.listdir(path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # writer = cv2.VideoWriter(output_path, fourcc, 15, (640, 480))
    writer = cv2.VideoWriter(output_path, fourcc, 15, (1920, 1080))

    for file_name in files:
        img = os.path.join(path, file_name)
        flame = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        r, g, b, a = cv2.split(flame)

        fg = cv2.merge((r, g, b)).astype(float)
        mask = cv2.merge((a, a, a)).astype(float) / 255

        foreground = cv2.multiply(mask, fg)
        background = cv2.multiply(1-mask, bg)

        out_array = (foreground + background)
        # cv2.imshow('img', out_array)
        # cv2.waitKey()

        # cv2.imwrite(os.path.join(cp_path, str(cnt) + '.jpg'), out_array)
        out_array = out_array.astype(np.uint8)

        # cv2.imshow("img", out_array)
        # cv2.waitKey(0)

        scale = 1080 / ori_h
        new_width = int(ori_w * scale)  # 1440
        new_height = int(ori_h * scale)  # 1080
        resized_image = cv2.resize(out_array, (new_width, new_height))  # 1080 1440

        target_image = np.zeros((1080, 1920, 3), dtype=np.uint8)  # 1920 1080
        x_offset = (1920 - new_width) // 2  # 240
        y_offset = (1080 - new_height) // 2

        target_image[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image

        writer.write(target_image)
        os.remove(img)

    writer.release()


if __name__ == '__main__':
    gen(640, 480)

