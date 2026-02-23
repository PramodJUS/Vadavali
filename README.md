# 🕉️ Vadavali - वादावली

A web application for studying **Vadavali** by Sri Jayatirtha with multiple Sanskrit commentaries, featuring transliteration to 8+ Indian scripts.

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://your-demo-url-here)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

Vadavali (वादावली) is a seminal philosophical text in Dvaita Vedanta by **Sri Jayatirtha** (Teeka Acharya). This application presents the text along with classical Sanskrit commentaries:

- **वादावली** - Source text by Sri Jayatirtha
- **भावदीपा** - Commentary by Raghavendra Tirtha
- **प्रकाशः** - Commentary by Srinivasa Tirtha
- **विवर्णम्** - Commentary by Umarji Krishna

## ✨ Features

### Core Features
- 📖 **Multiple Commentaries** - View all commentaries side-by-side with pagination
- 🌐 **8 Language Scripts** - Transliterate to Kannada, Telugu, Tamil, Malayalam, Gujarati, Odia, Bengali, IAST
- 🔍 **Sanskrit Search** - Smart search with sandhi rules and pratika (quotation) highlighting
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 💾 **State Preservation** - Remembers your position, expanded commentaries, and preferences

### User Interface
- Collapsible left info panel with philosophy principles
- Topic navigation with adhyaya and pada selectors
- Expand/collapse individual commentaries
- Auto-hide headers for focused reading
- Commentary-specific font size controls
- Pratika grahana (quotations ending in इति) highlighted in bold

### Technical Features
- **No backend required** - Pure client-side application
- **Local libraries** - All transliteration and search libraries included
- **Performance optimized** - Virtual scrolling for long lists
- **Cache-friendly** - Version-based cache busting

## 🚀 Quick Start

### View the Application

Simply open `index.html` in a web browser. No build process or server required!

```bash
# Clone the repository
git clone https://github.com/yourusername/vadavali.git
cd vadavali

# Open in browser
open index.html  # Mac
start index.html # Windows
xdg-open index.html # Linux
```

### Admin Panel

For content management, open `admin.html` (requires password authentication).

## 📝 Data Entry for Non-Technical Users

We provide Excel-based workflow for easy data entry:

### For Data Entry Teams

1. **Get the Excel file** from project maintainer
2. **Read** `DATA_ENTRY_GUIDE.md` for instructions
3. **Fill** Sanskrit commentary text in Excel
4. **Send back** the completed file

### For Project Maintainers

```bash
# Export current data to Excel
python json_to_excel.py
# OR double-click: export-to-excel.bat (Windows)

# Share grantha-details.xlsx with data entry team

# After receiving filled Excel file
python excel_to_json.py
# OR double-click: import-from-excel.bat (Windows)
```

See **[OUTSOURCING_INSTRUCTIONS.txt](OUTSOURCING_INSTRUCTIONS.txt)** for complete workflow.

## 📁 Project Structure

```
vadavali/
├── index.html              # Main application
├── admin.html              # Content management panel
├── config.js               # Configuration settings
│
├── Grantha/                # Data files
│   ├── grantha-details.json    # Main content (commentaries)
│   ├── mainpage.csv            # Topic list
│   ├── Author.csv              # Commentary metadata
│   └── vishaya-details.json    # Topic details
│
├── js/
│   └── bs.js               # Main application JavaScript
│
├── css/
│   └── bs.css              # Styles
│
├── transliterate-library/  # Local transliteration engine
├── sanskrit-search-library/# Sanskrit search with sandhi rules
│
├── images/                 # Author images and icons
│
└── Data Entry Tools/
    ├── json_to_excel.py        # Export to Excel
    ├── excel_to_json.py        # Import from Excel
    ├── export-to-excel.bat     # Windows export script
    ├── import-from-excel.bat   # Windows import script
    ├── DATA_ENTRY_GUIDE.md     # Instructions for data entry
    └── OUTSOURCING_INSTRUCTIONS.txt
```

## 🛠️ For Developers

### Prerequisites

- Python 3.7+ (only for data conversion tools)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Setup Data Conversion Tools

```bash
pip install -r requirements.txt
```

### Adding New Commentary

1. **Add author info** to `Grantha/Author.csv`:
   ```csv
   Vadavali,"नया-कोमेंटरी","Author Name",author-image.jpg
   ```

2. **Add commentary text** to `Grantha/grantha-details.json`:
   ```json
   "topicId": {
     "Part#1": {
       "वादावली": "...",
       "नया-कोमेंटरी": "new commentary text..."
     }
   }
   ```

3. Commentary will be automatically detected and displayed!

### Cache Busting

When modifying `js/bs.js` or `css/bs.css`, update version in `index.html`:

```html
<script src="js/bs.js?v=YYYYMMDD-description"></script>
```

## 📚 Documentation

- **[CLAUDE.md](CLAUDE.md)** - Architecture and development guide
- **[DATA_ENTRY_GUIDE.md](DATA_ENTRY_GUIDE.md)** - For data entry teams
- **[OUTSOURCING_INSTRUCTIONS.txt](OUTSOURCING_INSTRUCTIONS.txt)** - Complete outsourcing workflow

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Data Contributions

Have Sanskrit commentary to add? See [DATA_ENTRY_GUIDE.md](DATA_ENTRY_GUIDE.md) for the easy Excel-based workflow.

## 📖 Philosophy Background

### Dvaita Vedanta (द्वैत वेदान्त)

The philosophy presented in Vadavali:

- **पञ्चभेद** (Panchabheda) - Five-fold eternal differences
- **स्वतन्त्र-परतन्त्र** - God as independent, souls as dependent
- **विष्णु-सर्वोत्तमता** - Supremacy of Vishnu
- **तत्त्ववाद** - Realism (differences are real)

### Key Figures

- **Sri Madhvacharya** (1238-1317) - Founder of Dvaita Vedanta
- **Sri Jayatirtha** (1365-1388) - Author of Vadavali, "Teeka Acharya"
- **Sri Raghavendra Tirtha** (1595-1671) - Author of Bhavadipa commentary
- **Sri Srinivasa Tirtha** - Author of Prakasha commentary

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Sanskrit texts from traditional sources
- Transliteration library based on IAST standards
- Sanskrit search algorithms incorporating classical sandhi rules
- Community contributors for data entry and corrections

## 📞 Contact

For questions, suggestions, or collaboration:
- Open an issue on GitHub
- Email: your-email@example.com

---

<div align="center">

**॥ श्री कृष्णार्पणमस्तु ॥**

*For educational and spiritual study purposes*

</div>
