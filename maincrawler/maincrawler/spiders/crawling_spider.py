from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):

    name = "maincrawler"

    allowed_domains = ["www.reed.co.uk"]

    start_urls = [
        f"https://www.reed.co.uk/jobs/data-analyst-jobs?pageno=1"]

    rules = (



        Rule(link_extractor=LinkExtractor(
             allow=["source=searchResults&filter"], restrict_xpaths=["//article[@class='card job-card_jobCard__MkcJD']"]), callback="parse_items"),

        Rule(link_extractor=LinkExtractor(
            restrict_xpaths=["//ul[@class='pagination']/li[last()]"])),



    )

    def parse_items(self, response):

        url = response.url
        title = response.css("h1::text").get().strip()

        print(response.xpath(
            "//div[contains(@class, 'mobile-metadata-container')]"))
        print(response.xpath(
            "//div[contains(@class, 'job-info--permament-icons')]"))

        if response.xpath("//div[contains(@class, 'mobile-metadata-container')]"):
            job_desc = response.css(".mobile-metadata-container")

        elif response.xpath("//div[contains(@class, 'job-info--permament-icons')]"):
            job_desc = response.css(".job-info--permament-icons")

        salary = job_desc.xpath("string(normalize-space(div[1]))").get()
        address = job_desc.xpath("string(normalize-space(div[2]))").get()

        contract_type = job_desc.xpath(
            "string(normalize-space(div[3]))").get().split(",")[0].strip()

        job_type = job_desc.xpath(
            "string(normalize-space(div[3]))").get().split(",")[1].strip()

        yield {
            "Url": url,
            "Title": title,
            "Salary": salary,
            "Contract Type": contract_type,
            "Job Type": job_type,
            "Address": address
        }
