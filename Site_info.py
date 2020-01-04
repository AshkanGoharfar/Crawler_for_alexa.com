import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random
from itertools import cycle


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


def do_crawler_with_chromedrivers(my_urls):
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")
    driver.get(my_urls)
    html = driver.page_source
    soup = BeautifulSoup(html)
    list_of_data = []

    # Optimization Opportunities, Keyword Gaps, Easy-to-Rank Keywords, Buyer Keywords
    keyword_opportunities_breakdown = []

    # Keyword Gaps , Easy-to-Rank Keywords , Buyer Keywords , Optimization Opportunities , Top Keywords
    all_topics = []

    # Search traffic(this site, comp avg), bounce rate(this site, comp avg), sites linking in(this site, comp avg)
    comparison_metrics_data = []

    # Sites overlap score, similar sites to this site, alexa rank
    audience_overlap = []

    # This site ranks in global internet engagement, daily time on site
    alexa_rank_90_days_trend = []

    # site name, Percentage overall site traffic from each channel in -- JUST FOR Saerch(is not premium !)
    traffic_source = []

    # referral sites, Sites by how many other sites drive traffic to them
    referral_sites = []

    # internet, more likely, interest level, Sites in this category this site’s audience visits
    sites_audience_interests = []
    # it is just for facebook -> not google
    for tag in soup.find_all('div'):
        list_of_data.append(tag)
    # print(list_of_data[0])
    full_data = [get_keyword_op_br(list_of_data, keyword_opportunities_breakdown),
                 get_all_topics(list_of_data, all_topics),
                 get_comparison_metrics(list_of_data, comparison_metrics_data),
                 get_audience_overlap(list_of_data, audience_overlap),
                 get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend),
                 get_traffic_source(list_of_data, traffic_source),
                 get_referral_sites(list_of_data, referral_sites),
                 get_sites_audience_interests(list_of_data, sites_audience_interests)]
    print()
    return full_data


def get_sites_audience_interests(list_of_data, sites_audience_interests):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    row = []
    row2 = []
    for item in page_data:
        limit_for_crawl = current_position
        if 'section class="interests"' in page_data[limit_for_crawl - 6]:
            each_category = []
            limit_for_depth_crawl = 45
            while 'class="subText truncation"' in page_data[limit_for_crawl]:
                each_category_depth = []
                while '"truncation">' in page_data[limit_for_crawl + limit_for_depth_crawl]:
                    row.append(page_data[limit_for_crawl + limit_for_depth_crawl].split('>')[1].split('<')[0])
                    limit_for_depth_crawl += 1
                    # print(limit_for_crawl + limit_for_depth_crawl)
                    # each_category.append(row)
                each_category.append(page_data[limit_for_crawl].split('truncation">')[1].split('<')[0])
                each_category.append(page_data[limit_for_crawl + 32].split('>')[1].split('<')[0])
                if 'bar full' in page_data[limit_for_crawl + 7]:
                    each_category.append(page_data[limit_for_crawl + 15].split(
                        '									      	                ')[1].split('  ')[0])
                else:
                    each_category.append(page_data[limit_for_crawl + 13].split(
                        '									      	                ')[1].split('  ')[0])
                limit_for_crawl += 69
                each_category.append(row)
                # print(each_category)
            sites_audience_interests.append(each_category)
            # each_category.append(each_category_depth)
        current_position += 1
    return sites_audience_interests


def get_referral_sites(list_of_data, referral_sites):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        each_category = []
        if 'class="Body">' in page_data[limit_for_crawl - 2] and 'class="Row"' in page_data[
            limit_for_crawl - 1] and 'class="site' in page_data[limit_for_crawl]:
            while 'class="site' in page_data[limit_for_crawl]:
                row = [page_data[limit_for_crawl].split('class="truncation">')[1].split('<')[0],
                       page_data[limit_for_crawl + 2].split('">')[1].split('<')[0]]
                limit_for_crawl += 6
                each_category.append(row)
            referral_sites.append(each_category)
        current_position += 1
    return referral_sites


def get_traffic_source(list_of_data, traffic_source):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        each_category = []
        if 'div class="row-fluid" data-foldering="search" style' in page_data[limit_for_crawl]:
            while '<div class="flex" style="margin-bottom: 12px;">' in page_data[limit_for_crawl + 1]:
                if 'class="truncation"><strong>' in page_data[limit_for_crawl + 2]:
                    row = [page_data[limit_for_crawl + 2].split('class="truncation"><strong>')[1].split('<')[0],
                           page_data[limit_for_crawl + 5].split(
                               '										    	              ')[1].split('%')[0]]
                else:
                    row = [page_data[limit_for_crawl + 2].split('class="truncation">')[1].split('<')[0],
                           page_data[limit_for_crawl + 5].split(
                               '										    	              ')[1].split('%')[0]]

                limit_for_crawl += 10
                each_category.append(row)
            traffic_source.append(each_category)
        current_position += 1
    return traffic_source


def get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        if '<div class="rankmini-rank">' in page_data[limit_for_crawl]:
            row = [page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0],
                   page_data[limit_for_crawl + 9].split('									                  ')[
                       1].split(' ')[0]]
            alexa_rank_90_days_trend = row
            return alexa_rank_90_days_trend
        current_position += 1


def get_audience_overlap(list_of_data, audience_overlap):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        each_category = []
        if '<div class="overlap" data-index="0"' in page_data[limit_for_crawl]:
            while '<div class="overlap" data-index="' in page_data[limit_for_crawl]:
                row = [page_data[limit_for_crawl + 1].split('">')[1].split('<')[0],
                       page_data[limit_for_crawl + 4].split('">')[1].split('<')[0],
                       page_data[limit_for_crawl + 7].split('">')[1].split('<')[0]]
                limit_for_crawl += 11
                each_category.append(row)
            audience_overlap.append(each_category)
        current_position += 1
    return audience_overlap


def get_comparison_metrics(list_of_data, comparison_metrics_data):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        each_category = []
        if 'span class="CompoundTooltips maxUncanny" data-alightbox="CompoundTooltips_competitors"' in page_data[
            limit_for_crawl]:
            while '"Third thissite"' in page_data[
                limit_for_crawl + 34] or '<h3>Similar Sites by Audience Overlap</h3>' in page_data[
                limit_for_crawl + 60]:
                if '"Third thissite"' in page_data[
                    limit_for_crawl + 34]:
                    row = [page_data[limit_for_crawl + 36].split('">')[1].split('<')[0],
                           page_data[limit_for_crawl + 52].split('"> ')[1].split('<')[0]]
                elif '<h3>Similar Sites by Audience Overlap</h3>' in page_data[
                    limit_for_crawl + 60]:
                    # print("ok")
                    # print(page_data[limit_for_crawl + 36], page_data[limit_for_crawl + 47])
                    row = [page_data[limit_for_crawl + 36].split('<span>')[1].split('<')[0],
                           page_data[limit_for_crawl + 47].split('<span>')[1].split('<')[0]]
                limit_for_crawl += 34
                each_category.append(row)
            comparison_metrics_data.append(each_category)

        current_position += 1
    # if comparison_metrics_data[0] == comparison_metrics_data[1]:
    #     del comparison_metrics_data[1]
    return comparison_metrics_data


# city,name,id,KEYWORD OPPORTUNITIES BREAKDOWN-optimi
# 3,tehran,2,278
def get_keyword_op_br(list_of_data, keyword_opportunities_breakdown):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        current_position += 1
        # if '"color: rgb(84, 84, 84); in item!!!!!!!!!!!!!!
        if 'font-size="24px" text-anchor="middle">' in item:
            keyword_opportunities_breakdown.append(
                item.split('font-size="24px" text-anchor="middle">')[1].split('<')[0])

        if '"color: rgb(84, 84, 84);' in item:
            keyword_opportunities_breakdown.append(
                (page_data[current_position].split('<span class="truncation">')[1].split('<')[0]))

    # print(keyword_opportunities_breakdown)
    return keyword_opportunities_breakdown


def get_all_topics(list_of_data, all_topics):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        # if '"color: rgb(84, 84, 84); in item!!!!!!!!!!!!!!
        limit_for_crawl = current_position
        each_category = []
        # print(current_position)
        if '<div class="keyword">' in page_data[current_position - 2] and '<div class="Row">' in page_data[
            current_position - 3] and '<div class="transparency"></div>' in page_data[
            current_position - 4] and '<div class="Body">' in page_data[current_position - 5]:
            while ('<div class="keyword">' in page_data[limit_for_crawl + 9] or '</section>' in page_data[
                limit_for_crawl + 9]):
                if '"truncation" title="' in page_data[limit_for_crawl - 1]:
                    row = [page_data[limit_for_crawl - 1].split('">')[1].split('<')[0],
                           page_data[limit_for_crawl + 2].split('">')[1].split('<')[0],
                           page_data[limit_for_crawl + 5].split('">')[1].split('<')[0]]
                else:
                    row = [page_data[limit_for_crawl - 1].split('<span class="truncation">')[1].split('<')[0],
                           page_data[limit_for_crawl + 2].split('<span class="truncation">')[1].split('<')[0],
                           page_data[limit_for_crawl + 5].split('<span class="truncation">')[1].split('<')[0]]
                limit_for_crawl += 11
                each_category.append(row)

            all_topics.append(each_category)
        current_position += 1
    # print(all_topics)
    return all_topics


# do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/google.com')
# get_api_from_alexa('https://www.alexa.com/siteinfo/google.com')

do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/facebook.com')
get_api_from_alexa('https://www.alexa.com/siteinfo/facebook.com')
