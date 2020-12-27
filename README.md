# ProductScraper

Idea: Send an email alert when the price of the product goes down.

1. Used smtplib package for email
2. Used BeautifulSoup package for HTML parsing

Functionality: When a specific URL of the product from Amazon is provided, it keeps track of the pricing and notifies with an email alert when pricing goes down. Currently, the code is scheduled to run every day at a specific time to receive email alert.

Scope of Improvement: 
1. Make Dynamic inputs available.
2. Notify immediately after the price goes down instead of scheduled run once in a day.
