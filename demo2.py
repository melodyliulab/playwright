from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/stock1.html")

# input('1....')
suggestion_text = page.locator("#suggestion").fill("this is a test")
# input('2....')
submit_button = page.locator("#submit-suggestion")
# input('3....')
submit_button.click()
# input('4....')

# try to get this element by class
stock_item_1 = page.locator(".search-header strong").inner_text()
print(stock_item_1)

# 尝试查找一个多层嵌套的元素 - 包商股份
item_2 = page.locator(".search-result .result-item:first-child p.name").inner_text()
print(item_2)
