# Ecommerce-Zone

Welcome to Ecommerce-Zone. We have watchs of all brands and accessories for you and your loved ones. Explore the local neighborhood in style & comfort on our watchs.

![Ecommerce-Zone](https://gomosorbucket.s3.amazonaws.com/1_Gedn9fj.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYS2NU2KI4WCNJTEX%2F20240114%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240114T090443Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=1a368d8a1cd99e7229f979f0e8bbd17aca8b8c5010e5e2fc1040760d17417684)

Ecommerce-Zones is a responsive Django web application that allows users to view information about the watcah shop.

Ecommerce-Zones is hosted in the Digital Ocean Cloud for public use.

Click the link below to access Ecommerce-Zones and the watch collection.

[Access Ecommerce-Zone's](https://django-ecom-zone-1-70efee035f25.herokuapp.com/)

## Table Of Contents

- [Ecommerce-Zones](#robert-s-watch)
  * [Ecommerce-Zones Tech Stack](#robert-s-watch-tech-stack)
  * [Ecommerce-Zones Features & Goals](#robert-s-watch-features---goals)
    + [watch Guest Goals](#watch-guest-goals)
    + [watch Customer Goals](#watch-customer-goals)
    + [watch Employee Goals](#watch-employee-goals)
    + [watch Site Administrator Goals](#watch-site-administrator-goals)
  * [Ecommerce-Zones User Stories](#robert-s-watch-user-stories)
    + [watch Guest User Stories](#watch-guest-user-stories)
    + [watch Customer User Stories](#watch-customer-user-stories)
    + [watch Employee User Stories](#watch-employee-user-stories)
    + [watch Site Administrator User Stories](#watch-site-administrator-user-stories)
  * [User Interface Design](#user-interface-design)
    + [Theming And Colors](#theming-and-colors)
  * [Ecommerce-Zone' Store Pages](#robert-s-watch-store-pages)
    + [Home Page](#home-page)
    + [About Page](#about-page)
    + [Accessories Page](#accessories-page)
    + [Login Page](#login-page)
    + [Register Page](#register-page)
    + [Contact Page](#reserve-watchs-page)
    + [Search watchs Page](#manage-watchs-page)
  * [Security For Ecommerce-Zones](#security-for-robert-s-watch)
    + [Super Admin Users](#super-admin-users)
    + [Standard Authenticated Users](#standard-authenticated-users)
  * [Known Bugs](#known-bugs)
  * [Ecommerce-Zone's Deployment](#robert-s-watchs-deployment)
    + [Ubuntu Linux Server](#ubuntu-linux-server)
    + [Deploy Postgres Database](#deploy-postgres-database)
    + [Deploying Ecommerce-Zone'](#deploying-robert-s-watch)
    + [Preview Ecommerce-Zone's](#preview-robert-s-watchs)
  * [Credits](#credits)
  * [Quick Start Installation](#quick-start-installation)

## Ecommerce-Zones Tech Stack

Ecommerce-Zone's is built with the following technologies.

* `hosting` { digital-ocean ubuntu }

    the app is hosted on a linux server that runs the Ecommerce-Zone's source code.

* `database` { postgres pgadmin4 }

    the app uses a postgres database. pgadmin is used to monitor and manage the postgres database.

* `backend` { django4 } 

    the app backend is django mvc.

* `interface` { html bootstrap bootswatch liquid }

    the app user interface is built html pages customized with liquid templating to render backend content.

## Ecommerce-Zones Features & Goals

![Ecommerce-Zone Home](/docs/screenshots/home.png)

### watch Guest Goals

Features for end users of the Ecommerce-Zone's django application:

    [`store info`] Guests can see watch store information

    [`store info`] Guests can see watch accessories

    [`accounts`] Guests can register a new account to reserve watchs

    [`accounts`] Guests can login in to existing account to reserve watchs

### watch Customer Goals

    [`watch`] Authenticated customers can view reservation status of all watchs

    [`watch`] Authenticated customers can reserve a watch

    [`watch`] Authenticated customers can cancel their reserved watch reservations

### watch Employee Goals

Features for employee users of the Ecommerce-Zone's django application:

    [`crud`] Can manage watchs in the system

    [`crud`] Can manage watch reservations in the system

### watch Site Administrator Goals

Features for site administration users of the Ecommerce-Zone's django application:

    [`cloud`] Can manage the resources in the digital ocean cloud

    [`linux`] Can manage the system processes on the linux server

    [`manage.py`] Can manage the store employee users in the django system

## Ecommerce-Zones User Stories

### watch Guest User Stories

    As a watch guest i can see information about the watch store so that i can make an informed decision about watchs

    As a watch guest i can see watch accessories so that i can know my options for accessories for my watch

    As a watch guest i can create a new account with Ecommerce-Zones so that i can manage watch

    As a watch guest i can log in an existing account on Ecommerce-Zones so that i can reserve a watch

### watch Customer User Stories

    As a watch customer i can view the reservation status of all watchs so that i can select a watch available for purchase

    As a watch customer i can reserve an available watch so that i can use this watch as a later time

    As a watch customer i can cancel a previously made watch reservation so that i can return a watch i do not need

### watch Employee User Stories

    As a watch employee i can manage the watchs in the systems so that i modify watchs as needed

    As a watch employee i can manage the watch reservations in the system so that i can get see which watchs are rented

    As a watch employee i can return a customer's watch so that assist our customer with watch reservations

### watch Site Administrator User Stories

    As a watch site administrator i can manage the digital ocean cloud resources so that servers can be turned on and off

    As a watch site administrator i can manage the linux server processes so that databases and applications can be turned on and off

    As a watch site administrator i can manage the superadmins in the django application so that store employees can be created

## User Interface Design

Ecommerce-Zone's uses standard html pages with liquid template.

below are details about the interface, it's design, and considerations.

### Theming And Colors

Colors for Ecommerce-Zone's were chosen from options on bootswatch.

Bootswatch provides the color theming used across the application.

Ecommerce-Zone's uses the `lumen` theme set.



## Ecommerce-Zone' Store Pages

### Home Page

the home page is the initial landing page for Ecommerce-Zone's. the home provides text about Ecommerce-Zone's and what we offer.

![home page](/docs/screenshots/home.png)

### About Page

the about page provides detail about Ecommerce-Zone's. the about page has a call to action for the user to reserve a watch.

![about page](/docs/screenshots/about.png)

### Accessories Page

the accessories page lists a static collection of accessories for the Ecommerce-Zone users. the accessories page has a call to action for the user to reserve a watch.

![accessories page](/docs/screenshots/accessories.png)

### Login Page

the login page is a standard login form. the user provides their username and password. the login page provides a call action to sign up for a new account.

![login page](/docs/screenshots/login.png)

### Register Page

the register page is a standard register form. the user provides their username and password. the register page provides a call action to log in with an existing account.

![register page](/docs/screenshots/register.png)

### Contact Page

the reserve page allows the user to see each of the watchs in the store and it's rentail availability. the reserve page allows the user to reserve a watch listed as available. the reserve page allows the users to cancel a currently reserved watch owned by them.

![reserve page](/docs/screenshots/reserve.png)

### Search watchs Page

the manage watchs page allows a super user to see each of the watchs in the store and it's rentail availability. the manage watchs page allows a super user to return a reservation made by a customer.

![manage page](/docs/screenshots/manage.png)

## Security For Ecommerce-Zones

Ecommerce-Zones has a few simple security rules.

### Super Admin Users

    [`superadmins`] only superadmins can manage watchs and accounts

    [`superadmins`] only superadmins may return other user's

### Standard Authenticated Users

    [`authenticated`] only authenticated users can reserve a watch

    [`authenticated`] only authenticated users can their own

    [`authenticated`] authenticated user sessions are invalidated after two minutes of inactivity and the user must re-authenticate

## Agile Project Management

Ecommerce-Zone's has an agile project tracking board with each of the user stories and their current progress.

Click the link below to view the agile board.

[Agile Project Management](/docs/agile.md)

## Known Bugs

the following are bugs currently known within the Ecommerce-Zone's application.

### New Accounts Can Not View watchs To Rent

	on the first login for a new user, there are no watchs available to view or reserve.

	Solution #1: The new user has to log out and then log back in. Then the watchs are available to view and manage.

	Solution #2: The new user needs to manually click on the 'reserve watch` link.

## Ecommerce-Zone's Deployment

Ecommerce-Zone's is hosted on an ubuntu linux server in the `Digital Ocean` cloud.

### Ubuntu Linux Server

The Ubuntu Linux Server has the following specs:

    ip address / 104.248.100.154

    os / ubuntu linux 22.04

    ram / 2 GiB

    cpu / 1 vCPU

    disk / 50 GiB

### Deploy Postgres Database

A postgress database is used for backend storage.

The postgress database uses docker compose to run:

```yaml
version: "3"

services:

    roberts-watch-postgres:

        container_name: roberts-watch-postgres
        
        image: postgres:14.1-alpine

        restart: always

        user: root

        environment:

            - POSTGRES_USER=robertswatc

            - POSTGRES_DB=robertswatc

            - POSTGRES_PASSWORD=roberts!watch

        ports:

            - "5432:5432"

        volumes: 

            - ./volume/postres:/var/lib/postgresql/data
 
    roberts-watch-pgadmin4:

        container_name: roberts-watch-pgadmin4

        user: root

        image: dpage/pgadmin4
        
        restart: always

        ports:
        
            - "5480:80"
            
        environment:
        
            PGADMIN_DEFAULT_EMAIL: robert@robertswatc.com
            
            PGADMIN_DEFAULT_PASSWORD: roberts!watch

        volumes:
        
            - ./volume/pgadmin4:/var/lib/pgadmin            
```

running the docker-compose script to start the database.

```bash
docker-compose up -d
```

see the running docker containers on the linux server.

```bash
docker ps
```

### Deploying Ecommerce-Zone'

The Ecommerce-Zone's application is executed by pulling the Ecommerce-Zone's source code from GitHub and executing the `quick-start.sh` script using the linux terminal.

get the code from github.

```bash
git clone https://github.com/Gomsur/roberts-watch.git
```

enter the repo directory.

```bash
cd roberts-watch
```

```bash
sudo nohup ./quick-start.sh &
```

nohup runs the application in the background after disconnecting from the terminal. if you don't put nohup, then the app closes when you disconnect.

### Preview Ecommerce-Zone's

![Ecommerce-Zone Home](/docs/screenshots/home.png)

Ecommerce-Zones is deployed and available for usage.

Click the link below to access Ecommerce-Zones.

[Access Ecommerce-Zone's](http://104.248.100.154/)

## Credits

The Ecommerce-Zone' application was build w/ help from the following resources across the internet.

| website | how the site helped |
|---------|---------------------|
|[Bootswatch](https://bootswatch.com/)|bootstrap compatible prebuild color theming and css|
|[Digital Ocean](https://www.digitalocean.com/community/tutorials)|cloud server hosting and tutorials|
|[Internet Tutorials](/docs/tutorials.md)|various tutorials from the internet with how-to help and information|
|[Stock Imagery](/docs/attribution.md)|free stock imagery from the internet, with attribution.|
|[TOC Generator](https://ecotrust-canada.github.io/markdown-toc/)|github wiki toc generator.|

## Quick Start Installation

You can run Ecommerce-Zone's at home.

Follow the instructions below on an Ubuntu Linux server.

[Quick Start Guide](/docs/quick-start.md)
