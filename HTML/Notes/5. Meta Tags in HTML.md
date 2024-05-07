```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!-- Character encoding -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Responsive design -->
    <meta http-equiv="X-UA-Compatible" content="ie=edge"> <!-- Internet Explorer compatibility -->
    <meta name="description" content="This is a description of the web page"> <!-- Description for search engines -->
    <meta name="keywords" content="HTML, CSS, JavaScript"> <!-- Keywords for search engines -->
    <meta name="author" content="Your Name"> <!-- Author name -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <title>Document</title>
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

# HTML Meta Tags

- The `<meta>` tags in HTML provide metadata about the HTML document. Metadata is information about webpage. 
- `<meta>` tags always go inside the document's `<head>` tag and are typically used to specify the character set, page description, keywords, author, and other metadata.
### Explanation of each meta tag:

1. **Character Encoding (`charset`)**: `<meta charset="UTF-8">` sets the character encoding for the webpage. UTF-8 is the most common and recommended.
2. **Viewport**: `<meta name="viewport" content="width=device-width, initial-scale=1.0">` sets the viewport to scale the page to the screen width, useful for responsive design.
3. **IE Compatibility**: `<meta http-equiv="X-UA-Compatible" content="ie=edge">` specifies that the page should be rendered using the latest rendering engine available on Internet Explorer.
4. **Description**: `<meta name="description" content="This is a description of the web page">` provides a brief description of the webpage, which search engines may use in search results.
5. **Keywords**: `<meta name="keywords" content="HTML, CSS, JavaScript">` specifies keywords for the webpage, which were historically used by search engines but are less relevant today.
6. **Author**: `<meta name="author" content="Your Name">` indicates the name of the author of the webpage.

# Favicon in Web page:

![[favicon.png]]

- A favicon is a small icon that appears next to your website's title in browser tabs. It helps in branding and easy identification among multiple tabs.
- To add a favicon:
	1. Create/Choose Favicon:
		Make a square image, usually 16x16 or 32x32 pixels, in `.ico` format. You can create a favicon from [this website](https://favicon.io/)
	2. Update HTML:
		Insert the following code in the `<head>` section of your `index.html` file: `<link rel="icon" href="favicon.ico" type="image/x-icon">`, favocon.ico being the path of the favicon file.

---
# [[|Next Chapter>>]]