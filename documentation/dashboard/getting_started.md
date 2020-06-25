---
layout: base
permalink: /documentation/dashboard/getting-started/
sidebar: dashboard_getting_started_sidebar.html
title: Getting Started
---

Getting Started
===============
{: .anchor}

Registering an account on the Solar Forecast Arbiter is a two step process:

1. [Sign up](#signing-up) for an account. This automatic process immediately
grants you access to the Arbiter's reference data and reference forecasts.

2. [Create a new Organization](#creating-an-organization) or [join an existing
Organization](#joining-an-organization). This manual process grants you access
to the rest of the Arbiter's features including uploading data, sharing data,
running reports, and participating in trials.

The sections below describe these steps in more detail.

### Signing up
{: .anchor}

New framework users sign up through the [Solar Forecast Arbiter dashboard](https://dashboard.solarforecastarbiter.org).
The signup form is found by following the 'Log in' link on the front page of
 the dashboard. You will be prompted with an Auth0 login window
([Auth0](https://auth0.com/docs/getting-started/overview) is a secure
authentication service). Click the sign up tab and enter your information.
Users will receive an email from Solar Forecast Arbiter to verify their
account. Account verification is required before you will be able to access
data in the Solar Forecast Arbiter.

### Organizations
{:.anchor}

Organizations are groups of users whose permissions and data are managed by
the same group of administrators. An organization retains ownership of all data
submitted by its members. Only organization administrators will be authorized
to grant users permissions to view or alter data owned by their organization.

#### Creating an Organization
{: .anchor}

To create an new organization, send a signed
[Data Use Agreement](/assets/45864%20Approved_Final%20version%201.1.pdf)
to the Solar Forecast Arbiter Administrators at
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org). The
administrators will create a new organization for you and assign your user
account to administer it.


#### Joining an Organization
{: .anchor}

Users can join an existing organization by emailing the framework
administrators at [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).
Framework administrators will verify with the organization's point of contact
that the user is authorized to join the organization. To expedite this process,
an organization's point of contact may initiate a request to add the user to
their organization.

### User Classifications
{: .anchor}

Users of the Solar Forecast Arbiter are described by one or more of the
following classifications.

#### Organization Point of Contact
{:.anchor}

An organization's point of contact is a representative of the organization who
is authorized to approve or request changes to the organization. There may be
more than one point of contact for an organization.

A point of contact may coordinate with framework administrators to:

- Add and remove users from the organization.

- Promote users to [organization administrators](#organization-administrators).

- Coordinate organization participation in a forecast trial.

#### Organization Administrators
{: .anchor}

Organization Administrators are users with special permission to manage [users](/documentation/dashboard/administration/#users), [roles](/documentation/dashboard/administration/#roles)
and [permissions](/documentation/dashboard/administration/#permissions). Organization administrators are
also granted full access to their organization's data. An organization's point
of contact may request that users in their organization be promoted to an
organization administrator by emailing a request to
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).

Administrators may [grant](/documentation/dashboard/administration#granting-roles-to-a-user)
and [revoke](/documentation/dashboard/administration#revoking-roles-from-a-user)
roles from users in their organization and add or remove permissions from
roles. Roles may be granted to members of other organizations provided their
organization has aggreed to the Data Use Aggreement.

All administrative permissions other than read access, e.g. those allowing
create, update, grant, revoke or delete on users, roles or permissions, are
restricted to sharing with users in the same organization. For example,
attempts to grant a role with permission to *update users* to a member of
another organization or to add the *update users* permission to a role that
has been granted outside the organization will not be allowed.


#### Standard User
{: .anchor}

Solar Forecast Arbiter users are added to the *Unaffiliated* organization by
default. Unaffiliated users will have access to the reference data set but
may not gain further access until they have joined an organization that has
accepted the data use agreement.

An organization's [point of contact](#organization-point-of-contact) may submit
a request to [admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org)
to add a user to their organization. Users new to an organization have no
access to the organization's data until an [organization administrator](#organization-administrators)
grants them access.
