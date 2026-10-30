import os
import time
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Entrada import NAME, LASTNAME, EMAIL, GENDER, MOBILE, DATE_OF_BIRTH, SUBJECTS, HOBBIES,PIC, ADDRESS, STATE, CITY



options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
open_browser = webdriver.Chrome(options=options)


open_browser.get("https://demoqa.com/forms")


wait = WebDriverWait(open_browser, 10)


time.sleep(5)

practice_form = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='text' and normalize-space()='Practice Form']")
    )
)
practice_form.click()


name = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "firstName")
    )
)
name.send_keys(NAME)

lastname = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "lastName")
    )
)
lastname.send_keys(LASTNAME)

email = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "userEmail")
    )
)
email.send_keys(EMAIL)

if GENDER.lower() == "male":
    gender = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Male']")
        )
    )
    gender.click()
elif GENDER.lower() == "female":
    gender = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Female']")
        )
    )
    gender.click()
elif GENDER.lower() == "other":
    gender = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Other']")
        )
    )
    gender.click()

mobile = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "userNumber")
    )
)
mobile.send_keys(MOBILE)

dob = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "dateOfBirthInput")
    )
)
fecha = datetime.strptime(DATE_OF_BIRTH, "%d-%m-%Y").strftime("%d %b %Y")
dob.click()
dob.send_keys(Keys.CONTROL, "a")
dob.send_keys(fecha)
dob.send_keys(Keys.ENTER)

subjects = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "subjectsInput")
    )
)
for subject in SUBJECTS:
    
    subjects.send_keys(subject)
    time.sleep(1)
    subjects.send_keys(Keys.TAB)
    time.sleep(1)

hobbies = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//label[normalize-space()='{HOBBIES}']")
    )
)
hobbies.click()

photo_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    PIC,
)
if not os.path.isfile(photo_path):
    raise FileNotFoundError(f"No se encontró la imagen: {photo_path}")

picture = wait.until(
    EC.presence_of_element_located(
        (By.ID, "uploadPicture")
    )
)
picture.send_keys(photo_path)

address = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "currentAddress")
    )
)
address.send_keys(ADDRESS)

state = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "react-select-3-input")
    )
)
state.send_keys(STATE)
state.send_keys(Keys.TAB)

city = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "react-select-4-input")
    )
)
city.send_keys(CITY)
city.send_keys(Keys.TAB)

submt_btton = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)
submt_btton.click()

time.sleep(5)

