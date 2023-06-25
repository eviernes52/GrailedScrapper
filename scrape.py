from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import io
import time
from PIL import Image

wd = webdriver.Chrome(service=Service("C:\\Users\\evier\\Desktop\\Python Projects\\GrailedScrapper\\chromedriver.exe"))

options = options = Options()
options.add_experimental_option("detach", True)

service = Service(executable_path="C:\\Users\\evier\\Desktop\\Python Projects\\GrailedScrapper\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=service, options=options)

image_url = "https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/auto_image/cache=expiry:max/rotate=deg:exif/resize=height:335/output=quality:50/no_metadata/compress/IDcwcOV7Tmqkc6JRDdvu"



#image from grailed function
def get_image_from_grailed(wd, delay, max_images):
    def scroll_down(wd):
            wd.execture_script("window.scrollTO(0, document.body.scrollHeight);")
            time.sleep(delay)

    url = "https://www.grailed.com/listings/43469132-dries-van-noten-dries-van-noten-vellow-backzip-bomber-jacket"
    wd.get(url)


#image download function
def download_image(download_path, url, file_name):
    try: 
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open (file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)

        print("Success!")
    except Exception as e:
        print('ERROR - Could not download - ', e)

download_image("", image_url, "test.jpg")


get_image_from_grailed(wd, 2, 10 )
# ...
#driver.quit()




