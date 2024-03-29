import csv
import datetime as dt

BASE_DIR = 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status = {}

    def process_item(self, item, spider):
        self.status[item['status']] = self.status.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        with open(
            (
                f'{BASE_DIR}/status_summary_'
                f'{str(dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}'
                f'.csv'
            ), 'w', encoding='utf-8'
        ) as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows([
                ('Статус', 'Количество'),
                *self.status.items(),
                ('Всего', sum(self.status.values()))
            ])
