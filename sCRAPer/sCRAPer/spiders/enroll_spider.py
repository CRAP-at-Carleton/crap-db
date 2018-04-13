import scrapy
import w3lib.html
from datetime import datetime
from .starter_data import DEPTS


class QuotesSpider(scrapy.Spider):
    name = "enroll"

    def start_requests(self):

        term = '18WI'
        base_url = 'https://apps.carleton.edu/campus/registrar/schedule/enroll/'
        urls = [base_url+'?term={}&subject={}'.format(term, dept) for dept in DEPTS]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Get rid of all those pesky <em> tags
        body = response.body_as_unicode()
        new_body = w3lib.html.remove_tags(body, which_ones=('em',))
        response = response.replace(body=new_body)

        for course in response.css('div.course'):
            yield get_parse_dict(course)


def get_parse_dict(course) -> dict:
    """helper fcn to QuotesSpider.parse()"""

    # course name, credits, building, room
    name = course.css('.title::text').extract_first().strip()
    credits = course.css('.title .credits::text').extract_first().strip().split(' ')[0]

    # dept, course_num, course_section
    dept, _tmp = course.css(".title .coursenum::text").extract_first().strip().split(' ')
    course_num, course_section = _tmp.split('.')

    # building, room_num
    _loc = course.css('.locations ::text').extract_first()
    building, room_num = _loc.rsplit(' ', 1) if _loc else (None, None)

    # prof, description
    prof, description = course.css('.description ::text').extract()[1:3]

    # prereq
    prereq = str(course.css('.description .prereq::text').extract_first())
    prereq = prereq.replace('Prerequisite: ', '')

    # schedule
    _struct = course.css('table.schedule td').extract()
    _vals = []
    for row in _struct:
        d = {'start': None, 'end': None,}
        content = w3lib.html.remove_tags(row)
        if content:
            mid = content.index('m') + 1
            d['start'] = datetime.strptime(content[:mid], '%I:%M%p')
            d['end'] = datetime.strptime(content[mid:], '%I:%M%p')
        _vals.append(d)
    _days = ['mon', 'tue', 'wed', 'thu', 'fri']
    sched = dict(zip(_days, _vals))

    return dict(
        name=name, credits=credits, dept=dept, course_num=course_num,
        course_section=course_section, prof=prof, description=description,
        prereq=prereq, building=building, room_num=room_num, sched=sched,)
