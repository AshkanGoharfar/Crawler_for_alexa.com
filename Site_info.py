import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random
from itertools import cycle


# try:
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


def do_crawler_with_chromedrivers(my_urls, category):
    # driver = webdriver.Chrome(
    #     executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")

    driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
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
    # print(get_keyword_op_br(list_of_data, keyword_opportunities_breakdown),
    #              get_all_topics(list_of_data, all_topics),
    #              get_comparison_metrics(list_of_data, comparison_metrics_data),
    #              get_audience_overlap(list_of_data, audience_overlap),
    #              get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend),
    #              get_traffic_source(list_of_data, traffic_source),
    #              get_referral_sites(list_of_data, referral_sites),
    #              get_sites_audience_interests(list_of_data, sites_audience_interests))
    full_data = [get_keyword_op_br(list_of_data, keyword_opportunities_breakdown),
                 get_all_topics(list_of_data, all_topics),
                 get_comparison_metrics(list_of_data, comparison_metrics_data),
                 get_audience_overlap(list_of_data, audience_overlap),
                 get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend),
                 get_traffic_source(list_of_data, traffic_source),
                 get_referral_sites(list_of_data, referral_sites),
                 get_sites_audience_interests(list_of_data, sites_audience_interests)]
    # print(full_data)
    # if my_urls == 'https://www.alexa.com/siteinfo/google.com':
    #     google_data = [full_data]
    # elif my_urls == 'https://www.alexa.com/siteinfo/facebook.com':
    all_sites_data = [full_data]
    # print(all_sites_data)
    # f = open('data.csv', 'w+', encoding="utf-8")
    # site_data_2 = do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/facebook.com')
    # f.write(
    #     # ' +
    #     'site link, category,keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps name, all_topics_keyword_gaps Avg traffic, all_topics_keyword_gaps search popularity ,all_topics_easy_to_rank_keywords name,all_topics_easy_to_rank_keywords relevance to site,all_topics_easy_to_rank_keywords search pop,all_topics_buyer_keywords name,all_topics_buyer_keywords Avg traffic,all_topics_buyer_keywords organic competition,all_topics_optimization_opportunities name,all_topics_optimization_opportunities search pop,all_topics_optimization_opportunities organic share of voice,all_topics_top_keywords name,all_topics_top_keywords search traffic,all_topics_top_keywords share of voice,comparison_metrics_search_traffic_this_site,comparison_metrics_search_traffic_Comp Avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience overlap sites overlap scores,audience overlap similar sites to this site,audience overlap alexa rank,alexa rank in 90 day trend in global internet engagement,alexa rank in 90 day trend daily time on site,traffic_source_site name,traffic_source_Percentage_overall_site_traffic,referral_sites_names,referral_sites_how_many_other_sites_drive_traffic_to_them,sites_audience_interests_internet,sites_audience_interests_more likely,sites_audience_interests_interest_level\n')

    # for i in range(0, 1):
    # all_sites_data.encode('utf-8')
    # print(all_sites_data[0][0][0])
    # print(all_sites_data[0][7])
    # print(all_sites_data[0][2][0][2][0])
    # print(all_sites_data[0][5][0])
    # print(all_sites_data[0][5][1])
    # print(all_sites_data[0][7][3])

    return all_sites_data


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
                # print(each_category)
                if 'bar full' in page_data[limit_for_crawl + 5]:
                    try:
                        each_category.append(page_data[limit_for_crawl + 13].split(
                            '									        	                ')[1].split('  ')[0])
                        # print(each_category)
                    except:
                        each_category.append('')
                # each_category.append(
                #     page_data[limit_for_crawl + 25].split(' transform="translate(0, 5)">')[1].split('<')[0])
                # else:
                #     print('ok-7')
                #     each_category.append(page_data[limit_for_crawl + 13].split(
                #         '									      	                ')[1].split('  ')[0])
                #     print(each_category)
                limit_for_crawl += 69
                each_category.append(row)
            sites_audience_interests.append(each_category)
            # print(sites_audience_interests)
            # each_category.append(each_category_depth)
        current_position += 1
    sites_audience_interests_sites_audience_interests_internet = []
    sites_audience_interests_sites_audience_interests_more_likely = []
    sites_audience_interests_interest_level = []
    sites_audience_interests_in_this_category_this_sites_audience_visits = []
    # print(sites_audience_interests[0])
    # print(sites_audience_interests[0][0])
    # print(len(sites_audience_interests[0]))
    # print(sites_audience_interests[0])
    for i in range(int(len(sites_audience_interests[0]) / 4)):
        try:
            sites_audience_interests_sites_audience_interests_internet.append(sites_audience_interests[0][(i - 2) * 4])
            # print(sites_audience_interests_sites_audience_interests_internet)
            sites_audience_interests_sites_audience_interests_more_likely.append(
                sites_audience_interests[0][(i - 2) * 4 + 1])
            # print(sites_audience_interests_sites_audience_interests_more_likely)
            sites_audience_interests_interest_level.append(sites_audience_interests[0][(i - 2) * 4 + 2])
            # print(sites_audience_interests_interest_level)
            sites_audience_interests_in_this_category_this_sites_audience_visits.append(
                sites_audience_interests[0][(i - 2) * 4 + 3])
            # print(sites_audience_interests_in_this_category_this_sites_audience_visits)
        except:
            sites_audience_interests_sites_audience_interests_internet.append([])
            sites_audience_interests_sites_audience_interests_more_likely.append([])
            sites_audience_interests_interest_level.append([])
            sites_audience_interests_in_this_category_this_sites_audience_visits.append([])

    sites_audience_interests = []
    sites_audience_interests.append(sites_audience_interests_sites_audience_interests_internet)
    sites_audience_interests.append(sites_audience_interests_sites_audience_interests_more_likely)
    sites_audience_interests.append(sites_audience_interests_interest_level)
    sites_audience_interests.append(sites_audience_interests_in_this_category_this_sites_audience_visits)
    # print('sites_audience_interests :' + str(sites_audience_interests))
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
                ############# changes ! #######################
                try:
                    row = [page_data[limit_for_crawl].split('class="truncation">')[1].split('<')[0],
                           page_data[limit_for_crawl + 2].split('">')[1].split('<')[0]]
                    limit_for_crawl += 6
                except:
                    row = ['', '']
                ############# changes ! #######################
                each_category.append(row)
            referral_sites.append(each_category)
        current_position += 1
        referral_sites_site_name = []
        referral_sites_how_many_other_sites_drive_traffic_to_them = []
    for i in range(len(referral_sites[0])):
        referral_sites_site_name.append(referral_sites[0][i][0])
        referral_sites_how_many_other_sites_drive_traffic_to_them.append(referral_sites[0][i][1])
    referral_sites = []
    referral_sites.append(referral_sites_site_name)
    referral_sites.append(referral_sites_how_many_other_sites_drive_traffic_to_them)
    # print('referral_sites :' + str(referral_sites))
    return referral_sites


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

def get_traffic_source(list_of_data, traffic_source):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        each_category = []
        if 'div class="row-fluid" data-foldering="search" style' in page_data[limit_for_crawl]:
            while '<div class="flex" style="margin-bottom: 12px;">' in page_data[limit_for_crawl + 1]:
                try:
                    if '<span class="truncation"><strong>' in page_data[limit_for_crawl + 2]:
                        row = [
                            page_data[limit_for_crawl + 2].split('<span class="truncation"><strong>')[1].split('<')[0],
                            page_data[limit_for_crawl + 5].split(
                                '									        	              ')[1].split('%')[0]]
                    else:
                        row = [
                            page_data[limit_for_crawl + 2].split('<span class="truncation">')[1].split('<')[0],
                            page_data[limit_for_crawl + 5].split(
                                '									        	              ')[1].split('%')[0]]
                # else:
                #     try:
                #         print('ok2')
                #         row = [page_data[limit_for_crawl + 2].split('class="truncation">')[1].split('<')[0],
                #                page_data[limit_for_crawl + 5].split(
                #                    '										    	              ')[1].split('%')[0]]
                #         print(row)
                except:
                    row = ['', '']
                limit_for_crawl += 10
                each_category.append(row)
            traffic_source.append(each_category)
        current_position += 1
        traffic_source_str = []
        referral_sites_how_many_other_sites_drive_traffic_to_them = []
    # print(traffic_source[0][0][0])
    for i in range(len(traffic_source[0])):
        try:
            traffic_source_str.append(traffic_source[0][i][0])
            referral_sites_how_many_other_sites_drive_traffic_to_them.append(traffic_source[0][i][1])
        except:
            traffic_source_str.append('')
            referral_sites_how_many_other_sites_drive_traffic_to_them.append('')
    traffic_source = []
    traffic_source.append(traffic_source_str)
    traffic_source.append(referral_sites_how_many_other_sites_drive_traffic_to_them)
    # print('traffic_source :' + str(traffic_source))
    return traffic_source


def get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend):
    page_data = str(list_of_data[0]).split('\n')
    current_position = 0
    for item in page_data:
        limit_for_crawl = current_position
        if '<div class="rankmini-rank">' in page_data[limit_for_crawl]:
            row = [page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0],
                   page_data[limit_for_crawl + 9].split('									                    ')[
                       1].split(' ')[0]]
            alexa_rank_90_days_trend = row
            # print('alexa_rank_90_days_trend:' + str(alexa_rank_90_days_trend))
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
        audience_overlap_percent = []
        audience_overlap_site_name = []
        audience_overlap_rank = []
    # print(audience_overlap[0][0])
    for i in range(len(audience_overlap[0])):
        try:
            audience_overlap_percent.append(audience_overlap[0][i][0])
            audience_overlap_site_name.append(audience_overlap[0][i][1])
            audience_overlap_rank.append(audience_overlap[0][i][2])
        except:
            audience_overlap_percent.append('')
            audience_overlap_site_name.append('')
            audience_overlap_rank.append('')

    audience_overlap = []
    audience_overlap.append(audience_overlap_percent)
    audience_overlap.append(audience_overlap_site_name)
    audience_overlap.append(audience_overlap_rank)
    # print('audience_overlap :' + str(audience_overlap))
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
    # print('comparison_metrics_data :' + str(comparison_metrics_data))
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
            # print(keyword_opportunities_breakdown)

        if '"color: rgb(84, 84, 84);' in item:
            keyword_opportunities_breakdown.append(
                (page_data[current_position].split('<span class="truncation">')[1].split('<')[0]))
        # print(keyword_opportunities_breakdown)

    # print('keyword_opportunities_breakdown :' + str(keyword_opportunities_breakdown))
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
                    try:
                        row = [page_data[limit_for_crawl - 1].split('<span class="truncation">')[1].split('<')[0],
                               page_data[limit_for_crawl + 2].split('<span class="truncation">')[1].split('<')[0],
                               page_data[limit_for_crawl + 5].split('<span class="truncation">')[1].split('<')[0]]
                    except:
                        row = ['', '', '']

                limit_for_crawl += 11
                each_category.append(row)

            all_topics.append(each_category)
        current_position += 1
    # print('all_topics :' + str(all_topics))
    return all_topics


# def write_in_data_csv():

# do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/google.com')
# get_api_from_alexa('https://www.alexa.com/siteinfo/google.com')

######################################################################################
######################################################################################
# def crawl_all_links():
#     driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
#     driver.get('https://www.alexa.com/topsites/category')
#     html = driver.page_source
#     soup = BeautifulSoup(html)
#     list_of_data = []
#     for tag in soup.find_all('div'):
#         list_of_data.append(tag)
#     links = []
#     # full_data = [links]
#     tags = []
#     # print(list_of_data[0])
#     for item in str(list_of_data[0]).split('\n'):
#         if 'li><a href="/topsites/category/Top/' in item:
#             links.append(item.split('">')[1].split('<')[0])
#     sites_and_categories = []
#     for element in links:
#         driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
#         url = 'https://www.alexa.com/topsites/category/Top/' + str(element)
#         driver.get(url)
#         html = driver.page_source
#         soup = BeautifulSoup(html)
#         list_of_data = []
#         for tag in soup.find_all('div'):
#             list_of_data.append(tag)
#         # get_direct_links(element, url)
#         same_category = []
#         for item in str(list_of_data[0]).split('\n'):
#             site_data = []
#             if '<a href="/siteinfo/' in item:
#                 site_name = item.split('fo/')[1].split('">')[0]
#                 site_data = [site_name, url]
#                 sites_and_categories.append(site_data)
#     # print(sites_and_categories)
#     return sites_and_categories
######################################################################################
######################################################################################

# changes !
all_sites_data = []

# all_sites = crawl_all_links()

all_sites = []
with open("sites.csv") as f:
    lis = [line.split() for line in f]  # create a list of lists
    for i, x in enumerate(lis):  # print the list items
        if i > 0:
            all_sites.append(
                str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(' '))
# print(all_sites)

category = []
my_urls = []

which_line = 20
j = 20
counter = j
while counter < 27:
    if all_sites[j][0] != 'bongacams.com' and all_sites[j][0] != 'fetlife.com' and all_sites[j][0] != 'liveleak.com' and \
            all_sites[j][
                0] != 'ebaumsworld.com' and all_sites[j][0] != 'iafd.com' and all_sites[j][0] != 'nudevista.com' and \
            all_sites[j][
                0] != 'adam4adam.com' and all_sites[j][0] != 'gfy.com' and all_sites[j][0] != 'nhentai.net' and \
            all_sites[j][0] != 'cam4.com':
        # print(all_sites[j][0])
        # print(all_sites[j][1])
        print(all_sites[j][0], str(all_sites[j][1]))
        my_urls.append(all_sites[j][0])
        category.append(all_sites[j][1])
        try:
            # print('https://www.alexa.com/siteinfo/' + str(all_sites[j][0]), str(all_sites[j][1]))
            all_sites_data.append(do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/' + str(all_sites[j][0]),
                                                                str(all_sites[j][1])))
            which_line += 1
            counter += 1
        except:
            print('not valid data' + '\n')
        # print(all_sites_data[j][0])
        print('counter in loop : ' + str(counter))
        print('which line : ' + str(which_line))
        # print(counter)
    j += 1
    print('j out of lopp : ' + str(j))
    print(
        '______________________________________________________________________________________________________________________________________________________________________________________')
    # print('j out of loop : ' + str(j))

print('end task 1')

# print(all_sites_data)

# f = open('data.csv', 'w+', encoding="utf-8", newline='')

f = open('data.csv', 'a', encoding="utf-8")
# site_data_2 = do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/facebook.com')
# print(all_sites_data)
# 
# all_sites_data = all_sites_data[0]
# print(all_sites_data[0])

# f.write(
#     # ' +
#     'site link, category,keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps name, all_topics_keyword_gaps Avg traffic, all_topics_keyword_gaps search popularity ,all_topics_easy_to_rank_keywords name,all_topics_easy_to_rank_keywords relevance to site,all_topics_easy_to_rank_keywords search pop,all_topics_buyer_keywords name,all_topics_buyer_keywords Avg traffic,all_topics_buyer_keywords organic competition,all_topics_optimization_opportunities name,all_topics_optimization_opportunities search pop,all_topics_optimization_opportunities organic share of voice,all_topics_top_keywords name,all_topics_top_keywords search traffic,all_topics_top_keywords share of voice,comparison_metrics_search_traffic_this_site,comparison_metrics_search_traffic_Comp Avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience overlap sites overlap scores,audience overlap similar sites to this site,audience overlap alexa rank,alexa rank in 90 day trend in global internet engagement,alexa rank in 90 day trend daily time on site,traffic_source_site name,traffic_source_Percentage_overall_site_traffic,referral_sites_names,referral_sites_how_many_other_sites_drive_traffic_to_them,sites_audience_interests_internet,sites_audience_interests_more likely,sites_audience_interests_interest_level')
# print('end task 2')

# q = 8
# for k in range(0, 7):
#     f.write('\n')

for i in range(len(all_sites_data)):
    print('end task shit!')
    f.write('\n' +
            str(my_urls[i]) + ',' + str(category[i]) + ',' +
            str(all_sites_data[i][0][0][1]) + ',' + str(all_sites_data[i][0][0][2]) + ',' + str(
        all_sites_data[i][0][0][3]) + ',' + str(
        all_sites_data[i][0][0][
            4]) + ',' + str(
        all_sites_data[i][0][1][0][0][0] + '&' + all_sites_data[i][0][1][0][1][0] + '&' + all_sites_data[i][0][1][0][2][
            0] + '&' + all_sites_data[i][0][1][0][3][0]) + ',' + str(
        all_sites_data[i][0][1][0][0][1] + '&' + all_sites_data[i][0][1][0][1][1] + '&' + all_sites_data[i][0][1][0][2][
            1] + '&' + all_sites_data[i][0][1][0][3][
            1]) + ',' + str(
        all_sites_data[i][0][1][0][0][2] + '&' + all_sites_data[i][0][1][0][1][2] + '&' + all_sites_data[i][0][1][0][2][
            2] + '&' + all_sites_data[i][0][1][0][3][
            2]) + ',' + str(
        all_sites_data[i][0][1][1][0][0] + '&' + all_sites_data[i][0][1][1][1][0] + '&' + all_sites_data[i][0][1][1][2][
            0] + '&' + all_sites_data[i][0][1][1][3][
            0]) + ',' + str(
        all_sites_data[i][0][1][1][0][1] + '&' + all_sites_data[i][0][1][1][1][1] + '&' + all_sites_data[i][0][1][1][2][
            1] + '&' + all_sites_data[i][0][1][1][3][
            1]) + ',' + str(
        all_sites_data[i][0][1][1][0][2] + '&' + all_sites_data[i][0][1][1][1][2] + '&' + all_sites_data[i][0][1][1][2][
            2] + '&' + all_sites_data[i][0][1][1][3][
            2]) + ',' + str(
        all_sites_data[i][0][1][2][0][0] + '&' + all_sites_data[i][0][1][2][1][0] + '&' + all_sites_data[i][0][1][2][2][
            0] + '&' + all_sites_data[i][0][1][2][3][
            0]) + ',' + str(
        all_sites_data[i][0][1][2][0][1] + '&' + all_sites_data[i][0][1][2][1][1] + '&' + all_sites_data[i][0][1][2][2][
            1] + '&' + all_sites_data[i][0][1][2][3][
            1]) + ',' + str(
        all_sites_data[i][0][1][2][0][2] + '&' + all_sites_data[i][0][1][2][1][2] + '&' + all_sites_data[i][0][1][2][2][
            2] + '&' + all_sites_data[i][0][1][2][3][
            2]) + ',' + str(
        all_sites_data[i][0][1][3][0][0] + '&' + all_sites_data[i][0][1][3][1][0] + '&' + all_sites_data[i][0][1][3][2][
            0] + '&' + all_sites_data[i][0][1][3][3][
            0]) + ',' + str(
        all_sites_data[i][0][1][3][0][1] + '&' + all_sites_data[i][0][1][3][1][1] + '&' + all_sites_data[i][0][1][3][2][
            1] + '&' + all_sites_data[i][0][1][3][3][
            1]) + ',' + str(
        all_sites_data[i][0][1][3][0][2] + '&' + all_sites_data[i][0][1][3][1][2] + '&' + all_sites_data[i][0][1][3][2][
            2] + '&' + all_sites_data[i][0][1][3][3][
            2]) + ',' + str(
        all_sites_data[i][0][1][4][0][0] + '&' + all_sites_data[i][0][1][4][1][0] + '&' + all_sites_data[i][0][1][4][2][
            0] + '&' + all_sites_data[i][0][1][4][3][
            0] + '&' + all_sites_data[i][0][1][4][4][
            0]) + ',' + str(
        all_sites_data[i][0][1][4][0][1] + '&' + all_sites_data[i][0][1][4][1][1] + '&' + all_sites_data[i][0][1][4][2][
            1] + '&' + all_sites_data[i][0][1][4][3][
            1] + '&' + all_sites_data[i][0][1][4][4][
            1]) + ',' + str(
        all_sites_data[i][0][1][4][0][2] + '&' + all_sites_data[i][0][1][4][1][2] + '&' + all_sites_data[i][0][1][4][2][
            2] + '&' + all_sites_data[i][0][1][4][3][
            2] + '&' + all_sites_data[i][0][1][4][4][2])
            + ',' + str(all_sites_data[i][0][2][0][0][0]) + ',' + str(all_sites_data[i][0][2][0][0][1]) + ',' + str(
        all_sites_data[i][0][2][0][1][0]) + ',' + str(all_sites_data[i][0][2][0][1][1]) + ',' + str(
        all_sites_data[i][0][2][0][2][0].replace(',', '')) + ',' + str(
        all_sites_data[i][0][2][0][2][1].replace(',', '')) + ',' + str(
        all_sites_data[i][0][3][0][0] + '&' + all_sites_data[i][0][3][0][1] + '&' + all_sites_data[i][0][3][0][
            2] + '&' +
        all_sites_data[i][0][3][0][3] + '&' + all_sites_data[i][0][3][0][4]) + ',' + str(
        all_sites_data[i][0][3][1][0] + '&' + all_sites_data[i][0][3][1][1] + '&' + all_sites_data[i][0][3][1][
            2] + '&' +
        all_sites_data[i][0][3][1][3] + '&' + all_sites_data[i][0][3][1][4]) + ',' + str(
        all_sites_data[i][0][3][2][0] + '&' + all_sites_data[i][0][3][2][1] + '&' + all_sites_data[i][0][3][2][
            2] + '&' +
        all_sites_data[i][0][3][2][3] + '&' + all_sites_data[i][0][3][2][4]) + ',' +
            str(all_sites_data[i][0][4][0]) + ',' + str(all_sites_data[i][0][4][1]) + ',' + str(
        all_sites_data[i][0][5][0][0] + '&' + all_sites_data[i][0][5][0][1] + '&' + all_sites_data[i][0][5][0][
            2] + '&' +
        all_sites_data[i][0][5][0][3] + '&' + all_sites_data[i][0][5][0][4]) + ',' + str(
        all_sites_data[i][0][5][1][0] + '&' + all_sites_data[i][0][5][1][1] + '&' + all_sites_data[i][0][5][1][
            2] + '&' +
        all_sites_data[i][0][5][1][3] + '&' + all_sites_data[i][0][5][1][4]) + ',' + str(
        all_sites_data[i][0][6][0][0] + '&' + all_sites_data[i][0][6][0][1] + '&' + all_sites_data[i][0][6][0][
            2] + '&' +
        all_sites_data[i][0][6][0][3] + '&' + all_sites_data[i][0][6][0][4]) + ',' + str(
        all_sites_data[i][0][6][1][0] + '&' + all_sites_data[i][0][6][1][1] + '&' + all_sites_data[i][0][6][1][
            2] + '&' +
        all_sites_data[i][0][6][1][3] + '&' + all_sites_data[i][0][6][1][4]) + ',' + str(
        all_sites_data[i][0][7][0][0] + '&' + all_sites_data[i][0][7][0][1]) + ',' + str(
        all_sites_data[i][0][7][1][0] + '&' + all_sites_data[i][0][7][1][1]) + ',' + str(
        all_sites_data[i][0][7][2][0] + '&' + all_sites_data[i][0][7][2][1]))
    print('end task 3')
    # q += 1

f.close()

print('end task 4')
# get_api_from_alexa('https://www.alexa.com/siteinfo/facebook.com')

# except:
#     print('error!')


########### be kar giri algorithm baraye shabih sazi kalamate moshabe bara kalamati ke eshtebah type shode va to data base hast
######### be kar giri algorithm lcs longest common subsequence #######################
