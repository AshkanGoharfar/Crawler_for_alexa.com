from bs4 import BeautifulSoup
from selenium import webdriver


def crawl_all_links():
    driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
    driver.get('https://www.alexa.com/topsites/category')
    html = driver.page_source
    soup = BeautifulSoup(html)
    list_of_data = []
    for tag in soup.find_all('div'):
        list_of_data.append(tag)
    links = []
    # full_data = [links]
    tags = []
    # print(list_of_data[0])
    for item in str(list_of_data[0]).split('\n'):
        if 'li><a href="/topsites/category/Top/' in item:
            links.append(item.split('">')[1].split('<')[0])
    sites_and_categories = []
    for element in links:
        driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\bin\chromedriver.exe")
        url = 'https://www.alexa.com/topsites/category/Top/' + str(element)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html)
        list_of_data = []
        for tag in soup.find_all('div'):
            list_of_data.append(tag)
        # get_direct_links(element, url)
        same_category = []
        for item in str(list_of_data[0]).split('\n'):
            site_data = []
            if '<a href="/siteinfo/' in item:
                site_name = item.split('fo/')[1].split('">')[0]
                site_data = [site_name, url]
                sites_and_categories.append(site_data)

    f = open('sites.csv', 'w+', encoding="utf-8")
    # site_data_2 = do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/facebook.com')

    f.write('site link, category')

    for i in range(len(sites_and_categories)):
        print(i)
        print(sites_and_categories[i][0])
        print(sites_and_categories[i][1])
        f.write('\n' + str(sites_and_categories[i][0]) + ',' + str(sites_and_categories[i][1]).split('https://www.alexa.com/topsites/category/Top/')[1])
        print('written ' + str(i) + 'o min website')
    return sites_and_categories


print(crawl_all_links())

# print(len(sites_and_categories))

sites_and_categories = []
with open("sites.csv") as f:
    lis = [line.split() for line in f]        # create a list of lists
    for i, x in enumerate(lis):              #print the list items
        if i > 1:
            sites_and_categories.append(str("line{0} = {1}".format(i, x).split(' = [\'')[1].split('\']')[0]).replace(',', ' ').split(' '))
print(sites_and_categories)
for i in range(len(sites_and_categories)):
    print(sites_and_categories[i][0])
    print(sites_and_categories[i][1])

# a = [['31.8 k', '18 k', '7.6 k', '5.8 k', '411 '], [[['butakoma 300g', '53', '30'], ['human lovers committee', '48', '21'], ['mushi sezaru o enu machi...!', '46', '17'], ['crossdressing ehentai', '45', '22']], [['doujinshi hentia', '58', '19'], ['manga porn', '64', '28'], ['porn manga', '63', '22'], ['erocos', '66', '12']], [['noroi no video vs tanetsuke ojisan', '52', '66'], ['sword art online doujin', '50', '63'], ['read hentai online', '49', '51'], ['sword art online hentai', '46', '63']], [['tsunade', '42', '0.12%'], ['aeba no mori', '12', '3.45%'], ['tiny evil', '36', '0.13%'], ['今夜、夫の上司に抱かれに行きます', '14', '4.14%']], [['nhentai', '16.64%', '44.49%'], ['n hentai', '1.94%', '65.46%'], ['nhentai english', '1.21%', '82.44%'], ['hentai manga', '0.94%', '8.49%'], ['my hero academia hentai', '0.73%', '31.38%']]], [[['17.8%', '35.4%'], ['18.3%', '31.9%'], ['136', '336']]], [['52.4', '51.5', '50.9', '47.6', '32.6'], ['hentai2read.com', 'simply-hentai.com', 'hitomi.la', 'e-hentai.org', 'luscious.net'], ['9,796', '40,989', '2,031', '1,028', '12,697']], ['1,303', '8:49'], [['simply-hentai.com', 'hentai2read.com', 'hitomi.la', 'nhentai.net', 'e-hentai.org'], ['63.3', '41.5', '23.2', '17.8', '13.5']], [['e-hentai.org', 'hentai2read.com', 'simply-hentai.com', 'nhentai.net', 'hitomi.la'], ['826 ', '229 ', '186 ', '136 ', '103 ']], [['Adult', 'Comics'], ['3.6x', '10x'], ['', ''], [['hentai2read.com', 'rule34.xxx', 'nutaku.net'], ['hentai2read.com', 'rule34.xxx', 'nutaku.net']]]]
