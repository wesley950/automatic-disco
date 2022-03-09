import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

steam_user = "wilgot8"
steam_password = "Password123x!"
target_profiles = [
    "https://steamcommunity.com/profiles/76561199250407823",
    "https://steamcommunity.com/id/Blasxhemy"
]
comments_to_make = [
    "first comment",
    "second comment"
]


driver : webdriver.Chrome = None


def perform_login() -> None:
    global driver

    # creates the chrome driver instance and navigate to the login page
    login_page_url = "https://steamcommunity.com/login/home"
    driver = webdriver.Chrome(executable_path=".\\chromedriver.exe")
    driver.maximize_window()
    driver.get(login_page_url)

    # find the input fields, submit info and click login
    login_field = driver.find_element(By.ID, "input_username")
    password_field = driver.find_element(By.ID, "input_password")
    submit_btn = driver.find_element(By.CLASS_NAME, "btn_blue_steamui")

    login_field.send_keys(steam_user)
    password_field.send_keys(steam_password)
    submit_btn.click()

    # let the user input the steam guard code whilst we are waiting for
    # the indicative element to be visible
    try:
        WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "actual_persona_name")))
    except:
        print("The program could not continue because you took too long to input the Steam Guard code.")
        exit(-3)


def make_comments() -> None:
    global target_profiles, comments_to_make, driver

    for target_profile_url in target_profiles:
        driver.get(target_profile_url)

        for comment_to_make in comments_to_make:
            try:
                comment_field = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "commentthread_textarea")))
                comment_field.send_keys(comment_to_make)
                
                try:
                    post_comment_btn = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_green_white_innerfade")))
                    post_comment_btn.click()
                    time.sleep(1)
                except:
                    print("The program could not continue because somehow the post comment button at\n%s\ndoes not seem to appear!" % (target_profile_url, ))
                    driver.quit()
                    exit(-2)

            except:
                print("The program could not continue because the provided user profile at\n%s\ndoes not accept comments or some other error occurred!" % (target_profile_url, ))
                driver.quit()
                exit(-1)


def release() -> None:
    global steam_user, steam_password, target_profiles, comments_to_make, driver

    steam_user = ""
    steam_password = ""
    target_profiles = []
    comments_to_make = []
    driver.quit()


def main() -> None:
    global steam_user, steam_password, target_profiles, comments_to_make

    while True:
        perform_login()
        make_comments()
        release()

        time.sleep(60*60*2)


if __name__ == "__main__":
    main()