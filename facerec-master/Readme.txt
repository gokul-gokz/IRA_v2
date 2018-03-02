Instructions:
--------------
1.Check whether dependencies are installed or not:
	opencv2,
	opencv contrib

2. Follow the steps below to install opencv locally with additional dependencies for running face recognition package

Steps:
------------
sudo apt-get -y install libopencv-dev build-essential cmake libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils
======================================================================================================================================
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.0.0
======================================================================================================================================
cd ~
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.0.0
=======================================================================================================================================
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D WITH_QT=ON \
	-D WITH_OPENGL=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
========================================================================================================================================

make -j3

=========================================================================================================================================
sudo make install
sudo ldconfig
///////////////////////////////////////////////////////INSTALLATION OVER///////////////////////////////////////////////////////////////////


Running the package
--------------------
Refer:fac_rec.pdf
 
