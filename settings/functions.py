from settings.library import *
from settings import database
from settings import logger



requests_session = requests.Session()
requests_session.mount('http://', HTTPAdapter(max_retries=5))
requests_session.mount('https://', HTTPAdapter(max_retries=5))




# logger = logger.log()

# 时间戳转日期
def timestamp_to_date(timestamp):
    timeArray = time.localtime(float(str(timestamp)[:10]))
    date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return date


def new_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


# 日期转时间戳
def date_to_timestamp(date):
    try:
        timeArray = time.strptime(date, "%Y-%m-%d")
    except:
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    md = hashlib.md5()
    md.update(url)
    return md.hexdigest()


def selenium_driver():
    # 返回一个selenium的driver对象
    options = webdriver.ChromeOptions()
    # 浏览器开发者模式
    options.add_experimental_option('excludeSwitches', ['enable-automation'],)
    # 最大化窗口
    options.add_argument("--start-maximized")
    # 不加载图片
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    return driver


def download_response_get(url, headers=None, data=None, json=None, proxies=None, params=None, allow_redirects=True):
    try:
        response = requests_session.get(url, headers=headers, data=data, json=json, params=params, proxies=proxies, timeout=10, allow_redirects=allow_redirects)
        return response
    except:
        return 0


def download_response_post(url, headers=None, data=None, json=None, proxies=None):
    try:
        response = requests_session.post(url, headers=headers, data=data, json=json, proxies=proxies, timeout=10)
        return response
    except:
        return 0


def tm_login_cookies(driver):
    try:
        driver.get('https://login.tmall.com')
        while True:
            try:
                #判断是否出现登陆名称，报错为未登陆
                driver.find_element_by_xpath("//*[@id='login-info']/span/span")
                time.sleep(2)
                return driver
            except:
                time.sleep(5)

    except Exception as e:
        logging.error(e)

def tm_login(driver):
    #天猫登陆
    while True:
        try:
            # 是否出现登陆名称
            WebDriverWait(driver, 10, 1).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='login-info']/span/span")), "等待登陆")
            return driver
        except:
            pass


def new_date():
    # 当前日期:年月日
    now = datetime.datetime.now()
    return str(now.year) + "-" + str(now.month) + "-" + str(now.day)


def tb_slip_path():
    # 淘宝滑块一个随机轨迹
    return random.choice(json.loads(open("F:/workspace2/codes/settings/static/trajectory.txt").read()))


def tb_slider_verification(driver):
    a = 0
    while a < 5:
        a += 1
        try:
            driver.find_element_by_xpath("//*[@class='nc-lang-cnt']/a").click()
        except:
            pass
        try:
            #模拟滑块滑动
            slider = driver.find_element_by_id("nc_1_n1z")
            attl = webdriver.ActionChains(driver)
            attl.click_and_hold(slider)
            # 获取一个滑动轨迹
            for i in tb_slip_path():
                attl.move_by_offset(xoffset=i[0], yoffset=0)
            attl.release(slider).perform()
            time.sleep(5)
        except:
            time.sleep(5)

        # try:
        #     if driver.find_element_by_xpath("//*[@class='nc-lang-cnt']/b").text == '验证通过':
        #         break
        # except:
        #     pass

def isElementExist(driver, xpath):
    flag = True
    try:
        driver.find_element_by_xpath(xpath)
        return flag
    except:
        flag = False
        return flag



def check_wph_cookie(account):
    mongo_server, conn = database.mongo_mongo()
    while True:
        account = conn.order_system['account'].find_one({'name': account['name']})
        url = 'http://vis.vip.com/index.php'
        headers = {
            'Cookie': account['cookie'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'http://vis.vip.com/index.php'
        }
        res = download_response_get(url, headers=headers)
        if '首页' in res.text:
            conn.close()
            mongo_server.close()
            return account['cookie']

        else:
            conn.order_system['account'].update({'shop_id': account['shop_id']}, {'$set': {'cookie': ''}})
            time.sleep(3)





def check_jd_cookie(account):
    mongo_server, conn = database.mongo_mongo()
    while True:
        account = conn.order_system['account'].find_one({'name': account['name']})
        url = 'https://sz.jd.com/sz/view/indexs.html'
        headers = {
            'cookie': account['cookie'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'http://vis.vip.com/index.php'
        }
        res = download_response_get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            conn.close()
            mongo_server.close()
            return account['cookie']
        else:
            conn.order_system['account'].update({'shop_id': account['shop_id']}, {'$set': {'cookie': ''}})
            time.sleep(3)


def check_tm_cookie(account):
    mongo_server, conn = database.mongo_mongo()
    while True:
        account = conn.order_system['account'].find_one({'name': account['name']})
        url = 'https://mai.taobao.com/seller_admin.htm'
        headers = {
            'cookie': account['cookie'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Referer': 'http://vis.vip.com/index.php'
        }
        res = download_response_get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            conn.close()
            mongo_server.close()
            return account['cookie']
        else:
            conn.order_system['account'].update({'shop_id': account['shop_id']}, {'$set': {'cookie': ''}})
            time.sleep(3)


if __name__ == "__main__":
    # cookie = 'cookie2=173bdcd161e5c9070558a41ab5e3d494; t=203595f1eac74f18a09765ee3319eeb7; _tb_token_=587ed5355757; x=494858290; everywhere_tool_welcome=true; unb=2206831890012; sn=%E6%B4%81%E4%B8%BD%E9%9B%85%E6%97%97%E8%88%B0%E5%BA%97%3A%E6%95%B0%E6%8D%AE1; csg=6244827e; skt=a4fb7837050620cb; cna=F9t4FpRqFz0CAXPFUgtvPVtR; v=0; uc1=cookie14=UoTbm8VyMVHMPQ%3D%3D&lng=zh_CN; l=dB_9dnkVqthw5XDQKOCNZuI-gc_9jIRAguPRwqEwi_5Q618_4w7OkEvzeeJ6cjWftQYB4NSLzt29-etksZLF6Mf-DsGZ_xDc.; isg=BN_f_meo_mUYEfp7jEv1oYR_bjOp7Ev9io5SWnEseA7VAP6CeRVoNvfawtDbmAte'
    # cookie = 'JSESSIONID=16C4EE017483CDA374D3BAF1767787F0.s1;__jdb=122270672.3.15764072366172078668988|1.1576407237;__jda=122270672.15764072366172078668988.1576407237.1576407237.1576407237.1;_vender_new_=GI63BGTJFDBQ5TBHS2OP6T2WVXVHM2XDR5WKKXZL2APQPZQYA2VJMWMHGXWW7F5AFM4LIJNZLHBRINN46DESPASI3YPZH46VIBA6EQEO3OPREPBECDGF2HLSWDJJPQ6JJRHPTS76CZ5FTS3TT4TYWXKLXHURMJTZVN7GTVJPKMCPBVRQW3KIVUV7KKPCGPDLGDMICUEPCW3LHJ4JHSYRHB5PVH5XVNYCPJEDXJZON5LPCQ5OMDGHSUL33DC2B6W6HGOQTEAGEUZZIW4H6NINGKEZLBXGZGABR5L7VLFF2MZ3L54LXB7LVUXZCFXCL6VKUMM5CKSJ2YOTPNUNHMK5SEHAQS5NF6IRNYS7VKVDDHISUSOWDU3VFUB6C442HABFTNOMQG6G7TADLKUOMRVAS744EQH2PDD2L5A27UJ5CFQPXT5UXHCAGZCZSQEZ322VKFSD6LQJX26P6VIIXWR4JAVLTR754GTQZPHP5MNK7OSTMJGUD734VD2SOYDUA6DPU4YSLPNXRVGVYJLGQLA5BJFIMA6RKPTL33Z6B4JPOXQWML2MUA5DOZXRRQEQH6AGDAJUKJOTRZTIN5FXODONUWBPDQO6H43WWJHHYRTWLMNUHFX7LX2A;_BELONG_CLIENT_=WPSC4XJXWK5USS4JNZY2X7VRLR5MCBKRSVHEXABGTHDGISIQK5YOLZUXYE7IOIM7MOKO74H6CRN6WHAAR4TMDV3XZWMXZRCRT5XRNE3V356BTOB2Y7LPK66VWQK6HPTGWVXIDXDCPVE3W5WMHAIO6AT2LX2XXVNUCXR34ZWFK6HY45CORGIKOSYDYZBF27WOKTUX6BS4FZMIJWNUX6CB4JAA25ZLF7ZEKYOO4QV5HTSBXGNRM3E242MBI6V5D4C5VJDQ3EOYCOW5BMTUJZACIBHXQFAVLRF76VQY5PNJGGJNBEZHSFYYJA3YORRT7FB5AHCOIFQKF3W5RWNUX6CB4JAA26JNMO7AYWNUPZF5HTSBXGNRM3E242MBI6V5D4C5VJDQ3EOYCOW5BWZDKMOJ5BS6II53ERY6ALV3ZWPF42L4CPUHEGPYIII35KDC4FCNVCORCXFD6IVNLBEDPB2GGP4UHWNRUDOQBDIW7RZJXBA2WV5ANZOTEGUCDWYRVQS2YUTIZNZ276PRYG4N56V6YTII7MBKBC7LYHO7C555HTSBXGNRM3E466AYN67DHWVM5HQFJ4NFDO5BTDT5AQHZ7EU2EBAMZPKXZLAUCYI;_base_=YKH2KDFHMOZBLCUV7NSRBWQUJPBI7JIMU5R3EFJ5UDHJ5LCU7R2NILKK5UJ6GLA2RGYT464UKXAI5KK7PNC5B5UHJ2HVQ4ENFP57OC2LMMUEMI3EC6RZQB4TGETH4BS2SQPBWUUGJFLNLQLQVBL4USBXB3O3GCTT6M3HKXTSIWB4JZFYXUMXMCXGARN235SMJQHSXU4WI6U67KX3UU3CJVA766GKCCMD6VZ72BQNYYIUXLHENC2LH43Z6OPTT56SEVTIFQOQUSUGAPIVHZV5547A6GYEX4WLMS5LWC36LDNEERERTGCU7PSVNHI34M4P7KRVMUOKISK4PVQAQIWW3S2YBFYLQDG4WLODLRKAVVGIARICLAAHXOVXFTPOSQMJ;thor=451E3469911BFD5253B213F381497B29A3F20A7EFF3580E16285BA8468E17D3F847BF14BFFB7E8ECA040E103C8377BE9F9AA0D58783B138C25B0A670354C4E2447BA1D796A9BC88ABE16A8D75DE11D35F115C01519B4560689AAF776A5DA48DFD796B9ADF4F0124D4AE737A0E27787B78878EDDDD0549CBEB78593BF39D25A20;_tp=shJo%2FBR%2FxruZcBtRbAaYfyoNeb6k441dmph4yR9%2FozhSWmU0dr7edk6WY2CpG4BUYP4IZlQ1MVgpkRghTkdupw%3D%3D;ceshi3.com=000;pinId=ctrtCwmCaQUPQHNUrkI3QGPZAD2LllOb;pin=%E6%B4%81%E4%B8%BD%E9%9B%85%E6%96%B0%E7%81%AF%E5%A1%94;UIDKEY=50832480987944231;3AB9D23F7A4B3C9B=WYXMDD6WRLAK3AY2HV6DC5C6QETYSURGUYLMPA4337O4JJFW7ROLH33EIIFKMV5REOUCSYL2MV7NAPPBIMG727JVUE;b-sec=7Z5GQCWH5VJBHWAKHO363PS5QDYZ7LO7M4XMG5JTMED3GCGLNSLKG5SULZE7DOJMOZJKN2GZERU7R7SHF42YL6V2Q4;_pst=%E6%B4%81%E4%B8%BD%E9%9B%85%E6%96%B0%E7%81%AF%E5%A1%94;unick=%E6%B4%81%E4%B8%BD%E9%9B%85%E6%96%B0%E7%81%AF%E5%A1%94;TrackID=1rxyfriA4TUbyuQu5PnUFhcAsy0_UbwNXk0VM2ekootf3-m_t6m8Rw2OkbWRSyffTuRAvyRMPPiUMOw7eLhBCPcH13tc7Bh0XFpfQaiPloyoB-10SmI41lsh6wJMtBDfw;__jdu=15764072366172078668988;QRCodeKEY=F10E3B92E639266F53B763DA73F2FF5192C98A6F834E62131447DFA32907FA739D2938D1818DA81A6C2501F503C01641;language=zh_CN;__jdv=95931165|direct|-|none|-|1576407236619;__jdc=122270672;AESKEY=C27CF44142552518;'
#     # # cookie = ''
#     # print(check_jd_cookie(cookie))
    print(tb_slip_path())