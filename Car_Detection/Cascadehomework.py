import cv2 as cv

#Load test image
img = cv.imread('Code_Python/test.jpg', cv.IMREAD_COLOR)

#Load cascade filter
cars_cascade = cv.CascadeClassifier()
cars_cascade.load('Code_Python/cars.xml')
cars = cars_cascade.detectMultiScale(img)

#Detect cars
n=1
for (x,y,w,h) in cars:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    #PutText
    text = '#' + str(n)
    center = (x,y)
    cv.putText(img, text, center, cv.FONT_HERSHEY_SIMPLEX, 0.5, (80,255,0), 1)
    n += 1
print('#The number of cars in parking lot 1: ', len(cars))
cv.imshow('Detect', img)
cv.waitKey()
cv.destroyAllWindows()

   


