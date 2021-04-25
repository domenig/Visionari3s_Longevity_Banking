# Visionari3s_Longevity_Banking

Team name:      Visionari3s
Project name:   Longivity Bank

## Team Members
Team 4
*   Alfonso Meraz(USA)
*    Alejandra Gassó Azanza (UK)
*    Philipp Domenig(Austria)
*    Oghenekparobo Onosemuode( Nigeria)
*    Eros Moura Lima(Brasil)
*    Rafael Gago (Chile)

## Team Location
International (following UK timezones).

# Project Guideline
* Development tools used to build the project:
  * Back-end: Python (Visual studio). Use of two different APIs to scrape financials and recommendations using Yahoo for the interactive investment bot.
            Also developed a beta version of the interactive investment bot using Interactive Brokers (IBAPI, not used in final project due to limited data access).
  * Front-end: JavaScript. Connected to back-end through Flask.

* SDKs used:
  * Adobe Dreamweaver.
  * Bootstrap4 (framework).

* APIs used:
  * Yahoo Finance API: 2 different ones, to scrape financials and stock recommendations respectively.
  * Interactive Brokers API (IBAPI): Used in beta version to feed real-time stock-related data into back-end code. Not used because we could not access the data needed without a private account (hence the switch to Yahoo Finance).

* Datasets with links and a description of how the data has been reused:
  * No third-party datasets used: Aside from real-time stock data scraped from Yahoo Finance all was own work.

* Assets used:
  * None (all own work, e.g. logo).

* Libraries used:
  * Back-end (Python libraries): numpy, pandas, os, flask, csv, datetime, time, io, requests, yfinance, sys (+ own/created libraries).
  * Front-end: Adobe XD wireframes components.
  
* Components not created at the Hackathon:
  * None.

# Project Summary
  In this hackathon we decided to focus on the challenge of longevity banking because we believe there is great growth potential to provide comprehensive, user-friendly services that empower over 60s to take control of their investment decisions. In order to facilitate this we created an algorythm that assesses their risk aversion together with their interest in ESG to build an investment portfolio that provides them with the risk-return ratio they desire while enabling them to be in control of their investments. Additionally, we built a service within the app that helps diminish one of the main pain points of this age group: tax payable on inheritance. We created a second algorythm that calculates how to distribute payments annually based on certain user inputs (such as user age, money to be passed down, relationship with person to inherit the money) in order to minimize tax payable. Note this last algorythm works with Pennsylvania's (US) tax rates and fgure estimates for demonstration purposes in the beta version.
