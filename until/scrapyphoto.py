from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
class SpiderPhoto(object):
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.List=[]
        self.driver = webdriver.Chrome(options=options)
        self.url = "http://image.baidu.com"
        self.header_list = [
          {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'},
        ]
    def photoname(self,key):
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").send_keys(key)
        time.sleep(1)
        self.driver.find_element_by_class_name("s_search").click()
        time.sleep(3)
    def parse_page(self):
        for i in range(600,3000,600):
            self.driver.execute_script(
                'window.scrollTo(100,{})'.format(i)
            )
            time.sleep(3)
        # html = self.driver.page_source
        # src = re.findall('src=\"(.*?)\"',html,re.S)
        r_list = self.driver.find_elements_by_xpath('//div[@class="imgbox"]//a//img')
        for x in r_list:
            self.List.append(x.get_attribute("src"))
    def work_on(self,key):
        self.photoname(key)
        self.parse_page()
        self.driver.close()
        self.driver.quit()
        return self.List

if __name__ == "__main__":
    spider = SpiderPhoto()
    spider.work_on("lily")
