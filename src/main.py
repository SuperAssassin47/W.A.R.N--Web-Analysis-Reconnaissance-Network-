from web_scraping_engine import fetch_website, analyse_html, generate_report

def App_Entry_Point():
    # collecting URL from user
    webURL = input("Enter website URL to scrape: ").strip()

    print(f"\nFetching website source code from {webURL}...")
    html_src = fetch_website(webURL) # collecting HTML source code

    if html_src: # after collecting HTML...
        print("\nAnalyzing source code for embedded malware...")
        malware_detected = analyse_html(html_src) # analyse for embedded malware

        print("\nGenerating Report...")
        generate_report(webURL, malware_detected) # then generate the report

    else:
        # if program failed to collect website source code, ERROR
        print("[!] Error! Failed to analyse website source code.")
