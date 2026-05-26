import os.path

from seleniumbase import BaseCase

#code of lecture 44
#Upload multiple files in box - Assert the image of file below - Click on Upload button - Assert success message
class MultipleFileUpload(BaseCase):
    def test_multiple_file_upload(self):
        self.open('https://practice-react.sdetunicorns.com/')
        self.click('#root > header > div.header-padding-1.sticky-bar.header-res-padding.clearfix > div.container-fluid > div > div.col-xl-8.col-lg-8.d-none.d-lg-block > div > nav > ul > li:nth-child(5) > a')
        self.sleep(3)
        file_path1 = os.path.abspath('data/1.jpg')
        file_path2 = os.path.abspath('data/2.jpg')
        multiple_file_path = f'{file_path1}\n{file_path2}'
        #file input selector
        file_input = '.multiple input[type="file"]'

        #upload file
        self.choose_file(file_input,multiple_file_path)

        #assert the file is visible
        self.assert_element('.preview img')

        #click the upload button
        self.click('.cart-main-area button')

        #assert file uoloaded
        self.assert_text('Images uploaded successfully', 'div > div > div.react-toast-notifications__toast__content.css-1ad3zal')

        self.sleep(3)