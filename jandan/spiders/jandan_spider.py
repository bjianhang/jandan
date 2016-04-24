from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from jandan.items import JandanItem

class JandanSpider(CrawlSpider):
    name = "jandan"
    allowed_domains = ["jandan.net"]
    start_urls = [
        "http://jandan.net/ooxx"
    ]


    rules = (
        Rule(LinkExtractor(allow=('http://jandan.net/ooxx/page-\d+#comments', )), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        for href in response.xpath('//a[@class="view_img_link"]/@href').extract():
            item = JandanItem(image_urls=[href])
            yield item
