---
layout: base
permalink: /datapolicies/
title: Data Policies
---
# Data Policies

This page summarizes the data sharing and privacy policies of the
Solar Forecast Arbiter.

An **organization** is an entity that owns data or obtains license to
submit data to the framework. A **user** is an individual working for an
organization that performs tasks such as submitting data to the
framework and downloading data from the framework. An **organization
administrator** is a user that has can also grant permissions to view or
modify data to other users, including users outside of the
administrator's own organization.

The [Data Use Agreement](/assets/45864 Approved_Final version 1.1.pdf)
(DUA) is a **non-negotiable** legal document that all parties are bound to.
The DUA must be signed by an authorized representative
of an organization before its employees will be allowed to upload data,
view data contributed by other users, or generate summary statistics.

The data policies can be summarized as:

* Signing the DUA does **not** obligate an organization to upload data,
  nor does it obligate an organization to share uploaded data.
* Organizations retain ownership of the data they upload to the framework.
* Users upload data to the framework on behalf of organizations.
* Organization administrators have complete control over how their
  organization's data may be accessed by other users.
* Organization administrators may delete their organization's data from the
  Arbiter at any time.
* Uploading data does **not** give Solar Forecast Arbiter team members
  the ability to study it. Sharing data with project team members
  follows the same procedures as sharing data with any other user.
* All data will be securely deleted within 30 days of the termination of
  the project (anticipated late 2021).

The DUA describes two types of data that participants may contribute:
*Open Project Data* and *Limited Project Data*. Limited Project Data is
proprietary data for which access controls are required. Most of the
data policies are structured around addressing concerns about Limited
Project Data. Open Project Data is data that users contribute to the
project's reference data set. This data immediately benefits the whole
community, but organizations lose control over who can access it.

## Contributing data

Each organization contributing data to the framework retains ownership
and control of its data. Each framework user is a member of an
organization and contributes data on behalf of the organization.

Through the framework web interface or API calls, the user associates
data with data access policies. These policies allow specific
users to access to the data. The web interface shows
an organization administrator a list of all of the submitted metadata/data
it owns and the access roles given to other users. Please see the
[Data Access Control documentation](/data-access-workflow/) for more
information.

Under a forecast trial use case, anonymized time series data and/or
summary statistics derived from the data are owned by the framework.
This ensures trial fairness, transparency, and reproducibility. However,
the framework operators are not allowed to view or disclose anonymized
data or statistics unless given permission using the data sharing
features of the web service.

## Deleting data

An organization may delete its data from the framework at any time, or
an organization may ask the framework operators to delete its data from
the framework.

All non-public data will be securely deleted within 30 days of the
termination of the project (anticipated late 2021).

## Other

The Solar Forecast Arbiter uses national standards and best practices
for security of stored data and data transmission.

Stakeholders have questioned the ability for framework operators to
access user-contributed data. Accessing user-contributed data requires
highly-restricted super user access on the servers. This access is
restricted to the smallest number of people possible. The DUA expressly
forbids the framework operators from analyzing or examining
user-contributed data except when required to solve service issues.

Stakeholders have also questioned the ability for framework operators to
deanonymize data contributed to anonymous forecast trials. With some
study of IP logs the framework operator could potentially determine who
contributed what data. This too would require highly-restricted super
user access on the servers. Data contributors that want to prevent this
possibility can use a VPN.
