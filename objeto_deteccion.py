import cv2


class Clase_detector():
    def __init__(self):
        pass

    def detector_objetos(self, frame):
        # Convertir imagen a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Creación de mascara
        mask = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # Encontrar contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.imshow("mask", mask)
        objects_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 2000:
                #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
                objects_contours.append(cnt)

        return objects_contours
