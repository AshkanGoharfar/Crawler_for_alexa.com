import csv

# mylist = []
# with open(..., 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)

# Optimization Opportunities, Keyword Gaps, Easy-to-Rank Keywords, Buyer Keywords
keyword_opportunities_breakdown = []
# keyword_opportunities_breakdown_optimization_opportunities
# keyword_opportunities_breakdown_keyword_gaps
# keyword_opportunities_breakdown_easy_to_rank_keywords
# keyword_opportunities_breakdown_buyer_keywords

# Keyword Gaps , Easy-to-Rank Keywords , Buyer Keywords , Optimization Opportunities , Top Keywords
all_topics = []
# all_topics_keyword_gaps
# all_topics_easy_to_rank_keywords
# all_topics_buyer_keywords
# all_topics_optimization_opportunities
# all_topics_top_keywords

# Search traffic(this site, comp avg), bounce rate(this site, comp avg), sites linking in(this site, comp avg)
comparison_metrics_data = []
# comparison_metrics_data_search_traffic_this_site, comparison_metrics_data_search_traffic_comp_avg
# comparison_metrics_data_bounce_rate_this_site, comparison_metrics_data_bounce_rate_comp_avg
# comparison_metrics_data_sites_linking_in_this_site, comparison_metrics_data_sites_linking_in_comp_avg

# Sites overlap score, similar sites to this site, alexa rank
audience_overlap = []
# audience_overlap_sites_overlap_score
# audience_overlap_similar_sites_to_this_site
# audience_overlap_alexa_rank

# This site ranks in global internet engagement, daily time on site
alexa_rank_90_days_trend = []
# alexa_rank_90_days_trend_global_internet_engagement
# alexa_rank_90_days_trend_daily_time_on_site

# site name, Percentage overall site traffic from each channel in -- JUST FOR Saerch(is not premium !)
traffic_source = []
# traffic_source_site name
# traffic_source_Percentage_overall_site_traffic

# referral sites_names, Sites by how many other sites drive traffic to them
referral_sites = []
# referral_sites_names
# referral_sites_how_many_other_sites_drive_traffic_to_them

# internet, more likely, interest level, Sites in this category this site’s audience visits
sites_audience_interests = []
# sites_audience_interests_internet
# sites_audience_interests_more_likely
# sites_audience_interests_interest_level
# sites_audience_interests_in_this_category_this_sites_audience_visits

# List = [[1, 2, 3], [2, [2, 3]]]
# # all_topics_keyword_gaps
# f = open('data.csv', 'w+')
# name = ['hasan', 'null']
# family_name = ['sd', 'null']
#
# f.write(
#     'keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,# keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps,all_topics_easy_to_rank_keywords,all_topics_buyer_keywords,all_topics_optimization_opportunities,all_topics_top_keywords,comparison_metrics_data_search_traffic_this_site,comparison_metrics_data_search_traffic_comp_avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience_overlap_sites_overlap_score,audience_overlap_similar_sites_to_this_site,audience_overlap_alexa_rank,alexa_rank_90_days_trend_global_internet_engagement,alexa_rank_90_days_trend_daily_time_on_site,traffic_source_site name,traffic_source_Percentage_overall_site_traffic,referral_sites_names,referral_sites_how_many_other_sites_drive_traffic_to_them,sites_audience_interests_internet,sites_audience_interests_more likely,sites_audience_interests_interest_level,sites_audience_interests_in_this_category_this_sites_audience_visits\n')
# for i in range(len(name)):
#     f.write(name[i][0] + ',' + family_name[i] + '\n')
# f.close()

all_site_data = [[['230.6 k', '168.2 k', '55.7 k', '4.9 k', '1.9 k'], [[['thumbzilla', '60', '55'], ['porndude', '56', '53'], ['sex stories', '55', '51'], ['wife sharing', '55', '34']], [['woodman casting', '64', '44'], ['vr porn', '58', '51'], ['liya silver', '72', '46'], ['thumbzilla', '66', '55']], [['free porn', '93', '67'], ['free sex', '80', '65'], ['free porn videos', '79', '66'], ['free porno', '78', '65']], [['desnudando las risas', '13', '4.57%'], ['bangla hot song', '12', '2.75%'], ['teacher creampie', '7', '4.97%'], ['hot redheads', '27', '0.82%']], [['xvideos', '4.12%', '44.44%'], ['xvideo', '2.31%', '46.6%'], ['pornhub', '1.5%', '6.58%'], ['xnxx', '1.12%', '11.66%'], ['porn hub', '0.97%', '15.03%']]], [[['33.1%', '28.8%'], ['18.6%', '28.5%'], ['4,940', '3,872']]], [['93.8', '88.3', '75.5', '54.4', '53.9'], ['xnxx.com', 'pornhub.com', 'xhamster.com', 'youporn.com', 'redtube.com']]]]
all_site_data = [[['217.8 k', '155.3 k', '55.7 k', '5 k', '1.9 k'], [[['vr porn', '59', '51'], ['melody wylde', '57', '40'], ['lesbians latex anal tube', '57', '26'], ['mia melano', '56', '50']], [['4k porn', '57', '52'], ['woodman casting', '64', '44'], ['mia melano', '73', '50'], ['vr porn', '58', '51']], [['free porn', '93', '67'], ['free sex', '80', '65'], ['free porn videos', '79', '66'], ['free porno', '78', '65']], [['chaturbate pee', '27', '0.41%'], ['kristen bell porn', '18', '2.24%'], ['teen hardcore', '15', '3.42%'], ['pornstar jordi', '12', '4.72%']], [['xnxx', '5.32%', '49.29%'], ['xvideos', '1.96%', '18.8%'], ['pornhub', '1.46%', '5.66%'], ['xvideo', '1.34%', '24.04%'], ['free porn', '0.99%', '21.24%']]], [[['37%', '27.8%'], ['19%', '28.4%'], ['2,403', '4,506']]], [['93.8', '77.6', '76.8', '54.2', '48.4'], ['xvideos.com', 'xhamster.com', 'pornhub.com', 'redtube.com', 'youporn.com']]]]
