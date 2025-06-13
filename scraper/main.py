"""Entrypoint for running scrapy spiders."""

from scrapy.crawler import CrawlerProcess

from scraper.spiders.builders_spider import BuildersSpider


def run():
    """Launch the BuildersSpider using Scrapy's CrawlerProcess."""
    process = CrawlerProcess()
    process.crawl(BuildersSpider)
    process.start()


if __name__ == "__main__":
    run()
