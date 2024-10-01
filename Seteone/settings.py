# Scrapy settings for Seteone project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Seteone"

SPIDER_MODULES = ["Seteone.spiders"]
NEWSPIDER_MODULE = "Seteone.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Seteone (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# ITEMS_PIPELINES = {
#     "Seteone.pipelines.SeteonePipeline": 300,
# }
# DATABASE = {
#     "drivername": "postgres",
#     "host": os.environ["POSTGRES_HOST"],
#     "port": os.environ["POSTGRES_PORT"],
#     "username": os.environ["POSTGRES_USER"],
#     "password": os.environ["POSTGRES_PASS"],
#     "database": os.environ["POSTGRES_DB"],
# }
# username = 'avnadmin'
# password = 'AVNS_OZaFMf--rCU9QzzfxpE'
# host = 'mysql-198e88e7-sszapis-39be.g.aivencloud.com'
# port = '22057'  # Порт по умолчанию для MySQL
# database = 'defaultdb'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'ROUTE=.accstorefront-5944bff4d7-mtq99; accountPageId=; allowBlockAccess=none; siteone-cart=f94c3713-3ce5-4d8c-baa8-97b70641aee2; gls=1003; AMCVS_44BC3F5859E47A930A495D8E%40AdobeOrg=1; _gcl_au=1.1.334648884.1722361175; _lfa=LF1.1.6ab2d15a92daf043.1722361176041; com.silverpop.iMAWebCookie=d1d02d16-68ab-cbe2-85cd-ebb2a336e139; s_cc=true; _gid=GA1.2.1174516156.1722361257; _fbp=fb.1.1722361259868.891558262566629955; JSESSIONID=4C318D3CB06F5E060D9C59E0471181ED.accstorefront-5944bff4d7-mtq99; _abck=8207946FB29DCFE5B21703E38A85B0EA~0~YAAQWHjOFw/pgAaRAQAAyd90CQwTKKUmKhh7yVcpn68T6EjFq05i5TsDLqZWoDRPVykAycWq53OnqhHEO4jXv3N0Z0ncg1IpznQ+FKhRp8hPonue/ZrEiAHYfbaFGjiy/1T6jmNjbnGtVlzLg/p1VB6gGhUkasuJ1csTaLurfM2Z8vJffXgsjelEoXgTycFacjBq+Ka9AfeTfLy66Z1MtFrTT4OnnnJwg/nZiZszP7KXkPH78pmvF7ygk5MRF9jj59rsaNpO+FEnKYZ/9iLLKSuTu2/Sl7UG/2zsYBjkNKirj8UNU260M+vVFxyoE0U9EqNTVgjFyOoeMwnhlQfRfJJHiAFzGHT4WwXRtStTqMp+LKm9bo/iNK292F8Zt87lQ36gH4UKAfy8Vp6QCw0X3848q52cKy2Jew==~-1~-1~-1; s_lv_s=Less%20than%201%20day; _ga_NB436M2T0P=deleted; com.silverpop.iMA.session=96b9332c-8ad3-c1a8-bd69-1e35b4156c25; AMCV_44BC3F5859E47A930A495D8E%40AdobeOrg=1176715910%7CMCIDTS%7C19935%7CMCMID%7C86505869982574825551914714817971891429%7CMCAAMLH-1723052924%7C7%7CMCAAMB-1723052924%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1722455324s%7CNONE%7CMCAID%7C331A514E3CF025EB-60001A9AA07F23C8%7CvVersion%7C5.4.0; bm_mi=014DC46BABCF1534D059BB9AB92C3752~YAAQUnjOF5JrkuuQAQAA/znvCRhqXEf0cXQTcj8gmTAAjpXGZjcbrLSi9n2WIEaSMthN4mog6bkiOy6wCED55gdxOpVyQzv6oQ5x3vpQa7pyDz9npE6lEPqb1f3e+TdiTu2UXtmEFhZ3aZYG0/KF2GaIZgk6lL2GNyTudJoeDfDa2H94cTwEuzJRxStILgx+nIZqUKlXaI9r8LUoCjGcE+qJyFukQNLZuIdzkCfKIp0hGHhYWMuoL0Cnbmi29PsLQ+GLR2CUikit/hWC49pnhcnoKZBDO8yJ5v631FS1uU/ZtSel78yPh38bT3IDA6IZGaTssF2LpfJrxEB1xg==~1; ak_bmsc=5F417C344ED85E9014178EF2623E7632~000000000000000000000000000000~YAAQUnjOFxyKkuuQAQAAIHvvCRgXjLpZvdpynxO5N4Dsis5y3c/BIHdcSBsbkhbOIeJgVD1yZD8yoJwpgK3XO4vTzvfbMeu/Bkwhlf5+5nkL+d3TdxcYxel2GbAH1VdNzh4qtp4jmznx82LvrzPlseCXzwHEJKSSeT/8qwqSfYYVrIfJSDr1t90DeJDhWGDU4OMIybn21y6qAxPxNA8J06IB5cRUx3kn7hWBXNN/vxrztu7SnCkW5ZDqYYHX4J4Vm2mxCWsB+kxTZYkg9zKS6K40o6l9yxHBc3mHl5vaHsUMO91Zjr/nZkkRz//+udtrjwSa8kD0F/+H7oVFJZNZeX9wDitLpmNT11pbxvQr3yDp8cr+qTBt7mu2kjn8TWoOYeRPedGqR397fl1JL2mES/hXV2hrThD9tGw70BOasdCu2a47i/45uFWAHtmNFLD58ejCIPYmEYuIFc2blfFhVCV83v0siHaEc9geJro9AgoplZHU724g30nNtBE9iqj5; csc=1002; com.silverpop.iMA.page_visit=-1486763195:941829075:1169047474:-1882466775:931128564:; s_sq=%5B%5BB%5D%5D; bm_sv=055332EDC5CA507351B81E609B1E251A~YAAQZ1XIF+tFqeOQAQAAjfvzCRjgmB9Qc8U63AMXjptTmZKZN7pAnzEYTSAS2uSUiaO93GZQclfUC/ConyCW51juyAoEdpLwgmzCXpcK8NUdhZEpsKmSM7LqWclWJM6Yrsc1AqX/H4cPk/DXTSfDBtogc8VrErPbgQTuDi64bBOkllBFWiu5t0Lhq7GM1mJrbKirz+w1bFxV/NLUGheLj8lmi5Lq0yyt2AkOS96Uf0QbcBpoR9WGpwELzujCZTkLHPA=~1; bm_sz=06B48E3AFD3D9B0CE9B9BE6AA425B375~YAAQZ1XIF+xFqeOQAQAAjfvzCRjuxPxjuQ48kh1ZwxHmqMOzkOE4Jqi8Us+XdqGyVIpdBUbfgkZBoZvbZYdIOxNhwzZ/27qsFAG0yXNh1o8FMyjxsm1MEq/EDLxVAZGrQoNoODll599PSDM0r6YjpOMVIfBz0JjIjD3fvrAeYT+BmCAv39c3YQyUjfGC8MuTEwyc7DkymKsYBkvAqXLRkGd42X46IQV0ufdWqLb9hKZCF+GaiVz6rtIvxaR0MiYE207vumKtQ73kmTvgUbpHhWV962UlDTfDJgut0Zo1plYk7NZ335t3W8Ljjfgv++ry+WBcz5tfDc8XNU7KAqzZOOWK6oXS+lqhcz+4eo7RAFpgOfy5yan2AaaqH+OsqY0++WutBINJYE23TdiQShWxsuoFkY/7V0vSh9QCB2MafRg+J0ZQ0vT4TwUUHKUONXp7eZVB4K6YDvrdDkWwxwSM31C6fvZU47BPhF4W8ZJIcCfOuvDeduvtRalUQIX71YVy/BLVA/nKTMDC25v/PDHDzyi0Pd19nkuh3VNvJ9ggPyE2~3355440~3486534; gpv=store%3A%20store%20finder; RT="z=1&dm=siteone.com&si=cd40yboksui&ss=lz9lg06e&sl=0&tt=0"; fs_lua=1.1722448880381; fs_uid=#HHD7H#1d29774c-bbbb-4038-81af-3e66b4baa222:3bb995e5-e976-432e-9837-b617e8926329:1722444332365::23#/1753897377; _rdt_uuid=1722361173867.dbd3b2ba-9209-40c5-8bd4-b97e611d587e; _gat_gtag_UA_23083629_11=1; _ga_QWN01LTG1X=GS1.1.1722444334.4.1.1722448881.0.0.0; _ga=GA1.1.1272780326.1722361176; _ga_NB436M2T0P=GS1.1.1722444334.4.1.1722448885.46.0.0; s_ppvl=My%2520Account%2520%253A%2520Login%2520Page%2C49%2C49%2C809%2C1731%2C809%2C1730%2C973%2C1.11%2CP; s_ppv=store%253A%2520store%2520finder%2C60%2C60%2C809%2C1042%2C809%2C1730%2C973%2C1.11%2CP; s_nr=1722448893117-Repeat; s_lv=1722448893119; _abck=8207946FB29DCFE5B21703E38A85B0EA~-1~YAAQ00A2F/PF3OKQAQAAP7r8CQwylKXdrqPpo4W7SWaJyBChVljDWkbJcagkwBw4VjkIWlgAZIZJS7Sj/dNd6dqCRDFOicIjBFle3KcrRaKI+1xu87chmVyjjxwCWiIGc+NKotXL7MJ4gSdTvGDypUo1ecO0Ld1KOJ/fAYLGOMWgdsEdTSVZBE1A/cfSSEsCpHBWzGDfdHiG1vAvS7w2gEQPu1/cKa0mGZgcc9b/NrOqiWh5xwHBy+hecASL0fsOe92/czabDRO4FHBhF+JgDug3rc2/FVp4CGVGZ1vK4PUjmU3UAT7fFvl2AJDqDYWlTSRdyt7HR5Hc42aBiDFeQfIL1mo/S2YuFAw1bfRmT53YVlCaRZGkRdTCaUDxm5dvMU7ebpFScrIHSFy3EKeq7bZ566m4bBYaMw==~0~-1~-1; bm_mi=014DC46BABCF1534D059BB9AB92C3752~YAAQUnjOF8ExkOuQAQAAk0/rCRhyrf8Gy2jEIxMlwwaiNwNtsi+CGox5GC8N7ufRHwTwbDcrd6lR5t/jba3s0ZHydP8d5haPCx8FL3gduFnuvowcKAe5L4CwXGF5KIyoZpUkrzhypwt9wXdDNf8r6UsdIGBrNMT5yGOPfauEGu1BgtlPv2+Gw0q2x4NW3zRrdwv6PSOKT7/HGEAP3bouvraVyctuSizJt0Yx7hWmkw5uv26/Lv/HmR6418RBUSa6FA3BcnUT8+RbTDc0jhQKV1RwF1ul3UTWtGz+fzMh9R7fIa9zor5NUB0cjyypAwZT+X3ohd8oNx4ByalTRMoig2Gwl7g=~1; bm_sv=055332EDC5CA507351B81E609B1E251A~YAAQ00A2F/TF3OKQAQAAP7r8CRioDiTMiL4u8nRNd1kYlRrCaR1FtN3sfLksIu2s6da9/aeApM5okgpCqGcH9k880uw9O5yg9q0+inxJ9VaVx5qPK2zFloUSCc1iGFCz/8nfRBV8AoyEOoKzR8qQmwJym4CwNOln792codcy35muuz7dBomi2Hgr+t+uWWWF7Ci6evpoTI2inDOTFt81RutNg2KqtZlBJ8+QxX/T+NfFbY2ehmyQGyU0REzxw6sf8rs=~1; JSESSIONID=4C318D3CB06F5E060D9C59E0471181ED.accstorefront-5944bff4d7-mtq99; ROUTE=.accstorefront-5944bff4d7-h2hj2; csc=485; siteone-cart=f94c3713-3ce5-4d8c-baa8-97b70641aee2',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.siteone.com/en/store-finder',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Seteone.middlewares.SeteoneSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "Seteone.middlewares.SeteoneDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "Seteone.pipelines.SeteonePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
