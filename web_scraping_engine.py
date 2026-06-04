import requests, re
from datetime import datetime

import os

def fetch_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Ensure ONLY HTML code is analysed
        if "text/html" not in response.headers.get("Content-Type", ""):
            return None

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error! Unable to fetch site source code: {e}")
        return None

def analyse_html(html):
    html = re.sub(r"\s+", " ", html) # normalising the HTML code first

    threats_dict = {
        "Encoded JS (atob/btoa)": r"(?:atob|btoa)\s*\(",
        "Base64 Data URIs": r"data:[^;]+;base64,[A-Za-z0-9+/=]+",
        "Document Write Injection": r"document\.write\s*\(\s*(atob|unescape|String\.fromCharCode)",
        "Suspicious iframes": r"<iframe[^>]*src\s*=\s*['\"]?([^'\"> ]+)",
        "Hidden iframes": r"<iframe[^>]*(display\s*:\s*none|visibility\s*:\s*hidden|width\s*=\s*['\"]?0|height\s*=\s*['\"]?0)",
        "Hex-encoded JavaScript": r"\\x[0-9A-Fa-f]{2}",
        "Unicode escape sequences": r"\\u[0-9A-Fa-f]{4}",
        "Suspicious charcode arrays": r"\[(?:\d{2,3},){3,}\d{2,3}\]",
        "Suspicious redirects": r"(window\.location|location\.replace|meta\s+http-equiv=['\"]refresh['\"])",
        "Suspicious eval usage": r"(?:eval|window\[['\"]eval['\"]\]|this\[['\"]eval['\"]\])"
    }

    threats_found = {}

    for threat_name, pattern in threats_dict.items():
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            threats_found[threat_name] = matches # add detected threats to threats_found
    return threats_found

def generate_report(url, threats, filename="web_scraping_report.txt"):

    base_dir = os.path.join(os.getenv("LOCALAPPDATA"), "W.A.R.N", "reports")
    os.makedirs(base_dir, exist_ok=True)

    report_path = os.path.join(base_dir, filename)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Website Scraping Report for: {url}\n")
        f.write("=" * 40 + "\n")

        if threats:
            f.write("\nThreats Found:\n\n")
            for threat, details in threats.items():
                f.write(f"{threat}:\n")
                for detail in details:
                    safe_detail = str(detail).replace("\n", "\\n")
                    f.write(f"  - {safe_detail}\n")
            f.write("\n")
        else:
            f.write("No threats detected.\n")
        f.write("=" * 40 + "\n")
    print(f"[/] Report saved to {report_path}")
