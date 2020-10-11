import urllib.request
from bs4 import BeautifulSoup
from lxml import html
import requests
import datetime
from datetime import timedelta, datetime
from selenium import webdriver
import random
from itertools import cycle


def crawl_webpage(my_urls, category):
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

    for tag in soup.find_all('div'):
        list_of_data.append(tag)
    # print(list_of_data[0])
    full_data = [get_keyword_op_br(list_of_data, keyword_opportunities_breakdown),
                 get_all_topics(list_of_data, all_topics),
                 get_comparison_metrics(list_of_data, comparison_metrics_data),
                 get_audience_overlap(list_of_data, audience_overlap),
                 get_alexa_rank_90_days_trend(list_of_data, alexa_rank_90_days_trend)]
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
                        try:
                            row = [page_data[limit_for_crawl + 36].split('<span>')[1].split('<')[0],
                                   page_data[limit_for_crawl + 47].split('<span>')[1].split('<')[0]]
                        except:
                            row = ['null', 'null']
                    limit_for_crawl += 34
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
    try:
        current_position = 0
        for item in page_data:
            current_position += 1
            if 'font-size="24px" text-anchor="middle">' in item:
                keyword_opportunities_breakdown.append(
                    item.split('font-size="24px" text-anchor="middle">')[1].split('<')[0])
            if '"color: rgb(84, 84, 84);' in item:
                keyword_opportunities_breakdown.append(
                    (page_data[current_position].split('<span class="truncation">')[1].split('<')[0]))
        if len(keyword_opportunities_breakdown) == 5:
            keyword_opportunities_breakdown = [keyword_opportunities_breakdown[1], keyword_opportunities_breakdown[2],
                                               keyword_opportunities_breakdown[3], keyword_opportunities_breakdown[4]]
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
    return keyword_opportunities_breakdown


def get_all_topics(list_of_data, all_topics):
    page_data = str(list_of_data[0]).split('\n')
    try:
        current_position = 0
        for item in page_data:
            limit_for_crawl = current_position
            each_category = []
            if '<div class="keyword">' in page_data[current_position - 2] and '<div class="Row">' in page_data[
                current_position - 3] and '<div class="transparency"></div>' in page_data[
                current_position - 4] and '<div class="Body">' in page_data[current_position - 5]:
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


all_sites_data = []
all_sites = []
with open("Categories.csv") as f:
    lis = [line.split() for line in f]  # create a list of lists
    fail_counter_1 = 0
    for i, x in enumerate(lis):  # print the list items
        if i > 1:
            try:
                all_sites.append(
                    str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(' '))
            except:
                fail_counter_1 += 1

category = []
my_urls = []

f = open('data_V3_update.csv', 'w+', encoding="utf-8")

f.write(
    # ' +
    'site link,category,keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps_name,all_topics_keyword_gaps Avg_traffic,all_topics_keyword_gaps_search_popularity,all_topics_easy_to_rank_keywords_name,all_topics_easy_to_rank_keywords_relevance_to_site,all_topics_easy_to_rank_keywords_search_pop,all_topics_buyer_keywords_name,all_topics_buyer_keywords_Avg_traffic,all_topics_buyer_keywords_organic_competition,all_topics_optimization_opportunities_name,all_topics_optimization_opportunities_search_pop,all_topics_optimization_opportunities_organic_share_of_voice,all_topics_top_keywords_name,all_topics_top_keywords_search_traffic,all_topics_top_keywords_share_of_voice,comparison_metrics_search_traffic_this_site,comparison_metrics_search_traffic_Comp Avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience_overlap_sites_overlap_scores,audience_overlap_similar_sites_to_this_site,This_site_rank_in_global_internet_engagement,Daily_time_on_site')
f.close()

failed_counter = 0
success_counter = 0

failed_in_execute = 0
j = 0
counter = j
while counter < 5:
    f = open('data_V3_update.csv', 'a', encoding="utf-8")
    print(all_sites[j][0], str(all_sites[j][1]))
    my_urls.append(all_sites[j][0])
    category.append(all_sites[j][1])
    all_sites_data = []
    try:
        all_sites_data = crawl_webpage('https://www.alexa.com/siteinfo/' + str(all_sites[j][0]),
                                       str(all_sites[j][1]))
        counter += 1
    except:
        print('not valid data' + '\n')
        failed_in_execute += 1
        print('failed in execute : ' + str(failed_in_execute))
    print('all site data: ' + str(all_sites_data))
    print('counter in loop : ' + str(counter))

    full_null_data = [[['null', 'null', 'null', 'null'], [
        [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
        [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
        [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
        [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null']],
        [['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'], ['null', 'null', 'null'],
         ['null', 'null', 'null']]], [[['null', 'null'], ['null', 'null'], ['null', 'null']]],
                       [['null', 'null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null', 'null']],
                       ['null', 'null']]]
    try:
        if all_sites_data is not full_null_data:
            f.write('\n' +
                    str(all_sites[j][0]) + ',' + str(all_sites[j][1]) + ',' +
                    str(all_sites_data[0][0][0]) + ',' + str(all_sites_data[0][0][1]) + ',' + str(
                all_sites_data[0][0][2]) + ',' + str(
                all_sites_data[0][0][3]) + ',' + str(
                all_sites_data[0][1][0][0][0] + '&' + all_sites_data[0][1][0][1][0] + '&' + all_sites_data[0][1][0][2][
                    0] + '&' + all_sites_data[0][1][0][3][0]) + ',' + str(
                all_sites_data[0][1][0][0][1] + '&' + all_sites_data[0][1][0][1][1] + '&' + all_sites_data[0][1][0][2][
                    1] + '&' + all_sites_data[0][1][0][3][
                    1]) + ',' + str(
                all_sites_data[0][1][0][0][2] + '&' + all_sites_data[0][1][0][1][2] + '&' + all_sites_data[0][1][0][2][
                    2] + '&' + all_sites_data[0][1][0][3][
                    2]) + ',' + str(
                all_sites_data[0][1][1][0][0] + '&' + all_sites_data[0][1][1][1][0] + '&' + all_sites_data[0][1][1][2][
                    0] + '&' + all_sites_data[0][1][1][3][
                    0]) + ',' + str(
                all_sites_data[0][1][1][0][1] + '&' + all_sites_data[0][1][1][1][1] + '&' + all_sites_data[0][1][1][2][
                    1] + '&' + all_sites_data[0][1][1][3][
                    1]) + ',' + str(
                all_sites_data[0][1][1][0][2] + '&' + all_sites_data[0][1][1][1][2] + '&' + all_sites_data[0][1][1][2][
                    2] + '&' + all_sites_data[0][1][1][3][
                    2]) + ',' + str(
                all_sites_data[0][1][2][0][0] + '&' + all_sites_data[0][1][2][1][0] + '&' + all_sites_data[0][1][2][2][
                    0] + '&' + all_sites_data[0][1][2][3][
                    0]) + ',' + str(
                all_sites_data[0][1][2][0][1] + '&' + all_sites_data[0][1][2][1][1] + '&' + all_sites_data[0][1][2][2][
                    1] + '&' + all_sites_data[0][1][2][3][
                    1]) + ',' + str(
                all_sites_data[0][1][2][0][2] + '&' + all_sites_data[0][1][2][1][2] + '&' + all_sites_data[0][1][2][2][
                    2] + '&' + all_sites_data[0][1][2][3][
                    2]) + ',' + str(
                all_sites_data[0][1][3][0][0] + '&' + all_sites_data[0][1][3][1][0] + '&' + all_sites_data[0][1][3][2][
                    0] + '&' + all_sites_data[0][1][3][3][
                    0]) + ',' + str(
                all_sites_data[0][1][3][0][1] + '&' + all_sites_data[0][1][3][1][1] + '&' + all_sites_data[0][1][3][2][
                    1] + '&' + all_sites_data[0][1][3][3][
                    1]) + ',' + str(
                all_sites_data[0][1][3][0][2] + '&' + all_sites_data[0][1][3][1][2] + '&' + all_sites_data[0][1][3][2][
                    2] + '&' + all_sites_data[0][1][3][3][
                    2]) + ',' + str(
                all_sites_data[0][1][4][0][0] + '&' + all_sites_data[0][1][4][1][0] + '&' + all_sites_data[0][1][4][2][
                    0] + '&' + all_sites_data[0][1][4][3][
                    0]) + ',' + str(
                all_sites_data[0][1][4][0][1] + '&' + all_sites_data[0][1][4][1][1] + '&' + all_sites_data[0][1][4][2][
                    1] + '&' + all_sites_data[0][1][4][3][
                    1]) + ',' + str(
                all_sites_data[0][1][4][0][2] + '&' + all_sites_data[0][1][4][1][2] + '&' + all_sites_data[0][1][4][2][
                    2] + '&' + all_sites_data[0][1][4][3][
                    2])
                    + ',' + str(all_sites_data[0][2][0][0][0]) + ',' + str(all_sites_data[0][2][0][0][1]) + ',' + str(
                all_sites_data[0][2][0][1][0]) + ',' + str(all_sites_data[0][2][0][1][1]) + ',' + str(
                all_sites_data[0][2][0][2][0].replace(',', '')) + ',' + str(
                all_sites_data[0][2][0][2][1].replace(',', '')) + ',' + str(
                all_sites_data[0][3][0][0] + '&' + all_sites_data[0][3][0][1] + '&' + all_sites_data[0][3][0][
                    2] + '&' +
                all_sites_data[0][3][0][3] + '&' + all_sites_data[0][3][0][4]) + ',' + str(
                all_sites_data[0][3][1][0] + '&' + all_sites_data[0][3][1][1] + '&' + all_sites_data[0][3][1][
                    2] + '&' +
                all_sites_data[0][3][1][3] + '&' + all_sites_data[0][3][1][4]) + ',' + all_sites_data[0][4][0] + ',' +
                    all_sites_data[0][4][1])
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

print('end task 1')

print(failed_counter)

print('end task 4')
