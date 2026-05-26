import os.path
from seleniumbase import BaseCase
import pages.Udemy_9_51_Upload_Page
from pages.Udemy_9_53_Upload_Page_Optimization import UploadPage


class TestUploadPage(BaseCase):
    def test_upload_single_file(self):
        upload_page = UploadPage(self)
        upload_page.open()

        #file path
        file_path = os.path.abspath('../data/profile.jpeg')

        upload_page.upload_single_file(file_path)

        # assert file uploaded
        self.assert_text('Image uploaded successfully',upload_page.success_message)
        self.sleep(3)

    def test_upload_multiple_files(self):
        upload_page = UploadPage(self)
        upload_page.open()

        #provide file paths
        file_path_1 = os.path.abspath('../data/1.jpg')
        file_path_2 = os.path.abspath('../data/2.jpg')

        upload_page.upload_multiple_files([file_path_1, file_path_2])

        # assert file uploaded
        self.assert_text('Images uploaded successfully', upload_page.success_message)
        self.sleep(3)