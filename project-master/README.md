# “The TV Mirror”: Evolution of Swiss Radio/TV Broadcasts in The Course of The 20th Century

## Abstract
The popular media is an (imperfect) mirror of the society. In this project, we want to study the effect of social trends and events of the 20th century on TV/Radio broadcasts. The 20th century saw the invention and ubiquity of the broadcast media: first radio and then television. Having access to a wealth of information about TV/Radio emissions all the way from 1930's until today, we believe we can track these events and gain unique insights into the evolution of Swiss society. To this end, we are going to mainly use the RTS dataset. However, to complement our analyses, we will potentially make use of Spinn3r, different Swiss Open datasets, and Wikimedia data as well.

## Research questions

1. What type of programs were produced in each time period? What/Who are the dominant themes/characters for the different historical periods ?
2. General evolution of the emissions: How long does a show run (how many seasons)? What are the influence factors ? Is it linkable to the audience type ?
3. How did the RTS coverage of important social phenomena like the sexual revolution, women's voting right, and terrorism evolved over time.
4. How has the distribution of genders for anchors and presenters evolved over the course of the years? Was there a gender bias? If yes, how is it changed?
5. How has the RTS covered the news around the globe ? How equitable was the coverage? Is there any noticeable bias?
6. How has RTS coverage evolved across the years?

## Datasets

The dataset is accessible by [queries](https://api.srgssr.ch/rts-archives-public-api/apis/get/archives) in the JSON format, it is also continuously updated. All entries seem to be formatted the same way, in general we get the basic information (title, source, genre, presenter, duration, media type, publication date, etc...) and sometimes we can get other information such as the theme or a full list of related persons. Metadata about all RTS TV and Radio Broadcasts from 1935 until now. The dataset includes [more than 350'000 shows](https://opendata.swiss/en/dataset/rts-tv-and-radio-broadcasts) and covers all RTS audio and video channels : RTS 1, RTS 2, La Première, Espace 2, Couleur 3, … Data comes from three distinct systems: RTS Website CMS, TV Archives System and Radio Archives System.


## Group member contribution
Leonardo
- Data collection and preparation
- Compute term occurrences per year
- Wordcloud visualization of the term occurrences per year
- Setup and manage jekyll blog
- Poster Design


Sina
- Initial Investigation and project proposal
- Obtaining genders of all names in dataset using external JSON service
- Analysis and presentation on gender inequalities
- Analysis and presentation on major social phenomenas
- Poster Design


Mohammad
- Handling locations in the data
- Extracting locations' exact coordinates using Google Geolocating API
- Producing Heat Maps for news occurrences
- Producing the interactive heatmap visualization in JavaScript
- Poster Design
