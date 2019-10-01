---
layout: blog
author: Will Holmgren
---

Several stakeholders have expressed interest in publicly sharing
anonymous power plant data in the Solar Forecast Arbiter. While the Arbiter does not
explicitly support anonymous data exchange, we can provide some
recommendations for how to use the Arbiter's features to accomplish this
goal. Please keep in mind that these are only recommendations for how to
conceal plant identity -- they do **not** guarantee anonymity! It is
solely the user's responsibility to provide enough information about the
plant to be useful, but not so much as to reveal its identity.

## Location

The first challenge for making a plant anonymous is determining how to
specify its location. Forecast techniques that rely on numerical weather
models or satellite data need to know plant location with a reasonable
degree of accuracy. On the other hand, the plant location must be
sufficently vague so as to make it impossible to determine which of many
plants it may be within a region. Regions with only a few plants
therefore require specification of less precise coordinates than regions
with many plants. Clicking around Google Maps or Google Earth are easy
ways to find suitable coordinates. We also recommend that users make a
note in the *extra parameters* metadata field to indicate that the
metadata describes an anonymous plant in the region.

The xkcd comic below provides some practical guidance on what the digits
of latitude and longitude coordinates specify:

![https://xkcd.com/2170/](https://imgs.xkcd.com/comics/coordinate_precision.png)

For day ahead forecasts in most locations, one degree is likely too
coarse, but a tenth of a degree may be precise enough. Additional care
must be taken in areas of varying topography. For example, avoid
specifying plant locations that are at higher or lower elevations than
the true location. Also, avoid specifying locations on lakes or oceans.
Don't specify a location that already has another solar plant on it --
that's unnecessarily confusing and could lead to issues with the other
plant owners/operators.

For intraday forecasts, a tenth of a degree may not be precise enough.
Carefully consider the compromises when pursuing intraday forecasts for
anonymous plants.

Forecast techniques that only use plant data (e.g. persistence) do not
need location data unless they include corrections based on solar
position (e.g. persistence of clear sky index). For this reason, we
still recommend specifying coordinates to about a tenth of a degree.

## Data normalization

Anonymous plant data should be normalized so that the AC power output
cannot be determined and cross-referenced with publicly available power
plant data (e.g. from [eia.gov](https://www.eia.gov/maps/)). We
recommend normalizing data to the AC capacity of the plant. In this
case, the uploaded generation data would all fall between 0 (no
generation) and 1 (generation = AC capacity). Specify the plant metadata
with an AC capacity of 1. Take some care in specifying the corresponding
DC capacity because an exact DC:AC ratio could allow someone to identify
the plant. There's no point in trying to hide the tracker vs. fixed tilt
selection -- it will be obvious in the data. However, it's prudent to
round the axis tilt and azimuth of a fixed tilt system to 5 degrees or
so (e.g. if the true tilt/azimuth are 26/179 degrees, round them to
25/180 degrees).

## Aggregation

Another method to conceal plant generation is to only include its
generation data as part of an aggregate of many plants. This strategy
may be used to represent generation from a fleet of PV plants or a
neighborhood of rooftop PV installations. Depending on the use case, it
may still be desirable to provide exact metadata for the constituent
plants. In either case, a new Site is created that represents the
aggregate of all of the plants (exact metadata is irrelevant), an AC
power Observation is attached to the Site, and user-aggregated
generation data is uploaded. More information on the Arbiter's built-in
aggregation capabilities will be provided soon.
