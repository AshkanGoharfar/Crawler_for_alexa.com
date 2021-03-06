from Crawl_sites import *


def sites_name_category():
    with open("Categories.csv") as f:
        lis = [line.split() for line in f]  # create a list of lists
        fail_counter_1 = 0
        for i, x in enumerate(lis):  # print the list items
            if i > 1:
                try:
                    all_sites.append(
                        str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(
                            ' '))
                except:
                    fail_counter_1 += 1
    return all_sites


if __name__ == '__main__':
    all_sites_data = []
    all_sites = sites_name_category()

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
                    all_sites_data[0][3][1][3] + '&' + all_sites_data[0][3][1][4]) + ',' + all_sites_data[0][4][
                            0] + ',' +
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
