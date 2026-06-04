# W.A.R.N--Web-Analysis-Reconnaissance-Network-

W.A.R.N is a Web Scraping application which provides you with different types of web scraping modules. The first scraper takes in website URLs and, upon clicking 'Enter', the scraper begins crawling the website to search for malware definitions using pre-defined patterns.

# What are the malware patterns?

The malware patterns which are used to identify potentially suspicious code are as follows:
- eval/atob/btoa --> this searches for suspicious/obfuscated JavaScript code. This also identifies little scripts enveloped inside <script> tags that potentially load shady domains.
- iframes --> this searches for iframe elements within HTML code with either 'width=0' or 'height=0'. This also searches for hidden iframes as well to make sure all embedded malicious software surfaces.
- The scraper also flags potentially suspicious external links like within advertisements which e-commerce websites like Amazon have propagated over everywhere.
- The scraper is also configured to search Obfuscated or encoded content, such as obfuscated JavaScript. This is done by searching for suspicious Base64 strings, hex-encoded JavaScript and long unreadable strings inside <script> tags, for example. These are the basis for detecting hidden payloads.

These malware patterns are some of the many patterns which I am using within this web scraper to uncover embedded or hidden malicious code before it does any harm.

DISCLAIMER: This is can ongoing project. I will implementing more modules to go alongside the initial malware detection web scraper.

Happy Coding and enjoy the app :)
