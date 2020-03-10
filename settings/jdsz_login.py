from settings.library import *
from settings import functions

def is_pixel_equal(img1, img2, x, y):
    """
    判断两个像素是否相同
    :param image1: 图片1
    :param image2: 图片2
    :param x: 位置x
    :param y: 位置y
    :return: 像素是否相同
    """
    # 取两个图片的像素点
    pix1 = img1.convert('RGBA').load()[x, y]
    pix2 = img2.convert('RGBA').load()[x, y]
    if abs(pix1[0]-pix2[0]) > 60:
        return True
    else:
        return False


def get_gap(img1, img2):
    """
    获取缺口偏移量
    :param img1: 不带缺口图片
    :param img2: 带缺口图片
    :return:
    """
    left = 45
    for i in range(left, img1.size[0]):
        for j in range(img1.size[1]):
            if is_pixel_equal(img1, img2, i, j):
                left = i
                return left


def generate_tracks1(s):
    # 滑动轨迹
    lists = [1, 3, 6]
    s1 = round(s / 10 * 7)
    s2 = round(s / 10 * 3)

    while s1 >= 0:
        t = random.choice([7])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)

    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, -1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def generate_tracks2(s):
    lists = [1, 2, 5]
    s1 = round(s / 10 * 6)
    s2 = round(s / 10 * 4)

    while s1 >= 0:
        t = random.choice([7])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)

    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def generate_tracks3(s):
    lists = [1, 2, 6]
    s1 = round(s / 10 * 7)
    s2 = round(s / 10 * 3)

    while s1 >= 0:
        t = random.choice([7])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)


    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def generate_tracks4(s):
    lists = [1, 2, 4]
    s1 = round(s / 10 * 8)
    s2 = round(s / 10 * 2)



    while s1 >= 0:
        t = random.choice([6])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)

    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def generate_tracks5(s):
    lists = [3, 4]
    s1 = round(s / 9 * 5)
    s2 = round(s / 9 * 4)

    while s1 >= 0:
        t = random.choice([7])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)

    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def generate_tracks6(s):
    lists = [1, 3, 7]
    s1 = round(s / 10 * 8)
    s2 = round(s / 10 * 2)

    while s1 >= 0:
        t = random.choice([8])
        s1 = s1 - t
        if s1 >= 0:
            lists.append(t)
        else:
            lists.append(t + s1)

    while s2 >= 0:
        t = random.choice([2])
        s2 = s2 - t
        if s2 >= 0:
            lists.append(t)
        else:
            lists.append(t + s2)

    back_tracks = [0, 0, 0, 0, -1, -1, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, -1, 0, 0, 0, 0, 0]
    return {'forward_tracks': lists, 'back_tracks': back_tracks}


def getPngPix(pngPath):
    # 获取1行rgb，比对缺口原图
    img_src = Image.open(pngPath)
    # convert()转换图片格式，总共有8中形式
    img_src = img_src.convert('RGBA')
    # 获取图片像素值
    str_strlist = img_src.load()
    lists = []
    # 获取第一行的像素值
    for i in range(1, img_src.size[0]):
        data = str_strlist[i, 0]
        lists.append(data)
    return lists


def get_track7(distance):
    """
    根据偏移量和手动操作模拟计算移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 时间间隔
    t = 0.2
    # 初始速度
    v = 0
    while current < distance:
        if current < mid:
            a = 3  # 加速度为+3
        else:
            a = -3  # 加速度为-3
        v0 = v  # 初速度v0
        v = v0 + a * t  # 当前速度
        move = v0 * t + 1 / 2 * a * t * t  # 移动距离
        current += move  # 当前位移
        tracks.append(round(move))  # 加入轨迹
    return tracks


def loadpage(userid, password):
    brower = functions.selenium_driver()
    url = "https://passport.shop.jd.com/login/index.action?ReturnUrl=https://shop.jd.com"
    # url1 = "https://passport.jd.com/uc/login?ltype=logout"
    brower.get(url)
    time.sleep(3)
    try:
        brower.find_element_by_id("account-login").click()
    except:
        pass
    time.sleep(3)

    iframe = brower.find_element_by_id("loginFrame")
    brower.switch_to.frame(iframe)

    username = brower.find_element_by_id("loginname")
    username.clear()
    username.send_keys(userid)
    userpswd = brower.find_element_by_id("nloginpwd")
    userpswd.send_keys(password)
    # time.sleep(5)
    brower.find_element_by_id("paipaiLoginSubmit").click()
    time.sleep(3)
    while True:
        try:
            getPic(brower)
        except:
            print("----京东登陆成功----")
            break
    time.sleep(5)

    try:
        brower.find_element_by_id("tab_phoneV").click()
        brower.find_element_by_id("sendCode").click()
        input()
    except:
        pass
    return brower, userid


def getPic(brower):
    s2 = r'//div[@class="JDJRV-bigimg"]/img'
    # 用来找到登录图片的小滑块
    s3 = r'//div/div[@class="JDJRV-slide-inner JDJRV-slide-btn"]'
    bigimg = brower.find_element_by_xpath(s2).get_attribute("src")
    # 背景大图命名
    backimg = "backimg.png"
    # 下载背景大图保存到本地
    # urlretrieve(url, filename=None, reporthook=None, data=None)
    request.urlretrieve(bigimg, backimg)
    S = 0
    father_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".")
    # 循环找出对应的完整的背景图，再通过循环比较像素点获得滑块的偏移量
    for i in os.listdir(father_path + "/jd_yzm_img"):
        pngPath = father_path + "/jd_yzm_img/" + i
        if getPngPix(pngPath) == getPngPix("./backimg.png"):
            S = get_gap(Image.open(pngPath), Image.open("./backimg.png"))

    element = brower.find_element_by_xpath(s3)
    ttt = random.choice([1, 2, 3, 4, 5, 6])
    if ttt == 1:
        S = generate_tracks1(int(S / 360 * 278))
    elif ttt == 2:
        S = generate_tracks2(int(S / 360 * 278))
    elif ttt == 3:
        S = generate_tracks3(int(S / 360 * 278))
    elif ttt == 4:
        S = generate_tracks4(int(S / 360 * 278))
    elif ttt == 5:
        S = generate_tracks5(int(S / 360 * 278))
    elif ttt == 6:
        S = generate_tracks5(int(S / 360 * 278))
    else:
        pass
    attl = ActionChains(brower)
    attl.click_and_hold(element)
    for i in S["forward_tracks"]:
        attl.move_by_offset(i, 0)

    for j in S["back_tracks"]:
        attl.move_by_offset(j, 0)

    attl.release(on_element=element).perform()
    time.sleep(3)


if __name__ == "__main__":
    name = '洁丽雅兰新灯塔'
    password = 'xin16605717007'
    loadpage(name, password)
    # checkCode()
    # get_track7(80)