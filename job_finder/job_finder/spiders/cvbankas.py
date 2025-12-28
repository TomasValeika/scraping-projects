import scrapy
from job_finder.items import JobFinderItem


class CvbankasSpider(scrapy.Spider):
    name = "cvbankas"
    allowed_domains = ["www.cvbankas.lt"]
    start_urls = ["https://www.cvbankas.lt/"]

    def parse(self, response):
        # job_url fronm page
        jobs_url = response.css(
            "a.list_a.can_visited.list_a_has_logo::attr(href)"
        ).getall()

        # next page url
        next_page_url = response.css("a.prev_next::attr(href)").get()

    def parse_jobs(self, response):
        """
        aprasome is kur ir kokia informacija surinkti
        sukuriame klase ir pagal klase surenkame duomenis
        """
        item = JobFinderItem()

        item["job_name"] = response.css("h1.heading1::text").get()
        item["salary"] = response.css(
            "span.data_tag_component_salary_amount::text"
        ).get()
        item["tax_info"] = response.css("div.label_component_body::text").getall()[1]
        item["job_type"] = response.css("div.label_component_body::text").getall()[2]
        item["city"] = response.css('span[itemprop="addressLocality"]::text').get()
        item["company_name"] = response.css('h2[id="jobad_company_title"]::text').get()
        item["saw_job"] = response.css('strong[class="jobad_stat_value"]::text').get()
        item['time_till_end'] = response.css('time::text').get()
        item['description'] = 
