import pandas as pd
import json
import os

def clean_text(text):
    """Clean and properly escape text for JSON"""
    if pd.isna(text) or text is None:
        return ""

    # Convert to string
    text = str(text)

    # Remove leading/trailing whitespace
    text = text.strip()

    # Replace NaN string with empty
    if text.lower() == 'nan':
        return ""

    return text

def main():
    print("Reading Excel file...")

    # Read the "Vadavali Data" sheet
    df = pd.read_excel('grantha-details.xlsx', sheet_name='Vadavali Data')

    print(f"Found {len(df)} rows in Excel")

    # Filter out empty rows
    df = df[df['Topic ID'].notna()]

    print(f"Processing {len(df)} valid rows...")

    # Initialize the output structure
    grantha_data = {}

    # Commentary columns to process (including personal notes columns)
    commentary_columns = [
        'वादावली',
        'भावदीपा',
        'प्रकाशः',
        'विवर्णम्',
        'वैय्यक्तिकटिप्पणि',
        'वैय्यक्तिकटिप्पणि - सम्स्क्रुत​ (AI Powered)',
        'वैय्यक्तिकटिप्पणि - कन्नड (AI Powered)',
        'वैय्यक्तिकटिप्पणि - आग्ला​ (AI Powered)'
    ]

    # Process each row
    for idx, row in df.iterrows():
        topic_id = str(int(row['Topic ID']))
        part = row['Part']

        # Skip if Part is NaN
        if pd.isna(part):
            print(f"Skipping row {idx+1}: Topic {topic_id} has no Part specified")
            continue

        # Initialize topic if not exists
        if topic_id not in grantha_data:
            grantha_data[topic_id] = {}

        # Initialize part if not exists
        if part not in grantha_data[topic_id]:
            grantha_data[topic_id][part] = {}

        # Add commentary texts
        for col in commentary_columns:
            if col in row:
                text = clean_text(row[col])
                if text:  # Only add if not empty
                    grantha_data[topic_id][part][col] = text

    # Read existing grantha-details.json if it exists
    # Use parent directory path since script is in ImportFromXL folder
    json_path = '../Grantha/grantha-details.json'
    existing_data = {}

    if os.path.exists(json_path):
        print(f"\nReading existing {json_path}...")
        with open(json_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"Existing data has {len(existing_data)} topics")

    # Merge new data with existing data
    print("\nMerging data...")
    for topic_id, parts in grantha_data.items():
        if topic_id not in existing_data:
            existing_data[topic_id] = {}

        for part, commentaries in parts.items():
            if part not in existing_data[topic_id]:
                existing_data[topic_id][part] = {}

            # Update/add commentaries
            existing_data[topic_id][part].update(commentaries)

    # Save to grantha-details.json with proper formatting
    print(f"\nSaving to {json_path}...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)

    print("\n[SUCCESS] Data imported to grantha-details.json")

    # Print summary
    print("\nSummary:")
    print(f"  Total topics: {len(existing_data)}")
    for topic_id in sorted(existing_data.keys(), key=lambda x: int(x)):
        parts = existing_data[topic_id]
        print(f"  Topic {topic_id}: {len(parts)} parts")

if __name__ == "__main__":
    main()
