# Scrapy settings for bookscrapper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bookscrapper"

SPIDER_MODULES = ["bookscrapper.spiders"]
NEWSPIDER_MODULE = "bookscrapper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bookscrapper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

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
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

#USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

SCRAPEOPS_API_KEY = "api-key"
SCRAPEOPS_PROXY_ENABLED = True
#SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = "https://headers.scrapeops.io/v1/user-agents"
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 10

# ROTATING_PROXY_LIST_PATH = '/proxies.txt'

# ROTATING_PROXY_LIST = [
#     '139.180.170.204:44444',
#     '200.70.34.22:4153',
#     '78.47.53.17:10005',
#     '212.83.137.150:24054'
# ]

# PROXY_USER = 'username'
# PROXY_PASSWORD = 'password'
# PROXY_ENDPOINT = 'gate.smartproxy.com'
# PROXY_PORT = '7000'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bookscrapper.middlewares.BookscrapperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'bookscrapper.middlewares.BookscrapperDownloaderMiddleware': 543,
    # 'bookscrapper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
    #'bookscrapper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 300,
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    #-----------------------------------------------------------
    # 'bookscraper.middlewares.MyProxyMiddleware': 350, 
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    #-------------------------------------------------------------
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725 
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   "bookscrapper.pipelines.BookscrapperPipeline": 300,
   "bookscrapper.pipelines.SaveToMySQLPipeline": 400,
}

FEEDS = {
    'bookdata.json': { 'format': 'json' } 
}

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
