# 📝 Data Entry Guide for Vadavali

## For Non-Technical Users

This guide explains how to add Sanskrit commentary data to Vadavali using Excel/Google Sheets.

---

## 🚀 Quick Start

### Step 1: Export to Excel

**Windows:**
1. Double-click `export-to-excel.bat`
2. Wait for "Successfully created grantha-details.xlsx"
3. Open `grantha-details.xlsx`

**Manual method:**
```bash
python json_to_excel.py
```

---

### Step 2: Edit Data in Excel

Open `grantha-details.xlsx` - you'll see:

| Topic ID | Topic Title (Reference) | Part | वादावली | भावदीपा | प्रकाशः | विवर्णम् |
|----------|------------------------|------|----------|----------|---------|----------|
| 1 | मङ्गलश्लोक: | Part#1 | text... | text... | text... | text... |

**How to edit:**
- ✅ **Topic Title column is REFERENCE ONLY** (grayed out) - shows what you're working on
- ✅ Add/edit Sanskrit text in commentary columns (columns 4-7)
- ✅ Use **Alt+Enter** (Windows) or **Option+Enter** (Mac) for line breaks
- ✅ Copy-paste from Word/PDF works fine
- ❌ Don't change Topic ID, Topic Title, or Part columns
- ❌ Don't modify header row

**Tips:**
- Work on one topic at a time
- Save frequently (Ctrl+S)
- Use Google Sheets if multiple people are editing

---

### Step 3: Convert Back to JSON

**Windows:**
1. Save and close Excel
2. Double-click `import-from-excel.bat`
3. Check for errors
4. Review `grantha-details-new.json`

**Manual method:**
```bash
python excel_to_json.py
```

---

### Step 4: Replace Original File

If everything looks good:
1. Delete old `Grantha/grantha-details.json`
2. Rename `Grantha/grantha-details-new.json` to `grantha-details.json`
3. Refresh website to see changes

**Backups are created automatically** in `Grantha/` folder with timestamp.

---

## 📋 Column Guide

| Column | Description | Example | Editable? |
|--------|-------------|---------|-----------|
| **Topic ID** | Topic number | 1, 2, 3... | ❌ No |
| **Topic Title** | Sanskrit title (REFERENCE) | मङ्गलश्लोक: | ❌ No (Read Only) |
| **Part** | Part number | Part#1, Part#2 | ❌ No |
| **वादावली** | Source text by Jayatirtha | Sanskrit verses | ✅ Yes |
| **भावदीपा** | Commentary by Raghavendra Tirtha | Sanskrit commentary | ✅ Yes |
| **प्रकाशः** | Commentary by Srinivasa Tirtha | Sanskrit commentary | ✅ Yes |
| **विवर्णम्** | Commentary by Umarji Krishna | Sanskrit commentary | ✅ Yes |

---

## ❓ Common Questions

### Q: How do I add line breaks?
**A:** Press **Alt+Enter** (Windows) or **Option+Enter** (Mac) inside the cell.

### Q: Can multiple people edit at once?
**A:** Yes! Upload to Google Sheets and share with "Can edit" permission.

### Q: What if I make a mistake?
**A:** Backups are automatic. Check `Grantha/` folder for backup files.

### Q: How do I add a new topic?
**A:** Add a new row with the next Topic ID and Part#1.

### Q: Can I add more parts?
**A:** Yes! Use Part#1, Part#2, Part#3, etc. for the same topic.

### Q: Excel shows '#####' in cells?
**A:** The column is too narrow. Double-click the column border to auto-fit.

---

## 🔧 Setup (One-Time)

Install Python if not already installed:
1. Download from python.org
2. Install with "Add to PATH" checked
3. Run: `pip install openpyxl`

---

## 📞 Support

If you encounter errors:
1. Check the error message
2. Make sure Excel file is closed before converting
3. Verify Topic ID and Part format
4. Contact developer with screenshot

---

## ✨ Pro Tips

1. **Use Google Sheets** - Easier for team collaboration
2. **Keep backups** - Before big changes, copy the Excel file
3. **Work in batches** - Complete 5-10 topics, then convert and test
4. **Preview often** - Convert and check website frequently
5. **Track progress** - Add a "Status" column in Excel (not converted to JSON)
