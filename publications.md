---
layout: base
permalink: /publications/
title: Publications
---
# Publications

## Presentations
{% for presentation in site.data.presentations %}
- _{{ presentation.title }}_<br/>
  {{ presentation.authors }}, {{ presentation.place}}. {{ presentation.date }}. <a href="{{ presentation.link | relative_url }}">download<span class="sr-only"> presentation {{ presentation.title }} by {{ presentation.authors}}</span></a>

{% endfor %}

## Posters
{% for poster in site.data.posters %}
- _{{ poster.title }}_<br/>
  {{ poster.authors }}, {{ poster.place }}. {{ poster.date }}. <a href="{{ poster.link | relative_url }}">download<span class="sr-only"> presentation {{ poster.title }} by {{ poster.authors}}</span></a>
{% endfor %}
