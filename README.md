## Python websrappers


### 1. canada-crs-score-scrapper
Get the latest CRS score for Express entry for Canadian residency as per their [doc](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html)

### Output
```
CRS score of lowest-ranked candidate invited: 471
```

---

### 2. data-entry-to-csv

Convert data entry from all listing into CSV as per HTML contents of http://sulphuric-acid.com.

### Pre-req

1. BeautifulSoup: ```pip install bs4```
2. lxml: ```pip install lxml```

### Output:

```results.csv``` would look something like this:

![Sample CSV results](/images/csv_output.JPG)


---

### 3. remitly

Scrape https://www.remitly.com/us/en/india/pricing for latest USD to INR currency exchange rate based off the current value. Can be used to run in cronjob for fetching at regular intervals, or plot a graph like: https://github.com/shreyasgaonkar/remitly-graph
