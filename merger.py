from pypdf import PdfMerger

merger = PdfMerger()

merger.append('Aragya_Resume\main.pdf')
merger.append('Aragya_Resume\Aragya_Resume_QR_Codes\main.pdf')
merger.write('Aragya_Final_Resume.pdf')
merger.close()