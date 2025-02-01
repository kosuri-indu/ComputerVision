# OpenCV

## Overview

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It contains more than 2500 optimized algorithms, which can be used for various computer vision tasks.

## What are Images?

Images are numpy arrays. An image is defined by its height, width, and number of channels. An image is made up of pixels, and in most cases, pixel values range from 0 to 255. For binary images, pixel values range from 0 to 1, and for 16-bit images, pixel values range from 0 to 65535.

- Black: 0
- White: 1

For more information, visit the [OpenCV documentation](https://docs.opencv.org/4.x/).

## Human Vision - Perception of Color

- The human eye has 3 types of photoreceptor cells for color.
- The responsibility spectra of human cone cells are centered at red, green, and blue.
- Trichromacy: At any given time, we are capturing information from 3 different sensors.

Fun fact: Mantis shrimp have 16 photoreceptor cells.

## Directory Structure

The `opencv` directory contains the following Python files, each demonstrating different functionalities of OpenCV:

| File | Description |
|------|-------------|
| [input_output_image.py](input_output_image.py) | Demonstrates how to read, write, and display images. |
| [input_output_video.py](input_output_video.py) | Shows how to read and display video files. |
| [input_output_webcam.py](input_output_webcam.py) | Demonstrates how to capture and display video from a webcam. |
| [basic_operations.py](basic_operations.py) | Demonstrates basic image operations such as resizing and cropping. |
| [colorspaces.py](colorspaces.py) | Explains how to convert images between different color spaces (e.g., BGR to RGB, grayscale, HSV). |
| [blurring.py](blurring.py) | Shows different blurring techniques like averaging, Gaussian, median, and bilateral blurring. |
| [thresholding.py](thresholding.py) | Explains different thresholding techniques to create binary images. |
| [edge_detection.py](edge_detection.py) | Explains edge detection techniques, including Canny edge detection. |
| [drawing.py](drawing.py) | Shows how to draw shapes (lines, rectangles, circles) and text on images. |
| [contours.py](contours.py) | Demonstrates how to find and draw contours in an image. |