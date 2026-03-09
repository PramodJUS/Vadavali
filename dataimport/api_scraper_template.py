"""
API-Based Scraper Template
(Use this if you find a direct API endpoint via network tab inspection)

INSTRUCTIONS:
1. Do manual network inspection (see inspect_network_api.md)
2. Find the API endpoint that returns article data
3. Update the constants below with actual values
4. Test with test_api() function
5. Run full scrape with scrape_all_via_api()
"""

import requests
import json
import time
from pathlib import Path

# ============================================================================
# CONFIGURATION - UPDATE THESE AFTER NETWORK TAB INSPECTION
# ============================================================================

# API endpoint (example - replace with actual)
API_BASE_URL = "https://dvaitavedanta.in/api/articles"  # UPDATE THIS

# Headers copied from browser DevTools
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://dvaitavedanta.in/',
    'Accept': 'application/json, text/html',
    'X-Requested-With': 'XMLHttpRequest',  # Common for AJAX requests
    # Add Cookie if required (copy from browser):
    # 'Cookie': 'session_id=xxx; _ga=yyy; ...',
}

# Output paths
OUTPUT_JSON = "../Grantha/grantha-details-api.json"
OUTPUT_CSV = "../Grantha/mainpage-api.csv"

# Topic configurations (same as scrape_selenium.py)
TOPIC_URLS = [
    {"id": 1, "category_id": 9011, "title": "मङ्गलमाचरणम्"},
    {"id": 2, "category_id": 9012, "title": "विप्रतिपत्तिविचार:"},
    # ... add all 47 topics
]


# ============================================================================
# API INTERACTION FUNCTIONS
# ============================================================================

def fetch_articles_for_category(category_id, max_pages=20):
    """
    Fetch all articles for a given category using the API

    Args:
        category_id: The category/topic ID
        max_pages: Maximum number of pages to fetch

    Returns:
        List of article data dictionaries
    """
    articles = []

    for page in range(1, max_pages + 1):
        print(f"    Fetching page {page}...")

        # UPDATE THIS based on actual API structure
        params = {
            'category': category_id,
            'page': page,
            # Add other params as needed (offset, limit, etc.)
        }

        try:
            response = requests.get(API_BASE_URL, headers=HEADERS, params=params, timeout=10)
            response.raise_for_status()

            # Parse response - adjust based on actual format
            if 'application/json' in response.headers.get('Content-Type', ''):
                data = response.json()

                # UPDATE THIS based on actual JSON structure
                # Example structures:
                # Option 1: {"articles": [{...}, {...}]}
                # Option 2: {"data": {"items": [{...}]}}
                # Option 3: [{...}, {...}]  # Direct array

                # PLACEHOLDER - UPDATE THIS
                new_articles = data.get('articles', [])

                if not new_articles:
                    print(f"      No more articles on page {page}")
                    break

                articles.extend(new_articles)
                print(f"      Got {len(new_articles)} articles")

                time.sleep(0.5)  # Be polite

            else:
                # HTML response - may need to parse
                print(f"      [WARNING] Got HTML response instead of JSON")
                # You might need to use BeautifulSoup here
                break

        except requests.exceptions.RequestException as e:
            print(f"      [ERROR] API request failed: {e}")
            break

    print(f"    Total articles fetched: {len(articles)}")
    return articles


def extract_text_from_article(article_data):
    """
    Extract and structure text from API article data

    Args:
        article_data: Single article dict from API

    Returns:
        Dict with {वादावली, भावदीपा, प्रकाशः, विवर्णम्}
    """
    # UPDATE THIS based on actual article structure

    # Example structure from API might be:
    # {
    #   "id": 9061,
    #   "vadavali_text": "...",
    #   "bhava_deepa_text": "...",
    #   "prakasha_text": "...",
    #   "vivarnam_text": "..."
    # }

    # PLACEHOLDER - UPDATE THIS
    return {
        'वादावली': article_data.get('vadavali_text', ''),
        'भावदीपा': article_data.get('bhava_deepa_text', ''),
        'प्रकाशः': article_data.get('prakasha_text', ''),
        'विवर्णम्': article_data.get('vivarnam_text', ''),
    }


# ============================================================================
# MAIN SCRAPING LOGIC
# ============================================================================

def scrape_topic_via_api(category_id, topic_title):
    """
    Scrape a single topic using the API

    Returns:
        Dict with parts: {Part#1: {...}, Part#2: {...}}
    """
    print(f"\n  Fetching via API: Category {category_id}")

    articles = fetch_articles_for_category(category_id)

    if not articles:
        print("    [WARNING] No articles found")
        return {}

    # Structure data into parts
    parts = {}

    for idx, article in enumerate(articles, 1):
        part_data = extract_text_from_article(article)

        # Show stats
        print(f"    Part#{idx}:")
        for key, text in part_data.items():
            print(f"      {key}: {len(text)} chars")

        parts[f'Part#{idx}'] = part_data

    return parts


def scrape_all_via_api():
    """
    Main API scraping orchestrator
    """
    print("="*70)
    print(" API-Based Vadavali Scraper")
    print(" - Direct API calls (no browser needed)")
    print(" - Fast and reliable")
    print("="*70)
    print()

    grantha_data = {}
    csv_data = []

    print(f"[STEP 1/2] Scraping {len(TOPIC_URLS)} Topics via API")
    print("-"*70)

    for topic_info in TOPIC_URLS:
        topic_id = str(topic_info['id'])
        category_id = topic_info['category_id']
        topic_title = topic_info['title']

        print(f"\n[Topic {topic_id}] {topic_title}")

        parts = scrape_topic_via_api(category_id, topic_title)

        if parts:
            grantha_data[topic_id] = parts
            csv_data.append({'id': topic_id, 'sutra_text': topic_title})
            print(f"  [OK] Scraped {len(parts)} part(s)")
        else:
            print(f"  [FAIL] No content extracted")

    # Save files
    print(f"\n[STEP 2/2] Saving Files")
    print("-"*70)

    # Save JSON
    json_path = Path(OUTPUT_JSON)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(grantha_data, f, ensure_ascii=False, indent=2)

    print(f"  [OK] JSON: {json_path.resolve()}")
    print(f"      Topics: {len(grantha_data)}")

    # Save CSV
    import csv
    csv_path = Path(OUTPUT_CSV)
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'sutra_text'])
        writer.writeheader()
        writer.writerows(csv_data)

    print(f"  [OK] CSV: {csv_path.resolve()}")

    print("\n" + "="*70)
    print("[SUCCESS] API Scraping Complete!")
    print("="*70)


# ============================================================================
# TESTING FUNCTIONS
# ============================================================================

def test_api():
    """
    Test API on a single topic to verify configuration
    """
    print("="*70)
    print(" API Configuration Test")
    print("="*70)
    print()

    # Test on Topic 4 (known to have missing articles)
    test_category = 9014
    print(f"Testing API on category {test_category}...")
    print(f"API URL: {API_BASE_URL}")
    print(f"Headers: {HEADERS}")
    print()

    articles = fetch_articles_for_category(test_category, max_pages=5)

    if articles:
        print(f"\n✅ SUCCESS: API returned {len(articles)} articles")

        # Check for missing article IDs
        article_ids = [a.get('id') for a in articles]
        print(f"Article IDs: {article_ids}")

        # Check if the problematic articles are present
        missing_ids = [9065, 9076, 9080]
        found = [aid for aid in missing_ids if aid in article_ids]

        if found:
            print(f"\n🎉 GREAT! Found previously missing articles: {found}")
        else:
            print(f"\n⚠️  Missing articles not in this category")

    else:
        print(f"\n❌ FAILURE: API returned no data")
        print(f"\nPossible issues:")
        print(f"  1. Incorrect API_BASE_URL")
        print(f"  2. Missing or incorrect headers (especially Cookie)")
        print(f"  3. Wrong query parameters")
        print(f"  4. API requires authentication")
        print(f"\nNext steps:")
        print(f"  1. Check Network tab in browser DevTools")
        print(f"  2. Copy exact request URL and headers")
        print(f"  3. Update configuration above")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        # Test mode
        test_api()
    else:
        # Full scrape
        try:
            scrape_all_via_api()
        except KeyboardInterrupt:
            print("\n\n[INFO] Scraping interrupted by user")
        except Exception as e:
            print(f"\n\n[ERROR] {e}")
            import traceback
            traceback.print_exc()
