from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from image_convert import get_converted_images
from datetime import datetime


def generate_pdf(image_path, output_path):
    pdf_file = canvas.Canvas(output_path)

    pdf_file.setAuthor("NakagamiYuta")
    pdf_file.setTitle("Auto Generated PDF")
    pdf_file.setSubject("Original : FlipbooKit")

    image_list_A, image_list_B = get_converted_images(image_path)
    cnt_A = 23
    cnt_B = 0

    x_list = [0.19*cm, 10.65*cm]
    y_list = [1.63*cm, 10.61*cm, 19.59*cm]

    for page in range(4):
        pdf_file.setPageSize((21.0*cm, 29.7*cm))  # A4
        pdf_file.setFillColorRGB(0, 0, 0)

        x_list = [0.19*cm, 10.65*cm]
        y_list = [1.63*cm, 10.61*cm, 19.59*cm]
        y_list = [29.7*cm - pos - 4.24*cm for pos in y_list]

        for y in range(3):
            for x in range(2):
                # 枠
                pdf_file.rect(x_list[x], y_list[y] + 4.28*cm,
                              10.16*cm, -4.24*cm, stroke=1, fill=0)
                pdf_file.rect(x_list[x], y_list[y],
                              10.16*cm, -4.24*cm, stroke=1, fill=0)

                # 画像
                pdf_file.drawInlineImage(image_list_A[cnt_A % 24],
                                         x_list[x], y_list[y],
                                         width=10.16*cm, height=4.24*cm)
                pdf_file.drawInlineImage(image_list_B[cnt_B % 24],
                                         x_list[x], y_list[y] - 4.28*cm,
                                         width=10.16*cm, height=4.24*cm)

                # 注釈
                pdf_file.drawString(x_list[x], y_list[y] + 4.34*cm,
                                    str(cnt_A % 24 + 1) + "A, " + str(cnt_B % 24 + 1) + "B")
                cnt_A += 1
                cnt_B += 1

        pdf_file.drawString(11.0*cm, 0.8*cm,
                            "Page : " + str(page+1) + ", Date: " + str(datetime.now()))
        pdf_file.showPage()

    pdf_file.save()
