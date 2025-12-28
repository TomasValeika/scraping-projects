# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobFinderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    tax_info = scrapy.Field()  # with or with out tax
    # salary_info = scrapy.Field()  # hourly, monthly, ect.
    job_type = scrapy.Field()  # part time, full day
    city = scrapy.Field()
    company_name = scrapy.Field()
    saw_job = scrapy.Field()  # how many people saw this job
    time_till_end = scrapy.Field()
    description = scrapy.Field()
