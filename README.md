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

Main navigation is defined in the `_data/navigation.yml` file. New menu items can be added by creating a yaml object with name and link attributes where name is the link text to display and link is the permalink, path or url to the target.  



### Adding Content

Pages can be added by creating a new html or markdown file in the root directory of this repo. 

If you wish to use a mixture of markdown and html, you may do so with a .md file.
