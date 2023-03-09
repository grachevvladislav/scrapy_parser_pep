import scrapy
from pep_parse.items import PepParseItem
import re


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_authors = response.css('a.pep.reference.internal::attr(href)')
        for author_link in all_authors:
            yield response.follow(author_link, callback=self.parse_pep)
        #yield response.follow(all_authors[0], callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'PEP (?P<number>\d+) – ((?P<name>.*))'
        h1_tag = response.xpath('string(//h1[@class="page-title"])').get()
        print(h1_tag)
        text_match = re.search(pattern, h1_tag)
        if text_match is not None:
            number = text_match.group('number')
            name = text_match.group('name')
        else:
            number, name = h1_tag, ''
        data = {
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get() or '',
        }
        yield PepParseItem(data)
