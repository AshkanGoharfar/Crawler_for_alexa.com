import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random
from itertools import cycle




def Crawl_each_site(my_urls):
    # driver = webdriver.Chrome(
    #     executable_path=r"C:\Users\Ashkan\AppData\Local\Temp\chocolatey\chromedriver\79.0.3945.360\chromedriver.exe")

    driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\lib-bad\chromedriver\tools\chromedriver.exe")
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
                 get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend),]
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
        e = get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend)
        print('get_keyword_op_br : ' + str(a))
        print('get_all_topics : ' + str(b))
        print('get_comparison_metrics : ' + str(c))
        print('get_audience_overlap : ' + str(d))
        print('get_alexa_rank_90_days_trend : ' + str(e))
        full_data = [a, b, c, d, e]
        all_sites_data = [full_data]
        driver.close()
    except:
        driver.close()

    return all_sites_data


def get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend):
    try:
        page_data = str(list_of_data[0]).split('\n')
        current_position = 0
        for item in page_data:
            limit_for_crawl = current_position
            if '<div class="rankmini-rank">' in page_data[limit_for_crawl]:
                if ',' in str(page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0]):
                    row = [str(int(str(page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0]).split(',')[
                                       0]) * 1000 + int(
                        str(page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0]).split(',')[1])),
                           str(page_data[limit_for_crawl + 9].split(
                               '									                    ')[
                                   1].split(' ')[0])]
                else:
                    row = [str(page_data[limit_for_crawl + 1].split('/span>')[1].split(' ')[0]),
                           str(page_data[limit_for_crawl + 9].split(
                               '									                    ')[
                                   1].split(' ')[0])]
                alexa_rank_90_days_trend = row
                # print('alexa_rank_90_days_trend:' + str(alexa_rank_90_days_trend))
                return alexa_rank_90_days_trend
            current_position += 1

        if len(alexa_rank_90_days_trend) == 0 or len(alexa_rank_90_days_trend) > 2:
            alexa_rank_90_days_trend = ['null', 'null']
        elif len(alexa_rank_90_days_trend) == 1:
            try:
                alexa_rank_90_days_trend = [alexa_rank_90_days_trend[0], 'null']
            except:
                alexa_rank_90_days_trend = ['null', alexa_rank_90_days_trend[1]]

    except:
        alexa_rank_90_days_trend = ['null', 'null']
    print('alexa_rank_90_days_trend : ' + str(alexa_rank_90_days_trend))


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
        # print('audience_overlap :' + str(audience_overlap))
        # if len(audience_overlap) == 0:
        #     audience_overlap = [['null', 'null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null', 'null']]
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
                    limit_for_crawl + 28] and 'span class="num purple"' in page_data[
                    limit_for_crawl + 30]:
                    # if '"Third thissite"' in page_data[
                    #     limit_for_crawl + 34]:
                    try:
                        row = [page_data[limit_for_crawl + 30].split('">')[1].split('<')[0],
                               page_data[limit_for_crawl + 46].split('"> ')[1].split('<')[0]]
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
    return comparison_metrics_data


def get_keyword_op_br(list_of_data, keyword_opportunities_breakdown):
    page_data = str(list_of_data[0]).split('\n')
    # print(list_of_data[0])
    op_list = []
    try:
        keyword_opportunities_breakdown = ['null', 'null', 'null', 'null']
        current_position = -1
        for item in page_data:
            current_position += 1
            if '" style="opacity: 1;"></path></g><text' in item:
                op_list.append([page_data[current_position + 6].split('"truncation">')[1].split('</')[0],
                                page_data[current_position + 9].split('">')[1].split('</')[0]])
                op_list.append([page_data[current_position + 15].split('"truncation">')[1].split('</')[0],
                                page_data[current_position + 18].split('">')[1].split('</')[0]])
                op_list.append([page_data[current_position + 24].split('"truncation">')[1].split('</')[0],
                                page_data[current_position + 27].split('">')[1].split('</')[0]])
                try:
                    op_list.append([page_data[current_position + 33].split('"truncation">')[1].split('</')[0],
                                    page_data[current_position + 36].split('">')[1].split('</')[0]])
                except:
                    op_list.append(['null', 'null'])
        for i in range(len(op_list)):
            if op_list[i][1] == 'Keyword Gaps':
                keyword_opportunities_breakdown[1] = op_list[i][0]
            elif op_list[i][1] == 'Easy-to-Rank Keywords':
                keyword_opportunities_breakdown[2] = op_list[i][0]
            elif op_list[i][1] == 'Optimization Opportunities':
                keyword_opportunities_breakdown[0] = op_list[i][0]
            elif op_list[i][1] == 'Buyer Keywords':
                keyword_opportunities_breakdown[3] = op_list[i][0]
        # for i in range(len(op_list)):
        #     if keyword_opportunities_breakdown[i] == '':
        #         keyword_opportunities_breakdown[i] = 'null'
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
        for i in range(len(keyword_opportunities_breakdown)):
            if keyword_opportunities_breakdown[i] == '0 ':
                keyword_opportunities_breakdown[i] = 'null'
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
    return all_topics


