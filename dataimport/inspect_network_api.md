# How to Find the Hidden API Endpoint

## Step 1: Manual Network Tab Inspection

1. **Open Chrome/Edge in normal mode** (NOT headless, NOT Selenium)

2. **Open DevTools:**
   - Press `F12` or `Ctrl+Shift+I`
   - Go to **Network** tab
   - Filter by **Fetch/XHR** (APIs only)

3. **Navigate to a multi-part topic:**
   ```
   https://dvaitavedanta.in/category-details/9014/4434/sharaj/vathav/vathav/anarav
   ```

4. **Scroll down slowly** and watch the Network tab

5. **Look for XHR requests that load new articles**
   - Watch for requests that trigger when new article divs appear
   - Note the URL pattern
   - Note any query parameters (page, offset, category ID, etc.)

6. **Click on the request and examine:**
   - **Request URL:** The full API endpoint
   - **Request Headers:** Look for:
     - `User-Agent`
     - `Cookie` (especially session cookies)
     - `X-Requested-With` (often "XMLHttpRequest")
     - `Referer`
   - **Response:** Check if it's JSON or HTML
     - If JSON: Look for article IDs (9065, 9076, 9080)
     - If HTML: It's rendering partial HTML

## Step 2: What You're Looking For

### Example API patterns (hypothetical):

**Pattern 1: Paginated JSON API**
```
GET https://dvaitavedanta.in/api/articles?category=9014&page=2
Response: {"articles": [{"id": 9065, "title": "...", "content": "..."}, ...]}
```

**Pattern 2: Lazy Load HTML**
```
POST https://dvaitavedanta.in/load-more
Payload: {category_id: 9014, offset: 3}
Response: <div id="article9065">...</div>
```

**Pattern 3: GraphQL**
```
POST https://dvaitavedanta.in/graphql
Payload: {query: "query { articles(categoryId: 9014, limit: 10) { id, content } }"}
```

## Step 3: Capture the Working Request

### Using Chrome DevTools:

1. **Right-click on the XHR request** → **Copy** → **Copy as cURL**

2. **Convert cURL to Python requests:**
   - Use https://curlconverter.com/
   - Or manually write the Python code

### Example cURL:
```bash
curl 'https://dvaitavedanta.in/api/articles?cat=9014&page=2' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
  -H 'Cookie: session_id=abc123; _ga=GA1.2.xxxxx' \
  -H 'X-Requested-With: XMLHttpRequest'
```

### Converted to Python:
```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Cookie': 'session_id=abc123; _ga=GA1.2.xxxxx',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'https://dvaitavedanta.in/api/articles'
params = {'cat': 9014, 'page': 2}

response = requests.get(url, headers=headers, params=params)
data = response.json()  # or response.text if HTML

print(data)
```

## Step 4: Test the API

Create `test_api.py`:

```python
import requests
import json

# Headers copied from browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://dvaitavedanta.in/category-details/9014/4434/sharaj/vathav/vathav/anarav',
}

# Test on Topic 4 (should return articles 9061-9065)
url = 'https://dvaitavedanta.in/REPLACE_WITH_ACTUAL_API_ENDPOINT'

response = requests.get(url, headers=headers)

print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Response length: {len(response.text)} chars")

# Parse response
if 'application/json' in response.headers.get('Content-Type', ''):
    data = response.json()
    print(f"JSON keys: {data.keys()}")

    # Look for missing article IDs
    if 'articles' in data:
        article_ids = [a['id'] for a in data['articles']]
        print(f"Article IDs: {article_ids}")

        # Check if missing ones are present
        missing = [9065, 9076, 9080]
        found = [aid for aid in missing if aid in article_ids]
        print(f"Found missing articles: {found}")
else:
    # HTML response
    print("First 500 chars:")
    print(response.text[:500])

    # Check for article divs
    if 'article9065' in response.text:
        print("✓ Found article9065 in HTML response!")
```

## Step 5: What If No API Exists?

If you find **no XHR/Fetch requests** and all loading happens via JavaScript DOM manipulation:

### Option A: Improve Selenium (recommended)
- Increase wait times
- Use explicit waits for specific elements
- Check for "Load More" buttons dynamically

### Option B: Browser Automation Tools
Use `undetected-chromedriver` to bypass bot detection:

```python
import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get(url)
# ... rest of code
```

### Option C: Use Playwright (more reliable)
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    # Wait for all network to be idle
    page.wait_for_load_state('networkidle')

    articles = page.query_selector_all("div[id^='article']")
```

## Next Steps

1. **Try the improved Selenium approach first** (already updated in scrape_selenium.py)
2. **If still missing articles**, do manual network inspection
3. **Document your findings** here (update this file with actual API endpoint)
4. **Create api_scraper.py** if API is found

## Expected Outcome

**If API exists:**
- You'll see clean JSON responses with all article data
- Much faster scraping (no browser needed)
- More reliable (no DOM timing issues)

**If no API (just JavaScript lazy loading):**
- Stick with improved Selenium
- Consider Playwright for better reliability
- Ensure sufficient wait times and scroll detection
