import fitz  # PyMuPDF
import logging

logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    logger.info(f"Extracting text from PDF file at {pdf_path}")
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
        logger.info("Text extraction completed successfully.")
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
    return text

    
