from selenium import webdriver

# driver1 = webdriver.Chrome()
driver2 = webdriver.Firefox()
# driver3 = webdriver.Edge()

# driver2.maximize_window() # This command will run only for Chrome and edge browsers
driver2.set_window_size(800, 600)

driver2.get("https://firefox.com")

'''
# Verification by title
expected_title = "Get Firefox for desktop -- Mozilla (US)"
actual_title = driver2.title

if actual_title == expected_title:
    print("Firefox opened successfully")
else:
    print("Another/wrong page open")


# Verification by URL
expected_url = "https://www.mozilla.org/en-US/firefox/new/?redirect_source=firefox-com"
actual_url = driver2.current_url

if actual_url == expected_url:
    print("URL is correct")
else:
    print("URL is incorrect")
'''
#################################
# Verify title
expected_title = "Get Firefox for desktop — Mozilla (US)"
assert driver2.title == expected_title, f"Title mismatch: expected '{expected_title}' but got '{driver2.title}'"

# Verify URL
expected_url = "https://www.mozilla.org/en-US/firefox/new/?redirect_source=firefox-com"
assert driver2.current_url == expected_url, f"URL mismatch: expected '{expected_url}' but got '{driver2.current_url}'"

print("Title and URL verification passed.")
# driver2.close() # This will close the current tab
# driver2.quit()



