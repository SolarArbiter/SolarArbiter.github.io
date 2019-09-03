"""
Simple script generate the static HTML for the Bokeh climate zone map
Requirements:
  - python >= 3.7
  - bokeh
  - ???
"""
import json
from pathlib import Path

from bokeh.embed import autoload_static
from bokeh.models import GeoJSONDataSource, WMTSTileSource
from bokeh.plotting import figure
from bokeh.resources import CDN

COLORS = [
    "#e41a1c",
    "#377eb8",
    "#4daf4a",
    "#984ea3",
    "#ff7f00",
    "#ffff33",
    "#f781bf",
    "#a65628",
]
FILL_ALPHA = 0.4


def main():
    tile_provider = WMTSTileSource(
        url=(
            "https://stamen-tiles.a.ssl.fastly.net/terrain"
            "/{Z}/{X}/{Y}.png"
        ),
        attribution=(
            'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
            'under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0'
            '</a>. Map data by <a href="http://openstreetmap.org">OpenStreetMap'
            '</a>, under <a href="https://creativecommons.org/licenses/by-sa/3.0">'
            "CC BY SA</a>"
        ),
    )
    fig = figure(
        x_axis_type="mercator",
        y_axis_type="mercator",
        title="Solar Forecast Arbiter Climate Zones",
        height=1241,
        width=1831,
        sizing_mode="scale_width",
        x_range=(-14549121.9, -6848522.3),
        y_range=(1705458.7, 6924707.2),
        tooltips=[("Region", "@region")],
        tools="pan,wheel_zoom,box_zoom,reset,hover,help",
    )
    fig.title.text_font_size = "24px"
    fig.add_tile(tile_provider)
    for i, area in enumerate(sorted(Path("./assets/climate_zones").glob("*.geojson"))):
        geodata = {
            "type": "FeatureCollection",
            "name": "climate_zones",
            "crs": {
                "type": "name",
                "properties": {"name": "urn:ogc:def:crs:EPSG::3857"},
            },
            "features": [],
        }
        region = area.name.split("_")[-1].split(".")[0]
        with open(area, "r") as f:
            gj = json.load(f)
        for feat in gj["features"]:
            feat["properties"]["region"] = region
            feat["properties"]["geojson"] = str(area)
            geodata["features"].append(feat)
        geo_source = GeoJSONDataSource(
            geojson=json.dumps(geodata), name=f"geo_source_{region}"
        )
        fig.patches(
            xs="xs",
            ys="ys",
            color=COLORS[i],
            legend=f"Region {region}",
            source=geo_source,
            fill_alpha=FILL_ALPHA,
        )
    fig.legend.click_policy = "hide"
    js_path = Path("assets/climate_zones/climate_zones.js")
    js, tag = autoload_static(fig, CDN, str(".." / js_path))
    with open(js_path, "w") as f:
        f.write(js)
    with open("_includes/climate_zones.html", "w") as f:
        f.write(tag)


if __name__ == "__main__":
    main()
