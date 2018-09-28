# Solar Forecast Arbiter Project site.
This site hosts static content for the Solar Forecast Arbiter project.

It's build using [Jekyll](https://jekyllrb.com/). 

### Architecture
Content is provided in html files at the root of the directory. The layout template to use is determined at the top of the file in the Front Matter (a yaml snippet preceded and followed by a line with three '-'s on it). 
Main navigation is defined in the `_data/navigation.yml` file.
```
---
layout: base
---
```
Directory structure:

  - `_layouts` Base templates that include organize content.
  - `_data` Variables for rendering in templates stored in yaml files.
  - `_includes` Reusable HTML elements.
	

