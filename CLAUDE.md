# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Vadavali is a web application for displaying Sanskrit philosophical texts with multiple commentaries. The app presents **वादावली** (Vadavali) by Sri Jayatirtha, a seminal text in Dvaita Vedanta philosophy, along with multiple Sanskrit commentaries (vyakhyanas).

## Architecture

### Data Layer

The application uses a **simple JSON structure** for storing commentary text:

```json
{
  "topicId": {
    "Part#1": {
      "वादावली": "source text...",
      "भावदीपा": "commentary text...",
      "प्रकाशः": "commentary text...",
      "विवर्णम्": "commentary text..."
    },
    "Part#2": { ... }
  }
}
```

**Key data files:**
- `Grantha/grantha-details.json` - Main content with all commentaries
- `Grantha/mainpage.csv` - Topic list (id, sutra_text)
- `Grantha/Author.csv` - Commentary metadata (Commentry_Name, Author_Name, Image_Name)
- `Grantha/vishaya-details.json` - Topic details and adhikaranas

### Commentary System

The application now includes **8 commentaries total**:
- 4 traditional commentaries
- 4 AI-powered personal notes (in Sanskrit, Kannada, and English)

Commentaries are **dynamically detected** from the JSON keys in `grantha-details.json`. The order is defined in `js/bs.js` line ~2787-2797:
```javascript
const commentaryOrder = [
    'वादावली',
    'भावदीपा',
    'प्रकाशः',
    'विवर्णम्',
    'वैय्यक्तिकटिप्पणि',
    'वैय्यक्तिकटिप्पणि - सम्स्क्रुत​ (AI Powered)',
    'वैय्यक्तिकटिप्पणi - कन्नड (AI Powered)',
    'वैय्यक्तिकटिप्पणi - आग्ला​ (AI Powered)'
];
```

**Note:** Some commentary keys contain Unicode zero-width characters (like \u200b) to maintain compatibility with existing data. These are handled transparently by the system.

Author mappings from `Author.csv` provide:
- Commentary display name
- Author name for attribution
- Optional author image (in `images/` folder)

### Image Support in Commentaries

Commentaries can include images using simple HTML `<img>` tags with the `.commentary-image` CSS class for consistent styling:

```html
<img src="images/jayateertha.jpg" class="commentary-image">
```

The CSS class (defined in `css/bs.css` lines 1380-1387) provides:
- Max width: 200px
- Automatic height scaling
- Rounded corners (8px border-radius)
- Drop shadow
- Block display with 10px vertical margin

Images should be placed in the `images/` folder and referenced with relative paths.

### Transliteration System

The app uses a **local transliteration library** (`transliterate-library/`) that converts Devanagari Sanskrit to multiple scripts:
- English (IAST romanization)
- Kannada, Telugu, Tamil, Malayalam
- Gujarati, Odia, Bengali

**All 8 languages are fully supported** with corrected translations. Both content AND commentary titles are transliterated when language changes.

### Sanskrit Search

A specialized **Sanskrit search library** (`sanskrit-search-library/`) handles:
- Sandhi splitting and joining
- Pratika (quotation) identification - text ending in `इति` is bolded
- Smart search with synonym matching

## Key Files

### Main Application
- `index.html` - Entry point with navigation controls
- `js/bs.js` - Core application (~4500 lines)
  - Topic rendering and navigation
  - Commentary pagination (splits long text into pages)
  - State management (expand/collapse, selected vyakhyanas)
  - Transliteration integration
- `css/bs.css` - All styling

### Admin Panel
- `admin.html` - Content management interface
- `config.js` - Admin configuration (editor colors, features, data paths)

### Configuration
- `config.js` - Global settings exported to `window.*`
  - `DATA_CONFIG.dataPath` - path to grantha-details.json
  - `DATA_CONFIG.authorCsvPath` - path to Author.csv

## Important Conventions

### Cache-Busting
When modifying `js/bs.js` or `css/bs.css`, **always update** the version query parameter in `index.html`:
```html
<script src="js/bs.js?v=YYYYMMDD-description"></script>
<link rel="stylesheet" href="css/bs.css?v=YYYYMMDD-description">
```

### Line Breaks in Commentary
Use `\n` in JSON data. The application converts to `<br>` tags:
```javascript
text.replace(/\n/g, '<br>')
```

### Pagination
Long commentaries are split into pages using `splitTextIntoPages()`. Pagination state is tracked per topic-commentary combination:
```javascript
const paginationKey = `${topicId}-${key}`;
vyakhyanaPagination[paginationKey] = currentPage;
```

### State Preservation

The app preserves UI state across navigation:
- `openVyakhyanas` (Set) - which commentaries are expanded
- `selectedVyakhyanaKeys` (Set) - which commentaries are visible (from dropdown)
- `vyakhyanaPagination` (Object) - current page for each commentary
- `lastViewedPages` (Object) - tracks last viewed page/part for each topic

#### Page Count Indicator

The info panel displays a page count indicator showing current page and total pages:
- **Format:** `Topic#X (Page#Y/Z)` or `A.B.C (Page#Y/Z)`
- **Location:** Info panel `.sutra-info-number` element (js/bs.js ~2331)
- **Calculation:** Counts `Part#N` keys in topic data, current from `currentPart` global
- **Updates:** Dynamically when navigating between parts

Example display:
- `Topic#1 (Page#1/1)` - Single page topic
- `Topic#2 (Page#2/3)` - Second page of three-page topic

#### Commentary Persistence Across Navigation

When navigating with `<<`, `<`, `>`, or `>>` buttons, the app automatically:

1. **Saves** which commentaries are currently open (by key name in `openVyakhyanas` Set)
2. **Navigates** to the new topic/part via `showTopicDetail()`
3. **Waits** 300ms for DOM to render
4. **Finds** each previously opened commentary by `data-key` attribute
5. **Opens** matching commentaries by reading `data-vyakhyana-num` and toggling display
6. **Scrolls** smoothly to first opened commentary using `requestAnimationFrame` + `scrollIntoView()`

**Implementation Details:**
- Uses DOM queries: `.commentary-item[data-key="${vyakhyanaKey}"]`
- Avoids calculating commentary numbers - reads from rendered DOM attributes
- Handles missing commentaries gracefully (e.g., भावदीपा in one topic but not another)
- Works across all navigation scenarios:
  - `<<` / `>>` - Previous/next topic
  - `<` / `>` - Previous/next part within topic
  - Edge cases: Jumping from last part to next topic's first part

**Scroll Behavior:**
```javascript
requestAnimationFrame(() => {
    firstOpenedVyakhyana.scrollIntoView({ behavior: 'smooth', block: 'start' });
});
```
Uses `requestAnimationFrame` to ensure DOM is painted before scrolling.

### Adding New Commentary

1. Add entry to `Grantha/Author.csv`:
   ```csv
   Vadavali,"कोमेन्तरी-नाम","Author Name",author-image.jpg
   ```

2. Add commentary key and text to `Grantha/grantha-details.json`:
   ```json
   "topicId": {
     "Part#1": {
       "वादावली": "...",
       "कोमेन्तरी-नाम": "new commentary text..."
     }
   }
   ```

3. Update `commentaryOrder` in `js/bs.js` line ~2787-2797 to control display order

4. **Optional**: Add images to commentary using:
   ```html
   <img src="images/author-name.jpg" class="commentary-image">
   ```

The commentary will be automatically detected and displayed.

### Translation System

All UI text is stored in `js/bs.js` in the `translations` object (lines ~280-450). Each language has:
- `title` - Page title
- `searchPlaceholder` - Search box text
- `infoText` - Information panel description
- `loading` - Loading message
- `noResults` - No results message
- `footer` - Footer text

**All 8 languages have been verified** to correctly reference "Vadavali by Jayatirtha" (not "Brahma Sutras by Madhvacharya").

### Info Panel Styling

The info panel displays topic information with specific font sizes:
- **`.sutra-info-number`** (css/bs.css ~728): `1.2rem` - Topic number and page indicator
- **`.sutra-info-text`** (css/bs.css ~777): `1.6rem` - Main sutra text (larger for readability)

This creates a visual hierarchy where the sutra text is prominent and metadata is compact.

### Null Checks for Removed Elements

When removing UI elements (like adhikarana selector), add null checks to prevent errors:
```javascript
if (!adhikaranaSelect) return;  // Element was removed from UI
```

## Development Notes

### No Build System
This is a **pure client-side application** - no build, compile, or bundling required. Just open `index.html` in a browser.

### Local Development Server
Use `start-server.bat` to run a local HTTP server on port 8080:
```bash
python -m http.server 8080
```
This avoids CORS issues when testing locally.

### Libraries Are Local
Both `transliterate-library/` and `sanskrit-search-library/` are included locally, not via CDN.

### Admin Features
The admin panel (`admin.html`) requires password authentication. Default password hash is in `config.js`.

### Performance
- Virtual scrolling for long topic lists
- Debounced search (300ms delay)
- Lazy loading of author images

## Excel Import/Export Tools

The `ImportFromXL/` folder contains Python scripts for data management:

### Import from Excel
```bash
cd ImportFromXL
python import_excel_to_json.py
```
Reads `grantha-details.xlsx` and imports all 8 commentary columns into `Grantha/grantha-details.json`. Automatically handles:
- JSON string escaping (newlines, tabs, special characters)
- Merging with existing data
- Preserving Unicode characters in commentary keys

**Commentary columns in Excel:**
1. वादावली
2. भावदीपा
3. प्रकाशः
4. विवर्णम्
5. वैय्यक्तिकटिप्पणि
6. वैय्यक्तिकटिप्पणि - सम्स्क्रुत​ (AI Powered)
7. वैय्यक्तिकटिप्पणi - कन्नड (AI Powered)
8. वैय्यक्तिकटिप्पणi - आग्ला​ (AI Powered)

### Export to Excel
```bash
cd ImportFromXL
python export_grantha_to_excel.py
```
Exports `Grantha/grantha-details.json` to Excel for easier editing.

### Batch Files
- `import-from-excel.bat` - Quick import
- `export-to-excel.bat` - Quick export

## Testing Folder

The `testing/` folder contains all test files and one-time scripts:
- `test.html` - Test HTML pages
- `debug.html` - Debug interface
- `*_check.txt` - Validation outputs
- `*.py` - One-time migration scripts

**Keep production code clean**: All test and temporary files go in `testing/`

## Build Timestamp

The `build-timestamp.txt` file in the root directory provides the "Updated on" date in the footer. Format:
```
February 25, 2026
```

**Important**: This file must be tracked in git (not in `.gitignore`) so it appears on GitHub Pages. The JavaScript in `js/bs.js` (lines 4089-4103) fetches this file and displays it in the footer.

**Error Handling**: The code checks `response.ok` before reading the text to prevent 404 HTML from being displayed:
```javascript
const response = await fetch('build-timestamp.txt');
if (!response.ok) {
    throw new Error('File not found');
}
```

## Data Format Details

### mainpage.csv Format
```csv
id,sutra_text
1,मङ्गलश्लोक:
2,मिथ्यात्वसाधकानुमानभङ्गः
```
Simple two-column CSV: topic ID and Sanskrit title.

### Author.csv Format
```csv
Grantha,Commentry_Name,Author_Name,Image_Name
Vadavali,"वादावली","jayateertha",jayateertha.jpg
```
Links commentary names to authors and images.

### vishaya-details.json Structure
Contains adhikarana (topic) metadata and detailed descriptions.

## Common Issues and Solutions

### GitHub Pages Showing 404 HTML in Footer
**Problem**: The footer "Updated on" field displays GitHub's 404 page HTML as text.

**Cause**: The `build-timestamp.txt` file is missing or in `.gitignore`, causing fetch to return 404 HTML.

**Solution**:
1. Ensure `build-timestamp.txt` exists in root directory
2. Remove from `.gitignore` if present
3. Add proper error handling in JavaScript (check `response.ok` before reading)
4. Commit and push the file to GitHub

### Commentary Not Appearing Despite Being in JSON
**Problem**: Commentary is in `grantha-details.json` but doesn't show in UI.

**Possible causes**:
1. **Missing from Author.csv** - Add entry with exact matching key
2. **Unicode characters in key** - Some keys contain invisible Unicode characters (e.g., \u200b). Copy the exact key from working data.
3. **Not in commentaryOrder array** - Add to `commentaryOrder` in `js/bs.js`
4. **HTML content breaking rendering** - If commentary contains full HTML documents (<!DOCTYPE html>...), it will break rendering. Use plain text or simple HTML fragments only.

### Translation Showing Wrong Text
**Problem**: Language selector shows incorrect text (e.g., "Brahma Sutras" instead of "Vadavali").

**Solution**: Update the `translations` object in `js/bs.js` (lines ~280-450) for the affected language code (sa, kn, te, ta, ml, gu, or, bn, en).

### CORS Errors on Local Development
**Problem**: Opening `index.html` directly causes CORS errors.

**Solution**: Use `start-server.bat` to run local HTTP server on port 8080.

### Cache Not Clearing After Updates
**Problem**: Changes to `js/bs.js` or `css/bs.css` not visible after deployment.

**Solution**:
1. Update cache-busting version in `index.html`:
   ```html
   <script src="js/bs.js?v=YYYYMMDD-description"></script>
   ```
2. Wait 1-2 minutes for GitHub Pages to rebuild
3. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
