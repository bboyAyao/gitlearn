from scrapy import cmdline

name = 'DoubanMovie'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())