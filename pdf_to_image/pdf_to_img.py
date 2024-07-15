from pdf2image import convert_from_path
import fitz
# def pdf_to_image(pdf_path, output_folder):

#   pages = convert_from_path(pdf_path, 500)  # Adjust resolution as needed
#   for i, page in enumerate(pages):
#     image_path = f"{output_folder}/page_{i+1}.jpg"
#     page.save(image_path, 'JPEG')



def pdf_to_images(pdf_path, output_folder, dpi=300):
  doc = fitz.open(pdf_path)
  for page_num in range(doc.page_count):
    page = doc[page_num]
    pix = page.get_pixmap(dpi=dpi)
    output_path = f"{output_folder}/page_{page_num+1}.png"
    pix.save(output_path)
  doc.close    

pdf_to_images("C:\\Users\\muskan.tyagi\\pdf_to_img\\file_format_change\\A-Calibrate-New-Client-Intake.pdf","C:\\Users\\muskan.tyagi\\file_format_change\\pdf_to_img")