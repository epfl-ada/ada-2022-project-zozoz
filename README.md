# Is John the reason for the success? A deep dive of the temporal changes in movie


## Abstract 📝 [Aamir]
The CMU movie [dataset](http://www.cs.cmu.edu/~ark/personas/) comes from 42,306 movie plot summaries extracted from Wikipedia. We want to assess what makes a movie successful. Success has different dimensions. We are using the box office and IMDB ratings to cover the two important ones. We take into account attributes like genres, actors, directors, character names etc. and want to analyse their contribution to the success of a movie. We want to see if we can find temporal changes in the data and create a blueprint for the next big hit.

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#research-questions-">Research Questions</a></li>
    <li><a href="#proposed-additional-datasets-">Proposed additional datasets</a></li>
    <li><a href="#methods-">Methods</a></li>
      <ol>
        <li><a href="#1-data-model-">Data Model</a></li>
        <li><a href="#2-data-wrangling-">Data Wrangling</a></li>
        <li><a href="#3-data-analysis-">Data Analysis</a></li>
      </ol>
    <li><a href="#proposed-timeline-️">Proposed timeline</a></li>
    <li><a href="#organization-within-the-team-">Organization within the team</a></li>
  </ol>
</details>

---
## Research Questions 🧠
- What makes a movie successful across the years?
    - What characteristics do they need to have for example director, actors, genres or character names?
- Can we cluster successful movie plots?
- Are the reasons for success and their evolution the same across countries?
- Can we create our own blueprint the next big hit?

## Proposed additional datasets 📠
- Wikipedia
  - Why? To complete missing release date values in our initial dataset.
  - How? Using the wikipedia python library, we were able to retrieve page information for many movies.
- IMDb
  - Why? To have more metadata for movies such as directors, music producers, ratings.
  - How? Using the IMDB public datasets and filtering the movies to keep only the ones that are in the CMU dataset.


## Methods 🤖

### 1. Data Model 𝌭
To get a better understanding of our data, we first build a relational model and format data according to it.

First, we decided to have two tables, `Actor` and `Movie`. Both tables contain the IDs needed to recognize the different movies and actors, as well as other attributes describing the elements. The "appears_in" table makes the link between movies and actors who play in them by also specifying the age of the actors at the time the movie was released. There is also a table for characters in movies, defined by their IDs as well as their names. All movies have characters, all characters belong to a certain movie. All actors play/dub characters, but not all characters are necessarily played by actors (T-Rex in Jurassic Park). It is important to note that we defined our relationships between tables by logic, not by checking the data, as it was before we started working with it.

Finally, there are three more tables providing information about movies, `country`, `is_of_type` and `spoken_languages`. We have separated these tables from the `movie` table since a movie can be linked to several elements in these different tables. We have described the links as complete for all except the link between `movie` and `spoken_language` since movies do not necessarily have a spoken_language (silent movies).

All the dataframes are [here](/data/generated/).



### 2. Data Wrangling 🥋
#### Missing data
#### Incorrect data?

### 3. Data Analysis 📈
- Time series analysis
- Clustering

## Proposed timeline 🗓️
| Period  | Description |
| ------------- | ------------- |
| 19.11 - 25.11  | Finish data processing  |
| 26.11 - 02.12  | Time series analysis  |
| 03.12 - 09.12  | Time series analysis, plotting graphs for presentation  |
| 10.11 - 16.12  | Cleaning graphs, data story, website programming  |
| 17.11 - 23.12  | Final revisions  |
| 23.12  | Project submission  |

## Organization within the team 👾

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


## Questions for TAs

## Instructions
Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:
- Title
- Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Research Questions: A list of research questions you would like to address during the project.
- Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
- Methods
- Proposed timeline
- Organization within the team: A list of internal milestones up until project Milestone P3.
- Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
