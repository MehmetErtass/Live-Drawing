# Live_Drawing
It creates a live drawing effect by taking a live image from the camera and processing the image.
* Applies image processing techniques using "cv2" (OpenCV) and "numpy" libraries. The "sketch" function resizes the image, sharpens it, grayscales it, inverts it, adds blur and finally applies a drawing effect. 
* The "cv2.VideoCapture()" method receives the video stream from a camera connected to your computer, and the "while" loop is used to process and display each captured frame. 
* The "cv2.imshow()" method displays the live drawing effect and the live camera view. 
* The "cv2.waitKey()" method causes the code to stop when any key is pressed, exiting the loop. 
* The "cv2.destroyAllWindows()" method closes all open windows.
