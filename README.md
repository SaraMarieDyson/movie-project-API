# Sara's Training Project

The goal of this project is to get you up to speed on some of the things that you are struggling with, as well as get you comfortable working to customer requests. It is expected that you will work on this regularly, and try to get things completed as if the "client" were actually expecting you to complete the work.

## Some things that we want you to work on:

* General Django skills, including working with a database and the ORM
* Be comfortable working through specs to come up with some value to the client
* Be comfortable working independently, and how to ask for help effectively

So first up is the project, after which we will talk about the technical side.
## Movie Watch List Site

I want you to create me a simple site that will allow people to create and share movie watch lists. People will be able to:

* Create and manage lists of movies that they want to watch
* Share the lists with other people
* Leave reviews and ratings about movies they have watched
* Also, we shouldn't gather information that we don't need, but it would be nice if people could have a profile about themselves.

Along side movies, I want people to be able to look up actors and actresses and see what movies they have been in. This is a good way for people to find new movies that they might be interested in. When it comes to actors, people will be able to:

* Find actors that have been in movies that they have watched
* See movies that an actor has been in
* Leave reviews of an actor

To run this website, I need to be able to manage the data in it. So I want to be able to do the following things:

* Create and manage movie records
* Create and manage actor and actress records
* Write blog posts about interesting movies and actors
* Manage accounts, including creating new ones and banning people that are causing problems

There are a few things that I think are important that should be kept in mind whilst doing this work:

* I want regular updates to the site. I don't mind if I get simple versions of things as long as I am getting new stuff regularly
* I want security. People should be able to have their own account, and no one else should be able to access it.
* I should be able to do anything that a normal person can do with the site, but they should not be able to access the management stuff that I have

## Technical Consideration

To build this you should use the following:

* Django 1.11.* and Python 3.6, because that is what we are using. No Django Rest Framework for this
* Basic HTML and CSS
* Git and GitLab

We should be able to pull this down and run it locally as you work along, but we will also look at actually deploying this somewhere at some point. Some other things to think about

* Don't look to use any complicated things like docker, vagrant, or vms. Simple virtualenv setup for local dev
* Don't worry about a more powerful DB like Postgres. Just use Sqlite for starters
* Make the frontend simple. No Javascript, just HTML. Dont even worry too much about the CSS.
* When dealing with the management side of things, feel free to use the Django admin stuff

> ### A Note On Testing

> Yes you should test things. That is a skill that is worth being good at. However, to start this project off, it is more relevant to get to grips with the skills of building the Django site then the testing, so don't worry if you don't have tests for everything.

## Approach

So how are we going to actually do the work? It would be best if you do some work regularly on this. At least the Thrusday back at Catalyst, and potentially some time each day as well, maybe an hour. We will work in one week chunks, aiming to get something new done by the end of the week. We will do a bit of work to come up with what the work will be each Monday. You will need to write up tickets that define the actual work that you are going to do, and we can look at this at the end of the week and see how it went.