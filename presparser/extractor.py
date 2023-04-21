import presparser.util as util
from presparser.prescription_parser import PrescriptionParser
from presparser.patientdetails_parser import PatientDetailsParser

def extractor(file_path, file_format):
    """
    This function will handle the extraction of Text from Image which is converted from OpenCV
    Utils.py will handle PDF to image conversion
    """
    # Stage1 : Extracting text from the PDF file
    
    pages = util.convert_from_path(file_path)
    document_text = " "
    if len(pages)>0:
        page = pages[0]    
        processed_image = util.preprocesing_img(page)
        extractedInformation = util.pytesseract.image_to_string(processed_image,lang = 'eng')
        document_text = '\n' + extractedInformation

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()        

    elif file_format == "patient_details":
        extracted_data = PatientDetailsParser(document_text).parse()
    
    else:
        raise Exception(f"Invalid Document:{file_format}")
    return extracted_data
