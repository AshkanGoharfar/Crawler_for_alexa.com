from bs4 import BeautifulSoup
from lxml import html
# import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random
from itertools import cycle
from multiprocessing import Pool


# try:
# def get_api_from_alexa(my_urls):
#     try:
#         from lxml import etree
#
#         print("running with lxml.etree")
#     except ImportError:
#         try:
#             # Python 2.5
#             import xml.etree.cElementTree as etree
#
#             print("running with cElementTree on Python 2.5+")
#         except ImportError:
#             try:
#                 # Python 2.5
#                 import xml.etree.ElementTree as etree
#
#                 print("running with ElementTree on Python 2.5+")
#             except ImportError:
#                 try:
#                     # normal cElementTree install
#                     import cElementTree as etree
#
#                     print("running with cElementTree")
#                 except ImportError:
#                     try:
#                         # normal ElementTree install
#                         import elementtree.ElementTree as etree
#
#                         print("running with ElementTree")
#                     except ImportError:
#                         print("Failed to import ElementTree from any known place")
#
#     page = requests.get(my_urls)
#     tree = html.fromstring(page.content)


def do_crawler_with_chromedrivers(my_urls):
    # driver = webdriver.Chrome(
    #     executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")

    driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\lib-bad\chromedriver\tools\chromedriver.exe")

    # driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
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
    # referral_sites = []

    # internet, more likely, interest level, Sites in this category this site’s audience visits
    # sites_audience_interests = []
    for tag in soup.find_all('div'):
        list_of_data.append(tag)
    # print(list_of_data[0])
    # full_data = [get_keyword_op_br(list_of_data, keyword_opportunities_breakdown),
    #              get_all_topics(list_of_data, all_topics),
    #              get_comparison_metrics(list_of_data, comparison_metrics_data),
    #              get_audience_overlap(list_of_data, audience_overlap),
    #              get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend),
    #              get_traffic_source(list_of_data, traffic_source),
    #              get_referral_sites(list_of_data, referral_sites),
    #              get_sites_audience_interests(list_of_data, sites_audience_interests)]
    all_sites_data = []
    # print('get_keyword_op_br : ' + str(get_keyword_op_br(list_of_data, keyword_opportunities_breakdown)))
    # print('get_all_topics : ' + str(get_all_topics(list_of_data, all_topics)))
    # print('get_comparison_metrics : ' + str(get_comparison_metrics(list_of_data, comparison_metrics_data)))
    # print('get_audience_overlap : ' + str(get_audience_overlap(list_of_data, audience_overlap)))
    try:
        a = get_keyword_op_br(list_of_data, keyword_opportunities_breakdown)
        b = get_all_topics(list_of_data, all_topics)
        c = get_comparison_metrics(list_of_data, comparison_metrics_data)
        d = get_audience_overlap(list_of_data, audience_overlap)
        print('get_keyword_op_br : ' + str(a))
        print('get_all_topics : ' + str(b))
        print('get_comparison_metrics : ' + str(c))
        print('get_audience_overlap : ' + str(d))
        full_data = [a, b, c, d]
        all_sites_data = [full_data]
        driver.close()
    except:
        print('ok----1')
        driver.close()

    return all_sites_data


# def get_sites_audience_interests(list_of_data, sites_audience_interests):
#     page_data = str(list_of_data[0]).split('\n')
#     current_position = 0
#     row = []
#     row2 = []
#     for item in page_data:
#         limit_for_crawl = current_position
#         if 'section class="interests"' in page_data[limit_for_crawl - 6]:
#             each_category = []
#             limit_for_depth_crawl = 45
#             while 'class="subText truncation"' in page_data[limit_for_crawl]:
#                 each_category_depth = []
#                 while '"truncation">' in page_data[limit_for_crawl + limit_for_depth_crawl]:
#                     try:
#                         row.append(str(page_data[limit_for_crawl + limit_for_depth_crawl].split('>')[1].split('<')[0]))
#                         limit_for_depth_crawl += 1
#                         # print(limit_for_crawl + limit_for_depth_crawl)
#                         # each_category.append(row)
#                     except:
#                         row.append('')
#                 try:
#                     each_category.append(str(page_data[limit_for_crawl].split('truncation">')[1].split('<')[0]))
#                     # print(each_category)
#                 except:
#                     each_category.append('')
#
#                 try:
#                     each_category.append(str(page_data[limit_for_crawl + 32].split('>')[1].split('<')[0]))
#                 except:
#                     each_category.append('')
#                 if 'bar full' in page_data[limit_for_crawl + 5]:
#                     try:
#                         each_category.append(str(page_data[limit_for_crawl + 13].split(
#                             '									        	                ')[1].split('  ')[0]))
#                         # print(each_category)
#                     except:
#                         each_category.append('')
#                 # each_category.append(
#                 #     page_data[limit_for_crawl + 25].split(' transform="translate(0, 5)">')[1].split('<')[0])
#                 # else:
#                 #     print('ok-7')
#                 #     each_category.append(page_data[limit_for_crawl + 13].split(
#                 #         '									      	                ')[1].split('  ')[0])
#                 #     print(each_category)
#                 limit_for_crawl += 69
#                 each_category.append(row)
#             sites_audience_interests.append(each_category)
#             # print(sites_audience_interests)
#             # each_category.append(each_category_depth)
#         current_position += 1
#     sites_audience_interests_sites_audience_interests_internet = []
#     sites_audience_interests_sites_audience_interests_more_likely = []
#     sites_audience_interests_interest_level = []
#     sites_audience_interests_in_this_category_this_sites_audience_visits = []
#     # print(sites_audience_interests[0])
#     # print(sites_audience_interests[0][0])
#     # print(len(sites_audience_interests[0]))
#     # print(sites_audience_interests[0])
#     for i in range(int(len(sites_audience_interests[0]) / 4)):
#         try:
#             sites_audience_interests_sites_audience_interests_internet.append(sites_audience_interests[0][(i - 2) * 4])
#             # print(sites_audience_interests_sites_audience_interests_internet)
#             sites_audience_interests_sites_audience_interests_more_likely.append(
#                 sites_audience_interests[0][(i - 2) * 4 + 1])
#             # print(sites_audience_interests_sites_audience_interests_more_likely)
#             sites_audience_interests_interest_level.append(sites_audience_interests[0][(i - 2) * 4 + 2])
#             # print(sites_audience_interests_interest_level)
#             sites_audience_interests_in_this_category_this_sites_audience_visits.append(
#                 sites_audience_interests[0][(i - 2) * 4 + 3])
#             # print(sites_audience_interests_in_this_category_this_sites_audience_visits)
#         except:
#             sites_audience_interests_sites_audience_interests_internet.append([])
#             sites_audience_interests_sites_audience_interests_more_likely.append([])
#             sites_audience_interests_interest_level.append([])
#             sites_audience_interests_in_this_category_this_sites_audience_visits.append([])
#
#     sites_audience_interests = []
#     sites_audience_interests.append(sites_audience_interests_sites_audience_interests_internet)
#     sites_audience_interests.append(sites_audience_interests_sites_audience_interests_more_likely)
#     sites_audience_interests.append(sites_audience_interests_interest_level)
#     sites_audience_interests.append(sites_audience_interests_in_this_category_this_sites_audience_visits)
#     # print('sites_audience_interests :' + str(sites_audience_interests))
#     return sites_audience_interests

#
# def get_referral_sites(list_of_data, referral_sites):
#     page_data = str(list_of_data[0]).split('\n')
#     current_position = 0
#     for item in page_data:
#         limit_for_crawl = current_position
#         each_category = []
#         if 'class="Body">' in page_data[limit_for_crawl - 2] and 'class="Row"' in page_data[
#             limit_for_crawl - 1] and 'class="site' in page_data[limit_for_crawl]:
#             while 'class="site' in page_data[limit_for_crawl]:
#                 ############# changes ! #######################
#                 try:
#                     row = [str(page_data[limit_for_crawl].split('class="truncation">')[1].split('<')[0]),
#                            str(page_data[limit_for_crawl + 2].split('">')[1].split('<')[0])]
#                     limit_for_crawl += 6
#                 except:
#                     row = ['null', 'null']
#                 ############# changes ! #######################
#                 each_category.append(row)
#             referral_sites.append(each_category)
#         current_position += 1
#         referral_sites_site_name = []
#         referral_sites_how_many_other_sites_drive_traffic_to_them = []
#     for i in range(len(referral_sites[0])):
#         referral_sites_site_name.append(referral_sites[0][i][0])
#         referral_sites_how_many_other_sites_drive_traffic_to_them.append(referral_sites[0][i][1])
#     referral_sites = []
#     referral_sites.append(referral_sites_site_name)
#     referral_sites.append(referral_sites_how_many_other_sites_drive_traffic_to_them)
#     # print('referral_sites :' + str(referral_sites))
#     return referral_sites


# def get_audience_overlap(list_of_data, audience_overlap):
#     page_data = str(list_of_data[0]).split('\n')
#     current_position = 0
#     for item in page_data:
#         limit_for_crawl = current_position
#         each_category = []
#         if '<div class="overlap" data-index="0"' in page_data[limit_for_crawl]:
#             while '<div class="overlap" data-index="' in page_data[limit_for_crawl]:
#                 row = [page_data[limit_for_crawl + 1].split('">')[1].split('<')[0],
#                        page_data[limit_for_crawl + 4].split('">')[1].split('<')[0],
#                        page_data[limit_for_crawl + 7].split('">')[1].split('<')[0]]
#                 limit_for_crawl += 11
#                 each_category.append(row)
#             audience_overlap.append(each_category)
#         current_position += 1
#         audience_overlap_percent = []
#         audience_overlap_site_name = []
#         audience_overlap_rank = []
#     # print(audience_overlap[0][0])
#     for i in range(len(audience_overlap[0])):
#         audience_overlap_percent.append(audience_overlap[0][i][0])
#         audience_overlap_site_name.append(audience_overlap[0][i][1])
#         audience_overlap_rank.append(audience_overlap[0][i][2])
#     audience_overlap = []
#     audience_overlap.append(audience_overlap_percent)
#     audience_overlap.append(audience_overlap_site_name)
#     audience_overlap.append(audience_overlap_rank)
#     # print(audience_overlap)
#     return audience_overlap

#############################################################

# def get_traffic_source(list_of_data, traffic_source):
#     page_data = str(list_of_data[0]).split('\n')
#     current_position = 0
#     for item in page_data:
#         limit_for_crawl = current_position
#         each_category = []
#         if 'div class="row-fluid" data-foldering="search" style' in page_data[limit_for_crawl]:
#             while '<div class="flex" style="margin-bottom: 12px;">' in page_data[limit_for_crawl + 1]:
#                 try:
#                     if '<span class="truncation"><strong>' in page_data[limit_for_crawl + 2]:
#                         row = [
#                             page_data[limit_for_crawl + 2].split('<span class="truncation"><strong>')[1].split('<')[0],
#                             page_data[limit_for_crawl + 5].split(
#                                 '									        	              ')[1].split('%')[0]]
#                     else:
#                         row = [
#                             page_data[limit_for_crawl + 2].split('<span class="truncation">')[1].split('<')[0],
#                             page_data[limit_for_crawl + 5].split(
#                                 '									        	              ')[1].split('%')[0]]
#                 # else:
#                 #     try:
#                 #         print('ok2')
#                 #         row = [page_data[limit_for_crawl + 2].split('class="truncation">')[1].split('<')[0],
#                 #                page_data[limit_for_crawl + 5].split(
#                 #                    '										    	              ')[1].split('%')[0]]
#                 #         print(row)
#                 except:
#                     row = ['null', 'null']
#                 limit_for_crawl += 10
#                 each_category.append(row)
#             traffic_source.append(each_category)
#         current_position += 1
#         traffic_source_str = []
#         referral_sites_how_many_other_sites_drive_traffic_to_them = []
#     # print(traffic_source[0][0][0])
#     for i in range(len(traffic_source[0])):
#         try:
#             traffic_source_str.append(traffic_source[0][i][0])
#             referral_sites_how_many_other_sites_drive_traffic_to_them.append(traffic_source[0][i][1])
#         except:
#             traffic_source_str.append('')
#             referral_sites_how_many_other_sites_drive_traffic_to_them.append('')
#     traffic_source = []
#     traffic_source.append(traffic_source_str)
#     traffic_source.append(referral_sites_how_many_other_sites_drive_traffic_to_them)
#     # print('traffic_source :' + str(traffic_source))
#     return traffic_source


# def get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend):
#     page_data = str(list_of_data[0]).split('\n')
#     current_position = 0
#     for item in page_data:
#         limit_for_crawl = current_position
#         if '<div class="rankmini-rank">' in page_data[limit_for_crawl]:
#             row = [page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0],
#                    page_data[limit_for_crawl + 9].split('									                    ')[
#                        1].split(' ')[0]]
#             alexa_rank_90_days_trend = row
#             print('alexa_rank_90_days_trend:' + str(alexa_rank_90_days_trend))
#             return alexa_rank_90_days_trend
#         current_position += 1


def get_audience_overlap(list_of_data, audience_overlap):
    page_data = str(list_of_data[0]).split('\n')
    try:
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
            audience_overlap_percent = []
            audience_overlap_site_name = []
            audience_overlap_rank = []
        # print(audience_overlap[0][0])
        for i in range(len(audience_overlap[0])):
            try:
                audience_overlap_percent.append(audience_overlap[0][i][0])
                audience_overlap_site_name.append(audience_overlap[0][i][1])
                # audience_overlap_rank.append(audience_overlap[0][i][2])
            except:
                audience_overlap_percent.append('')
                audience_overlap_site_name.append('')
                audience_overlap_rank.append('')

        audience_overlap = []
        audience_overlap.append(audience_overlap_percent)
        audience_overlap.append(audience_overlap_site_name)
        if len(audience_overlap[0]) == 1:
            audience_overlap = [[audience_overlap[0][0], 'null', 'null', 'null', 'null'],
                                [audience_overlap[1][0], 'null', 'null', 'null', 'null']]
        elif len(audience_overlap[0]) == 2:
            audience_overlap = [[audience_overlap[0][0], audience_overlap[0][1], 'null', 'null', 'null'],
                                [audience_overlap[1][0], audience_overlap[1][1], 'null', 'null', 'null']]
        elif len(audience_overlap[0]) == 3:
            audience_overlap = [
                [audience_overlap[0][0], audience_overlap[0][1], audience_overlap[0][2], 'null', 'null'],
                [audience_overlap[1][0], audience_overlap[1][1], audience_overlap[1][2], 'null', 'null']]
        elif len(audience_overlap[0]) == 4:
            audience_overlap = [
                [audience_overlap[0][0], audience_overlap[0][1], audience_overlap[0][2], audience_overlap[0][3],
                 'null'],
                [audience_overlap[1][0], audience_overlap[1][1], audience_overlap[1][2], audience_overlap[0][4],
                 'null']]
    except:
        audience_overlap = [['null', 'null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null', 'null']]
    return audience_overlap


def get_comparison_metrics(list_of_data, comparison_metrics_data):
    page_data = str(list_of_data[0]).split('\n')
    try:
        current_position = 0
        counter = 0
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
                        try:
                            row = [page_data[limit_for_crawl + 36].split('">')[1].split('<')[0],
                                   page_data[limit_for_crawl + 52].split('"> ')[1].split('<')[0]]
                        except:
                            row = ['null', 'null']
                    elif '<h3>Similar Sites by Audience Overlap</h3>' in page_data[
                        limit_for_crawl + 60]:
                        # print(page_data[limit_for_crawl + 36], page_data[limit_for_crawl + 47])
                        try:
                            row = [page_data[limit_for_crawl + 36].split('<span>')[1].split('<')[0],
                                   page_data[limit_for_crawl + 47].split('<span>')[1].split('<')[0]]
                        except:
                            row = ['null', 'null']
                    limit_for_crawl += 34
                    # print('row : ' + str(row))
                    each_category.append(row)
                    counter += 1
                comparison_metrics_data.append(each_category)

            current_position += 1
        if len(comparison_metrics_data) == 0:
            comparison_metrics_data = [[['null', 'null'], ['null', 'null'], ['null', 'null']]]
        elif len(comparison_metrics_data[0]) == 1:
            comparison_metrics_data = [[comparison_metrics_data[0][0], ['null', 'null'], ['null', 'null']]]
        elif len(comparison_metrics_data[0]) == 2:
            comparison_metrics_data = [[comparison_metrics_data[0][0], comparison_metrics_data[0][1], ['null', 'null']]]
    except:
        comparison_metrics_data = [[['null', 'null'], ['null', 'null'], ['null', 'null']]]
    # print('final comparison_metrics_data : ' + str(comparison_metrics_data))
    return comparison_metrics_data


def get_keyword_op_br(list_of_data, keyword_opportunities_breakdown):
    page_data = str(list_of_data[0]).split('\n')
    try:
        current_position = 0
        for item in page_data:
            current_position += 1
            # if '"color: rgb(84, 84, 84); in item!!!!!!!!!!!!!!
            if 'font-size="24px" text-anchor="middle">' in item:
                keyword_opportunities_breakdown.append(
                    item.split('font-size="24px" text-anchor="middle">')[1].split('<')[0])
                # print(item.split('font-size="24px" text-anchor="middle">')[1].split('<')[0])

            if '"color: rgb(84, 84, 84);' in item:
                keyword_opportunities_breakdown.append(
                    (page_data[current_position].split('<span class="truncation">')[1].split('<')[0]))
            # print('keyword_opportunities_breakdown :' + str(keyword_opportunities_breakdown))
            # print('keyword_opportunities_breakdown : ' + str(keyword_opportunities_breakdown))
        if len(keyword_opportunities_breakdown) == 5:
            keyword_opportunities_breakdown = [keyword_opportunities_breakdown[1], keyword_opportunities_breakdown[2],
                                               keyword_opportunities_breakdown[3], keyword_opportunities_breakdown[4]]
            # print('keyword_opportunities_breakdown : real : ' + str(keyword_opportunities_breakdown))
        if len(keyword_opportunities_breakdown) == 3:
            keyword_opportunities_breakdown = [keyword_opportunities_breakdown[0], keyword_opportunities_breakdown[1],
                                               keyword_opportunities_breakdown[2], 'null']
        elif len(keyword_opportunities_breakdown) == 2:
            keyword_opportunities_breakdown = [keyword_opportunities_breakdown[0], keyword_opportunities_breakdown[1],
                                               'null', 'null']
        elif len(keyword_opportunities_breakdown) == 1:
            keyword_opportunities_breakdown = [keyword_opportunities_breakdown[0], 'null',
                                               'null', 'null']
        elif len(keyword_opportunities_breakdown) == 0:
            keyword_opportunities_breakdown = ['null', 'null', 'null', 'null']
    except:
        keyword_opportunities_breakdown = ['null', 'null', 'null', 'null']
    # print('keyword_opportunities_breakdown : real ! ' + str(keyword_opportunities_breakdown))
    return keyword_opportunities_breakdown


def get_all_topics(list_of_data, all_topics):
    page_data = str(list_of_data[0]).split('\n')
    try:
        current_position = 0
        for item in page_data:
            # if '"color: rgb(84, 84, 84); in item!!!!!!!!!!!!!!
            limit_for_crawl = current_position
            each_category = []
            # print('limit_for_crawl : 1 ' + str(limit_for_crawl))
            if '<div class="keyword">' in page_data[current_position - 2] and '<div class="Row">' in page_data[
                current_position - 3] and '<div class="transparency"></div>' in page_data[
                current_position - 4] and '<div class="Body">' in page_data[current_position - 5]:
                # print('limit_for_crawl : 2 ' + str(limit_for_crawl))
                while ('<div class="keyword">' in page_data[limit_for_crawl + 9] or '</section>' in page_data[
                    limit_for_crawl + 9]):
                    counter_limit = 0
                    # print('limit_for_crawl : 3 ' + str(limit_for_crawl))
                    if '"truncation" title="' in page_data[limit_for_crawl - 1]:
                        # print('limit_for_crawl : 4 ' + str(limit_for_crawl))
                        row = [page_data[limit_for_crawl - 1].split('">')[1].split('<')[0],
                               page_data[limit_for_crawl + 2].split('">')[1].split('<')[0],
                               page_data[limit_for_crawl + 5].split('">')[1].split('<')[0]]
                        counter_limit = 1

                    else:
                        try:
                            row = [page_data[limit_for_crawl - 1].split('<span class="truncation">')[1].split('<')[0],
                                   page_data[limit_for_crawl + 2].split('<span class="truncation">')[1].split('<')[0],
                                   page_data[limit_for_crawl + 5].split('<span class="truncation">')[1].split('<')[0]]
                            counter_limit = 1
                        except:
                            row = ['null', 'null', 'null']
                            counter_limit = 1
                    # if counter_limit == 0:
                    # print(row)
                    limit_for_crawl += 11
                    each_category.append(row)

                all_topics.append(each_category)
            else:
                each_category = ['null', 'null', 'null']
            current_position += 1
        # print('all_topics : ' + str(all_topics))
        if len(all_topics) == 4:
            all_topics = [all_topics[0], all_topics[1], all_topics[2], all_topics[3],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']]]
        elif len(all_topics) == 3:
            all_topics = [all_topics[0], all_topics[1], all_topics[2],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']]]
        elif len(all_topics) == 2:
            all_topics = [all_topics[0], all_topics[1], all_topics[2],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']]]
        elif len(all_topics) == 1:
            all_topics = [all_topics[0],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']]]
        elif len(all_topics) == 0:
            all_topics = [[['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']],
                          [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                           ['null', 'null', 'null']]]
    except:
        all_topics = [[['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                       ['null', 'null', 'null']],
                      [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                       ['null', 'null', 'null']],
                      [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                       ['null', 'null', 'null']],
                      [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                       ['null', 'null', 'null']],
                      [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
                       ['null', 'null', 'null']]]
    # print('all real topics :' + str(all_topics))
    return all_topics


all_sites_data = []

# all_sites = crawl_all_links()

all_sites = []
with open("Categories.csv") as f:
    lis = [line.split() for line in f]  # create a list of lists
    fail_counter_1 = 0
    for i, x in enumerate(lis):  # print the list items
        if i > 1:
            try:
                # print(str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(' '))

                all_sites.append(
                    str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(' '))
                # print(all_sites)
            except:
                fail_counter_1 += 1
                # print('get all site data fail counter : ' + str(fail_counter_1))
                # print('list index out of range !!!!!!!!!!!!!')

# def execute_multi_proccessing(my_urls):
if __name__ == '__main__':
    category = []
    my_urls = []

    # f = open('data_V3.csv', 'w+', encoding="utf-8")
    #
    # f.write(
    #     # ' +
    #     'site link, category,keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps name, all_topics_keyword_gaps Avg traffic, all_topics_keyword_gaps search popularity ,all_topics_easy_to_rank_keywords name,all_topics_easy_to_rank_keywords relevance to site,all_topics_easy_to_rank_keywords search pop,all_topics_buyer_keywords name,all_topics_buyer_keywords Avg traffic,all_topics_buyer_keywords organic competition,all_topics_optimization_opportunities name,all_topics_optimization_opportunities search pop,all_topics_optimization_opportunities organic share of voice,all_topics_top_keywords name,all_topics_top_keywords search traffic,all_topics_top_keywords share of voice,comparison_metrics_search_traffic_this_site,comparison_metrics_search_traffic_Comp Avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience overlap sites overlap scores,audience overlap similar sites to this site')
    # f.close()

    # which_line = 180
    # print(all_sites)
    failed_counter = 0
    success_counter = 0

    failed_in_execute = 0
    j = 9800
    counter = j
    while counter < 11000:
        f = open('data_V3.csv', 'a', encoding="utf-8")
        print(all_sites[j][0], str(all_sites[j][1]))
        my_urls.append(all_sites[j][0])
        category.append(all_sites[j][1])
        all_sites_data = []
        # try:
        
        with Pool(10) as p:
            all_sites_data = p.map(do_crawler_with_chromedrivers,
                                   'https://www.alexa.com/siteinfo/' + str(all_sites[j][0]))
            #     all_sites_data = do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/' + str(all_sites[j][0]))
        counter += 1
        # except:
        print('not valid data' + '\n')
        failed_in_execute += 1
        print('failed in execute : ' + str(failed_in_execute))
        print('all site data: ' + str(all_sites_data))
        print('counter in loop : ' + str(counter))
        # print('all sites' + all_sites_data[0][0])
        full_null_data = [[['null', 'null', 'null', 'null'], [
            [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
            [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
            [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
            [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
            [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
             ['null', 'null', 'null']]], [[['null', 'null'], ['null', 'null'], ['null', 'null']]],
                           [['null', 'null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null', 'null']]]]
        try:
            if all_sites_data is not full_null_data:
                f.write('\n' +
                        str(all_sites[j][0]) + ',' + str(all_sites[j][1]) + ',' +
                        str(all_sites_data[0][0][0]) + ',' + str(all_sites_data[0][0][1]) + ',' + str(
                    all_sites_data[0][0][2]) + ',' + str(
                    all_sites_data[0][0][3]) + ',' + str(
                    all_sites_data[0][1][0][0][0] + '&' + all_sites_data[0][1][0][1][0] + '&' +
                    all_sites_data[0][1][0][2][
                        0] + '&' + all_sites_data[0][1][0][3][0]) + ',' + str(
                    all_sites_data[0][1][0][0][1] + '&' + all_sites_data[0][1][0][1][1] + '&' +
                    all_sites_data[0][1][0][2][
                        1] + '&' + all_sites_data[0][1][0][3][
                        1]) + ',' + str(
                    all_sites_data[0][1][0][0][2] + '&' + all_sites_data[0][1][0][1][2] + '&' +
                    all_sites_data[0][1][0][2][
                        2] + '&' + all_sites_data[0][1][0][3][
                        2]) + ',' + str(
                    all_sites_data[0][1][1][0][0] + '&' + all_sites_data[0][1][1][1][0] + '&' +
                    all_sites_data[0][1][1][2][
                        0] + '&' + all_sites_data[0][1][1][3][
                        0]) + ',' + str(
                    all_sites_data[0][1][1][0][1] + '&' + all_sites_data[0][1][1][1][1] + '&' +
                    all_sites_data[0][1][1][2][
                        1] + '&' + all_sites_data[0][1][1][3][
                        1]) + ',' + str(
                    all_sites_data[0][1][1][0][2] + '&' + all_sites_data[0][1][1][1][2] + '&' +
                    all_sites_data[0][1][1][2][
                        2] + '&' + all_sites_data[0][1][1][3][
                        2]) + ',' + str(
                    all_sites_data[0][1][2][0][0] + '&' + all_sites_data[0][1][2][1][0] + '&' +
                    all_sites_data[0][1][2][2][
                        0] + '&' + all_sites_data[0][1][2][3][
                        0]) + ',' + str(
                    all_sites_data[0][1][2][0][1] + '&' + all_sites_data[0][1][2][1][1] + '&' +
                    all_sites_data[0][1][2][2][
                        1] + '&' + all_sites_data[0][1][2][3][
                        1]) + ',' + str(
                    all_sites_data[0][1][2][0][2] + '&' + all_sites_data[0][1][2][1][2] + '&' +
                    all_sites_data[0][1][2][2][
                        2] + '&' + all_sites_data[0][1][2][3][
                        2]) + ',' + str(
                    all_sites_data[0][1][3][0][0] + '&' + all_sites_data[0][1][3][1][0] + '&' +
                    all_sites_data[0][1][3][2][
                        0] + '&' + all_sites_data[0][1][3][3][
                        0]) + ',' + str(
                    all_sites_data[0][1][3][0][1] + '&' + all_sites_data[0][1][3][1][1] + '&' +
                    all_sites_data[0][1][3][2][
                        1] + '&' + all_sites_data[0][1][3][3][
                        1]) + ',' + str(
                    all_sites_data[0][1][3][0][2] + '&' + all_sites_data[0][1][3][1][2] + '&' +
                    all_sites_data[0][1][3][2][
                        2] + '&' + all_sites_data[0][1][3][3][
                        2]) + ',' + str(
                    all_sites_data[0][1][4][0][0] + '&' + all_sites_data[0][1][4][1][0] + '&' +
                    all_sites_data[0][1][4][2][
                        0] + '&' + all_sites_data[0][1][4][3][
                        0]) + ',' + str(
                    all_sites_data[0][1][4][0][1] + '&' + all_sites_data[0][1][4][1][1] + '&' +
                    all_sites_data[0][1][4][2][
                        1] + '&' + all_sites_data[0][1][4][3][
                        1]) + ',' + str(
                    all_sites_data[0][1][4][0][2] + '&' + all_sites_data[0][1][4][1][2] + '&' +
                    all_sites_data[0][1][4][2][
                        2] + '&' + all_sites_data[0][1][4][3][
                        2])
                        + ',' + str(all_sites_data[0][2][0][0][0]) + ',' + str(
                    all_sites_data[0][2][0][0][1]) + ',' + str(
                    all_sites_data[0][2][0][1][0]) + ',' + str(all_sites_data[0][2][0][1][1]) + ',' + str(
                    all_sites_data[0][2][0][2][0].replace(',', '')) + ',' + str(
                    all_sites_data[0][2][0][2][1].replace(',', '')) + ',' + str(
                    all_sites_data[0][3][0][0] + '&' + all_sites_data[0][3][0][1] + '&' + all_sites_data[0][3][0][
                        2] + '&' +
                    all_sites_data[0][3][0][3] + '&' + all_sites_data[0][3][0][4]) + ',' + str(
                    all_sites_data[0][3][1][0] + '&' + all_sites_data[0][3][1][1] + '&' + all_sites_data[0][3][1][
                        2] + '&' +
                    all_sites_data[0][3][1][3] + '&' + all_sites_data[0][3][1][4]))
                print('Write to csv successfuly')
        except:
            print('can not write to csv file !')
            failed_counter += 1
            print('Write to csv fail_counter : ' + str(failed_counter))

        j += 1
        print('j out of loop : ' + str(j))
        f.close()
        print('file closed')

        print(
            '______________________________________________________________________________________________________________________________________________________________________________________')
        # print('j out of loop : ' + str(j))

    print('end task 1')
    print(failed_counter)
    print('end task 4')

# with Pool(10) as p:
#     records = p.map(execute_multi_proccessing, my_urls)
# execute_multi_proccessing(my_urls)
########### be kar giri algorithm baraye shabih sazi kalamate moshabe bara kalamati ke eshtebah type shode va to data base hast
######### be kar giri algorithm lcs longest common subsequence #######################
