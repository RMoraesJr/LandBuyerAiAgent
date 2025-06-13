"""Scrapy spider that collects builder information."""

import scrapy


class BuildersSpider(scrapy.Spider):
    name = "builders"

    def start_requests(self):
        """Generate initial requests for scraping."""
        urls = []  # TODO: populate with target URLs
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Parse builder data from a response."""
        # TODO: implement parsing logic
        yield {}
