from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# আপনার Chrome profile path দিন
profile_path = r"C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default"

options = Options()
options.add_argument(f"user-data-dir={profile_path}")  # Profile attach
options.add_experimental_option("detach", True)        # Script শেষে browser open থাকবে

# ✅ কোনো service দরকার নেই
driver = webdriver.Chrome(options=options)

# Instagram খোলা
driver.get("https://www.instagram.com/")
