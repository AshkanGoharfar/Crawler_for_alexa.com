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

List = [[1, 2, 3], [2, [2, 3]]]
# all_topics_keyword_gaps
f = open('data.csv', 'w+')
name = ['hasan', 'null']
family_name = ['sd', 'null']

f.write(
    'keyword_opportunities_breakdown_optimization_opportunities,keyword_opportunities_breakdown_keyword_gaps,keyword_opportunities_breakdown_easy_to_rank_keywords,# keyword_opportunities_breakdown_buyer_keywords,all_topics_keyword_gaps,all_topics_easy_to_rank_keywords,all_topics_buyer_keywords,all_topics_optimization_opportunities,all_topics_top_keywords,comparison_metrics_data_search_traffic_this_site,comparison_metrics_data_search_traffic_comp_avg,comparison_metrics_data_bounce_rate_this_site,comparison_metrics_data_bounce_rate_comp_avg,comparison_metrics_data_sites_linking_in_this_site,comparison_metrics_data_sites_linking_in_comp_avg,audience_overlap_sites_overlap_score,audience_overlap_similar_sites_to_this_site,audience_overlap_alexa_rank,alexa_rank_90_days_trend_global_internet_engagement,alexa_rank_90_days_trend_daily_time_on_site,traffic_source_site name,traffic_source_Percentage_overall_site_traffic,referral_sites_names,referral_sites_how_many_other_sites_drive_traffic_to_them,sites_audience_interests_internet,sites_audience_interests_more likely,sites_audience_interests_interest_level,sites_audience_interests_in_this_category_this_sites_audience_visits\n')
for i in range(len(name)):
    f.write(name[i][0] + ',' + family_name[i] + '\n')
f.close()
