from seleniumbase import BaseCase

class UploadPage:
    def __init__(self, sb: BaseCase):
        self.sb = sb

        #locators
        self.single_file_input = '.single input[type="file"]'
        self.multiple_file_input = '.multiple input[type="file"]'
        self.preview_image = '.preview img'
        self.upload_button = '//*[@id="root"]/div/div/button'
        self.success_message = 'div > div > div.react-toast-notifications__toast__content.css-1ad3zal'

    def open(self):
        self.sb.open("https://practice-react.sdetunicorns.com/upload")

    def upload_single_file(self, file_path):
        #uploading
        self.sb.choose_file(self.single_file_input, file_path)
        #asserting file visibility
        self.sb.assert_element('.preview img')
        self.sb.click('//*[@id="root"]/div/div/button')

    def upload_multiple_files(self, file_paths):
        multiple_file_paths = '\n'.join(file_paths)
        # uploading
        self.sb.choose_file(self.multiple_file_input, multiple_file_paths)
        # asserting file visibility
        self.sb.assert_element('.preview img')
        self.sb.click('//*[@id="root"]/div/div/button')