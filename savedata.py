import json
import pdfkit



def save_text_to_md_file(text, output_filename):
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to '{output_filename}' successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")



def save_webpage_to_pdf(url, pdf_output_path):
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }
    wkhtmltopdf_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'  

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    pdfkit.from_url(url, pdf_output_path, options=options, configuration=config)
    print(f'PDF saved to {pdf_output_path}')


# url = input("Enter the url of the webpage you want to save as PDF: ")
# pdf_output_path = input("Enter the path of the PDF file: ")
# save_webpage_to_pdf(url, pdf_output_path)