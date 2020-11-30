import cv2
import numpy as np
import io
from PIL import Image
import base64
from .Helpers import *


class ScanDocument:
    def __init__(self, path):
        self.path = path
    def RunProject(self):




        filestr = self.path
        npimg = np.frombuffer(filestr, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        ratio = image.shape[0] / 500.0
        orig = image.copy()
        image = Helpers.resize(image, height=500)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)

        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = Helpers.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

        for c in cnts:

            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                screenCnt = approx
                break

        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

        warped = Helpers.transform(orig, screenCnt.reshape(4, 2) * ratio)

        img = cv2.cvtColor(warped, cv2.COLOR_BGR2RGB)
        file_object = io.BytesIO()
        img = Image.fromarray(Helpers.resize(img, width=500))
        img.save(file_object, 'PNG')

        base64img = base64.b64encode(file_object.getvalue()).decode('ascii')


        def write_bytesio_to_file(filename, bytesio):
            """
            Write the contents of the given BytesIO to a file.
            Creates the file or overwrites the file if it does
            not exist yet.
            """
            with open(filename, "wb") as outfile:
                # Copy the BytesIO stream to the output file
                outfile.write(bytesio.getbuffer())


        return(base64img)
        """write_bytesio_to_file("out.png", file_object)"""
