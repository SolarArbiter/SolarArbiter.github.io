---
layout: dataaccessworkflow
permalink: /data-access-workflow/
---

# Solar Forecast Arbiter Data Access Control Workflow
{: .anchor}

This guide descibes how to use the the Solar Forecast Arbiter's
role based access control system to manage access to data on
the system.

# Account Creation
{: .anchor}

New framework users will need to sign up through the Solar Forecast
Arbiter dashboard. The signup form can be found by following the 'Log
in' link on the front page of the dashboard and clicking on the sign up
tab. New users will need to verify their email before they will be able
to access data in the Solar Forecast Arbiter.


Upon account creation users are granted access to view only the
reference data set, but may not contribute data. Users will need to be
part of an organization that has signed the Data Use Agreement to
contribute data, generate reports, or access data shared by an
organization.

# Establishing or Joining an Organization
{: .anchor}

After creating an account, users should contact the framework
administrators at [help@solarforecastarbiter.org](mailto:help@solarforecastarbiter.org) to
establish a new organization or join an existing organization. To
establish a new organization, the framework administrators will provide
the user with a non-negotiable Data Use Agreement, the user will review
the Data Use Agreement and return the Data Use Agreement signed by an
authorized representative of the organization. A point of contact will
be established to verify future updates to the organization. To join a
previously established organization, framework administrators will
verify with the organization's point of contact that the user is
authorized to join the organization.


An organization administrator will be appointed to manage data access,
this will typically be the user who initiated the request for an
Organization. Organization administrators are privileged users that
can grant and revoke access to data that their organization owns. An
organization administrator may grant administrative privileges to other
users. Organization administrators will use the data access controls
described below to grant access to data in the organization. To remove
a user from an organization, an organization admin should contact
framework administrators. When a user is removed from an organization, they
will lose access to all organizations' data but retain permission to view
the reference data set.

# Data Access Controls
{: .anchor}

Organization administrators will use the Solar Forecast Arbiter's data
access controls to grant users access to their data or to allow users to
submit data on their organization's behalf.


The Solar Forecast Arbiter uses a Role Based Access Control System to
control access to data. There are four main components in the access
control system:

- ### Organizations

    Organizations are groups of *users*. All data submitted by users
    within an organization will belong to that organization. An
    organization's administrators will control access to all
    of the data belonging to the organization.

- ### Users

    Framework user accounts determine what actions an end user can
    perform within the framework. A user is granted access to data through
    the *roles* they are assigned.

- ### Roles

    Roles are a collection of *permissions* that may be assigned to a
    user. A user's roles typically only grant permissions necessary for
    their job function or title. For instance, an organization
    administrator's roles will have permissions to create new roles and
    permissions, while a non-administrative user's roles may only have
    permission to view and write data to the organization's forecasts.
    Roles may also be created to share data with users outside of the
    organization.

- ### Permissions

    Permissions allow a user to perform an action on a piece of data or
    pieces of similar objects in the framework. For instance, a permission
    may allow a user to view the metadata of an observation or post values
    to all forecasts. Permissions are added to roles to enable users with
    that role to perform the permission's action. A permission can only
    allow actions on data owned by the organization in which it
    was created.

### Default Roles
{: .anchor}

When a new organization is created, a set of default roles will be
created for the organization.

The default roles are described below:

-   **View all data and metadata:** Access all of the metadata and
    values in the organization. This includes observations, forecasts,
    probabilistic forecasts, sites and reports.

-   **Write all values:** Allows a user to submit data within the
    organization e.g. adding measurements to an
    observation.

-   **Create metadata:** Allows a user to create new sites,
    observations, forecasts and probabilistic forecasts. Also allows
    the creation of reports.

-   **Delete data and metadata:** Allows a user to delete sites,
    observations, forecasts, probabilistic forecasts as well as any
    associated values.

-   **Administer data access controls:** Granted to organization
    administrators, this role allows:

    -   Create and delete new roles and permissions.

    -   Add and remove permissions from roles.

    -   Add or remove data objects from a permission.

    -   Grant and revoke roles on a user.


These roles are intended for use within the organization as they permit
actions on all existing and future data in an organization. For sharing
data with users outside their organization, organization administrators
are advised to create roles with specific permissions that apply to only
the data they would like to share.

Sharing Data With Other Organizations
-------------------------------------
{: .anchor}

An organization administrator may grant roles to users outside of their
organization. These roles allow organizations to share data with users
of other organizations. Roles granted to users outside of the
organization may not contain administrative permissions that allow users
to perform an update, create or delete action on roles, permissions or
users. Similarly, a permission allowing such actions may not be added to
a role that is currently shared with a user outside the
organization.
