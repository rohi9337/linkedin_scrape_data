import scrapy


class LinkedinspiderSpider(scrapy.Spider):
    name = "linkedinspider"
    allowed_domains = ["www.linkedin.com"]
    base_url = 'https://www.linkedin.com/jobs/search'
    params = {
        'keywords': 'django',
        'position': 1,
        'pageNum': 0
    }

    def start_requests(self):
        url = self.base_url + '?' + '&'.join([f"{key}={value}" for key, value in self.params.items()])
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        # job_titles = response.css('a.job-card-list__title::text').getall()
        # for title in job_titles:
        #     yield {'job_title': title}

        for job in response.css('a.base-card__full-link'):
            job_title = job.css('span.sr-only::text').get()
            job_url = job.css('::attr(href)').get()
            yield {
                'job_title': job_title.strip() if job_title else None,
                'job_url': job_url
            }
