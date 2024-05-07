
# HTML Semantic Tags

![[semantic Tags.png|500]]

HTML5 introduced a range of semantic tags that provide meaning to the structure of web content. This blog will guide you through the importance and usage of these tags.

## What are Semantic Tags?
Semantic tags add meaning to your HTML. 
They tell both the browser and the developer what kind of content is being presented.

Here are some of the key semantic tags you must know about:
1. `<header>`: Used to represent the top section of a web page, often containing headings, logos, and navigation.
2. `<nav>`: Signifies a navigation menu on a web page.
3. `<article>`: Indicates a self-contained piece of content, such as a blog post or news article.
4. `<section>`: Represents a thematic grouping of content on a web page.
5. `<aside>`: Typically used for sidebars or content that is tangentially related to the main content.
6. `<footer>`: Represents the footer of a web page, usually containing copyright information and contact details.
7. `<figure>` and `<figcaption>`: Used for embedding images, diagrams, or charts, along with a caption.
8. `<main>`: Signifies the main content area of a web page.
9. `<time>`: Used to represent time-related information, like dates and times.

## Why Use Semantic Tags?
They enhance SEO, improve accessibility, and make your code easier to read and maintain.

## Commonly Used Semantic Tags
Here are some commonly used semantic tags in HTML:
- **header**: Contains introductory content.
- **footer**: Holds footer information.
- **article**: Encapsulates a self-contained composition.
- **section**: Represents a standalone section.
- **aside**: Contains content aside from the content it is placed in.
- **nav**: Holds navigation links.

## Examples

### Using the `<header>` tags and `<footer>` tags

```html
<header>
    <h1>My Website</h1>
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
</header>

<footer>
    <p>Copyright 2023</p>
</footer>

```

### Using the `<article>` and `<section>` tags:

```html
<article>
    <h2>Article Title</h2>
    <section>
      <p>Content here</p>
    </section>
</article>

```

### Using the `<aside>` and `<nav>` tags:

```html
<aside>
    <p>This is an aside content</p>
  </aside>
<nav>
    <ul>
      <li>Home</li>
      <li>About</li>
    </ul>
</nav>
```


### Using the `<figure>` and `<figcaption>` tags

```html
<figure>
    <img src="image.jpg" alt="An example image">
    <figcaption>This is an example image.</figcaption>
</figure>

```

