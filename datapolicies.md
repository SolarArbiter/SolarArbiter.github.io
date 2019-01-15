---
layout: base
permalink: /datapolicies/
---
# Data Policies -- DRAFT

This page contains a **DRAFT** data policies proposal.

This page describes the disclosure levels for observational (generation
and environmental) and forecast data submitted to the framework, as well
as data derived from the process of comparing forecast fields to
observations (e.g. summary statistics).

An **organization** is an entity that owns data or obtains license to submit
data to the framework. A **user** is an individual working for an organization
that performs the tasks of submitting data to the framework, granting other
users or organizations rights to view data, and downloads data from the
framework.

Guiding Principles
------------------

The following principles guide our data policies.

1. Organizations retain ownership of the data they upload to the framework.
2. Users upload data to the framework on behalf of organizations.
2. Users have complete control over how their organization's data may be
   accessed by other users within organizations.
2. Users may delete their organization's data from the framework at any time.
2. The framework will not sell, donate, or otherwise disclose the data that it
   controls without express written consent of the data owner.
2. All non-public data will be securely deleted by the conclusion of the DOE
   funding period (June 30, 2021) unless express written permission to
   retain it is obtained.


Contributing data
-----------------

Each organization contributing data to the framework retains ownership
and control of its data. Each framework user is a member of an
organization and contributes data on behalf of the organization.

Through the framework web interface or API calls, the user associates
data with data access policies. These policies allow specific
organizations/users to access to the data. Example policies are shown
below. The web interface will show an organization a list of all of the
submitted metadata/data it owns and the users/organizations that can
access each data source.

Under some use cases, anonymized time series data and or summary statistics
derived from the data are owned by the framework. This ensures trial fairness,
transparency, and reproducibility. The framework is not allowed
to sell, donate, or otherwise disclose anonymized data or statistics.


Deleting data
-------------

An organization may delete its data from the framework at any time, or
an organization may ask the framework administrators to delete its data
from the framework.

All non-public data will be securely deleted at the conclusion of the
DOE funding period (June 30, 2021) unless express written consent is
granted by both the data contributor and the post-DOE-funding framework
administrator.


Data access policies
--------------------

A data access policy defines the ways in which the data can accessed by users.
The framework supports the following data access policies, ordered from least
to most permissible.

* Owner-only
    * Default access level for data uploaded by users.
* Peer-to-peer
    * A single user, working on behalf of an organization, grants another user
      working on behalf of another organization permission to view data.
* Multiparty Confidential Access anonymized
    * Groups of organizations/users will be defined in response to each need
      e.g. a particular forecast trial.
    * Anonymized data is accessible to all users within a specific group.
    * Anonymized data is not accessible by users outside of the group (or general public).
    * True owners of anonymized data are not known by framework administrators (see note below).
* Multiparty Confidential Access
    * Groups of organizations/users will be defined in response to each need
      e.g. a particular trial.
    * Data is accessible to all users within a specific group.
    * Data is not accessible by users outside of the group (or general public).
* Public (with required sign on)
    * Reference data such as SURFRAD, SOLRAD, Sandia, NREL MIDC, U Oregon,
      DOE Data Acquisition and Archive Portal (DAP), etc.



Non-Disclosure Agreements
-------------------------

The creator of an organization account must agree to common terms before
the account may be activated. The terms describe the data policies and
procedures outlined in this document. The representative of the
organization that agrees to the terms must have the authority to do so.
Only then can the user view data or add new members to the organization.
New members will be prompted to review and agree to the terms when creating a
user account.

In the event that the terms change, organization administrators will be
prompted to reverify their compliance.


Other
-----

The framework will use national standards and best practices for
security of stored data and data transmission. *For example*...

On anonymity from framework administrator/operator... with some study of
IP logs the framework operator could potentially determine who
contributed what data. This would require super user access on the
servers. This access will be restricted to the smallest number of people
possible. Data contributors that want to prevent this possibility can
use a VPN.
