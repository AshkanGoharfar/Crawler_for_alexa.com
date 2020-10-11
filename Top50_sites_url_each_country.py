from bs4 import BeautifulSoup
from selenium import webdriver


def crawl_all_links():
    driver = webdriver.Chrome(executable_path=r"C:\ProgramData\chocolatey\lib-bad\chromedriver\tools\chromedriver.exe")
    driver.get('https://www.alexa.com/topsites/countries')
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
        if '<li><a href="countries/' in item:
            links.append(item.split('f="countries/')[1].split('<')[0])
    sites_and_categories = []
    # print(links)
    for element in links:
        driver = webdriver.Chrome(
            executable_path=r"C:\ProgramData\chocolatey\lib-bad\chromedriver\tools\chromedriver.exe")
        url = 'https://www.alexa.com/topsites/countries/' + str(element.split('">')[0])
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
                site_data = [site_name, url + '/' + str(element.split('">')[1])]
                sites_and_categories.append(site_data)
        driver.close()

    f = open('sites_countries.csv', 'w+', encoding="utf-8")
    # site_data_2 = do_crawler_with_chromedrivers('https://www.alexa.com/siteinfo/facebook.com')

    f.write('site link, country')

    for i in range(len(sites_and_categories)):
        print(i)
        print(str(sites_and_categories[i][0]))
        print(str(sites_and_categories[i][1]).split('https://www.alexa.com/topsites/countries/')[1])
        f.write('\n' + str(sites_and_categories[i][0]) + ',' +
                str(sites_and_categories[i][1]).split('https://www.alexa.com/topsites/countries/')[1])
        print('written ' + str(i) + 'o min website')
    return sites_and_categories


print(crawl_all_links())
