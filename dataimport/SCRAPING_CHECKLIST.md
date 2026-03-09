# Scraping Checklist - Quick Reference

Use this checklist when scraping a new grantha. For detailed explanations, see [SCRAPING_RULES.md](SCRAPING_RULES.md).

## Pre-Scraping Setup

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Update grantha-specific configuration in script:
  - [ ] `GRANTHA_PATH`
  - [ ] `OUTPUT_JSON` filename
  - [ ] `OUTPUT_CSV` filename
  - [ ] `TOPIC_URLS` list
- [ ] Test on single topic: `python test_single_topic.py`
- [ ] Verify heading structure using `debug_headings.py`

## Extraction Rules Checklist

- [ ] Extract text ONLY between specific headings
- [ ] Main text: Between H2 and first H3
- [ ] Commentaries: Between each H3 and next H3
- [ ] Exclude all author attribution lines
- [ ] Handle multiple parts per topic (lazy loading)
- [ ] Scroll 15+ times to load all article divs
- [ ] Click "Load More" if present

## Text Cleanup Checklist

Run in this order:

1. [ ] Remove author attributions
   - [ ] ONLY remove SHORT lines (< 150 chars)
   - [ ] Lines containing: कृता, कृत:, विरचित, विरचिता
   - [ ] Check both start and end of text
   - [ ] DO NOT remove commentary prose mentioning authors

2. [ ] Normalize dandas
   - [ ] Replace `।।` with `॥`

3. [ ] Clean whitespace
   - [ ] Replace `\n\n+` with `\n`
   - [ ] Remove trailing spaces/newlines with `.rstrip()`
   - [ ] Remove zero-width spaces (\u200b)
   - [ ] Replace non-breaking spaces (\xa0)

## Quality Checks

### Automated Checks
- [ ] All topics have Part#1
- [ ] All parts have all 4 sections
- [ ] No author attributions in text
- [ ] No double newlines (\n\n)
- [ ] No trailing whitespace
- [ ] No ।। (should be ॥)

### Manual Checks
- [ ] Topic 1: ~80-100 chars for वादावली
- [ ] Topic 1: No "राघवेन्द्र" or "विरचित"
- [ ] Multi-part topic: All parts extracted
- [ ] Last topic: No closing attributions
- [ ] Random 5 topics: Verify clean text

### Verification (Optional but Recommended)
- [ ] Re-scrape Topic 1 to verify no typos
  ```bash
  python verify_topic1.py
  ```
- [ ] Check Sanskrit spellings are correct (compare scraped vs JSON)
- [ ] Compare scraped length with JSON data
- [ ] If differences found, investigate and use correct version

## Deployment Checklist

- [ ] Backup old data:
  ```bash
  mv grantha-details.json grantha-details_old.json
  mv mainpage.csv mainpage_old.csv
  ```
- [ ] Deploy new data:
  ```bash
  mv grantha-details-scraped.json grantha-details.json
  mv mainpage-scraped.csv mainpage.csv
  ```
- [ ] Test website with new data
- [ ] Verify random topics display correctly
- [ ] Check multi-part topics work
- [ ] Verify search functionality

## Common Issues Quick Reference

| Issue | Quick Fix |
|-------|-----------|
| Empty वादावली | Look for H2 not H3 |
| Identical वादावली & भावदीपा | Use exact match for वादावली |
| Only 1 part when multiple exist | Increase scroll attempts to 20+ |
| Author attribution still present | Add pattern to exclusion list |
| Double newlines remain | Run cleanup AFTER extraction |
| Trailing whitespace | Call .rstrip() before saving |

## Success Criteria

All must be ✓ before production:

- [ ] All topics scraped successfully
- [ ] All parts extracted (verify multi-part topics)
- [ ] All 4 sections present for each part
- [ ] No author attributions
- [ ] Proper dandas (॥)
- [ ] Single newlines only
- [ ] No trailing whitespace
- [ ] All automated checks pass
- [ ] Manual verification completed
- [ ] Website displays correctly

---

**When all items checked, data is ready for production! 🎉**
