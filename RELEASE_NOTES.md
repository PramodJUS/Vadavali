# Release Notes - Vadavali

## Version 1.0.2 - March 9, 2026

### Data Completeness
- **100% Complete Content**: All 47 topics now have complete data with no missing articles.
- **Fixed Missing Articles**: Captured previously missing articles (9065, 9076, 9080) that were loading via JavaScript.
- **New Scraping Strategy**: Implemented click-and-wait strategy for JavaScript-loaded content with 100% success rate.

### Data Quality Improvements
- **Danda Normalization**: Normalized 7,818 occurrences of improper dandas (`।।` → `॥`).
- **Whitespace Cleanup**: Removed all double newlines and trailing spaces for consistent formatting.
- **File Size**: Increased from 2.6M to 3.8M (+46% more complete content).

### Documentation Updates
- **Updated scraping documentation** with proven working approach (click-and-wait strategy).
- **Added comprehensive comparison** of API vs Selenium scraping approaches.
- **Cleaned up repository**: Removed 62+ duplicate, test, and temporary files (~9M).

### Technical Details
- Topic 4: Now has 5 complete parts (was 4)
- Topic 6: Now has 9 complete parts (was 8)
- Topic 7: Now has 4 complete parts (was 3)
- All text properly formatted with single newlines and correct Unicode characters

---

## Version 1.0.1 - February 25, 2026

### Bug Fixes
- **Fixed footer 404 error**: The "Updated on" date was displaying GitHub's 404 page HTML. Now properly handles missing files with fallback date.
- **Fixed language translations**: All 8 languages (Sanskrit, English, Kannada, Telugu, Tamil, Malayalam, Gujarati, Odia, Bengali) now correctly reference "Vadavali by Jayatirtha" instead of incorrectly showing "Brahma Sutras by Madhvacharya".

### New Features
- **Added 4 new AI-powered commentaries**:
  - वैय्यक्तिकटिप्पणि (Personal Notes)
  - वैय्यक्तिकटिप्पणि - सम्स्क्रुत​ (AI Powered) - Sanskrit AI commentary
  - वैय्यक्तिकटिप्पणि - कन्नड (AI Powered) - Kannada AI commentary
  - वैय्यक्तिकटिप्पणि - आग्ला​ (AI Powered) - English AI commentary
- **Image support in commentaries**: Added CSS class `.commentary-image` for consistent image styling in commentary text. Use `<img src="images/filename.jpg" class="commentary-image">` to add images.
- **Excel import/export tools**: Created `ImportFromXL` folder with Python scripts to import/export commentary data between Excel and JSON.

### Enhancements
- **Build timestamp tracking**: Added `build-timestamp.txt` to show last update date in footer.
- **Cache-busting improvements**: Updated versioning system for better browser cache management.

### Developer Tools
- **Import from Excel**: Use `ImportFromXL/import-from-excel.bat` to import commentary data from `grantha-details.xlsx`.
- **Export to Excel**: Use `ImportFromXL/export-to-excel.bat` to export JSON data to Excel for editing.
- **Local development server**: Use `start-server.bat` to run local HTTP server on port 8080.

---

## Version 1.0.0 - February 21, 2026

### Initial Release
- **Vadavali text with 4 traditional commentaries**:
  - वादावली (Vadavali) - Original text by Sri Jayatirtha
  - भावदीपा (Bhava Deepa) - Commentary by Raghavendra Tirtha
  - प्रकाशः (Prakasha) - Commentary by Srinivasa Tirtha
  - विवर्णम् (Vivarnam) - Additional commentary
- **Multi-language support**: 8 Indian languages plus English with IAST transliteration.
- **Sanskrit search**: Advanced search with sandhi splitting and synonym matching.
- **Responsive design**: Works on desktop, tablet, and mobile devices.
- **Navigation features**:
  - Browse by Adhyaya (Chapter) and Pada (Section)
  - Search functionality with Sanskrit text support
  - Collapsible commentary sections
  - Commentary pagination for long texts
  - Cross-reference highlighting

---

## About Vadavali

**Vadavali** (वादावली) is a seminal philosophical text composed by **Sri Jayatirtha** (also known as Teeka Acharya), presenting the core principles of **Dvaita (Dualistic) Vedanta** philosophy.

### Key Features
- **Original Sanskrit text** with accurate Devanagari rendering
- **Multiple commentaries** from renowned scholars
- **Educational focus** for students of Vedanta philosophy
- **Scholarly tools** for research and study

### Credits
- **Text Source**: Traditional Vadavali manuscripts
- **Commentaries**: Raghavendra Tirtha, Srinivasa Tirtha
- **Development**: Created for educational and research purposes
- **Repository**: [github.com/PramodJUS/Vadavali](https://github.com/PramodJUS/Vadavali)

---

## Technical Notes

### File Structure
- `Grantha/grantha-details.json` - Main content with all commentaries
- `Grantha/mainpage.csv` - Topic list
- `Grantha/Author.csv` - Commentary metadata and author information
- `js/bs.js` - Main application logic
- `css/bs.css` - All styling
- `transliterate-library/` - Local transliteration engine
- `sanskrit-search-library/` - Sanskrit search functionality

### Browser Compatibility
- Chrome/Edge: Fully supported
- Firefox: Fully supported
- Safari: Fully supported
- Mobile browsers: Responsive design with touch support

### Known Issues
None at this time.

---

For questions, issues, or contributions, please visit the [GitHub repository](https://github.com/PramodJUS/Vadavali).
