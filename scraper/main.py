"""Entrypoint for running Scrapy spiders and persisting data to Firebase."""

import os
from scrapy.crawler import CrawlerProcess
from scrapy import signals
from pydispatch import dispatcher

from firebase.firebase_client import init_firebase
from scraper.spiders.builders_spider import BuildersSpider

# Initialize Firebase using credentials path from environment or default
db = init_firebase(os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase/firebase_credentials.json"))


def save_to_firestore(item):
    """Persist scraped item to Firestore."""
    db.collection("builders").add(dict(item))


def setup_signal_handlers(spider):
    """Listen for Scrapy item scraped signal and store data."""
    dispatcher.connect(
        lambda item, response, spider: save_to_firestore(item),
        signal=signals.item_scraped,
    )


def run():
    """Launch the BuildersSpider using Scrapy's CrawlerProcess."""
    process = CrawlerProcess()
    process.crawl(BuildersSpider)
    setup_signal_handlers(BuildersSpider)
    process.start()


if __name__ == "__main__":
    run()
