from playwright.sync_api import sync_playwright, expect

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

# 尝试写第一个case
# 验证navigation中的文本是否为所期望的文本 - 白月黑羽 股票查询
def test_navigation_title():
    nav = page.get_by_role("navigation")
    expect(nav).to_have_text("白月黑羽 股票查询")

# 尝试写第二个case, 测试nav下方的搜索框部分
def test_search_box():
    search_box_text = page.locator(".search-header strong")
    expect(search_box_text).to_have_text("请输入")
    
    # 验证搜索框是可见的， 且里面的placeholder是所期望的文本
    search_box_placeholder = page.locator("#kw")
    expect(search_box_placeholder).to_be_visible()
    expect(search_box_placeholder).to_have_attribute("placeholder", "股票名称")

    # 验证搜索框后面的button是可见的， 是一个button类型，且里面的文本时所期待的文本
    search_button = page.get_by_role("button", name="查询")
    expect(search_button).to_be_visible()

    # 验证后面的搜索框是可见的， 并且placeholder是所期望的文本
    search_box_suggestion = page.locator("#suggestion")
    expect(search_box_suggestion).to_be_visible()
    expect(search_box_suggestion).to_have_attribute("placeholder", "一句话建议")

    # 验证后面的button是可见的，且里面的文本时期望的文本内容
    search_button_suggestion = page.get_by_role("button", name="提交")
    expect(search_button_suggestion).to_be_visible()

# 尝试写第三个case, 测试搜索结果部分
def test_search_result():
    # 验证搜索部分， 输入关键字后可以搜索到对应的结果
    search_box = page.locator("#kw")
    search_box.fill("包钢股份")
    search_button = page.get_by_role("button", name="查询")
    search_button.click()
    result_name = page.locator(".search-result .result-item").first
    expect(result_name.locator("p.name")).to_have_text("包钢股份")
    # expect(result_name.locator("p").nth(1)).to_have_text("代码: 600010")
    
    # 上面一行代码运行有误, 请注意中英文半角冒号以及空格, 代码中不易发现,请使用工具check
    expect(result_name.locator("p").nth(1)).to_have_text("代码：600010")

# 尝试写第四个case, 测试提交建议按钮
def test_submit_button():
    suggestion_text = page.locator("#suggestion")
    submit_button = page.get_by_role("button", name="提交")
    suggestion_text.fill("Hello, World!")
    
    # Verify the alert before accepting it.
    def handle_dialog(dialog):
        assert dialog.message == "感谢您的支持"
        dialog.accept()

    page.once("dialog", handle_dialog)
    submit_button.click()
    # 弹出的窗口有问题, 明天找时间再看



