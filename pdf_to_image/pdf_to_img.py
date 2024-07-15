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

pdf_to_images("C:\\Users\\muskan.tyagi\\pdf_to_img\\file_format_change\\pdf_to_img\\A-Calibrate-New-Client-Intake.pdf","C:\\Users\\muskan.tyagi\\pdf_to_img\\file_format_change\\pdf_to_img")

def pdf_to_single_images(pdf_path, output_image_path, dpi=300):
  pdf_document = fitz.open(pdf_path)
    
  # Store the images of each page
  images = []
  
  for page_num in range(len(pdf_document)):
      # Get the page
      page = pdf_document.load_page(page_num)
      
      # Render page to an image
      pix = page.get_pixmap()
      
      # Convert to a PIL image
      img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
      
      images.append(img)
  
  # Determine the total size of the final image
  total_width = max(img.width for img in images)
  total_height = sum(img.height for img in images)
  
  # Create a new blank image with the calculated size
  combined_image = Image.new('RGB', (total_width, total_height))
  
  # Paste all the images into the combined image
  current_height = 0
  for img in images:
      combined_image.paste(img, (0, current_height))
      current_height += img.height
  
  # Save the final combined image
  combined_image.save(output_image_path)

pdf_to_single_images("C:\\Users\\muskan.tyagi\\pdf_to_img\\file_format_change\\pdf_to_img\\A-Calibrate-New-Client-Intake.pdf","C:\\Users\\muskan.tyagi\\pdf_to_img\\file_format_change\\pdf_to_img\\single_img.png")
