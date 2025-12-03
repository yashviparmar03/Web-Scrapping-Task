# Web-Scrapping-Task
A Python-based web scraping tool that extracts all iPhone 13 Pro models from Flipkart along with their price and rating. Developed using BeautifulSoup4, Requests, Pandas, and Jupyter Notebook, this scraper collects product data and exports it into a clean, readable CSV file for analysis.

📱 Flipkart iPhone 13 Pro Scraper

A Python-based web scraping project that extracts details of all iPhone 13 Pro models from Flipkart, including product title, rating, and price.
It organizes the data and exports everything into a clean CSV file using BeautifulSoup and Jupyter Notebook.

📌 Project Overview

The Flipkart iPhone Scraper is designed to fetch real-time product information from Flipkart.
It helps users analyze prices, compare models, or prepare datasets for data analysis.

This scraper collects:

Product Name

Rating

Price

All the extracted information is stored in a structured CSV file.

⭐ Features

Extracts all available iPhone 13 Pro models from Flipkart

Scrapes Title, Rating, Price

Converts raw HTML into clean & readable data

Saves results into a CSV file

Easy to run in Jupyter Notebook

Beginner-friendly

Uses only lightweight libraries

🛠 Technologies Used

Python

BeautifulSoup4

Requests

Pandas

Jupyter Notebook

📂 Folder Structure
📁 Flipkart-iPhone-Scraper
│── 📄 scraper.ipynb
│── 📄 requirements.txt
│── 📄 output.csv
│── 📄 README.md

⚙️ Installation Steps
1️⃣ Clone the Repository
git clone https://github.com/your-username/Flipkart-iPhone-Scraper.git
cd Flipkart-iPhone-Scraper

2️⃣ Install Required Libraries

Make sure Python is installed.

Install dependencies:

pip install requests beautifulsoup4 pandas

3️⃣ Open Jupyter Notebook
jupyter notebook

4️⃣ Run the Notebook

Open scraper.ipynb

Run all cells

The scraper will fetch data from Flipkart

A CSV file will be created automatically

🧠 How the Scraper Works
Step 1 — Send request to Flipkart

The script uses the requests library to load the webpage HTML.

Step 2 — Parse HTML

BeautifulSoup extracts:

Product title

Price

Rating

It filters only iPhone 13 Pro models.

Step 3 — Store in Python lists

All extracted values are appended into lists.

Step 4 — Convert to DataFrame

Pandas organizes the data neatly.

Step 5 — Export to CSV

Final output is saved as:

output.csv

📊 Output Example
Product Name	Rating	Price
iPhone 13 Pro (128GB)	4.6	₹1,19,999
iPhone 13 Pro (256GB)	4.7	₹1,29,999
🚀 Future Enhancements

Add support for multiple iPhone versions

Track price changes daily

Build a visual dashboard

Add automation using Selenium

Screenshot:
<img width="869" height="784" alt="Screenshot 2025-09-23 114502" src="https://github.com/user-attachments/assets/2569793a-c11f-4fa1-8915-980b3ac7da27" />
