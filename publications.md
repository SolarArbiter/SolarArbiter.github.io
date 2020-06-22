---
layout: base
permalink: /publications/
title: Publications
---
# Publications

## Papers

{% for paper in site.data.papers %}
- _{{ paper.title }}_<br/>
  {{ paper.authors }}, {{ paper.publication}}, {{ paper.date }}. DOI: <a href="https://doi.org/{{ paper.DOI }}">{{ paper.DOI }}</a> <a href="{{ paper.link | relative_url }}">download</a>

{% endfor %}

## Presentations

{% for presentation in site.data.presentations %}
- _{{ presentation.title }}_<br/>
  {{ presentation.authors }}, {{ presentation.place}}. {{ presentation.date }}. <a href="{{ presentation.link | relative_url }}">download<span class="sr-only"> presentation {{ presentation.title }} by {{ presentation.authors}}</span></a>. {% if presentation.recording %}<a href="{{ presentation.recording | relative_url }}">recording<span class="sr-only"> presentation {{ presentation.title }} by {{ presentation.authors}}</span></a>. {% endif %}

{% endfor %}

## Posters

{% for poster in site.data.posters %}
- _{{ poster.title }}_<br/>
  {{ poster.authors }}, {{ poster.place }}. {{ poster.date }}. <a href="{{ poster.link | relative_url }}">download<span class="sr-only"> presentation {{ poster.title }} by {{ poster.authors}}</span></a>
{% endfor %}
