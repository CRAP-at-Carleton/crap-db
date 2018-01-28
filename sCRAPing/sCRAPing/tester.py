"""
Used to test/improve scraper.

Run:
`scrapy shell https://apps.carleton.edu/campus/registrar/schedule/enroll/\?term\=18WI\&subject\=ENGL`

Then copy and paste all/part of this code into REPL
"""

import w3lib.html
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Get rid of all those pesky <em> tags
body = response.body_as_unicode()
new_body = w3lib.html.remove_tags(body, which_ones=('em',))
response = response.replace(body=new_body)

courses = response.css('div.course')

for course in response.css('div.course'):

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
        d = {'start': None,'end': None,}
        content = w3lib.html.remove_tags(row)
        if content:
            mid = content.index('m') + 1
            d['start'] = content[:mid]
            d['end'] = content[mid:]
        _vals.append(d)
    _days = ['mon', 'tue', 'wed', 'thu', 'fri']
    sched = dict(zip(_days, _vals))

    # TODO: sophomore priority?

    d = dict(
        name=name, credits=credits, dept=dept,
        course_num=course_num, course_section=course_section,
        prof=prof, description=description, prereq=prereq,
        building=building, room_num=room_num,
        sched=sched)

    pp.pprint(d)
