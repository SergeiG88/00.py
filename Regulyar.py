import re

def extract_image_links(html_text):
    image_links = re.findall(r'(https?://\S+\.(?:jpg|jpeg|png|gif))', html_text)
    return image_links


html_text = """
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <img src="https://example.com/image1.jpg">
    <img src="https://example.com/image2.jpeg">
    <img src="https://example.com/image3.png">
    <img src="https://example.com/image4.gif">
    
</body>
</html>
"""

image_links = extract_image_links(html_text)
print(image_links)

