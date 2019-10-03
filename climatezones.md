---
layout: base
permalink: /climatezones/
---
{% capture download_str %}
<b>Region Definitions:</b> <a href="{{ 'assets/climate_zones/Region_NUM.shp' | relative_url }}">ESRI Shapefile</a> \| <a href="{{ 'assets/climate_zones/Region_NUM.geojson' | relative_url }}">GeoJSON</a> \| <a href="{{ 'assets/climate_zones/Region_NUM.kml' | relative_url }}">KML</a>
{% endcapture %}

# Climate Zones

Nine climate zones have been identified with the objective of sub-dividing the US climate into regions experiencing similar weather and climate regimes and thus similar forecasting challenges and levels of variability and uncertainty.

The interactive map below shows the climate zones and is followed by a description of each zone. A <a href="{{ 'assets/climate_zones/SFA_Climate_Zones.kmz' | relative_url }}">KMZ file</a> of the regions is available. The final [section](#Development-of-the-climate-zones) describes how the climate zones were developed.

{% include climate_zones.html %}

1. [Pacific Coastline and Maritime Pacific Northwest](#region1)
2. [Interior Pacific Northwest and Northern US Rockies](#region2)
3. [Desert Southwest and Southern US Rockies](#region3)
4. [Rocky Mountain Lee](#region4)
5. [Northeastern Plains, Great Lakes and Ohio Valley](#region5)
6. [Southeastern Plains States, Mississippi Valley and Southern Interior](#region6)
7. [Mid-Atlantic and New England](#region7)
8. [Florida and the Gulf Coast](#region8)
9. [US Tropical Island Territories](#region9)

## Region 1: Pacific Coastline and Maritime Pacific Northwest {#region1}
{: .anchor}

This is the region of the western USA that is heavily influenced by the eastern Pacific.  In the winter, frequent mid-latitude storms impact this region.  In the summer, the cold sea-surface has a dramatic impact on the climate wherever the path of cool dense air is not blocked by topography.  The cool, high humidity air creates a shallow stable layer that is typically either foggy throughout or capped by a stratus deck.  The associated clouds are quite dynamic in nature, forming and burning off according to local pressure gradients, solar insolation and larger scale weather impacts.

{{ download_str | replace: "NUM", "1" }}

## Region 2: Interior Pacific Northwest and Northern US Rockies {#region2}
{: .anchor}

While the Coastal Range of Oregon and Olympic Mountains of Washington reduce the marine influence in western Oregon and Western Washington, the Cascade mountains almost block the marine air, with only limited amounts flowing through low-lying conduits like the Columbia Gorge.  Thus, regions east of the Cascade crest have a dry continental climate: hot and dry in the summertime, and cool/cold and relatively dry in the winter.  A one size fits all categorization of this region should be caveated by saying that the topography of the many mountain ranges within it mean there are many regional and local circulations that can influence surface irradiance, but overall, this is a low-humidity, dry climate with lots of sunshine.

{{ download_str | replace: "NUM", "2" }}

## Region 3: Desert Southwest and Southern US Rockies {#region3}
{: .anchor}

The California Coastal Range mountains block much of the marine influence into the California Central Valley, and the Sierra Nevada range effectively blocks all marine influence its east.  Climate region 3 encapsulates all the arid region in the sub-tropical region outside of the strong marine influence along the immediate California coastline.  The region extents east to the Rocky Mountain crest.  Beyond the crest, the influence from moist Gulf of Mexico air and cold Canadian interior lead to a dramatic shift to a moister climate.  As for Region 2, the generalization of climate in this area needs to be caveated with caution that the complex topography does drive significant differences in climate in local areas, especially near mountain crests.

{{ download_str | replace: "NUM", "3" }}

## Region 4: Rocky Mountain Lee {#region4}
{: .anchor}

The Rocky Mountain Lee zone is the region extending eastwards for about 250 to 300 miles from the Rocky Mountain foothills where the terrain height descends (steeply at first, then gradually) from roughly 2400 m to 750 m.  The climate is defined by descending and drying air coming over the Rockies, and dry (and frigid in the winter) air coming south from interior Canada.  These air masses occassionally interact with moisture advected from the Gulf of Mexico.  This area is typically west of the [dry line](https://en.wikipedia.org/wiki/Dry_line) (i.e. on the dry side) where descending air tends to lead to many clear days.  In the winter months, the foothills act as a channel for frigid dry air to move southward. This is also a region where storms often begin to form or intensify before moving off into the plains.

{{ download_str | replace: "NUM", "4" }}

## Region 5: Northeastern Plains, Great Lakes and Ohio Valley {#region5}
{: .anchor}

The Northern Plains climate is defined by descending and drying air coming over the Rockies (particularly in the western portion of the zone), dry (and frigid in the winter) air coming south from interior Canada and humid air moving north from the Gulf of Mexico.  These influences make it one of the most interesting climate zones in the world with large extremes and sudden changes being common.  While the region has generally good solar resource, in spring, summer and to some extent autumn, this region is impacted by frequent convection, and the zone is on average east of the dry line.  Convection may be shallow, with only fair weather clouds forming, or may be deep with large supercell storms or long convective lines forming.  In both cases, accurate forecasting is challenging, and variability is high.  In the wintertime, the storm track will pass over this region bringing clouds, snow and ice, all of which are challenging to solar forecasting.

{{ download_str | replace: "NUM", "5" }}

## Region 6: Southeastern Plains States, Mississippi Valley and Southern Interior {#region6}
{: .anchor}

Region 6 is similar to Region 5 except that the Gulf influence dominates in all seasons.  Convection is much diminished in wintertime but is still possible.

{{ download_str | replace: "NUM", "6" }}

## Region 7: Mid-Atlantic and New England {#region7}
{: .anchor}

This region extends mostly from the Appalachian Mountains eastward.  In the summertime it is dominated by the influence of warm moist air sourced from the Gulf of Mexico and the warm waters of the Gulf Stream running up the Atlantic seaboard.  Thus the solar climatology is hazy with frequent fair weather and precipitating cumulo-form clouds.  In the winter the climate is more frequently dominated by continental air sourced from Canada and the upper mid-west with alternation between stormy and clear periods as mid-latitude storms pass.  Occasionally in the wintertime flow from the Gulf of Mexico or from the warmer Gulfstream waters will affect this region leading to strong storms due to the large temperature and humidity contrast between the maritime and continental air masses.  This regional also sees occasional hurricanes in late summer and autumn.

{{ download_str | replace: "NUM", "7" }}

## Region 8: Florida and the Gulf Coast {#region8}
{: .anchor}

This region is characterized by an almost permanently moist boundary layer due to its close proximity to the warm waters of the Gulf of Mexico.  It location mostly south of 30-degrees also means it sees strong insolation year round.  The combination of moisture, low stability due to insolation, and large land-ocean contrasts predominate the forecast challenge in this region.  Florida is further complicated by the fact that it is a flat peninsula that is narrow enough to see convergence of sea-breeze boundaries from both the east and west coasts.  Lastly, this region is an area that is often impacted by tropical storms and hurricanes.

{{ download_str | replace: "NUM", "8" }}

## Region 9: US Tropical Island Territories {#region9}
{: .anchor}

Despite their distance from one another, the Hawaiian archipelago in the Pacific and the US territories of Puerto Rico and the Virgin Islands in the Caribbean have very similar climate regimes.  As islands, they also exhibit similar grid challenges as well.  All of these islands sit in the easterly trade winds and are surrounded by relatively warm water, and most have significant topography.  The climate is warm and moist with frequent cumulus development that is moderated by diurnal circulations.

{{ download_str | replace: "NUM", "9" }}

## Development of the climate zones

The regions provided here are the result of a stakeholder vetting process. An initial draft was produced containing six regions that were identified by visually examining the NSRDB annual GHI estimates and considering the meteorology of the U.S. The initial draft was vetted during the June 2019 Solar Forecast 2 stakeholder meeting and subsequently updated. Other forecasting experts considered the proposed zones as basically how they would sub-divide the country, but the discussion revealed that Hawaii and the US territories in the Caribbean were not considered.  It was also thought that Florida should be its own climate region due to the complexities of the sea-breeze that develops almost daily along both the eastern and western coastlines, and often converges inland bring significant enhancement to cloud generating processes.  When examining this suggestion, it was decided to include the Gulf Coast in the Florida region, as strong land-sea temperature contrasts yield significant sea-breeze and land-breeze effects that make these areas unique in their forecast challenges.  The zones were again reviewed in the September 4, 2019 stakeholder webinar and another iteration was produced.  The next iteration was produced by overlaying the NSRDB annual PV potential estimates (fixed, latitude tilt) and topography using a GIS tool. This allowed us to tighten up the boundaries, especially where sharp transitions occur due to topography and proximity to oceans.  While doing this, it became apparent that the region in the immediate lee of the Rocky Mountains could be differentiated, and thus a ninth region was added, with area being taken from the northern and southern plains regions. Stakeholders were provided a opportunity to review these zones through September 30, 2019. The zones are now finalized, but we will issue minor revisions to correct any mistakes.

Finally, stakeholders have suggested creating a new set of zones based on statistical analyses of the reference dataset and/or satellite data. We think this would be a great stakeholder contribution to the project, but this is out of scope for the core project team.
