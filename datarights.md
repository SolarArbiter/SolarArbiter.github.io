---
layout: base
permalink: /datarights/
---
## Data Rights -- DRAFT

This page contains a **DRAFT** data rights and policies proposal.

This page describes the disclosure levels for observational (generation
and environmental) and forecast data submitted to the framework, as well
as data derived from the process of comparing forecast fields to
observations (e.g. summary statistics).

Guiding Principles
------------------

The following principles guide our data policies.

1. Organizations retain ownership of the data they upload to the framework.
2. Users upload data to the framework on behalf of organizations.
2. Users have complete control over how their data may be accessed by other users.
2. Users may delete data from the framework.
2. A forecast trial may require that data owners relinquish control of a
   copy of their data (optionally anonymized) to ensure trial fairness,
   transparency, and reproducibility. The terms of a trial and its data
   permissions will be fully defined before users contribute data to it.
2. The framework will not sell the data that it controls.
2. All non-public data will be securely deleted by the conclusion of the DOE
   funding period (June 30, 2021).


Contributing data
-----------------

Each organization contributing data to the framework retains ownership
and control of its data. Each framework user is a member of an
organization and contributes data on behalf of the organization.

Through the framework web interface or API calls, the user associates
data with data access policies. These policies allow specific
organizations/users to access to the data. Example policies are shown
below. The web interface will show an organization a list of all of the
submitted data/metadata it owns and the users/organizations that can
access each data source.


Deleting data
-------------

An organization may delete its data from the framework at any time, or
an organization may ask the framework administrators to delete its data
from the framework.

Anonymized time series data and summary statistics
derived from the data are owned by the framework and not deleted.
(Framework is not allowed to sell anonymized data or statistics.)

All non-public data will be securely deleted at the conclusion of the
DOE funding period (June 30, 2021). The post-DOE-funding framework
administrators and data contributors will need to resign new NDAs.

Users may delete data sooner than the end of the funding period.


Data access policies
--------------------

A data access policy defines the ways in which the data can accessed by users.
The framework supports the following data access policies, ordered from least
to most permissible.

* No access
    * Default access level for data uploaded by users.
* Peer-to-peer
    * A single user grants another user permission to view data.
* Multiparty Confidential Access anonymized
    * Groups of organizations/users will be defined in response to each need
      e.g. a particular forecast trial.
    * Anonymized data accessible is accessible to all users within a specific group.
    * Anonymized data is not accessible by users outside of the group (or general public).
    * True owners of anonymized data are not known by framework administrators (see note below).
* Multiparty Confidential Access
    * Groups of organizations/users will be defined in response to each need
      e.g. a particular trial.
    * Data accessible is accessible to all users within a specific group.
    * Data is not accessible by users outside of the group (or general public).
* Public (with required sign on)
    * Reference data such as SURFRAD, SOLRAD, Sandia, NREL MIDC, U Oregon,
      DOE Data Acquisition and Archive Portal (DAP), etc.



Non-Disclosure Agreements
-------------------------

The creator of an organization account must agree to common terms before
the account may be activated. The terms describe the data rights and
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
security of stored data and data transmission.

On anonymity from framework administrator/operator... with some study of
IP logs the framework operator could potentially figure out who
contributed what data. This would require super user access on the
servers. This access will be restricted to the smallest number of people
possible. Data contributors that want to prevent this possibility can
use a VPN.
