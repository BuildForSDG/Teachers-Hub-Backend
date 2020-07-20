# Teachers Hub Backend

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8f00e10e684b43ac812feba82c89b2da)](https://app.codacy.com/gh/BuildForSDG/Team-273-Backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDG/Team-273-Backend&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/BuildForSDG/Teachers-Hub-Backend.svg?branch=develop)](https://travis-ci.org/BuildForSDG/Teachers-Hub-Backend)
[![Coverage Status](https://coveralls.io/repos/github/BuildForSDG/Teachers-Hub-Backend/badge.svg)](https://coveralls.io/github/BuildForSDG/Teachers-Hub-Backend)

## About

The purpose of this project is to provide inclusive, equitable and quality education for all people, globally. Its targets to span a variety of challenges related to inclusion of marginalized populations at multiple levels of education and in the workforce.

This project addresses the following SDG targets:

-   Increased supply of qualified teachers in the community
-   Increased networking among teachers
-   Training of teachers by more qualified bodies
-   Accessibility to employment opportunities

## Usage

### AUTHENTICATION

| REQUEST | ROUTE              | FUNCTIONALITY    |
| ------- | ------------------ | ---------------- |
| POST    | api/v1/auth/login  | Logs in a user   |
| POST    | api/v1/auth/signup | Registers a user |

### COURSES

| REQUEST | ROUTE                                                | FUNCTIONALITY                             |
| ------- | ---------------------------------------------------- | ----------------------------------------- |
| GET     | api/v1/courses                                       | Fetches all courses                       |
| GET     | api/v1/courses/&lt;course_id>                        | Fetches a single course                   |
| POST    | api/v1/courses                                       | Adds a new course                         |
| PUT     | api/v1/courses/&lt;course_id>                        | Updates a single course                   |
| DELETE  | api/v1/courses/&lt;course_id>                        | Deletes a course                          |
| POST    | api/v1/courses/&lt;course_id>/enroll                 | Enroll for a course                       |
| POST    | api/v1/courses/&lt;course_id>/modules                | Add module to course                      |
| GET     | api/v1/courses/&lt;course_id>/modules                | Fetch modules on a course                 |
| GET     | api/v1/courses/&lt;course_id>/modules/&lt;module_id> | Fetch module content for a single module  |
| POST    | api/v1/courses/&lt;course_id>/modules/&lt;module_id> | Create module content for a single module |
| GET     | api/v1/courses/enrolled                              | Fetch courses enrolled for                |
| GET     | api/v1/courses/enrolled/<course_id>                  | Check enrollment status                   |

### PARTNERS

| REQUEST | ROUTE                                     | FUNCTIONALITY                 |
| ------- | ----------------------------------------- | ----------------------------- |
| GET     | api/v1/organizations                      | Fetches all organisations     |
| GET     | api/v1/organizations/&lt;organization_id> | Fetches a single organisation |
| POST    | api/v1/organizations                      | Adds a new organisation       |
| PUT     | api/v1/organizations/&lt;organization_id> | Updates a single organisation |
| DELETE  | api/v1/organizations/&lt;organization_id> | Deletes an organisation       |

### USERS

| REQUEST | ROUTE               | FUNCTIONALITY            |
| ------- | ------------------- | ------------------------ |
| GET     | api/v1/auth/profile | Fetches a user's profile |

### BLOG

| REQUEST | ROUTE                           | FUNCTIONALITY        |
| ------- | ------------------------------- | -------------------- |
| GET     | api/v1/articles                 | Fetch all articles   |
| POST    | api/v1/articles                 | Add New Article      |
| DELETE  | api/v1/articles/&lt;article_id> | Delete an article    |
| PUT     | api/v1/articles/&lt;article_id> | Update an article    |
| GET     | api/v1/articles/&lt;article_id> | Fetch single article |

### COMMUNITY QUESTIONS

| REQUEST | ROUTE                                     | FUNCTIONALITY                 |
| ------- | ----------------------------------------- | ----------------------------- |
| GET     | api/v1/questions                          | Fetches all organisations     |
| GET     | api/v1/questions/&lt;question_id>         | Fetches a single question     |
| POST    | api/v1/questions                          | Adds a new question           |
| PUT     | api/v1/questions/&lt;question_id>         | Updates a single question     |
| DELETE  | api/v1/questions/&lt;question_id>         | Deletes a question            |

## Setup

1.  You should have **Python 3.5+** and **git** installed.
2.  Inorder to get started, clone this repository using `git clone https://github.com/BuildForSDG/Teachers-Hub-Backend.git`
3.  Change in the repository directory `cd teachers-hub-backend`
4.  Set up a virtual environment by running `python3 -m venv <name_of_the_environment>`
5.  Install requirements by running `pip install -r requirements.txt`
6.  Start the flask server by running `python run.py`
7.  Navigate to `http://localhost:8000` in the browser to view the api.
8.  Alternatively, open [postman](https://www.postman.com/) to test the url endpoints

## Postman Setup for API Testing

Open this collection in postman by clicking the button below:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/6858a8faf4f7944f643a#?env%5Bherokuenv%5D=W3sia2V5IjoiYWRtaW5fdG9rZW4iLCJ2YWx1ZSI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUpwWVhRaU9qRTFOelUyTkRBME1ETXNJbTVpWmlJNk1UVTNOVFkwTURRd015d2lhblJwSWpvaVpqUXdOakF5TXpjdFlqWXlZaTAwWkRFNExXRTNZek10TnpRMllUSTVNMkl5Tnpoa0lpd2laWGh3SWpveE5UYzFOekl6TWpBekxDSnBaR1Z1ZEdsMGVTSTZleUoxYzJWeWJtRnRaU0k2SWtGa2JXbHVJaXdpY205c1pTSTZXeUpCWkcxcGJpSmRmU3dpWm5KbGMyZ2lPbVpoYkhObExDSjBlWEJsSWpvaVlXTmpaWE56SW4wLnBxS0VtX3JLX2pDSDJXTWp5UUZYNGNwNlFydGlvdUFnUnZZeGxrdkFGOGsiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InRva2VuIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlfV0=)

If you're using Postman for testing the REST api, you can use the following setup:

-   Make sure you have an environment set for your collection.

-   POST to `http://localhost:5000/api/v1/auth/signup` and add your details to sign up

-   POST to `http://localhost:5000/api/v1/auth/login/` to obtain token

-   Paste this code in Tests which will save the token to the environment.

        var jsonData = JSON.parse(responseBody);
        postman.setEnvironmentVariable("token", jsonData.token);

-   In the Authorization section of your subsequent posts, set the Authorization type as Bearer Token and add {{token}}
    in the token section

## Heroku deployment

View the deployed application here [Teachers Hub API](https://teachershub-backend.herokuapp.com/)

## Authors

-   [Daisy Macharia](https://github.com/daisymacharia) - Mentor
-   [Maria Nanfuka](https://github.com/mariamiah) - TTL
-   [Akiyo Fidel](https://github.com/drfidel)
-   [Lubwama Benjamin](https://github.com/lubwamabenja)
-   [Kizza Samuel](https://github.com/skizza8)
-   [Ainembabazi Kirabo](https://github.com/AineKiraboMbabazi)
-   [Jimmy Were](https://github.com/jwere)
-   [Simon Peter Ojok](https://github.com/simonojok19)

## LICENSE

MIT
