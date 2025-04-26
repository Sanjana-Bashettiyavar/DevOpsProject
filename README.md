# Node.js Scraper & Flask Web Server (Dockerized)


Author - Sanjana Bashettiyavar

## Overview
This project demonstrates a Devops-style containerized application using:

--Node.js with Puppeteer for web scraping.
--Python with Flask.
--Docker multi-stage builds foe efficient deployment.

The dockerized container(app) scrapes the title and heading from target url:http://wikipedia.org and serves as a JSON Interface with a JSON response.

## Build commands used

bash
docker build --build-arg SCRAPE_URL=https://wikipedia.org -t web-scraper .
docker run -p 5000:5000 scraper-app
