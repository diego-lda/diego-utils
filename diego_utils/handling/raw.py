"""The Raw module provides functionality to deal with raw data.

For example to load PDF files and update the metadata of a PDF file.
Functions:
    update_pdf_metadata
"""

from PyPDF2 import PdfFileReader, PdfFileWriter


def update_pdf_metadata(
    input_pdf_path: str,
    output_pdf_path: str,
    metadata: dict,
) -> None:
    """
    Updates the metadata of a PDF file and saves the updated PDF to a new file.

    Args:
        input_pdf_path (str): The path to the input PDF file.
        output_pdf_path (str): The path to save the output PDF file with new metadata.
        metadata (dict): A dictionary containing the metadata to be updated.
                            The keys should be metadata field names
                            and the values should be the corresponding metadata values.

    Returns
    -------
        None
    """
    # Read the existing PDF
    with open(input_pdf_path, "rb") as input_pdf_file:
        reader = PdfFileReader(input_pdf_file)
        writer = PdfFileWriter()
        writer.appendPagesFromReader(reader)

        # Check if the PDF has metadata
        existing_metadata = reader.getDocumentInfo()
        if existing_metadata:
            print("Existing metadata found:")
            for key, value in existing_metadata.items():
                print(f"{key}: {value}")
        else:
            print("No existing metadata found.")

        # Update metadata
        new_metadata = {f"/{key}": value for key, value in metadata.items()}
        writer.addMetadata(new_metadata)

        # Write the updated PDF to a new file
        with open(output_pdf_path, "wb") as output_pdf_file:
            writer.write(output_pdf_file)


if __name__ == "__main__":
    input_pdf_path = "path/to/your/input.pdf"
    output_pdf_path = "path/to/your/output.pdf"
    metadata = {
        "latest": "true",
        "release_date": "2020-04-27",
        "release_type": "real-estate-survey",
        "url_keywords": [
            "real estate",
            "survey report",
            "housing",
        ],
        "contact_name": "Macroeconomics Statistics",
        "contact_link": "mailto:macrostatistics@knbs.com",
        "title": "Real Estate Survey Report 2023/2024",
    }

    update_pdf_metadata(input_pdf_path, output_pdf_path, metadata)
