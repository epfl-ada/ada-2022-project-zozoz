# Is John the reason for the success? A deep dive of the temporal changes in movie


## Abstract 📝 [Aamir]
The CMU movie [dataset](http://www.cs.cmu.edu/~ark/personas/) comes from around 80k freebase movie entries and 42,306 movie plot summaries extracted from Wikipedia. We want to assess the reasons behind a successful movie and their evolution over time. Success has different dimensions and we are using the box office and IMDB ratings to cover two important ones. The analysis will be performed while taking into account different attributes such as genres, actors, directors, character names and so on. By using regular statistical methods and ML tools, the goal is to provide a robust analysis and come with a framework that allow us to draw meaningful conclusions. We want to see if we can create a blueprint for the next big hit.

## Structure of the repository

We splited our work in several folders for clarity. 

In the `/data` folder you can find several subfolders containing the [original dataset](/data/MovieSummaries), the datasets used for [wikipedia](/data/Wikipedia) and [IMDb](/data/imdb) integration and the [data formated](/data/generated) using our processing pipeline.

The `/imgs` folder contains the graphic displayed in this document.

Finally the `/src` folder contains all the code produced for this milestone. It contains two subfolders. The `/src/utils` folder contains the code with the helpers functions and notebook for data creation. The `/src/eda` folder contains notebooks dedicated to the data analysis. The first [notebook](/src/eda/data_inspection.ipynb) is handling the general data description and analysis. Whereas the second [notebook](/src/eda/initial_time_series_analysis.ipynb) focuses on analysis to support our research questions. Finally the `/src` folder contains a [notebook](/src/create_data.ipynb) that is used to generate our data in correct format (see below for more extensive explanations).
 
---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Research Questions">Research Questions</a></li>
    <li><a href="#Proposed additional datasets">Proposed additional datasets</a></li>
    <li><a href="#Run-the-code">Methods</a></li>
      <ol>
        <li><a href="#data-model">Data Model</a></li>
        <li><a href="#data-wrangling">Data Wrangling</a></li>
        <li><a href="#data-analysis">Data Analysis</a></li>
      </ol>
    <li><a href="#proposed-timeline">Proposed Timeline</a></li>
    <li><a href="#organisation">Organisation within the team</a></li>
  </ol>
</details>

---
## Research Questions 🧠
- What makes a movie successful across the years?
    - What are the key characteristics, for example director, actors, genres or character names?
- Can we cluster successful movie plots, and from the clustering extract meaningful reason for the success?
- Are the reasons for success the same across countries and time?
- Can we create our own blueprint the next big hit?
- Does the popular culture trends linked to the overall movie success.

## Proposed additional datasets 📠 
Even though the CMU dataset is quite complete, we used external ressources in order to fill-in missing information and increase the depth of our analysis. 
As we are interested in temporal changes, we need to have the release date for the maximum number of movie possible. To do so we will use the Wikipedia website. 
The other aspect that we want to cover is linked with the popularity of movies. This information and many more can be retrieved using the public [IMDB data](https://www.imdb.com/interfaces/). This datasets allow us also to investigate deeper the place of actors and characters and ask question about the technical crew of movies such as directors, music producer etc.
- Wikipedia
  - Wikipedia is an incredible source of information but the task of retrieval is sometimes cumbersome. In the CMU dataset, we have the wikipedia page ids for all the movies, which allow us to grep data using well established libraries. We used the wikipedia python library to retrieve the page content for many movies with missing release date, as it was our primary goal. The retrieval is not perfect nor complete as the structure of the wikipedia pages for different movie is not consistent and we were not able to retrieve the page for several ids. In practice we were able to get the release date for around 5k movies out of the 8k with missing release date in the CMU dataset.
  Note that we also retrieved many more information (directors, plot summary, etc) from the wikipedia pages but we do not plan to use them as they are more difficult to parse than the IMDB data.
For the code organisation, you can find the code for the grepping of the data in the ... folder. It produces three different files. Two keep track of the movies for which retrieval was impossible () and ... is the important file containing the wikipedia data for 5k movies.
- IMDb
  - To extend our analysis we choose to incorporate a well known movie database to our CMU dataset, IMDb. It allows us to extract popularity of movies based on user rating but also much more information on the actors/actresses, characters and the movie crews. Each movie in IMDB is referenced using a unique page id. Our main task was to find a mapping between our wikipedia id (that we use as main ids in the formated CMU dataset) and the IMDb ids. To do so we first mapped together movies that have the same names. The problem with this method is that many movies share the same name and that some name may be misspelled. To filter out duplicates, i.e. movies that are mapped twice in the CMU dataset, we ensure that two movies must have the same release year. Then for the remaining duplicates we were enforcing that they must share the same runtime. At this point we were left with 22 movies that were still duplicated entries, i.e. one movie in the CMU dataset was assigned to multiple IMDb entries. We drop the duplicates by end as the size of the duplicated set was small. We though initially to filter them by keeping only the movies with the highest number of vote. This was based on the hypothesis that most popular movies would be more likely to appear in the CMU dataset. But after verification, this assumption is not always true in practice. Thus we prefered to keep these filter stages and do the final round by hand.
The result of this processing is a table in ... which contains the mapping between around 50k wikipedia movie ids and IMDb ids. This allows us to merge tables from our formated CMU dataset and the IMDb dataset. For now we did not proceed to an extensive data analysis of the IMDb dataset, but our primary goal was to be sure that we could indeed use this data together with our original dataset.
  

## Methods 🤖

### 1. Data Model 𝌭 
To get a better understanding of our data, we first build a relational model and format data according to it.

First, we decided to have two tables, `Actor` and `Movie`. Both tables contain the IDs needed to recognize the different movies and actors, as well as other attributes describing the elements. The "appears_in" table makes the link between movies and actors who play in them by also specifying the age of the actors at the time the movie was released. There is also a table for characters in movies, defined by their IDs as well as their names. All movies have characters, all characters belong to a certain movie. All actors play/dub characters, but not all characters are necessarily played by actors (T-Rex in Jurassic Park). It is important to note that we defined our relationships between tables by logic, not by checking the data, as it was before we started working with it.

Finally, there are three more tables providing information about movies, `country`, `is_of_type` and `spoken_languages`. We have separated these tables from the `movie` table since a movie can be linked to several elements in these different tables. We have described the links as complete for all except the link between `movie` and `spoken_language` since movies do not necessarily have a spoken_language (silent movies).

All the dataframes are [here](/data/generated/).



### 2.Data Wrangling 🥋
#### Missing data
As previously stated, we used Wikipedia data to recover the release date for 5k different movies. The missing data is especially a problem for the revenue generated by the movies and actors/actresses general informations (height, ethnicity, birthdate). 
The first one is not our main priority and the retrieval would not be an easy task. We already gathered some information on Wikipedia, but the parsing is hard and the pipeline cannot guarantee 100% hit due to wrong wikipedia mapping and inconsistent page structure. One of the interest of the revenue would be to use it as a proxy of the movie success but we will use instead the ratings from IMDb users. The study of revenue over time could be interesting but would require comparison dataset to be sure that the findings are note simply due to inflation. Thus we would need extensive data on other industries. This question is left open for maybe another project.
#### Incorrect data
As seen in the initial data exploration, we can see that we have some entries with abnormal values, redundancy (e.g. ukrainian, ukranian) and other artifacts in the data. We already began to correct these problems by using for example mappings to converge to common values to avoid redundancy. Clustering could also help to gather data whose differences are likely due to generation/human errors. We plan to do an extensive cleaning and correction of the data only for movies for which we have an IMDb ids. It would allow us to focus on a subset of the data that would be consistent over our different analyses and that is preliminary cleaned. The use of advanced value imputation using similarity between movies is also considered.

### 3. Data Analysis 📈 

Our main focus of interest is the study of the reasons behind a movie success and their evolution over time. To perfom these analyses we plan to use several tools among which we can find time series analysis, clustering methods and the observational study machinery.
Time series analysis implies several mathematical methods ranging from statistical tests to regression and ARMA/ARIMA.
For movie clustering we plan to use standard unsupervised methods such as K-means or BIRCH.
Finally, to assess the values of our results in the scope of statistical findings, we plan to use the different tools that are involved in observationnal studies such as matching algorithm or logistic regression.

## Proposed timeline
| Period  | Description |
| ------------- | ------------- |
| 19.11 - 25.11  | Finish data processing  |
| 26.11 - 02.12  | Time series analysis  |
| 03.12 - 09.12  | Time series analysis, plotting graphs for presentation  |
| 10.11 - 16.12  | Cleaning graphs, data story, website programming  |
| 17.11 - 23.12  | Final revisions  |
| 23.12  | Project submission  |

## Organization within the team

<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Member</th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Aamir</td>
    <td class="tg-0lax">Develop the web interface<br><br>Develop clustering<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Cindy</td>
    <td class="tg-0lax">Come up with meaningful visualizations<br><br>Continue exploring the dataset<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Jérémy</td>
    <td class="tg-0lax">Define topic of interests<br><br>Develop clustering<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">Shayan</td>
    <td class="tg-0lax">Develop the web interface<br><br>Working on blueprint<br><br>Develop the final text for the data story</td>
  </tr>
</tbody>
</table>