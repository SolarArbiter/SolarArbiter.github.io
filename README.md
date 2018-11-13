# Solar Forecast Arbiter Project site.
This site hosts static content for the Solar Forecast Arbiter project.

It's built using [Jekyll](https://jekyllrb.com/). 

### Architecture
Directory structure:

  - `_layouts` Base templates that include organize content.
  - `_data` Variables for rendering in templates stored in yaml files.
     Data entered here is accessible via the `site.data` variable in templates.
  - `_includes` Reusable HTML elements.
	
Content is provided in html files at the root of the directory. The layout to use for a given page is declared at the top of the file in the `Front Matter` (a yaml snippet preceded and followed by a line with three '-'s on it). 
```
---
layout: base
permalink: /<path/
---
```
Note: Declaring a permalink provides a way for jekyll to link to pages regardless of where they reside in the directory structure or filename. 


### Navigation
Main navigation is defined in the `_data/navigation.yml` file. New menu items can be added by creating a yaml object with `name` and `link` attributes where name is the link text to display and link is the permalink, path or url to the target. Dropdown sub-navigation can be defined by creating a top level object with a `name` and `links` attribute, where the links attribute is a list of objects with `name` and `link` attributes. 

```
Example: Top level menu item

- name: Team
  link: /team/

Example: Subnav Dropdown

- name: Key Topics
  links:
  - name: Use Cases
    link: /usecases/
```


### Adding Content

Pages can be added by creating a new html or markdown file in the root directory of this repo. 

If you wish to use a mixture of markdown and html, you may do so with a .md file.

#### Blog Posts

Blog posts can be added in the `_posts` directory, with the format `<year>-<month>-<day>-<dash-separated-title>` in `.md` or `.html`. You should set the `author` field in the front-matter as well as setting the layout to `blog`, these values will be rendered in the blog post listing and the blog post page.
