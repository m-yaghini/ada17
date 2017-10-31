# “The TV Mirror”: Evolution of Swiss Radio/TV Broadcasts in The Course of The 20th Century

## Abstract
The popular media is an (imperfect) mirror of the society. In this project, we want to study the effect of social trends and events of the 20th century on TV/Radio broadcasts. The 20th century saw the invention and ubiquity of the broadcast media: first radio and then television. At the same time, many international events (World Wars, the rise and the fall of Communism, the formation of European Union, etc) as well as national incidents (sexual revolution of 1960's, the establishment of women voting right) took place in this period. All of these events had profound impact on the society, and as a result on broadcast media such as TV and Radio. Having access to a wealth of information about TV/Radio emissions all the way from 1930's until today, we believe we can track these events and gain unique insights into the evolution of Swiss society. To this end, we are going to mainly use the RTS dataset. However, to complement our analyses, we will potentially make use of Spinn3r, different Swiss Open datasets, and Wikimedia data as well.

## Research questions
A list of research questions you would like to address during the project.
1. What type of programs were produced in each time period? 
2. What/Who are the dominant themes/characters for the different historical periods ?
3. General evolution of the emissions: How long does a show run (how many seasons)? What are the influence factors ? Is it linkable to the audience type ?
4. How did the media react to the women's voting right’s referendum and its result, as well as to the sexual revolution of 1960’s?
5. How has the distribution of genders for anchors and presenters evolved over the course of the years? Was there a gender bias? If yes, how is it changed?
Additionally, if time permits, we would also like to analyse the following questions as well:
6.  How did the production evolved with respect to important national and international affairs? 
7.  What was the impact of World War II or the Cold War on the broadcasts? How did the themes changed? What new programs were introduced? 
8. (Using and comparing other datasets) How biased is the RTS? Specifically, is there any statistical indication that it is more right or left leaning? How does the answer to these questions evolve and change over time?
9. For the popular shows: what is the audience/ person-type (Education level, age range, social rank, etc.)? 

## Datasets
The dataset is accessible by [queries](https://api.srgssr.ch/rts-archives-public-api/apis/get/archives) in the JSON format, it is also continuously updated. All entries seem to be formatted the same way, in general we get the basic information (title, source, genre, presenter, duration, media type, publication date, etc...) and sometimes we can get other information such as the theme or a full list of related persons. Metadata about all RTS TV and Radio Broadcasts from 1935 until now. The dataset includes [more than 350'000 shows](https://opendata.swiss/en/dataset/rts-tv-and-radio-broadcasts) and covers all RTS audio and video channels : RTS 1, RTS 2, La Première, Espace 2, Couleur 3, … Data comes from three distinct systems: RTS Website CMS, TV Archives System and Radio Archives System. 

We would like to combine and enrich this dataset with other data sets provided to us, including (tentatively)
- The Spinn3r Dataset
- Swiss Open Data sets, and in particular, the "Historical Dictionary of Switzerland" that contains a list of important themes, geography, families and biographies in Switzerland at http://www.hls-dhs-dss.ch/opendata/

## A list of internal milestones up until project milestone 2
- **Get familiar with the data** via an exploratory data analysis, discover its strengths and limits : find out what questions we can *actually* answer using the data given to us. Also find the dominant features. 
- **Data Collection and Processing** since the data is also hosted on the ADA cluster, check whether we can avoid queries and work directly on the whole data set using *Spark*.
- **Data Correction and/or Augmentation** Find out what are we missing in the data and how we can fill the missing values. Do we need to augment our datasets using Spinn3r and Wikidata among others?
- **Rankings** Find if any TV ratings data is available, and find out if and how it can be integrated in the analyses.

### Short term goals:
- Find a way to guess the gender of presenters.
- Fill missing themes from title, person, media type, etc...
- Divide and distribute the tasks among team members. 

## Questions for TAs
- Since Spinn3r is a commercial dataset, how can we gain access to it ?
- In general how can we gain access to the datasets that are hosted on the ADA cluster? 
- What do you think about our problem statement ? Do you think its too broad or too narrow? Do you think we can make a good data story out of our analysis? 
- We proposed a long list of questions. At the same time, we are aware of the page (and time) limit. Is there any question that you find infeasible to answer? 
- Can we use TV ratings data? This could prove essential to our analyses of TV shows changing popularity over the time, as indicative of social change.
- In case you find a question interesting but also think that another formulation of the same question would be even more interesting to research, we would very much appreciate it if you tell us.