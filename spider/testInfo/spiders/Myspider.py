import re
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from testInfo.items import TestinfoItem


class MySpider(scrapy.Spider):

    name ='Myspider'
    allowed_domain=['wikipedia.org']
    start_url ='https://en.wikipedia.org/wiki/'

    def start_requests(self):
        url = self.start_url + 'List_of_universities_in_Australia'
        yield Request(url, self.parse)


    def parse_all(self, response):
        sel = Selector(response)
        base_url = get_base_url(response)
        item = TestinfoItem()

        item['link'] = base_url
        title_before = sel.css('title').xpath('text()').extract()
        title_clean = title_before[0].replace(' ', '_')
        title_clean = title_clean.replace('_-_Wikipedia','')
        item['title'] = title_clean

        colone = {}
        print("-------My spider--------")

        count_test = sel.xpath('count(//*[@id="mw-content-text"]/div/table[1]/tr)').extract()
        row_num1 = round(float("".join(count_test)))


        if(row_num1 != 1):
            for n in range(row_num1+2):

                col_1 = sel.xpath('//*[@id="mw-content-text"]/div/table[1]/tr[$s]/th/text()',s=n).extract()
                if(str(col_1) == " " or str(col_1) == '\n' or str(col_1) == "" or len(col_1) == 0):
                     col_1 = sel.xpath('//*[@id="mw-content-text"]/div/table[1]/tr[$s]/th//a/text()',s=n).extract()
                if (len(col_1) > 1):
                    col_1 = sel.xpath('//*[@id="mw-content-text"]/div/table[1]/tr[$s]/th//div/text()|'
                                      ' //*[@id="mw-content-text"]/div/table[1]/tr[$s]/th//a/text()'
                                                 , s=n).extract()

                col_2 = sel.xpath('//*[@id="mw-content-text"]/div/table[1]/tr[$s]/td/text() | '
                                  '//*[@id="mw-content-text"]/div/table[1]/tr[$s]/td//a/text() | '
                                  '//*[@id="mw-content-text"]/div/table[1]/tr[$s]/td//i/text()', s=n).extract()

                for i in range(len(col_1)):
                    n = col_1[i].replace(' ', '_')
                    col_1[i] = n
                    s = col_1[i].replace('\u00a0','_')
                    col_1[i] = s
                    f = re.sub(' ','_', col_1[i])
                    col_1[i] = f

                for i in range(len(col_2)):
                    col_2[i] = col_2[i].replace(' ', '_')
                    col_2[i] = col_2[i].replace(',', '')
                    rtxt = re.compile(r'"| |\n|\|.|}|{')
                    col_2[i] = rtxt.sub('', col_2[i])





                for i in col_2:
                    if (str(i) == '\n'):
                        col_2.remove(i)
                    if (i == ', '):
                        col_2.remove(i)
                    for s in range(2,10):
                        if (i == '['+str(s)+']'):
                            col_2.remove(i)
                    if (i ==' '):
                        col_2.remove(i)
                    if (i ==' ('):
                        col_2.remove(i)
                    if (i ==')'):
                        col_2.remove(i)

                colone.update(dict(zip(col_1,col_2)))

        else:
            count2 = sel.xpath('count(//*[@id="mw-content-text"]/div/table[2]/tr)').extract()
            row_num2 = round(float("".join(count2)))
            print(row_num2, title_clean)


            for m in range(1,row_num2):
                col_3 = sel.xpath('//*[@id="mw-content-text"]/div/table[2]/tr[$s]/th/text()',s=m).extract()
                print(title_clean,'Col_3',col_3,m)
                if(str(col_3) == " " or str(col_3) == '\n' or str(col_3) == "" or len(col_3) == 0):

                    col_3 = sel.xpath('//*[@id="mw-content-text"]/div/table[2]/tr[$s]/th/a/text()',s=m).extract()
                for i in col_3:
                    if (str(i) == '\n'):
                            col_3.remove(i)
                    if (i == ', '):
                            col_3.remove(i)
                    for s in range(2, 10):
                        if (i == '[' + str(s) + ']'):
                            col_4.remove(i)
                    if (i == ' '):
                            col_3.remove(i)
                    if (i == ' ('):
                            col_3.remove(i)
                    if (i == ')'):
                            col_3.remove(i)


                    if (len(col_3) > 1):
                        col_3 = sel.xpath('//*[@id="mw-content-text"]/div/table[2]/tr[$s]/th//div/text()| //*[@id="mw-content-text"]/div/table[1]/tr[$s]/th//a/text()'
                                                     , s=m).extract()
                        print('step3')
                    col_4 = sel.xpath('//*[@id="mw-content-text"]/div/table[2]/tr[$s]/td/text() | '
                                      '//*[@id="mw-content-text"]/div/table[2]/tr[$s]/td//a/text() | '
                                      '//*[@id="mw-content-text"]/div/table[2]/tr[$s]/td//i/text()', s=m).extract()
                    print(col_3,title_clean)

                    for i in range(len(col_3)):
                        n = col_3[i].replace(' ', '_')
                        col_1[i] = n
                        s = col_3[i].replace('\u00a0', '_')
                        col_1[i] = s
                        f = re.sub(' ', '_', col_1[i])
                        col_1[i] = f

                    for i in range(len(col_4)):
                        col_4[i] = col_4[i].replace(' ', '_')
                        col_4[i] = col_4[i].replace(',', '')
                        rtxt = re.compile(r'"| |\n|\|.|}|{')
                        col_4[i] = rtxt.sub('', col_4[i])



                    for i in col_4:
                        if (str(i) == '\n'):
                            col_4.remove(i)
                        if (i == ', '):
                            col_4.remove(i)
                        for s in range(2, 10):
                            if (i == '[' + str(s) + ']'):
                                col_4.remove(i)
                        if (i == ' '):
                            col_4.remove(i)
                        if (i == ' ('):
                            col_4.remove(i)
                        if (i == ')'):
                            col_4.remove(i)


                colone.update(dict(zip(col_3,col_4)))

        item['infoBox'] = colone
        return item



    def parse(self, response):
        sel = Selector(response)
        base_url = get_base_url(response)
        item = TestinfoItem()

        count = sel.xpath('count(//*[@id="mw-content-text"]/div/table/tr/td/table[1]/tr)').extract()
        print('university count',count)
        uni_num = round(float("".join(count)))
        print(uni_num)

        for n in range(2, uni_num+1):

            url = sel.xpath('//*[@id="mw-content-text"]/div/table/tr/td/table[1]/tr[$s]/td/a/text()', s=n).extract()
            link = "".join(url).replace(" ", "_")

            link = self.start_url+ link
            yield Request(link, self.parse_all)


