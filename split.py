''' Importing required libraries'''
import os
import PyPDF2


# Function to split a PDF file into multiple parts based on page range


def split_pdf(file_name, page_range, output_folder):
    '''Defining the function'''

    # Try to open the input PDF file and check if it's encrypted or not

    try:
        pdf_file = PyPDF2.PdfReader(file_name)
        if pdf_file.is_encrypted is False:
            # Get the total number of pages in the PDF file
            total_pages = len(pdf_file.pages)
            print(total_pages)
            if total_pages > 1:
                # Check if the page range is specified as a range (e.g. 2-5) or a comma-separated list of page ranges (e.g. 2-5,8-10)
                page_ranges = page_range.split(',')
                for page in page_ranges:
                    if "-" in page:
                        start_page, end_page = map(int, page.split('-'))
                        # Check if the page range is valid
                        if start_page > end_page or end_page > total_pages:
                            raise Exception(f"Error: Invalid page range ({start_page}-{end_page}), the total number of pages is {total_pages}")
                        end_page += 1
                    else:
                        start_page = int(page)
                        end_page = start_page + 1
                        # Check if the page number is valid
                        if start_page > total_pages:
                            raise Exception(
                                f"Error: Invalid page number ({start_page}), the total number of pages is {total_pages}")

                    # Create a new PDF file to store the extracted pages

                    output = PyPDF2.PdfWriter()
                    for i in range(start_page - 1, end_page-1):
                        output.add_page(pdf_file.pages[i])
                        # output.addPage(pdf_file.getPage(i))
                    # Generate the output file name
                    output_file_path = os.path.join(
                        output_folder, f"{os.path.basename(file_name).split('/')[-1]}_{page}.pdf")
                    # Write the extracted pages to the output file
                    with open(output_file_path, "wb") as output_file:
                        output.write(output_file)
            else:
                raise Exception("PDF has only one page so it cannot be splitted")
        else:
            raise Exception("PDF is password protected")
    except Exception as exception:
        # Printing the error message
        print(f"Error : {str(exception)}")
        raise exception

