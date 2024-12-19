from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours

from  objeto_deteccion import*
import serial,time
import numpy as np
import cv2
from Base_Puntos import Datoskukax, Datoskukay,Kukadot,clasificacion
import imutils
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
parametros=cv2.aruco.DetectorParameters_create()
aruco_dict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
#referencia
detector=Clase_detector()
#camara
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

azul = (255, 0, 0)
verde = (0, 255, 0)
rojo = (0, 0, 255)
amarillo=(0,255,255)
negro=(0,0,0)
transparente=(252,252,252)

x_ref_kuka=489.1866
y_ref_kuka=860.7555
kuka_x_inicial=1486.2
kuka_y_inicial=-513.6
pic = serial.Serial("COM6", 9600)
while True:

	_, imagen = cap.read()

	imag = cv2.imread('ejemplo5.jpeg')
	imagen = cv2.resize(imag, (1280, 720))
	gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)
	# perform edge detection, then perform a dilation + erosion to
	# close gaps in between object edges
	edged = cv2.Canny(gray, 50, 100)
	edged = cv2.dilate(edged, None, iterations=1)
	edged = cv2.erode(edged, None, iterations=1)
	# find contours in the edge map
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
							cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# sort the contours from left-to-right and, then initialize the
	# distance colors and reference object
	(cnts, _) = contours.sort_contours(cnts)
	colors = ((240, 0, 159), (240, 0, 159), (0, 165, 255), (255, 255, 0), (255, 0, 0))
	esquinas, _, _ = cv2.aruco.detectMarkers(imagen, aruco_dict, parameters=parametros)
	if esquinas:
		# Obtener poligono alrededor del marcador
		int_esquinas = np.int0(esquinas)
		cv2.polylines(imagen, int_esquinas, True, (verde), 5)

		# Perimetro de aruco
		aruco_perimetro = cv2.arcLength(esquinas[0], True)

		# Pasar de pixeles a cm
		pixel_cm = aruco_perimetro / 20

		contornos = detector.detector_objetos(imagen)
		
		detecciones = []

		# Dibujar contorno de objetos
		for cnt in contornos:
			# Dbtener rectangulo
			rect = cv2.minAreaRect(cnt)
			(x, y), (w, h), angle = rect
			# Obtener la base y altura de los objetos aplicando la conversión de pixel a cm
			objeto_Base = w / pixel_cm
			objeto_Altura = h / pixel_cm
			valor_x = x / pixel_cm
			valor_y = y / pixel_cm
			# Codigo seguimiento

			# Dibujar rectangulo

			cv2.putText(imagen, "Base= {} cm".format(round(objeto_Base, 1)), (int(x + 10), int(y - 15)),cv2.FONT_HERSHEY_PLAIN, 1.5, (negro), 2)
			cv2.putText(imagen, "Altura= {} cm".format(round(objeto_Altura, 1)), (int(x + 10), int(y + 15)),cv2.FONT_HERSHEY_PLAIN, 1.5, (negro), 2)
			Area=objeto_Base*objeto_Altura
			Area_aprox=round(Area,1)
			detecciones.append([Area_aprox])
			detecciones.sort(reverse=True)



	refObj = None
	refObj2 = None
	refObj3 = None
	# bucle sobre los contornos individualmente
	contornos = detector.detector_objetos(imagen)
	for c in cnts:
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < 1000:
			continue
		# compute the rotated bounding box of the contour
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		# order the points in the contour such that they appear
		# in top-left, top-right, bottom-right, and bottom-left
		# order, then draw the outline of the rotated bounding
		# box
		box = perspective.order_points(box)
		# compute the center of the bounding box
		cX = np.average(box[:, 0])
		cY = np.average(box[:, 1])

		cX2 = np.average(box[:, 0])
		cY2 = np.average(box[:, 1])

		cX3 = np.average(box[:, 0])
		cY3 = np.average(box[:, 1])
		# si este es el primer contorno que estamos examinando (es decir,
		# el contorno más a la izquierda), asumimos que este es el

		# objeto de referencia

		if refObj is None:
			# descomprima el cuadro delimitador ordenado, luego calcule el
			# punto medio entre los puntos superior izquierdo y superior derecho,
			# seguido del punto medio entre la parte superior derecha y
			# abajo a la derecha
			(tl, tr, br, bl) = box
			(tlblX, tlblY) = midpoint(tl, bl)
			(trbrX, trbrY) = midpoint(tr, br)
			# calcular la distancia euclidiana entre los puntos medios,
			# luego construye el objeto de referencia
			D = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
			refObj = (box, (cX, cY), D / 1.9685)

			continue

		if refObj2 is None:
			# descomprima el cuadro delimitador ordenado, luego calcule el
			# punto medio entre los puntos superior izquierdo y superior derecho,
			# seguido del punto medio entre la parte superior derecha y
			# abajo a la derecha
			(tl2, tr2, br2, bl2) = box
			(tlblX2, tlblY2) = midpoint(tl2, bl2)
			(trbrX2, trbrY2) = midpoint(tr2, br2)
			# calcular la distancia euclidiana entre los puntos medios,
			# luego construye el objeto de referencia
			D2 = dist.euclidean((tlblX2, tlblY2), (trbrX2, trbrY2))
			refObj2 = (box, (cX2, cY2), D / 1.9685)

			continue
		cv2.drawContours(imagen, [box.astype("int")], -1, (0, 255, 0), 2)
		if refObj3 is None:
			# descomprima el cuadro delimitador ordenado, luego calcule el
			# punto medio entre los puntos superior izquierdo y superior derecho,
			# seguido del punto medio entre la parte superior derecha y
			# abajo a la derecha
			(tl3, tr3, br3, bl3) = box
			(tlblX3, tlblY3) = midpoint(tl3, bl3)
			(trbrX3, trbrY3) = midpoint(tr3, br3)
			# calcular la distancia euclidiana entre los puntos medios,
			# luego construye el objeto de referencia
			D3 = dist.euclidean((tlblX3, tlblY3), (trbrX3, trbrY3))
			refObj3 = (box, (cX, cY), D / 1.9685)

			continue
		# dibujar los contornos en la imagen
		cv2.drawContours(imagen, [box.astype("int")], -1, (0, 255, 0), 2)
		cv2.drawContours(imagen, [refObj2[0].astype("int")], -1, (0, 255, 0), 2)
		#cv2.drawContours(imagen, [box.astype("int")], -1,amarillo, 2)
		#cv2.drawContours(imagen, [refObj[0].astype("int")], -1,amarillo, 2)
		#cv2.drawContours(imagen, [refObj2[0].astype("int")], -1,amarillo, 2)
		#cv2.drawContours(imagen, [refObj3[0].astype("int")], -1,amarillo, 2)

		# apilar las coordenadas de referencia y las coordenadas del objeto para incluir el centro del objeto
		refCoords = np.vstack([refObj[1]])
		objCoords = np.vstack([(cX, cY)])

		refCoords2 = np.vstack([refObj2[1]])
		objCoords2 = np.vstack([(cX2, cY2)])

		refCoords3 = np.vstack([refObj3[1]])
		objCoords3 = np.vstack([(cX3, cY3)])
		# bucle sobre los puntos originales

		for ((xA, yA), (xB, yB), color) in zip(refCoords, objCoords, colors):
			# dibujar círculos correspondientes a los puntos actuales y
			# conectarlos con una línea
			cv2.circle(imagen, (int(xA), int(yA)), 5, color, -1)
			cv2.circle(imagen, (int(xB), int(yB)), 5, rojo, -1)
			cv2.line(imagen, (int(xA), int(yA)), (int(xB), int(yB)), color, 2)
			# calcular la distancia euclidiana entre las coordenadas,
			# y luego convertir la distancia en píxeles a distancia en
			# unidades
			D = dist.euclidean((xA, yA), (xB, yB)) / refObj[2] * 2.54
			D2O2 = dist.euclidean((xA, yA), (xB, yA)) / refObj[2] * 2.54
			D2A2 = dist.euclidean((xB, yB), (xB, yA)) / refObj[2] * 2.54
			Objeto2y = round(D2O2, 1)
			Objeto2x = round(D2A2, 1)
			(mX, mY) = midpoint((xA, yA), (xB, yB))
			#cv2.putText(imagen, "{:.1f}cm".format(D), (int(mX), int(mY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro, 2)
			cv2.putText(imagen, "Coord Y= " "{:.1f} cm".format(D2A2), (int(xB + 10), int(yB + 75)),
						cv2.FONT_HERSHEY_SIMPLEX,
						0.55, negro, 2)
			cv2.putText(imagen, "Coord X= " "{:.1f} cm".format(D2O2), (int(xB + 10), int(yB + 45)),
						cv2.FONT_HERSHEY_SIMPLEX,
						0.55, negro, 2)

		for ((xA2, yA2), (xB2, yB2)) in zip(refCoords2, objCoords2):
			# dibujar círculos correspondientes a los puntos actuales y
			# conectarlos con una línea
			cv2.circle(imagen, (int(xA), int(yA)), 5, rojo, -1)
			cv2.circle(imagen, (int(xA2), int(yA2)), 5, rojo, -1)
			cv2.line(imagen, (int(xA), int(yA)), (int(xA2), int(yA2)), verde, 2)
			# calcular la distancia euclidiana entre las coordenadas,
			# y luego convertir la distancia en píxeles a distancia en
			# unidades
			D2 = dist.euclidean((xA, yA), (xA2, yA2)) / refObj2[2] * 2.54
			D2O1 = dist.euclidean((xA, yA), (xA2, yA)) / refObj2[2] * 2.54
			D2A1 = dist.euclidean((xA2, yA2), (xA2, yA)) / refObj2[2] * 2.54
			Objeto1y = round(D2O1, 1)
			Objeto1x = round(D2A1, 1)
			(mX2, mY2) = midpoint((xA, yA), (xA2, yA2))
			# cv2.putText(imagen,"{:.1f}cm".format(D2), (int(mX2), int(mY2 + 20)), cv2.FONT_HERSHEY_SIMPLEX,0.55, negro, 2)
			cv2.putText(imagen, "Coord X= " "{:.1f} cm".format(D2A1), (int(xA2 + 10), int(yA2 + 75)),
						cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro, 2)
			cv2.putText(imagen, "Coord Y= " "{:.1f} cm".format(D2O1), (int(xA2 + 10), int(yA2 + 45)),
						cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro, 2)
			cv2.putText(imagen, "Coord X=0 cm ", (int(xA - 50), int(yA - 100)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro,
						2)
			cv2.putText(imagen, "Coord Y=0 cm ", (int(xA - 50), int(yA - 130)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro,
						2)

		# mostrar la imagen de salida\



		for ((xA3, yA3), (xB3, yB3)) in zip(refCoords3, objCoords3):
			# dibujar círculos correspondientes a los puntos actuales y
			# conectarlos con una línea
			cv2.circle(imagen, (int(xA), int(yA)), 5, azul, -1)
			cv2.circle(imagen, (int(xA3), int(yA3)), 5, azul, -1)
			cv2.line(imagen, (int(xA), int(yA)), (int(xA3), int(yA3)), azul, 2)
			# calcular la distancia euclidiana entre las coordenadas,
			# y luego convertir la distancia en píxeles a distancia en
			# unidades
			D3 = dist.euclidean((xA, yA), (xA3, yA3)) / refObj3[2] * 2.54
			D2O3 = dist.euclidean((xA, yA), (xA3, yA)) / refObj3[2] * 2.54
			D2A3 = dist.euclidean((xA3, yA3), (xA3, yA)) / refObj3[2] * 2.54
			Objeto3y = round(D2O3, 1)
			Objeto3x = round(D2A3, 1)
			(mX3, mY3) = midpoint((xA, yA), (xA3, yA3))
			# cv2.putText(imagen, "{:.1f}cm".format(D3), (int(mX3-55), int(mY3 - 20)), cv2.FONT_HERSHEY_SIMPLEX,0.55, negro, 2)
			cv2.putText(imagen, "Coord X= " "{:.1f} cm".format(D2A3), (int(xA3 + 10), int(yA3 + 75)),
						cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro, 2)
			cv2.putText(imagen, "Coord Y= " "{:.1f} cm".format(D2O3), (int(xA3 + 10), int(yA3 + 45)),
						cv2.FONT_HERSHEY_SIMPLEX, 0.55, negro, 2)
	# mostrar la imagen de salida
	# mostrar la imagen de salida

	print("Area 1",detecciones[0],"x",Objeto1x,"y",Objeto1y)
	print("Area 2",detecciones[1],"x",Objeto2x,"y",Objeto2y)
	#Aruco print(detecciones[2])

	print("Area 3", detecciones[3], "x", Objeto3x, "y", Objeto3y)
	Area1 = ''.join(map(str, detecciones[0]))
	area1 = float(Area1)

	Area2 = ''.join(map(str, detecciones[1]))
	area2 = float(Area2)

	Area3 = ''.join(map(str, detecciones[3]))
	area3 = float(Area3)

	envio_tamaño1 = clasificacion(area1)
	print(envio_tamaño1)
	envio_tamaño2 = clasificacion(area2)
	print(envio_tamaño2)
	envio_tamaño3 = clasificacion(area3)
	print(envio_tamaño3)

	print("Area 3",detecciones[3],"x",Objeto3x,"y",Objeto3y)
	dato1x = round(1453.58 - (x_ref_kuka * Objeto1x / 50),1)
	dato1y = round(-513.61 + (y_ref_kuka * Objeto1y / 86.7),1)
	dato2x=round(1453.58-(x_ref_kuka*Objeto2x/50),1)
	dato2y =round(-513.61 + (y_ref_kuka * Objeto2y / 86.7),1)
	dato3x =round(1453.58 - (x_ref_kuka * Objeto3x / 50),1)
	dato3y =round(-513.61 + (y_ref_kuka * Objeto3y / 86.7),1)

	cv2.imshow("imagen",imagen)
	k = cv2.waitKey(1)
	if k == ord("q"):
		while 1:
			##############################################################################
			resultado1x = Datoskukax(dato1x)
			resultado1y = Datoskukay(dato1y)
			print("Punto aproximado 1 ", resultado1x, resultado1y)
			resultado2x = Datoskukax(dato2x)
			resultado2y = Datoskukay(dato2y)
			print("Punto aproximado 2 ", resultado2x, resultado2y)
			resultado3x = Datoskukax(dato3x)
			resultado3y = Datoskukay(dato3y)
			print("Punto aproximado 3 ", resultado3x, resultado3y)

			print("Punto Original 1", dato1x, dato1y)
			print("Punto Original 2", dato2x, dato2y)
			print("Punto Original 3", dato3x, dato3y)
			envio1 = Kukadot(resultado1x, resultado1y)
			envio2 = Kukadot(resultado2x, resultado2y)
			envio3 = Kukadot(resultado3x, resultado3y)
			print("Envio de datos 1 es:", envio1)
			print("Envio de datos 2 es:", envio2)
			print("Envio de datos 3 es:", envio3)
			menu = input()
			if menu == ("a"):
				pic.write(envio1.encode())
				pic.write(envio_tamaño1.encode())
				time.sleep(1)
				envio_pic = "000"
				pic.write(envio_pic.encode())
				pic.write(envio_tamaño1.encode())
			if menu == ("s"):
				pic.write(envio2.encode())
				pic.write(envio_tamaño2.encode())
				time.sleep(1)
				envio_pic = "000"
				pic.write(envio_pic.encode())
				pic.write(envio_tamaño2.encode())

			if menu == ("d"):
				pic.write(envio3.encode())
				pic.write(envio_tamaño3.encode())
				time.sleep(1)
				envio_pic = "000"
				pic.write(envio_pic.encode())
				pic.write(envio_tamaño3.encode())

		break
cap.release()
cv2.destroyAllWindows()

