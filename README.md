# Web Crawling and Scraping Task Project

The project is a submission to the task given by Parsedom.

The program is coded to not scrape the Promoted Jobs (first two same job posts in each pagination page) because each pagination page counts only 25 job posts.

- **Total scraped job data:** `3018`
- **Crawler file:** `maincrawler/maincrawler/spiders/crawling_spider.py`
- **Output file:** `maincrawler/data.csv`

- **Scrapy stats**:

```
{'downloader/exception_count': 150,
 'downloader/exception_type_count/twisted.internet.error.ConnectError': 149,
 'downloader/exception_type_count/twisted.internet.error.TimeoutError': 1,
 'downloader/request_bytes': 3661748,
 'downloader/request_count': 3292,
 'downloader/request_method_count/GET': 3292,
 'downloader/response_bytes': 104156284,
 'downloader/response_count': 3142,
 'downloader/response_status_count/200': 3140,
 'downloader/response_status_count/308': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 20084.672652,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2024, 3, 5, 16, 58, 20, 610722, tzinfo=datetime.timezone.utc),
 'httpcompression/response_bytes': 367916985,
 'httpcompression/response_count': 3141,
 'item_scraped_count': 3018,
 'log_count/DEBUG': 6313,
 'log_count/INFO': 345,
 'memusage/max': 97398784,
 'memusage/startup': 60919808,
 'request_depth_max': 121,
 'response_received_count': 3141,
 'retry/count': 150,
 'retry/reason_count/twisted.internet.error.ConnectError': 149,
 'retry/reason_count/twisted.internet.error.TimeoutError': 1,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 3291,
 'scheduler/dequeued/memory': 3291,
 'scheduler/enqueued': 3291,
 'scheduler/enqueued/memory': 3291,
 'start_time': datetime.datetime(2024, 3, 5, 11, 23, 35, 938070, tzinfo=datetime.timezone.utc)
 }
```

> Verified that there are no duplicate data.

---

### Technology Used

- Python
- Scrapy Framework

### Steps to run the project:

- Open terminal/cmd on root project directory
- Run
  `pip install requirements.txt`
  to install required python dependencies
- Run
  `cd maincrawler`
- Run
  `scrapy crawl maincrawler -o data2.csv`
  to run the crawler and save the scraped data to `data2.csv`
  > The actual scraped data by me remains in the `data.csv` file
