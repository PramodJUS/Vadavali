import json

# Read the JSON file
with open('Grantha/grantha-details.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Image HTML to add at the beginning (using CSS class)
image_html = '<img src="images/jayateertha.jpg" class="commentary-image">\n\n'

# Add image to Topic 1, Part#1, वैय्यक्तिकटिप्पणि
if '1' in data and 'Part#1' in data['1'] and 'वैय्यक्तिकटिप्पणि' in data['1']['Part#1']:
    current_text = data['1']['Part#1']['वैय्यक्तिकटिप्पणि']

    # Only add if image isn't already there
    if 'jayateertha.jpg' not in current_text:
        data['1']['Part#1']['वैय्यक्तिकटिप्पणि'] = image_html + current_text
        print("[SUCCESS] Added Jayatirtha image to Personal Notes")
    else:
        print("Image already exists in Personal Notes")
else:
    print("ERROR: Could not find the commentary to update")

# Save back to JSON
with open('Grantha/grantha-details.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
