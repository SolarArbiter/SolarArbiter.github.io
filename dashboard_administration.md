---
layout: dashboard_admin
permalink: /documentation/dashboard/administration
---

# Dashboard Administration
{: .anchor}

This section describes the user interface for managing data acces through
roles and permissions. An accompanying workflow description can be found in the
[Data Access Workflow Document](/data-access-workflow/).

User, permission and role administation can be accessed by clicking the **User
Administration** link in the Account menu in the top right corner of the site.
    <img class="my-3" src="/images/admin_menu.png"/>



Note that these menus are meant to assist organization administrators in viewing
and managing permissions, and users without admin privileges may not see anything
on these pages.


### Users
{: .anchor}

Unlike other types of data, *Users* are only created through the signup process
outlined in <a href="#getting-started">getting started</a>.

-   The *Users* tab will list the users you have access to administer or view.
	<img class="my-3" src="/images/users.png"/>


-	Clicking on an individual user will list information about the user and their
    roles. Roles may be revoked from the user by clicking the *Remove* link on the
    far right of each row of the listing.
    <img class="my-3" src="/images/user.png"/>


### Create New Role
{: .anchor}

1.  Navigate to the roles listing with the *Roles* tab of the admin menu. This page
    will list all of the Roles you have access to administer or view. 
    <img class="my-3" src="/images/roles.png"/>

2.  Click the *Create new Role* button. You will be prompted for a name and description
    of the role and a list of permissions the role should have. Check the boxes next 
    to each permission that the role should grant and click submit.
    <img class="my-3" src="/images/role_form.png"/>
    
-   *Created Role pages*

	Clicking on an individual Role will list information about it and the permissions
    associated with it. Use the tabs below the metadata section to switch between the
    list of permissions on the role and a list of users the role has been granted to.

    *Role permissions listing*
    <img class="my-3" src="/images/role.png"/>
    *Role users listing*
    <img class="my-3" src="/images/role_users.png"/>


### Create New Permission
{: .anchor}
1.	Navigate to the Permissions listing with the *Permissions* tab of the admin menu.
    This page will list all of the Permissions you have access to administer or view.
    <img class="my-3" src="/images/permissions.png"/>

2.  Click on the data type you would like to create a permission for in the "Create new
    Permission" box. You will be prompted for a description of the permission, the
    action the permission allows and a list of objects. Click the checkboxes for each
    object that the permission should allow its action on. Selecting *Applies to all*
    will cause the permission to affect all current and future objects of the
    permission's type.

    *Permission form for observation permsission*
    <img src="/images/permission_form.png"/>

-	*Created Permission pages*
    Clicking on an individual Permission will list information about it and the objects
    it applies to.
    <img class="my-3" src="/images/permission.png"/>

### Data Sharing

#### Granting roles to a user
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


#### Revoking roles from a user
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
