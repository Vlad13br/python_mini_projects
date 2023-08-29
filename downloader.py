from icrawler.builtin import GoogleImageCrawler


def googler_img_download():
    filters = dict(
        type='photo',
        size='large'
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword='', max_num=5,
                  filters=filters, file_idx_offset='auto')


def main():
    googler_img_download()


if __name__ == "__main__":
    main()
