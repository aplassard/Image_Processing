# contains functions for hist eq, smoothing/blue, sharpening, gradient, grayscaling and contrast enhancement
# all function s use Image object, not numpy ndarray. at least histeq does

import Image
import ImageOps
import ImageFilter
from common import *

def histNorm(image):
	im2=ImageOps.equalize(image)
	return im2

def smooth(image):
	im2=image.filter(ImageFilter.SMOOTH)
	return im2

def sharp(image):
	im2=image.filter(ImageFilter.SHARPEN)
	return im2

def blur(image):
	im2=image.filter(ImageFilter.BLUR)
	return im2

def gaussblur(image):
	im2=image.filter(ImageFilter.GaussianBlur)
	return im2

def minFilter(image):
	im2=image.filter(ImageFilter.MinFilter)
	return im2

def grayScale(image):
	im2=ImageOps.grayscale(image)
	return im2

def contour(image):
	im2=image.filter(ImageFilter.CONTOUR)
	return im2

def normalizeImage(image):
	im=image
	imTemp=minFilter(im)
	imTemp=histNorm(imTemp)
	imGray=grayScale(imTemp)
	d={}
	d[RGB]=imTemp
	d[grayscale]=imGray
	return d