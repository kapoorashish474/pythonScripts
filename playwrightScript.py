import json
from playwright.sync_api import sync_playwright

""" Time to First Byte (TTFB): This is the time from the start of the navigation until the first byte of the response is received. It’s an important metric for assessing the responsiveness of a server.
TTFB=responseStart−navigationStart


DNS Lookup Time: The time taken to resolve the domain name into an IP address.
DNS Lookup Time=domainLookupEnd−domainLookupStart


TCP Handshake Time: The time taken to establish a TCP connection between the client and the server.
TCP Handshake Time=connectEnd−connectStart


SSL/TLS Negotiation Time: The time taken for the SSL/TLS handshake to occur, which is part of establishing a secure connection.
SSL/TLS Negotiation Time=connectEnd−secureConnectionStart


Time to Interactive (TTI): The time until the page is fully interactive and responsive to user input.
TTI=domInteractive−navigationStart


DOM Content Loaded Time: The time taken for the HTML document to be fully parsed and the DOMContentLoaded event to fire.
DOM Content Loaded Time=domContentLoadedEventEnd−navigationStart


Page Load Time: The total time taken from the start of the navigation to the load event end.
Page Load Time=loadEventEnd−navigationStart """

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://google.com')  # Replace with your desired URL

    # Wait for the page to load
    page.wait_for_load_state('networkidle')

    # Retrieve and print performance metrics
    metrics_json = page.evaluate('''() => JSON.stringify(window.performance.timing)''')
    performance_timing = json.loads(metrics_json)
    
    # Calculations
    ttfb = performance_timing['responseStart'] - performance_timing['navigationStart']
    dns_lookup_time = performance_timing['domainLookupEnd'] - performance_timing['domainLookupStart']
    tcp_handshake_time = performance_timing['connectEnd'] - performance_timing['connectStart']
    ssl_negotiation_time = performance_timing['connectEnd'] - performance_timing['secureConnectionStart']
    tti = performance_timing['domInteractive'] - performance_timing['navigationStart']
    dom_content_loaded_time = performance_timing['domContentLoadedEventEnd'] - performance_timing['navigationStart']
    page_load_time = performance_timing['loadEventEnd'] - performance_timing['navigationStart']

    # Output results
    print(f"Time to First Byte (TTFB): {ttfb} ms")
    print(f"DNS Lookup Time: {dns_lookup_time} ms")
    print(f"TCP Handshake Time: {tcp_handshake_time} ms")
    print(f"SSL/TLS Negotiation Time: {ssl_negotiation_time} ms")
    print(f"Time to Interactive (TTI): {tti} ms")
    print(f"DOM Content Loaded Time: {dom_content_loaded_time} ms")
    print(f"Page Load Time: {page_load_time} ms")

    # Calculate the difference between connectStart and connectEnd
    connection_time = performance_timing['connectEnd'] - performance_timing['connectStart']

    print(f"Time difference between connectStart and connectEnd: {connection_time} ms")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
