import PyPDF2

#Une 2 archivos PDF en uno solo por ROBINSON SIERRA Parra
def merge_pdfs(pdf1, pdf2, output_file):
  """Párametros:
    pdf1: Ruta del primer archivo PDF.
    pdf2: Ruta del segundo archivo PDF.
    output_file: Ruta del archivo de salida.
  """      

  merger = PyPDF2.PdfMerger()
  merger.append(pdf1)
  merger.append(pdf2)
  merger.write(output_file)

if __name__ == "__main__":
  pdf1 = "DATA CLEANING.pdf"
  pdf2 = "12-12.pdf"
  output_file = "archivo_unido.pdf"

  merge_pdfs(pdf1, pdf2, output_file)

  print("Los archivos PDFS se han unido.")
