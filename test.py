import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random


def get_api_from_alexa(my_urls):
    try:
        from lxml import etree

        print("running with lxml.etree")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.cElementTree as etree

            print("running with cElementTree on Python 2.5+")
        except ImportError:
            try:
                # Python 2.5
                import xml.etree.ElementTree as etree

                print("running with ElementTree on Python 2.5+")
            except ImportError:
                try:
                    # normal cElementTree install
                    import cElementTree as etree

                    print("running with cElementTree")
                except ImportError:
                    try:
                        # normal ElementTree install
                        import elementtree.ElementTree as etree

                        print("running with ElementTree")
                    except ImportError:
                        print("Failed to import ElementTree from any known place")

    page = requests.get(my_urls)
    tree = html.fromstring(page.content)

    # def get_title():
    #     title = tree.xpath('//span[@class="page-title-text"]/text()')
    #     return str(title[0])
    #     # title = str(str(tree.xpath('//span[@class="page-title-text"]/text()')[0]).split('/span')[1])
    #     # return title
    #
    # def get_rank_sites():
    #     site = tree.xpath('//div[@class="listings table"]/text()')
    #     return str(site[0])

    # print("ranks : " + str(get_title()))

    def do_crawler_with_chromedrivers():
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")
        driver.get(my_urls)
        html = driver.page_source
        soup = BeautifulSoup(html)
        list_of_data = []
        rank_sites = []
        daily_page_views_per_visitors = []
        percent_of_traffic_from_search = []
        total_sites_linking_in = []
        daily_time_on_website = []
        for tag in soup.find_all('div'):
            list_of_data.append(tag)
        full_data = [get_best_sites_name(list_of_data, rank_sites),
                     get_measurement_between_sites(list_of_data, daily_time_on_website, daily_page_views_per_visitors,
                                                   percent_of_traffic_from_search, total_sites_linking_in)]
        return full_data

    def get_best_sites_name(list_of_data, rank_sites):
        if 'listings table' in str(list_of_data[0]):
            page_data = str(list_of_data[0]).split('\n')

        for item in page_data:
            if '<a href="/siteinfo/' in item:
                print(item)
                rank_sites.append(item.split('<a href="/siteinfo/')[1].split('"')[0])
        # print(rank_sites)
        return rank_sites

    def get_measurement_between_sites(list_of_data, daily_time_on_website, daily_page_views_per_visitors,
                                      percent_of_traffic_from_search, total_sites_linking_in):
        if 'listings table' in str(list_of_data[0]):
            page_data = str(list_of_data[0]).split('\n')

        i = 0
        for item in page_data:
            if 'td right' in item:
                i += 1
                if i % 4 == 1:
                    daily_time_on_website.append(item.split('td right"><p>')[1].split('</')[0])
                elif i % 4 == 2:
                    daily_page_views_per_visitors.append(item.split('td right"><p>')[1].split('</')[0])
                elif i % 4 == 3:
                    percent_of_traffic_from_search.append(item.split('td right"><p>')[1].split('</')[0])
                elif i % 4 == 0:
                    total_sites_linking_in.append(
                        int(''.join((str(item.split('td right"><p>')[1].split('</')[0]).split(',')))))
        measurement_data = [daily_time_on_website, daily_page_views_per_visitors, percent_of_traffic_from_search,
                            total_sites_linking_in]
        # print(measurement_data)
        return measurement_data

    print(do_crawler_with_chromedrivers())


# def do_crawler_with_chrome():
#     driver = webdriver.Chrome(executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")
#     driver.get(my_urls)
#     list_1 = []
#     html = driver.page_source
#     soup = BeautifulSoup(html)
#     bought_count = -1
#     rate = -1
#     test_list = []
#     for tag in soup.find_all('div'):
#         print(str(tag))
#     # for tag in soup.find_all('div'):
#     #     if 'deal-sold tkh-sold' in str(tag).split('\n')[0]:
#     #         if bought_count != str(tag).split('\n')[0].split('gt;">')[1].split('</div')[0]:
#     #             bought_count = str(tag).split('\n')[0].split('gt;">')[1].split('</div')[0]
#     #     if 'data-rating' in str(tag).split('\n')[0]:
#     #         if rate != str(tag).split('\n')[0].split('data-rating="')[1].split('" style="width')[0]:
#     #             rate = str(tag).split('\n')[0].split('data-rating="')[1].split('" style="width')[0]
#     #     if '"inn"' in str(tag).split('\n')[0]:
#     #         test_list.append(str(tag).split('\n')[0].split('"inn">')[1].split('</div')[0])
#     # test_list_1 = []
#     # for i in range(1, len(test_list)):
#     #     if i % 4 == 1:
#     #         test_list_1.append(test_list[i])
#     # days = 10 * int(test_list_1[1]) + int(test_list_1[3])
#     # hours = 10 * int(test_list_1[5]) + int(test_list_1[7])
#     # minutes = 10 * int(test_list_1[9]) + int(test_list_1[11])
#     # time_zone_result = str(datetime.today() + timedelta(days=days, hours=hours, minutes=minutes))
#     list_of_data = []
#     # list_of_data.append(bought_count)
#     # list_of_data.append(rate)
#     # list_of_data.append(time_zone_result)
#     return list_of_data


get_api_from_alexa('https://www.alexa.com/topsites')

# def get_measurement_between_sites(list_of_data, daily_time_on_website, daily_page_views_per_visitors,
#                                   percent_of_traffic_from_search, total_sites_linking_in):
#     if 'listings table' in str(list_of_data[0]):
#         page_data = str(list_of_data[0]).split('\n')
#
#     i = 0
#     for item in page_data:
#         if 'td right' in item:
#             i += 1
#             if i % 4 == 1:
#                 daily_time_on_website.append(item.split('td right"><p>')[1].split('</')[0])
#             elif i % 4 == 2:
#                 daily_page_views_per_visitors.append(item.split('td right"><p>')[1].split('</')[0])
#             elif i % 4 == 3:
#                 percent_of_traffic_from_search.append(item.split('td right"><p>')[1].split('</')[0])
#             elif i % 4 == 0:
#                 total_sites_linking_in.append(
#                     int(''.join((str(item.split('td right"><p>')[1].split('</')[0]).split(',')))))
#     measurement_data = [daily_time_on_website, daily_page_views_per_visitors, percent_of_traffic_from_search,
#                         total_sites_linking_in]
#     print(measurement_data)
#     return measurement_data
