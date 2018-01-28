# sCRAPer

## Usage

To generate JSON, run the following in this directory:

```bash
rm enroll.json
scrapy crawl enroll -o enroll.json
```

## Notes

For quick experimentation, try:

```bash
scrapy shell https://apps.carleton.edu/campus/registrar/schedule/enroll/\?term\=18WI\&subject\=ENGL
courses = response.css('div.course')
```