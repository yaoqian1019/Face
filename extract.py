# -*- coding:utf-8 -*-
import dlib
import numpy as np

class extract:
    """領域抽出クラス"""

    def cutArea(self, x_list, y_list):
        """抽出領域の頂点取得
        @ param1[in] x_list                     X座標リスト
        @ param2[in] y_list                     Y座標リスト
        @ param[out] top, bottom, left, right   矩形領域の頂点
        """
        top = min(y_list)
        bottom = max(y_list)
        left = min(x_list)
        right = max(x_list)
        return top, bottom, left, right

    def extractEyeArea(self, image, predictor, face):
        """目領域の抽出
        @ param1[in] image              描画する画像
        @ param2[in] predictor          予測器
        @ param3[in] face               検出した顔領域
        @ param[out] r_eye_img          右目領域
        @ param[out] l_eye_img          左目領域
        """
        r_pointX = []
        r_pointY = []
        l_pointX = []
        l_pointY = []
        height, width = image.shape[:2]
        shape = predictor(image, face)

        for i in range(shape.num_parts):
            # 右目
            if i >= 36 and i <= 41:
                r_pointX.append(shape.part(i).x)
                r_pointY.append(shape.part(i).y)
                r_top, r_bottom, r_left, r_right = self.cutArea(x_list=r_pointX, y_list=r_pointY)
                if r_top > 0 and r_left > 0 and r_bottom < height and r_right < width:
                    r_eye_img = image[r_top:r_bottom, r_left:r_right]
            # 左目
            elif i >= 42 and i <= 47:
                l_pointX.append(shape.part(i).x)
                l_pointY.append(shape.part(i).y)
                l_top, l_bottom, l_left, l_right = self.cutArea(x_list=l_pointX, y_list=l_pointY)
                if l_top > 0 and l_left > 0 and l_bottom < height and l_right < width:
                    l_eye_img = image[l_top:l_bottom, l_left:l_right]

        return r_eye_img, l_eye_img

    def getEyeContour(self, image, predictor, face):
        """目の輪郭取得
        @ param1[in] image              入力画像
        @ param2[in] predictor          予測器
        @ param3[in] face               検出した顔領域
        @ param[out] r_eye_contour      右目輪郭
        @ param[out] l_eye_contour      左目輪郭
        """
        r_eye_contour = []
        l_eye_contour = []
        shape = predictor(image, face)
        for i in range(shape.num_parts):
            # 右目
            if i >= 36 and i <= 41:
                r_eye_point = []
                r_eye_point.append(shape.part(i).x)
                r_eye_point.append(shape.part(i).y)
                r_eye_point = np.array(r_eye_point)
                r_eye_contour.append(r_eye_point)
            # 左目
            elif i >= 42 and i <= 47:
                l_eye_point = []
                l_eye_point.append(shape.part(i).x)
                l_eye_point.append(shape.part(i).y)
                l_eye_point = np.array(l_eye_point)
                l_eye_contour.append(l_eye_point)

        r_eye_contour = np.array(r_eye_contour)
        l_eye_contour = np.array(l_eye_contour)
        return r_eye_contour, l_eye_contour

    def getNoseSideContour(self, image, predictor, face):
        """鼻側面の輪郭取得
        @ param1[in] image              入力画像
        @ param2[in] predictor          予測器
        @ param3[in] face               検出した顔領域
        @ param[out] r_nose_contour      右鼻側面輪郭
        @ param[out] l_nose_contour      左鼻側面輪郭
        """
        r_nose_contour = []
        l_nose_contour = []
        shape = predictor(image, face)
        for i in range(shape.num_parts):
            r_nose_point = []
            l_nose_point = []

            if i == 27 or i == 30:
                r_nose_point.append(shape.part(i).x)
                r_nose_point.append(shape.part(i).y)
                r_nose_point = np.array(r_nose_point)
                r_nose_contour.append(r_nose_point)
                l_nose_point.append(shape.part(i).x)
                l_nose_point.append(shape.part(i).y)
                l_nose_point = np.array(l_nose_point)
                l_nose_contour.append(l_nose_point)
            elif i == 31:
                r_nose_point.append(shape.part(i).x)
                r_nose_point.append(shape.part(i).y)
                r_nose_point = np.array(r_nose_point)
                r_nose_contour.append(r_nose_point)
            elif i == 35:
                l_nose_point.append(shape.part(i).x)
                l_nose_point.append(shape.part(i).y)
                l_nose_point = np.array(l_nose_point)
                l_nose_contour.append(l_nose_point)

        r_nose_contour = np.array(r_nose_contour)
        l_nose_contour = np.array(l_nose_contour)
        return r_nose_contour, l_nose_contour

    def getFaceContour(self, image, predictor, face):
        """顔の輪郭取得
        @ param1[in] image              入力画像
        @ param2[in] predictor          予測器
        @ param3[in] face               検出した顔領域
        @ param[out] face_contour       顔輪郭
        """
        face_contour = []
        shape = predictor(image, face)
        for i in range(shape.num_parts):
            if i >= 0 and i <= 16:
                face_point = []
                face_point.append(shape.part(i).x)
                face_point.append(shape.part(i).y)
                face_point = np.array(face_point)
                face_contour.append(face_point)

        face_contour = np.array(face_contour)
        return face_contour
