# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

We want to work on the "Metadata about all RTS TV and Radio Broadcasts from 1935 until now" dataset. Due to its timespan, it is really sutable to analysed evolution of social habits and themes during the 20th century. This type of structure should work out well to tell a story by linking real life events with the RTS broadcasts. ...

# Research questions
A list of research questions you would like to address during the project.

- How long does a program last ? What are the influence factors ? Is it linkable to the audience type ?
- How has the gender distribution evolved from 1935 ?
- What/Who are the dominant themes/characters for the different periods ?

# Dataset
The dataset is accessible by queries on https://api.srgssr.ch/rts-archives-public-api/apis/get/archives in the JSON format, it is also continuously updated. All entries seem to be formatted the same way, in general we get the basic information (title, source, genre, presentator, duration, media type, publication date, etc...) and sometimes we get additionnal informations like the theme or a full list of related persons. We would like to enrich this dataset with
- another article retriever like spinn3r
- a way of findgin the gender of the cited persons.
SUGGESTION GUYS ! => Use the "Historical Dictionary of Switzerland" that contains a list of important themes, geography, families and biographies in Switzerland at http://www.hls-dhs-dss.ch/opendata/.

# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

- get familiar with the data and JSON data handling
- guess the pesons' gender
- fill missing themes from title, person, media type, etc...
- /!\ join with the Dictionary of Switzerland
- group data by periods and find dominant features
- ... 

# Questions for TAs
Add here some questions you have for us, in general or project-specific.

- Is it possible to have access to spinn3r ?
- 