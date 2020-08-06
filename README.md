# speedtestreader
Hello!

Welcome to the Speedtest Reader of Ookla speedtests!

What does it do?
The speedtest reader reads the speedtest data (specifically, the download and upload speeds) from screenshots/images of the Ookla Speedtest app.

Installation:
1. Anaconda must be installed in your system (works best in Linux)
2. Install the modules: cv2, pillow, pandas, numpy, tqdm
3. Install pytesseract 3.05


NOTE: Make sure to place all files in a single folder and set the directory path to that folder. 
When using Linux, run this code first before running the reader.py file:

export TESSDATA_PREFIX='/usr/local/share/'

How it works:
1. The first part of the code is the image cropper, where the raw screenshots of the speedtests must be inside the 'RawImg' folder.
2. The cropped images are placed in the 'IMAGES' folder. The cropped images consist of only the upper part of the screenshot which contains the Download and Upload speed, as well as the Ping, Jitter and Loss.
3. The next step is the conversion of the cropped images in 'IMAGES' folder into grayscale.
4. The grayscale images are placed in the 'grayscaleresult' folder.
5. The next step is where the OCR process will take. The grayscale images will undergo OCR using PyTesseract. The output will be in the form of a CSV file. 1 image = 1 CSV file result
6. The CSV files are placed in the 'csvresult' folder.
