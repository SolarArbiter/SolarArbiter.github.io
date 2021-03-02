---
layout: base
permalink: /documentation/dashboard/administration/
sidebar: dashboard_admin_sidebar.html
title: Administration
---

# Dashboard Administration
{: .anchor}

Data access control is ubiquitous in the Solar Forecast Arbiter. All users can
benefit from a cursory understanding of the access control system. Organization
administrators need a more thorough understanding to effectively and safely
manage their data.

This section describes the key concepts, outlines the user interface, and
provides several examples.

User, permission, and role administation can be accessed by clicking the **User
Administration** link in the Account menu in the top right corner of the site.
    <img class="my-3" src="/images/admin_menu.png"/>

These pages allow organization administrators to view and manage permissions.
Users without administrative privileges may not see anything on these pages.

## Data types
{: .anchor}

When we talk about *data access* we often fail to distinguish between types of
data. That's sometimes ok for plain communication, but a good data control
system requires precision.

### Sites, Observations, Forecasts, Aggregates and Reports
{: .anchor}

Most users will already be familiar with the site, observation, and forecast
data, but note the metadata is distinct from the time series values:

* Site metadata (e.g. location and capacity)
* Observation metadata (e.g. interval length)
* Observation time series values
* Forecast metadata (e.g lead time to start)
* Forecast time series values
* Probabilistic forecast metadata (e.g. fixed percentiles)
* Probabilistic forecast time series values
* Aggregate metadata (e.g. constituent observations)

Reports are also comprised of metadata and values:

* Report metadata (e.g. start and end times, metrics selections)
* Report values (e.g. the metric values)

Aggregates are fully described their metadata. Aggregate values are dynamically
computed and rely on the permissions associated with their constituent
observations.

### Organizations
{: .anchor}

Organizations are groups of *users*. All data submitted by users within an
organization belong to that organization. An organization's administrators
control access to all of the data belonging to the organization. See
[Managing Organizations and Users](#managing-organizations-and-users) for
more information on organizations.

### Users
{: .anchor}

Users are described by their *user name* and their *organization affiliation*.
See [User Classifications](#user-classifications) for more information on users.

### Data About Data Access
{: .anchor}

The data types that support the access control system are:

* Permissions (e.g. read site Y and site Z metadata)
* Roles (e.g. share forecasts with utility X)


## Role Based Access Control
{: .anchor}

Sharing data in the Solar Forecast Arbiter generally requires:

1. Creating *permissions* for reading or modifying data.
2. Grouping those permissions into *roles*.
3. Granting those roles to one or more user names.

This pattern is known as [Role Based Access
Control](https://www.google.com/search?q=role+based+access+control). The next
sections discuss [permissions](#permissions) and [roles](#roles) in more detail.

### Permissions
{: .anchor}

Permissions allow a user to perform an action on a piece of data or pieces of
similar objects in the framework. For instance, a permission may allow a user to
view the metadata of a single observation. Another permission may allow a user
to post values to all forecasts. Permissions are added to roles to enable users
with that role to perform the permission's action. A permission can only allow
actions on data owned by the organization in which it was created.

The [Permissions Reference Table](#Permissions-Reference-Table) describes the
full set of permissions.

#### Create New Permission
{: .anchor}

1. Navigate to the Permissions listing with the *Permissions* tab of the admin
   menu. This page will list all of the Permissions you have access to
   administer or view.
   <img class="my-3" src="/images/permissions.png"/>

2. Click on the data type you would like to create a permission for in the
   "Create new Permission" box. You will be prompted for a description of the
   permission, the action the permission allows and a list of objects. Click
   the checkboxes for each object that the permission should allow its action
   on. Selecting *Applies to all* will cause the permission to affect all
   current and future objects of the permission's type.

   *Permission form for observation permsission*
   <img src="/images/permission_form.png"/>

Clicking on an individual Permission will list information about it and the
objects it applies to.
    <img class="my-3" src="/images/permission.png"/>

### Roles
{: .anchor}

Roles are a collection of *permissions* that may be granted to a user. Granting
a role permits the user to perform actions defined by the role's permissions.

Best practice is to only grant users the permissions necessary to perform their
job function. For instance, an organization administrator's roles will have
permissions to create new roles and permissions, while a non-administrative
user's roles may only have permission to view and write data to the
organization's forecasts.

Roles may also be created to share data with users outside of the organization.
For instance, a utility may create a role "Share with forecasters" that
includes permissions for reading site metadata, observation metadata, and
observation values.

#### Default Roles
{: .anchor}

When a new organization is created, a set of default roles is created for the
organization. These roles are intended for use within the organization as they
permit actions on all existing and future data in an organization.
Administrators are encouraged to create new roles with permissions tailored to a
specific user or group of users. When sharing data with users outside their
organization, organization administrators are *strongly encouraged* to create
roles with specific permissions that apply to only the data they would like to
share.

The default roles are:

* **View all data and metadata:** Access all of the metadata and
  values in the organization. This includes observations, forecasts,
  probabilistic forecasts, sites, aggregates, and reports.
* **Write all values:** Allows a user to submit data within the
  organization e.g. adding measurements to an
  observation.
* **Create metadata:** Allows a user to create new sites, observations,
  forecasts, probabilistic forecasts, reports, and aggregates.
* **Delete data and metadata:** Allows a user to delete sites,
  observations, forecasts, probabilistic forecasts as well as any
  associated values.
* **Administer data access controls:** Granted to organization
    administrators, this role allows:

  * Create and delete new roles and permissions.
  * Add and remove permissions from roles.
  * Add or remove data objects from a permission.
  * Grant and revoke roles on a user.

#### Create New Role
{: .anchor}

1. Navigate to the roles listing with the *Roles* tab of the admin menu. This page
   lists all of the Roles you have access to administer or view.
   <img class="my-3" src="/images/roles.png"/>

2. Click the *Create new Role* button. Complete the form with a name and
   description of the role. After the role is created you may
   [add permissions to the role](#add-permissions-to-a-role) or
   [grant it to users](#grant-roles-to-a-user).

Clicking on an individual Role will list information about it and the
permissions associated with it. Use the tabs below the metadata section to
switch between the list of permissions on the role and a list of users the role
has been granted to.

    *Role permissions listing*
    <img class="my-3" src="/images/role.png"/>

    *Role users listing*
    <img class="my-3" src="/images/role_users.png"/>

### Grant and Revoke Roles
{: .anchor}

To give users permissions on data, an administrator *grants* a role to a user
that contains the relevant permissions. Users may be granted multiple roles.
Administrators may also *revoke* roles to remove the ability of a user to
interact with data.

#### Grant Roles to a User
{: .anchor}

Organization administrators may grant roles to other users through several
interfaces.

##### All Users
{: .anchor}

Roles can be any granted to any user, including those outside your organization,
through the role administration interface.

1. Navigate to the Role you would like to grant to a user. Click the
   *Grant Role* button.

2. Enter the email of the user to grant the role to and click submit.

##### Users within your organization
{: .anchor}

Roles may be granted to users within your organization through the user
administration interface.

1. Navigate to the User for which you would like to grant permissions and
   click the *Add Roles* button.

2. This page will list each role that is not already granted to the user.
   Check the box for each role to add to the user and submit the form. You
   will be returned to the user's page.

#### Revoke Roles from a User
{: .anchor}

Organization administrators may revoke roles to other users through several
interfaces.

##### All Users
{: .anchor}

Roles can be any removed from any user, including those outside your
organization, through the role administration interface.

1. Navigate to the Role you would like to revoke from a user and click on the
   *Users* tab.

2. Locate the user in the users table and click the *remove* link in the far
   right column. You will be presented with a confirmation page before the
   role is removed from the user.

##### Users within your organization
{: .anchor}

Roles may be revoked from users within your organization through the user
administration interface.

1. Navigate to the User you would like to revoke a role from.

2. Locate the Role to revoke in the roles table, and click the *remove* link
   in the far right column. You will be presented with a confirmation page
   before the role is removed from the user.

### Modify Role
{: .anchor}

Permissions may be added to or removed from an existing role. Administrative
permissions may not be added to a role that is currently shared with a user
outside the organization.

#### Add Permissions to a Role
{: .anchor}

1. Navigate to the Role you would like to add permissions to and click the
   **add permissions** button.

2. Check the box for each permission to add to the role and click submit.

#### Remove Permissions from a Role
{: .anchor}

1. Navigate to the Role you would like to remove Permissions from and click on
   the *Permissions* tab.

2. Locate the Permission to revoke in the table and click the *remove* link in
   the far right column. You will be presented with a confirmation page before
   the permission is removed from a role.

## User Classifications
{: .anchor}

Users of the Solar Forecast Arbiter are described by one or more of the
following classifications.

### Organization Administrators
{: .anchor}

Organization Administrators are users with roles that allow them to manage
[users](/documentation/dashboard/administration/#users),
[roles](/documentation/dashboard/administration/#roles) and
[permissions](/documentation/dashboard/administration/#permissions).
Organization administrators are also granted read and write access to all of
their organization's data. Administrators may
[grant](/documentation/dashboard/administration#granting-roles-to-a-user) and
[revoke](/documentation/dashboard/administration#revoking-roles-from-a-user)
roles from users in their organization. They may also add or remove permissions
from roles.

Administrators may grant roles to members of other organizations. The Solar
Forecast Arbiter will reject any attempt to grant roles to users that are not
affiliated with an organization (i.e. their employer has not signed the
platform Data Use Agreement).

An organization's point of contact may request that users in their organization
be promoted to an organization administrator by emailing a request to
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org).

### Standard User
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

### Organization Point of Contact
{: .anchor}

An organization's point of contact is a representative of the organization who
is authorized to approve or request changes to the organization. There may be
more than one point of contact for an organization.

A point of contact may coordinate with framework administrators to:

* Add and remove users from the organization.
* Promote users to [organization administrators](#organization-administrators).
* Coordinate organization participation in a forecast trial.

## Managing Organizations and Users
{: .anchor}

### Create New Organization
{: .anchor}

To create an organization, a company must first sign the Data Use Agreement and
provide it to the Solar Forecast Arbiter administrators. The Arbiter
administrators will then create the organization.

### Affiliate User with Organization
{: .anchor}

Users that are not affiliated with an organization only have the permissions
necessary the browse the reference data set. They cannot create new metadata or
upload data. Nor are they allowed to see data shared by other users.

To affiliate a new user with an organization, the user or the organization's
point of contact must email
[admin@solarforecastarbiter.org](mailto:admin@solarforecastarbiter.org) with the
request. The Solar Forecast Arbiter administrators will only affiliate a user
with an organization with the approval of the organization's point of contact.

### Managing Users
{: .anchor}

Users are associated with an organization through the signup process outlined
in [getting started](/documentation/dashboard/getting-started/#signing-up).
Administrators have access to a listing of users in their organization and a
page for each individual user in their organization and the roles they have
been granted.

* The *Users* tab of the *user administration* menu will list the users you
  have access to administer(users within your organization) or view (users
  outside your organization that have been granted access to your data).
  <img class="my-3" src="/images/users.png"/>

* Clicking on an individual user will list information about the user and their
  roles. See the *users within your organization* section of
  [granting roles to a user](/documentation/dashboard  administration#granting-roles-to-a-user) and
  [revoking roles from a user](/documentation/dashboard  administration#revoking-roles-from-a-user)
  for how to manage a user's roles.

  <img class="my-3" src="/images/user.png"/>



## Examples
{: .anchor}

Intro.

### Set up a new organization
{: .anchor}

Analyst Alice wants to use the Solar Forecast Arbiter.

### Share site metadata
{: .anchor}

Forecast User X would like to solicit forecasts from vendors at several power
plants.

### Share a forecast and report
{: .anchor}

Forecast Provider A would like to demonstrate their skill to Forecast User X. A
good way to demonstrate skill is to compare their forecast to the Solar Forecast
Arbiter's reference forecasts at a site within the service territory of Forecast
User X.

## Permissions Reference Table
{: .anchor}

This table gives a brief description of the effect of each type of permission
on each data type. In certain circumstances, a combination of permissions
may be necessary to perform a particular action.

|Data Type|create<sup><b>1</b></sup>|read|update|delete<sup><b>2</b></sup>|read_values|write_values|delete_values|grant|revoke|
|---------|------|----|------|------|-----------|------------|-------------|-----|------|
|sites|create new|read metadata|update all metadata|delete metadata<sup><b>3</b></sup>|n/a|n/a|n/a|n/a|n/a|
|observations|create new|read metadata|update name, uncertainty, and extra parameters|delete metadata and values|read timeseries values and quality flags|add timeseries values to observation|n/a|n/a|n/a|
|forecasts|create new|read metadata|update name and extra parameters|delete metadata and values|read timeseries values|add timeseries values to forecast|n/a|n/a|n/a|
|cdf_forecasts|create new <sup><b>4</b></sup>|read metadata|update name and extra parameters|delete metadata and values|read timeseries values of each bin |add timeseries values to bins|n/a|n/a|n/a|
|aggregates|create new <sup><b>5</b></sup>|read metadata|update name, description, timezone, extra parameters and add or remove observation from aggregate <sup><b>6</b></sup>|delete metadata and values|read timeseries values <sup><b>7</b></sup> |n/a|n/a|n/a|n/a|
|reports|create new|read metadata|set report status, store report metrics and raw_report|delete metadata and values|read processed values of report|store or update processed report values|n/a|n/a|n/a|
|users|create new|read metadata|n/a|delete metadata|n/a|n/a|n/a|n/a|n/a|
|roles|create new|read metadata|add and remove permissions from role|delete metadata|n/a|n/a|n/a|add role to user|remove role from user|
|permissions|create new|read metadata|add and remove objects from permissions|delete metadata|n/a|n/a|n/a|n/a|n/a|
{: .table .perm-table}

1. Create permissions are only effective within the organization that they are
   created. When users create metadata, the metadata is owned by that user's
   organization. User's that are granted `create` permissions outside their
   organization will not be allowed to create new metadata, they will require
   `create` permissions from their own organization.

2. Deleting any data type will remove that object from all permissions
   that affect it.

3. All of a site's forecasts and observations must be deleted before the site
   can be deleted.

4. The creation of a probabilistic forecast (cdf_forecast) requires
   both the `create` and `update` permission.

5. The creation of an aggregate requires the `create` permission to
   create an empty aggregate, and the `update permission` to add the observations that
   make up the aggregate.

6. Adding an observation to an aggregate requires that the user has
   `read` permissions on that observation.

7. Reading the full values of an aggregate requires `read_values` permissions
   on all of it's constituent observations. A partial aggregate value will
   be returned to users.

To prevent adminstrators of one organization from administering another
organization, many permissions related to the administration of users, roles,
and permissions are restricted to users within the same organization. For
example, attempts to grant a role with permission to *update users* to a member
of another organization or to add the *update users* permission to a role that
has been granted outside the organization will not be allowed. Specifically,
create, update, grant, revoke or delete on users, roles, or permissions, are
restricted to users in the same organization.
