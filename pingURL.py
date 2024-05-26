from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def open_incognito_browsers(urls, num_repeats=10):
    # Set up Chrome options for incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    try:
        # Initialize the WebDriver (assuming chromedriver is in your system PATH)
        driver = webdriver.Chrome(options=chrome_options)

        for url in urls:
            for _ in range(num_repeats):
                # Open each URL in a new tab
                driver.execute_script(f"window.open('{url}', '_blank');")
                print(f"Opened {url} in a new tab.")

                # Wait for a few seconds (you can adjust this as needed)
                time.sleep(5)

        # Don't close the browser here; we'll close it after all iterations
        print("All URLs opened successfully.")
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()

    # Close the browser after all iterations are done
    driver.quit()
    print("Incognito browsers closed.")

if __name__ == "__main__":
    target_urls = [
        "https://www.stubhub.com/icc-men-s-t20-world-cup-new-york-tickets-6-12-2024/event/152953783/?quantity=2&sections=1955990&ticketClasses=5742&rows=&seatTypes=&listingQty=&listingId=7415264818",
        "https://www.linkedin.com/in/ashkap/",
        "https://x.com/kapoor_ashish4"  # Add more URLs here
    ]
    open_incognito_browsers(target_urls, num_repeats=10)
