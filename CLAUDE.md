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

Commentaries are **dynamically detected** from the JSON keys in `grantha-details.json`. The order is defined in `js/bs.js` line ~2827:
```javascript
const commentaryOrder = ['वादावली', 'भावदीपा', 'प्रकाशः', 'विवर्णम्'];
```

Author mappings from `Author.csv` provide:
- Commentary display name
- Author name for attribution
- Optional author image (in `images/` folder)

### Transliteration System

The app uses a **local transliteration library** (`transliterate-library/`) that converts Devanagari Sanskrit to multiple scripts:
- English (IAST romanization)
- Kannada, Telugu, Tamil, Malayalam
- Gujarati, Odia, Bengali

**Both content AND commentary titles are transliterated** when language changes.

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

3. Optionally update `commentaryOrder` in `js/bs.js` line ~2827 to control display order

The commentary will be automatically detected and displayed.

### Null Checks for Removed Elements

When removing UI elements (like adhikarana selector), add null checks to prevent errors:
```javascript
if (!adhikaranaSelect) return;  // Element was removed from UI
```

## Development Notes

### No Build System
This is a **pure client-side application** - no build, compile, or bundling required. Just open `index.html` in a browser.

### Libraries Are Local
Both `transliterate-library/` and `sanskrit-search-library/` are included locally, not via CDN.

### Admin Features
The admin panel (`admin.html`) requires password authentication. Default password hash is in `config.js`.

### Performance
- Virtual scrolling for long topic lists
- Debounced search (300ms delay)
- Lazy loading of author images

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
