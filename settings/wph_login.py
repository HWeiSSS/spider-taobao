from settings.library import *
from settings import functions


def wph_login(name, passwprd):
    driver = functions.selenium_driver()
    driver.get('https://vis.vip.com/login.php')
    while True:  # 验证码输入错误循环
        try:
            if '退出登录' in driver.page_source:
                print('---唯品会登录成功--')
                return driver, name
            driver.find_element_by_id("userName").send_keys(name)
            driver.find_element_by_id("passWord").send_keys(passwprd)
            # time.sleep(10)
            while True:   # 验证码识别错误处理
                driver.find_element_by_id("checkCode").click()
                get_image(driver)
                yzm = checkCode()
                if yzm and len(yzm) == 4:
                    break
            # print(yzm)
            driver.find_element_by_id("checkWord").send_keys(yzm)
            driver.find_element_by_id("subMit").click()
            time.sleep(10)
        except:
            driver.refresh()
            time.sleep(3)


def part_screenshot(driver):
    driver.save_screenshot("hello1.png")
    return Image.open("hello1.png")


def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    # img = driver.find_element_by_id("checkCode")
    # time.sleep(2)
    # location = img.location
    # location = {'x': 970, 'y': 360}
    # print(location, 111)
    # size = img.size
    # left = location['x']
    # top = location['y']
    # right = left + size['width']
    # bottom = top + size['height']
    page_snap_obj = part_screenshot(driver)
    # print((left, top, right, bottom))
    image_obj = page_snap_obj.crop((969, 359, 1070, 397))
    image_obj.save('checkcode.png')
    return image_obj  # 得到的就是验证码

def checkCode():
    image = Image.open('checkcode.png')
    gray = image.convert('L')
    threshold = 170
    # print()
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    bw = gray.point(table, "1")
    # bw.show()
    strcode = pytesseract.image_to_string(bw)
    return strcode


if __name__ == "__main__":
    name = '1509369332@qq.com'
    password = 'Cangshu_007'
    wph_login(name, password)
    # checkCode()