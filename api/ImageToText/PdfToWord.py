# import libraries
import urllib

import cv2
import pytesseract
import numpy as np

class PdfToWordExample:
    @staticmethod
    def pre_processing(image):

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # converting it to binary image
        threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Maintain output window until
        # user presses a key
        cv2.waitKey(0)
        # Destroying present windows on screen
        cv2.destroyAllWindows()

        return threshold_img

    @staticmethod
    def parse_text(threshold_img, language):

        # configuring parameters for tesseract
        tesseract_config = r'--oem 3 --psm 6'
        # now feeding image to tesseract
        details = pytesseract.image_to_data(threshold_img, output_type=pytesseract.Output.DICT,
                                            config=tesseract_config, lang=language)

        return details

    @staticmethod
    def draw_boxes(image, details, threshold_point):

        total_boxes = len(details['text'])
        for sequence_number in range(total_boxes):
            if int(details['conf'][sequence_number]) > threshold_point:
                (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number],
                                details['width'][sequence_number], details['height'][sequence_number])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Maintain output window until user presses a key
        cv2.waitKey(0)
        # Destroying present windows on screen
        cv2.destroyAllWindows()

    @staticmethod
    def format_text(details):

        parse_text = []
        word_list = []
        last_word = ''
        for word in details['text']:
            if word != '':
                word_list.append(word)
                last_word = word
            if (last_word != '' and word == '') or (word == details['text'][-1]):
                parse_text.append(word_list)
                word_list = []

        return parse_text

    def write_text(formatted_text):

        out_str = " "

        # traverse in the string
        for ele in formatted_text:
            (out_str.join(ele))

    def __init__(self, path):
        self.path = path


    def RunProject(self):

        # reading image from local


        img = cv2.imdecode(np.fromstring(self.path, np.uint8), cv2.IMREAD_UNCHANGED)


        # calling pre_processing function to perform pre-processing on input image.
        thresholds_image = self.pre_processing(img)
        # calling parse_text function to get text from image by Tesseract.
        parsed_data = self.parse_text(thresholds_image, 'tur')
        # defining threshold for draw box
        accuracy_threshold = 30
        # calling draw_boxes function which will draw dox around text area.
        self.draw_boxes(thresholds_image, parsed_data, accuracy_threshold)
        # calling format_text function which will format text according to input image
        arranged_text = self.format_text(parsed_data)
        # calling write_text function which will write arranged text into file
        return arranged_text


















