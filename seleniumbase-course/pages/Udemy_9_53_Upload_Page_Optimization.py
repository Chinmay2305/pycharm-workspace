#same file of Section9_51_Upload_page - Optimized methods upload_single_file and upload_multiple_files
from seleniumbase import BaseCase

class UploadPage:
    def __init__(self, sb: BaseCase):
        self.sb = sb

        #locators
        self.single_file_input = '.single input[type="file"]'
        self.multiple_file_input = '.multiple input[type="file"]'
        self.preview_image = '.preview img'
        self.upload_button = '.cart-main-area button'
        self.success_message = '.react-toast-notifications__toast__content'

    def open(self):
        self.sb.open("https://practice-react.sdetunicorns.com/upload")

    def _upload_file(self, file_selector, file_path):
        self.sb.choose_file(file_selector,file_path)
        self.sb.assert_element(self.preview_image)
        self.sb.click(self.upload_button)

    def upload_single_file(self, file_path):
        self._upload_file(self.single_file_input,file_path)
        #self.sb.choose_file(self.single_file_input, file_path)
        #self.sb.assert_element('.preview img')
        #self.sb.click('.cart-main-area button')

    def upload_multiple_files(self, file_paths):
        multiple_file_paths = '\n'.join(file_paths)
        self._upload_file(self.multiple_file_input, multiple_file_paths)
        #self.sb.choose_file(self.multiple_file_input, multiple_file_paths)
        #self.sb.assert_element('.preview img')
        #self.sb.click('.cart-main-area button')