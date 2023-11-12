import time

chrome_version = ''

# https://googlechromelabs.github.io/chrome-for-testing/#stable
def GetStableWebdriverVersion():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    #return '119.0.6045.105'
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.minimize_window()
    driver.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
    #elem = driver.find_element_by_name("q")
    #elem.send_keys("pycon")
    #elem.send_keys(Keys.RETURN)
    #print(driver.page_source)
    time.sleep(5)
    version = driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[1]/td[1]/code').text
    driver.quit()
    #print(elem.text)
    SetLocalChromeVersion(version)
    return version

def GetLocalChromeVersion():
    global chrome_version 
    return chrome_version

def SetLocalChromeVersion(version):
    global chrome_version
    chrome_version = version

def DownloadLastestWebdriver(target):
    #import urllib3
    #import requests
    from urllib.request import urlopen
    import os
    
    #https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win32/chromedriver-win32.zip
    version = GetStableWebdriverVersion()
    print('download file version {} begin:\n'.format(version))
    url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/'+ version +'/win32/chromedriver-win32.zip'
    f = urlopen(url)
    with open(target, "wb") as code:
        code.write(f.read())
    print('download file end\n')

def UnzipChromeDriverZipFiles(target):
    import zipfile
    with zipfile.ZipFile(target, 'r') as zip_ref:
        zip_ref.extractall('.')

def ZipChromeDriverFiles(zipFileName):
    import zipfile
    import os

    zipObj = zipfile.ZipFile(zipFileName, 'w')

    folder = 'chromedriver-win32'
    for _,_,filename in os.walk(folder):
        for fn in filename:
            #print(fn)
            if '.exe' in fn:
                filePath = os.path.join(folder, fn)
                zipObj.write(filePath, os.path.relpath(filePath, folder))
    zipObj.close()

def CleanTmpFileAndDirs():
    import os
    import shutil
    folder = "chromedriver-win32"
    # 如果目标不存在，就不需要删除了
    if not os.path.exists(folder):
        return
    
    # 遍历删除目录中的所有文件后，再删除目录
    try:
        shutil.rmtree(folder)
    except:
        pass
    os.remove("dr_tmp.zip")

def MoveZipFile2VersionDir():
    import os
    import shutil
    #folder = os.path.join(os.getcwd, "chromedriver-win32")

    folder = "chromedriver"
    fileName = 'chromedriver-win32.zip'
    verDir = os.path.join(folder, GetLocalChromeVersion())
    if not os.path.exists(verDir):
        os.makedirs(verDir)

    targeFile = os.path.join(verDir, fileName)
    if os.access(fileName, os.F_OK) and not os.access(targeFile, os.F_OK):
        shutil.move(fileName, targeFile)

    
    target = r"D:/Server/htdocs/app/chromedriver"
    try:
        shutil.rmtree(target)
    except:
        pass
    shutil.copytree(folder, target)

if __name__ == '__main__':    
    target = "dr_tmp.zip"
    DownloadLastestWebdriver(target)
    UnzipChromeDriverZipFiles(target)

    zipFileName = "chromedriver-win32.zip"
    ZipChromeDriverFiles(zipFileName)
    CleanTmpFileAndDirs()
    #SetLocalChromeVersion('119.0.6045.105')

    MoveZipFile2VersionDir()
