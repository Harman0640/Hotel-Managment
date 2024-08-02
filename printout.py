import os
from fpdf import FPDF
company=" Royal Hotel "
address="Jalandhar"
contact="9873853282"

class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(61, 82, 160) # RGB
        self.set_font('Helvetica', 'B', 20)

        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, company) # write on console  (width,height,text)
        self.ln(10) # line break

        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, address)
        self.ln(10)

        w = self.get_string_width(contact) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, contact)
        self.ln(10)

        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(129, 129, 129 )
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C',False)#width,height,text,border,newline,align,fill

    def page_content(self,headings,data):
        self.add_page()
        self.ln()
        self.ln()

        self.set_font('Arial', 'B', 11)
        spacing=1
        col_width = self.w /(len(headings)+1)   # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size+2

        #Table heading
        for i in headings:  # for headings
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)

        #table body
        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        # Line break

        self.ln()


        self.set_fill_color(237, 232, 245 )
        # Mention in italics
        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '(---------------------  end of page  -----------------------)'
        w = self.get_string_width(text1) + 6
        self.cell(0, 6, text1,1,0,'C',True)


if __name__ == '__main__':
    pdf = my_cust_PDF()

    headings = ['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB']


    pdf.page_content(headings)
    pdf.output('pdf_file1.pdf')
    os.system('explorer.exe "pdf_file1.pdf"')