import time
from selenium import webdriver

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open Google in the first tab
driver.get("https://google.com")

# Open a new tab and automatically switch focus to it
driver.switch_to.new_window("tab")

# Open Python.org in the new tab
driver.get("https://www.python.org")

# Wait for 20 seconds
time.sleep(20)

# Switch back to the first tab (Google)
driver.switch_to.window(driver.window_handles[0])

# Print the title of the first tab
print("First tab title:", driver.title)

# Close the browser
driver.quit()
