from flask import Flask, request, send_file
from PIL import Image
from werkzeug import secure_filename
import shutil
import os
from generate import generate_pdf

app = Flask(__name__)
base_url = "/flipbook"

@app.route(base_url + "/")
def index():
    return "FlipBook"


@app.route(base_url + "/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        image_list = request.files.getlist("images")
        if len(image_list) != 24:
            return "Error : Invalid amount of files!"

        os.makedirs("images", exist_ok=True)
        for idx in range(24):
            name = secure_filename(image_list[idx].filename)
            image = Image.open(image_list[idx].stream)
            image.save("./images/" + name)

        generate_pdf("./images/*", "flipbook_generate.pdf")
        shutil.rmtree("images")
        return send_file("flipbook_generate.pdf",
                         as_attachment=True,
                         attachment_filename="flipbook_generate.pdf",
                         mimetype="application/pdf")

    return \
        """
        <html>
        <head>
            <title>Generate PDF</title>
        </head>
        <body>
            <h1>Upload the file to generate PDF</h1>
            <form method=\"POST\" name=\"image_form\" enctype=\"multipart/form-data\">
                <input type=\"file\" name=\"images\" multiple=\"multiple\" accept=\"image/*\"><br><br>
                <input type=\"submit\" value=\"PDF生成\">
            </form>
        </body>
        </html>
        """


if __name__ == '__main__':
    app.run(port=17000)