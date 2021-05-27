import fitz
import time
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # or put wherever directory tesseract.exe is at!! 

def get_text_pdf_and_images(pdf_file, page_number):

    File = fitz.open(pdf_file)

    page = File.load_page(page_number - 1)

    text = page.getText()

    images = page.getImageList()
    
    if images:

        for i in range(len(images)):
            xref = images[i][0]

            pix = fitz.Pixmap(File, xref)

            if pix.n > 4:

                pix = fitz.Pixmap(fitz.csRGB, pix)
            
                pix.writePNG(f'image_page{page_number}_imageN{i + 1}.png')

                time.sleep(4)

                png_image = Image.open(f'image_page{page_number}_imageN{i + 1}.png')

                img_text = pytesseract.image_to_string(png_image)

                final_text = text + "\n" + "\n" + f"image{i+1}" + "\n" + "\n" + img_text

                return final_text

            elif pix.n < 4:
                
                pix = fitz.Pixmap(fitz.csRGB, pix)
            
                pix.writePNG(f'image_page{page_number}_imageN{i + 1}.png')

                time.sleep(4)

                png_image = Image.open(f'image_page{page_number}_imageN{i + 1}.png')

                img_text = pytesseract.image_to_string(png_image)

                final_text = text + "\n" + "\n" + f"image{i+1}" + "\n" + "\n" + img_text

                return final_text

            else:

                return text
        
    else:

            return text
        

scraped_page = get_text_pdf_and_images('math.pdf', 1)

print(scraped_page)

with open("pdf_text.txt", "w", encoding= "utf-8") as f:
    f.write(scraped_page)

