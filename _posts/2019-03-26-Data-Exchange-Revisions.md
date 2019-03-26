---
layout: blog
author: Will Holmgren
---

Thanks to all of the stakeholders that provided feedback on the data exchange proposals. This blog post describes:

* [Revised missing, irregular, and regular data policies](#missing-irregular-and-regular-data)
* [New probabilistic forecast formats](#probabilistic-forecast-formats)
* [Miscellaneous changes to data exchange policies](#miscellaneous-feedback)

The revised versions of the dashboard documentation, API, and data model are now available:

* [https://solarforecastarbiter.org/dashboarddoc/](https://solarforecastarbiter.org/dashboarddoc/)
* [https://api.solarforecastarbiter.org/](https://api.solarforecastarbiter.org/)
* [https://solarforecastarbiter.org/datamodel/](https://solarforecastarbiter.org/datamodel/)

Please review the materials fill out this very short form with any additional feedback concerning data templates:

* [https://goo.gl/forms/pzrFFHICacvZAnsB3](https://goo.gl/forms/pzrFFHICacvZAnsB3)

Five stakeholders participated in the webinar and six stakeholders provided feedback using the feedback form or email. We address the reviewer feedback below.


## Missing, irregular, and regular data
{: .anchor}

Important feedback concerned missing data and if data was required to have a regular time interval (e.g. a point every minute) vs. points at arbitrary record times (similar to many PI historian configurations). We have made the following changes to the Observation data requirements:

* Observation metadata must now include an interval length parameter.
* Observation data uploads will be rejected if any time interval does not match the associated metadata interval length parameter.
* Missing data must be specified with an empty field, NaN, or NULL. The following is an example of valid 5 minute interval length data:

```
timestamp,value,quality_flag
2019-03-01T12:00:00Z,5,0
2019-03-01T12:05:00Z,,1
2019-03-01T12:10:00Z,5,0
2019-03-01T12:15:00Z,NaN,1
2019-03-01T12:20:00Z,NULL,1
```

A new Observation container must be created if the interval length parameter changes.

We will create a recommendations document for PI users to refer to when preparing archived irregular data for upload as regular interval data. Revisions to the observation data requirements will be considered in Year 2 in response to stakeholder requests.


## Probabilistic forecast formats
{: .anchor}

Several stakeholders questioned how the Solar Forecast Arbiter would support probabilistic forecast data exchange. We have now added probabilistic forecast descriptions to the [Forecast Definitions](https://solarforecastarbiter.org/usecases/#probforecastdef), the [Data Model](https://solarforecastarbiter.org/datamodel/#probabilistic-forecasts), and the [API](https://api.solarforecastarbiter.org/#tag/Probabilistic-Forecasts). In short, the Solar Forecast Arbiter quantifies probabilistic forecasts using cumulative distribution functions (CDFs). Users may discretize the CDF into constant values along either the variable axis or the percentile axis, and then forecast for the corresponding value on the complementary axis. Each component of a probabilistic forecast must be uploaded to a predetermined endpoint. We believe that this is a practical way to allow for both flexible specifications and simple formatting of probabilistic forecasts. Please see the links above for more information.

The addition of probabilistic forecasts to the API required that the non-probabilistic forecast API changed slightly in order for the API to remain RESTful. Please see [solarforecastarbiter-api#67](https://github.com/SolarArbiter/solarforecastarbiter-api/pull/67) for details.


# Miscellaneous feedback
{: .anchor}

Stakeholders agreed that the dashboard sketches demonstrate a reasonable way to define Sites, Observations, and Forecasts.

Several stakeholders asked about editing metadata for a Site, Observation, or Forecast. Users will not be able to edit most metadata. Instead, users should create a new Site, Observation, or Forecast, or contact the administrators to change a metadata value.

We clarified that the metadata forms will require users to input valid input in all required fields. For most parameters, default values are not assumed and the user must provide a value. Exceptions will only be made where the default is obvious or where the metadata is less important and users may have a difficult time locating metadata. Tooltips will specify valid input ranges and API responses will indicate the fields that do not conform to the required input ranges.

We added two loss factor parameters to the PV system specification based on user feedback. The loss factors are: 1. DC loss factor: applied to DC current. 2. AC loss factor: applied to inverter power output.

Stakeholders asked for more information about the extra parameters field. This field is free form text. It is not used by the Solar Forecast Arbiter, but site owners and forecasters may use it to communicate additional modeling parameters. We recommended JSON or YAML because these are commonly used formats for specifying metadata, but CSV could also be used. A detailed system specification is beyond the scope of the Solar Forecast Arbiter.

Stakeholders agreed that the web dashboard sketches demonstrate a reasonable way to manually upload or download data.

We added a download data sketch in response to stakeholder requests. The download form will contain information about the period of record for the observation/forecast in the database.

We clarified that the dashboard will return useful error messages if data is formatted incorrectly.

Stakeholders agreed that the csv and json Observation and Forecast data templates are reasonable.

A stakeholder asked why we are supporting json rather than XML. We choose to support json because, in our experience, it is more commonly used in RESTful APIs and it is less verbose. We also recognize that some forecasters and forecast users use XML. We will reevaluate adding XML support in Year 2 of the project if there is sufficient stakeholder interest.

Stakeholders agreed that the API provides a reasonable way to automate the upload and download of Observation and Forecast data.

Stakeholders pointed out the challenge of creating a scalable framework that can remain responsive when large amount of data are provided. We agree that this is a challenge. The Data Model and data formats are designed in ways that we believe will help with this scalability. We also note that the forecast evaluation time series requires non-overlapping data, which helps with some of the dimensionality problems associated with forecasts.

We added Availability and Curtailment to the list of supported variables in the data model.

A stakeholder suggested that we consider that bifacial PV will become more common over the next several years and that additional metadata will be required for these systems. We agree. For now, we recommend using the free-form Extra Parameters field to specify bifacial modeling parameters. In years 2 and 3 we can investigate if and how some parameters should be added to the standard metadata options.

We made minor consistency and grammar improvements suggested by stakeholders.

We changed the forecast attribute “value type” to “interval value type” to avoid confusion.

If you’ve read this far, you may be interested to download and run a local instance of the API with a file storage backend for testing. You can even run a local instance of the dashboard against the API! Please see these GitHub repositories for more information:

* [https://github.com/SolarArbiter/solarforecastarbiter-api](https://github.com/SolarArbiter/solarforecastarbiter-api)
* [https://github.com/SolarArbiter/solarforecastarbiter_dashboard](https://github.com/SolarArbiter/solarforecastarbiter_dashboard)
