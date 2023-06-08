# PDF-to-Mokuro

Simply change the path to the folder of the pdfs and the path, where the output should be and run the script. 

1. At first it converts the .pdf to .jpg's and puts them in the output folder for all available pdfs. 
2. It runs a command like ``mokuro /path/to/manga/vol1 /path/to/manga/vol2 /path/to/manga/vol3`` for all volumes that were provided as pdfs. 
3. The HTML with selectable text is in the output Folder

I used Python Version 3.10 on Windows. For the PDF -> JPG Conversion Poppler is required. On Windows you can get it from here https://github.com/oschwartz10612/poppler-windows and you have to put it as Environment Variable

Here is also a good guide to follow if you have a NVIDIA GPU that can use CUDA for faster compilation https://rentry.co/lazyXel#Local%20Processing%20Method
