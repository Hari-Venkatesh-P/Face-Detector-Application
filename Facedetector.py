import cv2
face_cascade = cv2.CascadeClassifier("E:\\Python\\Open CV\\FaceDetector\\haarcascade_frontalface_default.xml") #cascader for detecting front face
img = cv2.imread("E:\\Python\\Open CV\\FaceDetector\\2017-04-08-19-32-35-637.jpg",1) # 1 denotes colored image and 0 zero grayscale image 
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
	print(x,y,w,h)
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("OpenCV",resized)
cv2.waitKey(0) # 0 indicates if a key is pressed windows destroys 
cv2.destroyAllWindows()