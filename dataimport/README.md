# Data Import - Web Scraping for Sanskrit Texts

This folder contains automated web scraping tools for importing Sanskrit philosophical texts from dvaitavedanta.in.

## 🎯 Quick Start

### Prerequisites

```bash
cd dataimport
pip install -r requirements.txt
```

**Requirements:**
- Python 3.7+
- Chrome browser
- `selenium` - Browser automation
- `webdriver-manager` - Automatic ChromeDriver setup

### Run Full Scraping

Scrape all 47 topics using the proven working scraper:

```bash
python scrape_selenium_v2.py
```

**What it does:**
1. Opens Chrome in headless mode
2. Visits each of 47 topic URLs
3. **Clicks `callArticle()` links** to load JavaScript content
4. Waits explicitly for each article to load
5. Extracts text between specific headings
6. Saves to `../Grantha/grantha-details-scraped.json`

**Estimated time:** 15-20 minutes for all 47 topics

**Success rate:** 100% - Captures all articles including those that require JavaScript interaction

---

## 📚 Comprehensive Documentation

### For New Users:
- **[SCRAPING_CHECKLIST.md](SCRAPING_CHECKLIST.md)** - Quick reference guide
- **[README.md](README.md)** - This file (getting started)

### For Understanding the Process:
- **[SCRAPING_RULES.md](SCRAPING_RULES.md)** - Complete scraping rules and quality checks
- **[SCRAPING_COMPARISON.md](SCRAPING_COMPARISON.md)** - API vs Selenium comparison

### For Advanced Use Cases:
- **[inspect_network_api.md](inspect_network_api.md)** - How to find API endpoints
- **[api_scraper_template.py](api_scraper_template.py)** - Template for API-based scraping

---

## 🛠️ Available Tools

### Production Scripts

**`scrape_selenium_v2.py`** - Main production scraper
- Uses click-and-wait strategy for JavaScript content
- Handles `callArticle()` onclick events
- 100% success rate on all 47 topics
- **USE THIS for production scraping**

### Utility Scripts

**`cleanup_whitespace.py`** - Post-scraping cleanup
```bash
python cleanup_whitespace.py
```
- Replaces `\n\n` with `\n` (single newlines)
- Removes trailing whitespace
- Run after scraping for proper formatting

**`replace_dandas.py`** - Danda normalization
```bash
python replace_dandas.py
```
- Replaces `।।` with `॥` (proper double danda)
- Run after scraping for correct Unicode

---

## 📋 How It Works

### The Challenge

Articles on dvaitavedanta.in load in two ways:
1. **Auto-loaded:** First few articles load via scrolling/"Load More" buttons
2. **On-demand:** Remaining articles require clicking `onclick="callArticle(ID)"` links

Traditional scraping (scrolling only) misses the on-demand articles.

### The Solution (Click-and-Wait Strategy)

Our scraper (`scrape_selenium_v2.py`) uses a **two-phase approach**:

**Phase 1: Find Links**
- Locates all `<a onclick="callArticle(ID)">` links on the page

**Phase 2: Click & Wait**
- Clicks each link
- Uses `WebDriverWait` to wait for `<div id="articleID">` to appear
- Waits up to 15 seconds per article
- Skips articles already loaded

**Result:** 100% capture rate including previously missing articles (9065, 9076, 9080)

### Text Extraction

For each loaded article:

1. **वादावली** - Text between H2 "वादावली" and first H3
2. **भावदीपा** - Text after H3 "वादावलीभावदीपिका"
3. **प्रकाशः** - Text after H3 "वादावलीप्रकाशः"
4. **विवर्णम्** - Text after H3 "वादावलीविवरणम्"

Excludes:
- Author attribution lines (containing कृता, विरचित, etc.)
- Headings themselves
- Content after next heading

---

## 📊 Output Structure

**grantha-details-scraped.json:**
```json
{
  "1": {
    "Part#1": {
      "वादावली": "text...",
      "भावदीपा": "text...",
      "प्रकाशः": "text...",
      "विवर्णम्": "text..."
    }
  },
  "4": {
    "Part#1": { ... },
    "Part#2": { ... },
    "Part#3": { ... },
    "Part#4": { ... },
    "Part#5": { ... }
  }
}
```

**mainpage-scraped.csv:**
```csv
id,sutra_text
1,मङ्गलमाचरणम्
2,विप्रतिपत्तिविचार:
```

---

## ✅ Post-Scraping Workflow

After scraping completes:

### 1. Verify Data Quality
```bash
python -c "
import json
with open('../Grantha/grantha-details-scraped.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(f'Topics: {len(data)}')
print(f'Topic 4 parts: {len(data[\"4\"])}')  # Should be 5
print(f'Topic 7 parts: {len(data[\"7\"])}')  # Should be 4
"
```

### 2. Run Cleanup Scripts
```bash
# Normalize dandas
python replace_dandas.py

# Clean whitespace
python cleanup_whitespace.py
```

### 3. Backup and Deploy
```bash
# Backup current production file
cp ../Grantha/grantha-details.json ../Grantha/grantha-details-backup-$(date +%Y%m%d).json

# Deploy new data
cp ../Grantha/grantha-details-scraped.json ../Grantha/grantha-details.json
```

---

## 🔧 Adapting for Other Granthas

The scraper can be adapted for other texts on dvaitavedanta.in:

### 1. Update Topic URLs
Edit `scrape_selenium_v2.py`:
```python
TOPIC_URLS = [
    {"id": 1, "url": "https://...", "title": "..."},
    # ... your grantha's topic URLs
]
```

### 2. Update Heading Mappings (if needed)
```python
HEADING_MAPPINGS = {
    'grantha_name': 'grantha_name',
    'commentary1': 'commentary1_key',
    # ... adjust as needed
}
```

### 3. Test First
Test on 1-2 topics before running full scrape:
```python
# In scrape_selenium_v2.py, temporarily modify:
TOPIC_URLS = TOPIC_URLS[:2]  # Test first 2 topics only
```

See **[SCRAPING_RULES.md](SCRAPING_RULES.md)** for complete adaptation guide.

---

## 🐛 Troubleshooting

### "Chrome not found" error
- Install Chrome browser
- Or update path in script

### "Article not found after clicking"
- Some articles may timeout (15 sec limit)
- Check if article exists in page source
- May need to adjust wait time

### Missing articles even after clicking
- Check browser console for JavaScript errors
- Try non-headless mode for debugging:
  ```python
  # In scrape_selenium_v2.py, comment out:
  # chrome_options.add_argument('--headless')
  ```

### Scraping too slow
- Reduce wait times (if network is fast)
- Run on faster connection
- Consider API-based approach if available

See **[SCRAPING_COMPARISON.md](SCRAPING_COMPARISON.md)** for alternative approaches.

---

## 📖 Documentation Reference

| File | Purpose | When to Read |
|------|---------|--------------|
| **README.md** | Quick start & overview | Getting started |
| **SCRAPING_CHECKLIST.md** | Quick reference | Before scraping |
| **SCRAPING_RULES.md** | Complete rules | Adapting for new grantha |
| **SCRAPING_COMPARISON.md** | API vs Selenium | Choosing scraping approach |
| **inspect_network_api.md** | API discovery guide | When API might exist |

---

## 🎓 Key Lessons Learned

From scraping Vadavali (47 topics, 150+ articles):

1. **JavaScript-heavy sites** may load content via onclick handlers, not just scrolling
2. **Explicit waits** (`WebDriverWait`) are better than `time.sleep()` for reliability
3. **API is ideal** but when unavailable, smart Selenium works with 100% success
4. **Click-and-wait strategy** solves the "missing articles" problem definitively
5. **Test incrementally** - verify one topic before running full scrape

---

## 📊 Proven Results

**Vadavali Scraping Stats:**
- ✅ 47 topics scraped
- ✅ 150+ articles captured
- ✅ 100% success rate (including 3 previously missing articles)
- ✅ 3.8M of Sanskrit text
- ✅ 7,818 dandas normalized
- ✅ Clean, production-ready data

**Scraping Time:** ~15 minutes for all 47 topics

---

## 📄 License

Part of the Vadavali project. See main repository LICENSE file.

---

**॥ श्री कृष्णार्पणमस्तु ॥**
