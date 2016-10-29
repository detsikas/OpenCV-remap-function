//
//  main.cpp
//  RippleEffect
//
//  Created by peeknpoke.net on 18/9/16.
//  Copyright ... no copyright

#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

float f = 0.25f*CV_PI;
float p = 3.0f*CV_PI/4.0f;


static void rippleEffect(Mat const & inputImage, Mat & outputImage, Mat const & mapX, Mat const & mapY)
{
	remap(inputImage, outputImage, mapX, mapY, CV_INTER_LINEAR, BORDER_REPLICATE);
}

int main(int argc, const char * argv[])
{
	// Check usage
	if (argc<2)
	{
		cerr<<"Usage "<<argv[0]<<" <filename>"<<endl;
		exit(EXIT_FAILURE);
	}

	// Read input image
	Mat inputImage = imread(argv[1]);
	imshow("Input image", inputImage);
	waitKey(0);
	
	// Create output image
	Mat outputImage;
	outputImage.create(inputImage.rows, inputImage.cols, inputImage.type());
	
	// Create remap maps
	Mat mapX, mapY;
	mapX.create(inputImage.rows, inputImage.cols, CV_32FC1);
	mapY.create(inputImage.rows, inputImage.cols, CV_32FC1);

	// Constant ripple paramters
	float const A = 10.0f;							// Ripple magnitude
	float const dir = (1.0f/5.0f)*CV_PI/2.0f;		// Ripple direction
	float const omega = CV_PI*(2.0f/inputImage.rows);	// Ripple frequency
	unsigned int const rippleFrames = 100;			// Ripple frames

	while(1)
	{
		for (unsigned int m=0; m<rippleFrames; m++)
		{
			float p = (float)m*2.0f*CV_PI/rippleFrames+CV_PI; // Ripple phase
			for (int j=0; j<inputImage.rows; j++)
			{
				for (int i=0; i<inputImage.cols; i++)
				{
					mapX.at<float>(j,i) = i+A*(i/inputImage.cols)*sin(omega*j+p)*cos(dir);
					mapY.at<float>(j,i) = j+A*sin(omega*i+p)*sin(dir);
				}
			}

			rippleEffect(inputImage, outputImage, mapX, mapY);

			imshow("Output image", outputImage);
			waitKey(3);
		}
	}
	return 0;
}
