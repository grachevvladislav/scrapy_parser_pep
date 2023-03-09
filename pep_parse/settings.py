BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"


ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        'headers': ['Номер', 'Название', 'Статус'],
    },
}

ITEM_PIPELINES = {
   'pep_parse.pipelines.PepParsePipeline': 300,
}
