import os.path

from seleniumbase import BaseCase

#code of lecture 42
#Upload file in box - Assert the image of file below - Click on Upload button - Assert success message
class SingleFileUpload(BaseCase):
    def test_single_file_upload(self):
        self.open("https://practice-react.sdetunicorns.com/")
        xpath = '/html/body/div[1]/header/div[2]/div[1]/div/div[2]/div/nav/ul/li[5]/a'
        self.click(xpath)

        file_path = os.path.abspath('data/profile.jpeg')

        # file input selector
        file_input = '.single input[type="file"]'

        # upload file
        self.choose_file(file_input, file_path)

        # assert file is uploaded
        self.assert_element('.preview img')

        # click on upload button
        self.click('//*[@id="root"]/div/div/button')

        # assert file uploaded
        self.assert_text('Image uploaded successfully',
                         'div > div > div.react-toast-notifications__toast__content.css-1ad3zal')

        self.sleep(3)