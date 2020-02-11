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
