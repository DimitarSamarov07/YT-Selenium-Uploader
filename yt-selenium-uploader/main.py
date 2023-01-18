from time import sleep

import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import xpathlist as xpath
from classes import FileUpload

runInVirtualDisplay = False


def initialize_driver():
    driver = uc.Chrome(version_main=108)
    driver.implicitly_wait(10)
    if runInVirtualDisplay:
        display = Display(visible=False, size=(800, 600))
        display.start()

    return driver


def signIn(driver: uc.Chrome, email, password):
    driver.get("https://www.youtube.com/")
    signInBtn = driver.find_element(By.XPATH, xpath.SIGN_IN_BUTTON)
    signInBtn.click()

    driver.find_element(By.XPATH, xpath.EMAIL_ADDRESS_INPUT).send_keys(email)
    driver.find_element(By.XPATH, xpath.NEXT_SIGN_IN).click()
    driver.find_element(By.XPATH, xpath.PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, xpath.NEXT_PASSWORD).click()


def uploadThroughStudio(driver: uc.Chrome, upload: FileUpload):
    driver.get("https://studio.youtube.com/")
    driver.find_element(By.XPATH, xpath.CREATE_BTN).click()
    driver.find_element(By.XPATH, xpath.UPLOAD_VIDEOS_BTN).click()
    driver.find_element(By.XPATH, xpath.UPLOAD_FILE_INPUT).send_keys(upload.videoPath)
    titleInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath.VIDEO_TITLE_INPUT)))
    titleInput.send_keys(upload.title)
    driver.find_element(By.XPATH, xpath.VIDEO_DESCRIPTION_INPUT).send_keys(upload.description)
    driver.find_element(By.XPATH, xpath.THUMBNAIL_FILE_INPUT).send_keys(upload.thumbnailPath)

    nextPageBtn = driver.find_element(By.XPATH, xpath.VIDEO_NEXT_BTN)
    selectNotMadeForKids = driver.find_element(By.XPATH, xpath.NOT_MADE_FOR_KIDS_RADIO)
    viewMore = driver.find_element(By.XPATH, xpath.SHOW_MORE_EXPAND)
    scrollToElement(driver, viewMore)
    selectNotMadeForKids.click()
    viewMore.click()

    tagsString = upload.getTagsSeparated(",")
    tagsInput = driver.find_element(By.XPATH, xpath.TAGS_INPUT)
    scrollToElement(driver, tagsInput)
    tagsInput.send_keys(tagsString)

    nextPageBtn.click()
    nextPageBtn.click()
    nextPageBtn.click()

    privacyXPATH = xpath.PUBLIC_RADIO_BTN

    if upload.privacy == "unlisted":
        privacyXPATH = xpath.UNLISTED_RADIO_BTN
    elif upload.privacy == "private":
        privacyXPATH = xpath.PRIVATE_RADIO_BTN

    privacyRadio = driver.find_element(By.XPATH, privacyXPATH)
    privacyRadio.click()

    saveBtn = driver.find_element(By.XPATH, xpath.SAVE_VIDEO_BTN)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(saveBtn))

    saveBtn.click()

    while saveBtn.is_displayed():
        saveBtn.click()
        sleep(5)


def scrollToElement(driver, element):
    ActionChains(driver).move_to_element(element).perform()


# drivers = initialize_driver()
# signIn(drivers, "example@example.com", "test123")
# uploadFile = FileUpload()
# uploadFile.setVideo(os.path.abspath("./final.mp4"), "public")
# uploadFile.setMetadata("Test", "Test123", ["ama", "Reddit"])
# uploadFile.setThumbnail(os.path.abspath("./thumbnail.png"))
# uploadThroughStudio(drivers, uploadFile)