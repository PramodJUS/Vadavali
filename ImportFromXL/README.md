# ImportFromXL

This folder contains scripts for importing and exporting commentary data between Excel and JSON formats.

## Files

### Scripts

1. **import_excel_to_json.py**
   - Imports commentary data from Excel to grantha-details.json
   - Supports all 8 columns:
     - वादावली, भावदीपा, प्रकाशः, विवर्णम्
     - वैय्यक्तिकटिप्पणि (Personal notes)
     - वैय्यक्तिकटिप्पणि - सम्स्क्रुत​ (AI Powered)
     - वैय्यक्तिकटिप्पणि - कन्नड (AI Powered)
     - वैय्यक्तिकटिप्पणि - आग्ला​ (AI Powered)
   - Properly escapes JSON strings (newlines, tabs, etc.)
   - Merges with existing data in grantha-details.json

2. **json_to_excel.py**
   - Exports grantha-details.json to Excel format
   - Useful for editing commentary data in Excel

3. **import-from-excel.bat**
   - Windows batch file for easy one-click import
   - Runs import_excel_to_json.py with user-friendly interface

4. **export-to-excel.bat**
   - Windows batch file for easy one-click export
   - Runs json_to_excel.py with user-friendly interface

### Data Files

5. **grantha-details.xlsx**
   - Excel workbook with commentary data
   - Has two sheets:
     - "📖 Instructions" - Usage instructions
     - "Vadavali Data" - Actual commentary data

## Usage

### To Import from Excel to JSON:

**Option 1: Using batch file (Windows - easiest)**
```
Double-click import-from-excel.bat
```

**Option 2: Using Python directly**
```bash
cd ImportFromXL
python import_excel_to_json.py
```

This will:
- Read data from `grantha-details.xlsx` (Vadavali Data sheet)
- Merge with existing `../Grantha/grantha-details.json`
- Save updated JSON file

### To Export from JSON to Excel:

**Option 1: Using batch file (Windows - easiest)**
```
Double-click export-to-excel.bat
```

**Option 2: Using Python directly**
```bash
cd ImportFromXL
python json_to_excel.py
```

This will create/update `grantha-details.xlsx` with current data from JSON.

## Notes

- Always backup `grantha-details.json` before running import
- Excel file structure must match the expected format
- All text is properly JSON-escaped automatically
- Empty cells in Excel are skipped during import
