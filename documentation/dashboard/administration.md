---
layout: base
permalink: /documentation/dashboard/administration/
sidebar: dashboard_admin_sidebar.html
title: Administration
---

# Dashboard Administration
{: .anchor}

This section describes the user interface for organization administrators to
manage data access through roles and permissions.

User, permission and role administation can be accessed by clicking the **User
Administration** link in the Account menu in the top right corner of the site.
    <img class="my-3" src="/images/admin_menu.png"/>



Note that these menus are meant to assist organization administrators in viewing
and managing permissions, and users without administrative privileges may not
see anything on these pages.

## Data Access Components
{: .anchor}

Organization administrators will use the Solar Forecast Arbiter's data
access controls to grant users access to their data or to allow users to
submit data on their organization's behalf. The Solar Forecast Arbiter uses a
Role Based Access Control System to control access to data. There are four main
components in the access control system:

### Organizations
{: .anchor}

  Organizations are groups of *users*. All data submitted by users
  within an organization will belong to that organization. An
  organization's administrators will control access to all
  of the data belonging to the organization.

### Users
{: .anchor}

  Framework user accounts determine what actions an end user can
  perform within the framework. A user is granted access to data through
  the *roles* they are assigned.

#### User Classifications
{: .anchor}

Users of the Solar Forecast Arbiter are described by one or more of the
following classifications.

##### Organization Point of Contact
{: .anchor}

An organization's point of contact is a representative of the organization who
is authorized to approve or request changes to the organization. There may be
more than one point of contact for an organization.

A point of contact may coordinate with framework administrators to:

- Add and remove users from the organization.

- Promote users to [organization administrators](#organization-administrators).

- Coordinate organization participation in a forecast trial.

##### Organization Administrators
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

### Roles
{: .anchor}

  Roles are a collection of *permissions* that may be granted to a
  user. Best practice is to only grant users the permissions necessary to
  perform their job function. For instance, an organization administrator's
  roles will have permissions to create new roles and permissions, while a
  non-administrative user's roles may only have permission to view and write
  data to the organization's forecasts. Roles may also be created to share
  data with users outside of the organization.

### Permissions
{: .anchor}

  Permissions allow a user to perform an action on a piece of data or
  pieces of similar objects in the framework. For instance, a permission
  may allow a user to view the metadata of an observation or post values
  to all forecasts. Permissions are added to roles to enable users with
  that role to perform the permission's action. A permission can only
  allow actions on data owned by the organization in which it
  was created.

## Default Roles
{: .anchor}

When a new organization is created, a set of default roles will be
created for the organization. These roles are intended for use within the
organization as they permit actions on all existing and future data in an
organization. Administrators are encouraged to create new roles with
permissions tailored to a specific user or group of users. When sharing data
with users outside their organization, organization administrators are *strongly encouraged*
to create roles with specific permissions that apply to only the data they
would like to share.


The default roles are described below:

-   **View all data and metadata:** Access all of the metadata and
    values in the organization. This includes observations, forecasts,
    probabilistic forecasts, sites, aggregates, and reports.

-   **Write all values:** Allows a user to submit data within the
    organization e.g. adding measurements to an
    observation.

-   **Create metadata:** Allows a user to create new sites, observations,
    forecasts, probabilistic forecasts, reports, and aggregates.

-   **Delete data and metadata:** Allows a user to delete sites,
    observations, forecasts, probabilistic forecasts as well as any
    associated values.

-   **Administer data access controls:** Granted to organization
    administrators, this role allows:

    -   Create and delete new roles and permissions.

    -   Add and remove permissions from roles.

    -   Add or remove data objects from a permission.

    -   Grant and revoke roles on a user.


## Managing Users
{: .anchor}

Users are associated with an organization through the signup process outlined
in [getting started](/documentation/dashboard/getting-started/#signing-up).
Administrators have access to a listing of users in their organization and a
page for each individual user in their organization and the roles they have
been granted.

-   The *Users* tab of the *user administration* menu will list the users you
    have access to administer(users within your organization) or view (users
    outside your organization that have been granted access to your data).
	<img class="my-3" src="/images/users.png"/>


-	Clicking on an individual user will list information about the user and their
    roles. See the *users within your organization* section of
    [granting roles to a user](/documentation/dashboard/administration#granting-roles-to-a-user) and
    [revoking roles from a user](/documentation/dashboard/administration#revoking-roles-from-a-user)
    for how to manage a user's roles.

    <img class="my-3" src="/images/user.png"/>


## Create New Role
{: .anchor}

1.  Navigate to the roles listing with the *Roles* tab of the admin menu. This page
    lists all of the Roles you have access to administer or view.
    <img class="my-3" src="/images/roles.png"/>

2.  Click the *Create new Role* button. Complete the form with a name and
     description of the role. After the role is created you may
    [add permissions to the role](#add-permissions-to-a-role) or
    [grant it to users](#grant-roles-to-a-user).

-   *Created Role pages*

	Clicking on an individual Role will list information about it and the permissions
    associated with it. Use the tabs below the metadata section to switch between the
    list of permissions on the role and a list of users the role has been granted to.

    *Role permissions listing*
    <img class="my-3" src="/images/role.png"/>
    *Role users listing*
    <img class="my-3" src="/images/role_users.png"/>




## Create New Permission
{: .anchor}
1.	Navigate to the Permissions listing with the *Permissions* tab of the admin
    menu. This page will list all of the Permissions you have access to
    administer or view.
    <img class="my-3" src="/images/permissions.png"/>

2.  Click on the data type you would like to create a permission for in the
    "Create new Permission" box. You will be prompted for a description of the
    permission, the action the permission allows and a list of objects. Click
    the checkboxes for each object that the permission should allow its action
    on. Selecting *Applies to all* will cause the permission to affect all
    current and future objects of the permission's type.

    *Permission form for observation permsission*
    <img src="/images/permission_form.png"/>

-   Clicking on an individual Permission will list information about it and the
    objects it applies to.
    <img class="my-3" src="/images/permission.png"/>

## Data Sharing
{: .anchor}

An organization admin can share data by granting roles to a user. Granting a
role permits the user to perform actions defined by the role's permissions.
Roles granted to users outside of the organization may not contain
administrative permissions. Administrative permissions are those that allow
users to perform an update, create, or delete action on roles, permissions, or
users. Similarly, administrative permissions may not be added to a role that is
currently shared with a user outside the organization.

### Grant Roles to a User
{: .anchor}

**Users within your organization**

1.  Navigate to the User for which you would like to grant permissions and
    click the *Add Roles* button.

2.  This page will list each role that is not already granted to the user.
    Check the box for each role to add to the user and submit the form. You
    will be returned to the user's page.


**Users in other organizations**

1.  Navigate to the Role you would like to grant to a user. Click the
    *Grant Role* button.


2.  Enter the email of the user to grant the role to and click submit.


### Revoke Roles from a User
{: .anchor}

**Users within your organization**

1.  Navigate to the User you would like to revoke a role from.

2.  Locate the Role to revoke in the roles table, and click the *remove* link
    in the far right column. You will be presented with a confirmation page
    before the role is removed from the user.

**Users in other organizations**

1.  Navigate to the Role you would like to revoke from a user and click on the
    *Users* tab.

2.  Locate the user in the users table and click the *remove* link in the far
    right column. You will be presented with a confirmation page before the
    role is removed from the user.


### Add Permissions to a Role
{: .anchor}

1.  Navigate to the Role you would like to add permissions to and click the
    **add permissions** button.

2.  Check the box for each permission to add to the role and click submit.


### Remove Permissions from a Role
{: .anchor}

1.  Navigate to the Role you would like to remove Permissions from and click on
    the *Permissions* tab.

2.  Locate the Permission to revoke in the table and click the *remove* link in
    the far right column. You will be presented with a confirmation page before
    the permission is removed from a role.


Permissions Reference Table
---------------------------
{: .anchor}

This table gives a brief description of the effect of each type of permission
on each data type. In certain circumstances, a combination of permissions
may be necessary to perform a particular action.

|Data Type|create<sup><b>6</b></sup>|read|update|delete<sup><b>1</b></sup>|read_values|write_values|delete_values|grant|revoke|
|---------|------|----|------|------|-----------|------------|-------------|-----|------|
|observations|create new|read metadata|n/a|delete metadata and values|read timeseries values and quality flags|add timeseries values to observation|n/a|n/a|n/a|
|forecasts|create new|read metadata|n/a|delete metadata and values|read timeseries values|add timeseries values to forecast|n/a|n/a|n/a|
|cdf_forecasts|create new <sup><b>2</b></sup>|read metadata|add a constant value to a cdf_forecast|delete metadata and values|read timeseries values of each bin |add tiemseries values to bins|n/a|n/a|n/a|
|aggregates|create new <sup><b>3</b></sup>|read metadata|add/remove observation from aggregate <sup><b>4</b></sup>|delete metadata and values|read timeseries values <sup><b>5</b></sup> |n/a|n/a|n/a|n/a|
|reports|create new|read metadata|set report status, store report metrics and raw_report|delete metadata and values|read processed values of report|store or update processed report values|n/a|n/a|n/a|
|users|create new|read metadata|n/a|delete metadata|n/a|n/a|n/a|n/a|n/a|
|roles|create new|read metadata|add and remove permissions from role|delete metadata|n/a|n/a|n/a|add role to user|remove role from user|
|permissions|create new|read metadata|add and remove objects from permissions|delete metadata|n/a|n/a|n/a|n/a|n/a|
{: .table .perm-table}

1. Deleting any data type will remove that object from all permissions
   that affect it.

2. The creation of a probabilistic forecast (cdf_forecast) requires
   both the `create` and `update` permission.

3. The creation of an aggregate requires the `create` permission to
   create an empty aggregate, and the `update permission` to add the observations that
   make up the aggregate.

4. Adding an observation to an aggregate requires that the user has
   `read` permissions on that observation.

5. Reading a the full values of an aggregate requires `read_values`
   permissions on all of it's constituent observations. A partial aggregate value will
   be returned to users.

6. Create permissions are only effective within the organization that they are
   created. When users create metadata, the metadata is owned by that user's
   organization. User's that are granted `create` permissions outside their
   organization will not be allowed to create new metadata, they will require
   `create` permissions from their own organization.
