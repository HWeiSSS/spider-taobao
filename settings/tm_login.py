from settings.library import *
from settings import functions


# driver = functions.selenium_driver()
# driver.get('https://login.taobao.com')


def tb_login(name, passwprd):
    driver = functions.selenium_driver()
    driver.get('https://login.taobao.com')
    while True:
        try:
            WebDriverWait(driver, 5, 0.5).until(
                EC.presence_of_element_located((By.ID, 'J_Quick2Static'))
            ).click()
        except:
            pass

        driver.find_element_by_id("TPL_username_1").send_keys(name)
        driver.find_element_by_id("TPL_password_1").send_keys(passwprd)

        time.sleep(2)

        try:
            # 模拟滑块滑动
            if driver.find_element_by_id("nc_1_n1z").get_attribute("data-spm-anchor-id"):
                functions.tb_slider_verification(driver)
            else:
                pass
        except:
            pass

        driver.find_element_by_id("J_SubmitStatic").click()

        try:
            WebDriverWait(driver, 3, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='J_Message']/p"))
            )
            return 0
        except:
            pass
        try:
            # 定位到弹出框
            iframe = driver.find_element_by_xpath("//*[@class='login-check-left']/iframe")
            driver.switch_to.frame(iframe)

            try:
                # 出现问题验证
                driver.find_element_by_xpath("//*[@class='ui-form-other']").click()
            except Exception as e:
                pass

            try:
                # 出现问题验证
                driver.find_element_by_id("otherValidator").click()
            except Exception as e:
                pass
            time.sleep(3)
            # 点击手机短信验证
            for i in driver.find_elements_by_xpath("//*[@class='select-strategy']/li"):
                if "手机验证码" in i.find_element_by_xpath("./div/h3/span").text:
                    i.find_element_by_xpath("./a").click()
            time.sleep(3)

            while True:
                try:
                    # 模拟鼠标悬浮点击获取验证码
                    webdriver.ActionChains(driver).move_to_element(
                        driver.find_element_by_id("J_GetCode")).click().perform()
                    # 是否成功获取到验证码，获得提示
                    try:
                        WebDriverWait(driver, 3, 0.5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "ui-form-explain"))
                        )
                    except:
                        pass
                    break
                except Exception as e:
                    break
            # driver.find_element_by_id("J_Phone_Checkcode").send_keys("")  # 输入验证码
            driver.find_element_by_id("submitBtn").click()  # 点击确认

            # 定位到主句柄
            driver.switch_to.default_content()

        except:
            pass
        try:
            time.sleep(5)

            driver.find_element_by_xpath('//*[contains(@id,"J_Logout") or contains(@id,"J_SiteNavMytaobao")]')
            print('----淘宝登录成功----')
            return driver, name
        except:
            continue

if __name__ == "__main__":
    # name = "洁丽雅旗舰店:数据1"
    # password = "jly123456"
    name = '15225164596'
    password = 'shan852456'
    a = tb_login(name, password)
    print(a)
    # checkCode()