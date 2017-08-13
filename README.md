# Image_Processing
Computer Vision

First of all you should know the basic syntax of Python.
To start with computer vision you need to have a basic knowledge about Deep Learning, neural neworks, CNN , RCNN , fast RCNN , faster RCNN.

Here are some resourses,

	Deep learning, CNN (Startup)

	[1] https://www.youtube.com/watch?v=vq2nnJ4g6N0&t=1546s

	RCNN, fast RCNN, faster RCNN (Startup)

	[1] https://www.youtube.com/watch?v=u6aEYuemt0M&t=238s  
	[2] Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks by Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun

Step1:
	Lets start with OpenCV for the neural networks.
	For this install OpenCV in Ubuntu.
	Refer to this documentation for installation : http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
	
	The repository contains an example of a neural network made with OpenCV called "RedEyeOpenCV" which 
	-converts the img into gray scale, 
	-splits and merge the image into BGR components, 
	-puts boxes one eyes, puts text on the image, 
	-save the given image in a different format eg.png.
	Run it by typing "python RedEyes.py" on terminal.
	
	The repository also contains a GUI made with opencv called "trackbar.py" that makes colours.
	Run it by typing "python trackbar.py" on terminal.
	
Step2:
	Make a neural network that detect faces and eyes in images using opencv and haarcascades.
	Find a folder named "Eyes and face Detection".
	Run it by typing "python face.py" and "python eye_and_face_detection.py" respectively on terminal.
	
Step3:
	Start making GUI for neural networks.
	For this, use OpenCV along with 'Tkinter' which is a standard package in Python.
	Insure OpenCV is installed on Linux.
	Repository contains 'Tkinter' named folder which contains files that demonstrates some features of tkinter.
	-"camera.py" opens a videoa and contains a button through which you can capture any moment of the video and save.
	-"askfile.py" contains GUI for file browse.
	-"btton.py" is a GUI for button and pops a window on click.
	Run the files by typing "python camera.py", "python askfile.py" and "python btton.py" respectively.
	
