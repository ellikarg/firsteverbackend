# Stories

## Project goals

## Table of contents
- [Stories](#stories)
  * [Project goals](#project-goals)
  * [Table of contents](#table-of-contents)
  * [Planning](#planning)
    + [Data models](#data-models)
    + [**Notification**](#--notification--)
  * [API endpoints](#api-endpoints)
  * [Frameworks, libraries and dependencies](#frameworks--libraries-and-dependencies)
    + [django-cloudinary-storage](#django-cloudinary-storage)
    + [dj-allauth](#dj-allauth)
    + [dj-rest-auth](#dj-rest-auth)
    + [djangorestframework-simplejwt](#djangorestframework-simplejwt)
    + [dj-database-url](#dj-database-url)
    + [psychopg2](#psychopg2)
    + [python-dateutil](#python-dateutil)
    + [django-recurrence](#django-recurrence)
    + [django-filter](#django-filter)
    + [django-cors-headers](#django-cors-headers)
  * [Testing](#testing)
    + [Manual testing](#manual-testing)
    + [Python validation](#python-validation)
    + [Resolved bugs](#resolved-bugs)
      - [Bugs found while testing the API in isolation](#bugs-found-while-testing-the-api-in-isolation)
      - [Bugs found while testing the React front-end](#bugs-found-while-testing-the-react-front-end)
    + [Unresolved bugs](#unresolved-bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Planning


### Data models


### **Notification**
The Notification model represents user notifications. Currently these are implemented for invitations and changes to calendar events, however further notification types could be implemented in the future to compliment additional features.

Notifications are created programatically when a new event is created or details of an existing event changed - there is no API endpoint to directly create a new notification.
Notifications have a many to one relationship with the User model to record who the notification is for, and a one to many relationship to the Event model to record which event the notification relates to. The `event` field can have a value of `None` so that it could be utilised for non-event related functionality in the future.

Users can only access and delete their own notifications.

## API endpoints
| **URL** | **Notes** | **HTTP Method** | **CRUD operation** | **View type** | **POST/PUT data format** |
|---|---|---:|---|---:|---|
|  |  |  |  |  |  |
| **Custom user <br>account endpoints** |  |  |  |  |  |
|  |  |  |  |  |  |

Table generated using https://www.tablesgenerator.com/markdown_tables/load

## Frameworks, libraries and dependencies


### django-cloudinary-storage

### dj-allauth

### dj-rest-auth

### djangorestframework-simplejwt

### dj-database-url

### psychopg2

### python-dateutil

### django-recurrence

### django-filter

### django-cors-headers

## Testing

### Manual testing

### Python validation

### Resolved bugs

#### Bugs found while testing the API in isolation

#### Bugs found while testing the React front-end  

### Unresolved bugs

## Deployment

## Credits

In addition, the following documentation was extensively referenced throughout development:

- [Django documentation](https://www.djangoproject.com)
- [Django Rest Framework documentation](https://www.django-rest-framework.org)
- [django-filter documentation](https://django-filter.readthedocs.io/en/stable/)
- [django-recurrence documentation](https://django-recurrence.readthedocs.io/en/latest/)
- [Python datetime documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil documentation](https://dateutil.readthedocs.io/en/stable/index.html)
