import json

# Read the JSON file
with open('Grantha/grantha-details.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Replace the old long image tag with the simple one
if '1' in data and 'Part#1' in data['1'] and 'वैय्यक्तिकटिप्पणि' in data['1']['Part#1']:
    current_text = data['1']['Part#1']['वैय्यक्तिकटिप्पणि']

    # Replace the old long style attribute with class
    old_tag = '<img src="images/jayateertha.jpg" alt="Jayatirtha" style="max-width:200px; height:auto; border-radius:8px; margin:10px 0; display:block;">'
    new_tag = '<img src="images/jayateertha.jpg" class="commentary-image">'

    if old_tag in current_text:
        data['1']['Part#1']['वैय्यक्तिकटिप्पणि'] = current_text.replace(old_tag, new_tag)
        print("[SUCCESS] Updated image tag to use CSS class")
    else:
        print("Old tag not found (might already be updated)")

# Save back to JSON
with open('Grantha/grantha-details.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done!")
