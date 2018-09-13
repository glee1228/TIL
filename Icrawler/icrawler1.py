from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': '/Users/donghoon/clothes/cotton'})
filters = dict(
    size='large'
    )
google_crawler.crawl(keyword='cotton clothes png', filters=filters, max_num=10000, file_idx_offset=0)