"""
Contain the logic for loading data from the data folder.
"""

import pandas as pd
import numpy as np
import json

DATA_PATH = "../data"

# CMU
FOLDER_CMU = "MovieSummaries"


CAT_GENDER = pd.CategoricalDtype(categories=['M', 'F'])

COL_CMU_CHAR_METADATA = ["wikipedia_movie_id", "freebase_movie_id",
                         "release_date", "character_name", "actor_birth_date",
                         "actor_gender", "actor_height", "actor_ethnicity", "actor_name",
                         "actor_age_at_release_date", "freebase_map_id", "freebase_character_id",
                         "freebase_actor_id"]
COL_CMU_MOVIE_METADATA = ["wikipedia_movie_id", "freebase_id",
                          "movie_name", "release_date", "revenue",
                          "runtime", "languages", "countries", "genres"]
COL_CMU_NAME_CLUSTERS = ["name", "char_map_freebase"]
COL_CMU_PLOT_SUMMARIES = ["wikipedia_movie_id", "plot_summary"]
COL_CMU_TVTROPES_CLUSTERS = ["char_type", "char_actor_map"]

DTYPES_CMU_CHAR_METADATA = [int, pd.StringDtype(), object, pd.StringDtype(), object, CAT_GENDER, float, pd.StringDtype(
), pd.StringDtype(), pd.Int64Dtype(), pd.StringDtype(), pd.StringDtype(), pd.StringDtype()]
DTYPES_CMU_MOVIE_METADATA = [int, pd.StringDtype(
), pd.StringDtype(), object, float, float, object, object, object]
DTYPES_CMU_NAME_CLUSTERS = [pd.StringDtype(), pd.StringDtype()]
DTYPES_CMU_PLOT_SUMMARIES = [int, pd.StringDtype()]
DTYPES_CMU_TVTROPES_CLUSTERS = [pd.StringDtype(), pd.StringDtype()]

# IMDB
FOLDER_IMDB = "imdb"

NA_IMDB = ["\\N"]

COL_IMDB_NAME_BASICS = ["nconst", "primary_name", "birth_year",
                        "death_year", "primary_profession", "known_for_titles"]
COL_IMDB_TITLE_BASICS = ["tconst", "title_type", "primary_title", "original_title",
                         "is_adult", "start_year", "end_year", "runtime_minutes", "genres"]
COL_IMDB_TITLE_CREW = ["tconst", "directors", "writers"]
COL_IMDB_TITLE_PRINCIPALS = ["tconst", "ordering",
                             "nconst", "category", "job", "characters"]
COL_IMDB_RATE = ["tconst", "average_rating", "num_votes"]

DTYPES_IMDB_NAME_BASICS = [pd.StringDtype(), pd.StringDtype(
), pd.Int64Dtype(), pd.Int64Dtype(), object, object]
DTYPES_IMDB_TITLE_BASICS = [pd.StringDtype(), pd.StringDtype(), pd.StringDtype(), pd.StringDtype(), pd.Int64Dtype(), pd.Int64Dtype(
), pd.Int64Dtype(), object, object]
DTYPES_IMDB_TITLE_CREW = [pd.StringDtype(), object, object]
DTYPES_IMDB_TITLE_PRINCIPALS = [pd.StringDtype(), pd.Int64Dtype(
), pd.StringDtype(), pd.StringDtype(), pd.StringDtype(), pd.StringDtype()]
DTYPES_IMDB_RATE = [pd.StringDtype(), float, pd.Int64Dtype()]


# CMU Jeremy

COL_NAMES_RAW_CMU_MOVIE = ["wikipedia_id", "freebase_id",
                           "name", "release_date", "revenue",
                           "runtime", "languages", "countries", "genres"]
COL_NAMES_RAW_CMU_PLOT = ["wikipedia_id", "plot"]
INDEX_COL_NAME_RAW_CMU_MOVIE = "wikipedia_id"

COL_NAMES_RAW_CMU_CHARACTER = ["wikipedia_movie_id", "freebase_movie_id",
                               "release_date", "character_name", "actor_birth_date",
                               "actor_gender", "actor_height", "actor_ethnicity", "actor_name",
                               "actor_age_at_release_date", "freebase_map_id", "freebase_character_id",
                               "freebase_actor_id"]
INDEX_COL_NAME_RAW_CMU_CHARACTER = "freebase_character_id"

FREEBASE_EXTRA_SUFFIX = "language"

ACTOR_BIRTHDATE_MIN_LENGTH = 4
ACTOR_BIRTHDATE_COL_NAME = "birth_date"
ACTOR_NAME_COL_NAME = "name"


# Helpers for CMU dataset extraction and parsing

def get_raw_movie_dataframe(movie_metadata_path, plot_summary_path):
    """ 
    Create the dataframe containing all the metadata and plots for the movies in the CMU dataset. 

    :param movie_metadata_path: Path to the CMU movie metadata dataset.
    :param plot_summary_path: Path to the CMU movie plot dataset.

    :return: A pandas Dataframe with merged information from metadata and plots.
    """
    movie_meta_data = pd.read_csv(movie_metadata_path, sep="\t",
                                  names=COL_NAMES_RAW_CMU_MOVIE,
                                  index_col=INDEX_COL_NAME_RAW_CMU_MOVIE)
    movie_plots = pd.read_csv(plot_summary_path, sep="\t",
                              names=COL_NAMES_RAW_CMU_PLOT,
                              index_col=INDEX_COL_NAME_RAW_CMU_MOVIE)
    movie_raw_df = movie_meta_data.join(movie_plots)
    return movie_raw_df


def get_raw_character_dataframe(character_metadata_path):
    """
    Create the dataframe containing all the metadata for the characters in the CMU dataset.

    :param character_metadata_path: Path to the CMU character dataset.

    :return: A pandas Dataframe with the metadata for each character in the CMU dataset.
    """
    character_meta_data = pd.read_csv(character_metadata_path, sep="\t",
                                      names=COL_NAMES_RAW_CMU_CHARACTER,
                                      index_col=INDEX_COL_NAME_RAW_CMU_CHARACTER)
    return character_meta_data


def freebase_dict_parser_python(entry) -> list:
    """ 
    Parse the entry of the given raw data freebase based entry using built-in python functions. 

    :param entry: Raw freebase entry in string format.

    :return: A list of the data in the initial entry.
    """
    results = []
    for pair in entry[1:-1].split(","):
        if len(pair) > 0:
            single_element = pair.split("\"")[-2].lower()
            results.append(single_element.removesuffix(FREEBASE_EXTRA_SUFFIX))
    return results


def apply_entry_level_filter(entry, filter_dict) -> str:
    """ 
    Replace in the given entry the different terms in the filter dictionnary. 

    :param entry: Single freebase data entry.
    :param filter_dict: Dictionnary with mapping for terms to be replaced.

    :return: The newly filtered entry.    
    """
    new_entry = entry
    for old, new in filter_dict.items():
        new_entry = new_entry.replace(old, new)
    return new_entry


def freebase_dict_parser(entry, filter_dict) -> list:
    """ 
    Parse the entry of the given raw data freebase based entry using json format. 

    :param entry: Non parsed freebase data entry.
    :param filter_dict: Dictionnary with mapping for terms to be replaced.

    :return: List containing the parsed information from the raw freebase entry.
    """
    entry_dict = json.loads(entry)
    if len(entry_dict) > 0:
        return list(set([apply_entry_level_filter(s.lower(), filter_dict)
                         for s in entry_dict.values()]))
    else:
        return []


def create_flat_movie_entry_list(entry_name, movie_raw_df, filter_dict) -> list:
    """ 
    Create a flat list with the movie ids together with the given entry type. 

    :param entry_name: Name of the type of entry to be parsed.
    :param movie_raw_df: Dataframe with the raw metadata and plots for the CMU dataset movies.
    :param filter_dict: Dictionnary with mapping for terms to be replaced.

    :return: Flat list of tuples with the movie_id and a corresponding data entry.
    """
    flat_entry_list = [(idx, entry) for idx, entry_list in
                       movie_raw_df[entry_name].apply(
                           lambda e: freebase_dict_parser(e, filter_dict)).to_dict().items()
                       for entry in entry_list]
    return list(set(flat_entry_list))


def create_entry_and_relation_table(movie_raw_df, entry_name,
                                    entry_id_name, movie_id_name, filter_dict=dict()) -> tuple:
    """ 
    Creates the tables for both the given entity and its relation table with the movies. 

    :param movie_raw_df: Dataframe with the raw metadata and plots for the CMU dataset movies.
    :param entry_name: Name of the type of entry to be parsed.
    :param entry_id_name: Name of the entry in the raw movie dataframe.
    :param movie_id_name: Name of the wikipedia movie id in the raw movie dataframe.
    :param filter_dict: Dictionnary with mapping for terms to be replaced.

    :return: One dataframe containing the different entry values and one dataframe containing the 
             between the movies and these values.
    """
    entry_relation_df = pd.DataFrame(create_flat_movie_entry_list(
        entry_name, movie_raw_df, filter_dict), columns=[movie_id_name, entry_id_name])
    entry_df = pd.DataFrame(
        {entry_id_name: entry_relation_df[entry_id_name].unique()}).set_index([entry_id_name])
    return entry_df, entry_relation_df


# Helpers for actor duplication handling

def retrieve_duplicated_actors_ids(actor_dataframe) -> list:
    """ 
    Retrieve the indices of duplicated actors in the given df. 

    We state that an actor is duplicated if it has the same name
    and the same birthdate as another entry in the df. Note that
    we do not consider same years as to be same birth date.

    :param actor_dataframe: Pandas Dataframe containing actor information.

    :return: List of tuples of duplicated actors ids.
    """
    duplicated_actors_df = actor_dataframe[
        actor_dataframe.duplicated(keep=False)]
    # We stick to defined actors, the row containing only missing values cannot be
    # Assimilated one to another.
    duplicated_actors_df = duplicated_actors_df[~duplicated_actors_df.isna()]
    duplicated_actors_df = duplicated_actors_df.reset_index()
    duplicated_actors_df = duplicated_actors_df[
        ~duplicated_actors_df[ACTOR_BIRTHDATE_COL_NAME].isna()]
    duplicated_actors_df = duplicated_actors_df.groupby(
        ACTOR_NAME_COL_NAME, dropna=False)
    duplicated_actors_dict = duplicated_actors_df[ACTOR_BIRTHDATE_COL_NAME].apply(
        list).to_dict()
    # Filter actors
    duplicated_actors_ids = []
    for actor_name, birth_dates in duplicated_actors_dict.items():
        first_date, second_date = birth_dates[0], birth_dates[1]
        # We filter actors which do not have only the first same
        # birth year but the same birth date.
        if first_date == second_date and len(first_date) > ACTOR_BIRTHDATE_MIN_LENGTH:
            duplicated_actors_ids.append(
                actor_dataframe[(actor_dataframe[ACTOR_NAME_COL_NAME] == actor_name)
                                & (actor_dataframe[ACTOR_BIRTHDATE_COL_NAME] == first_date)
                                ].index.to_list())
    return duplicated_actors_ids


def rematch_duplicated_actor_ids(duplicated_ids, actor_dataframe, relationship_dataframes):
    """ 
    Merge the different duplicated ids in the given dataframes inplace. 

    :param duplicated_ids: List of tuples of duplicated actors ids.
    :param actor_dataframe: Pandas Dataframe containing actor information.
    :param relationship_dataframes: List of dataframes where actors are involved.
    """
    for conserved_id, thrown_id in duplicated_ids:
        actor_dataframe.drop(thrown_id, inplace=True)
        for relation_df in relationship_dataframes:
            relation_df["actor_id"] = relation_df["actor_id"].apply(
                lambda idx: conserved_id if idx == thrown_id else idx)
            relation_df.drop_duplicates(inplace=True)


def process_duplicated_actors(actor_dataframe, relationship_dataframes):
    """ 
    Identify duplicated actors entries and merge inplace the different entries together. 

    :param actor_dataframe: Pandas Dataframe containing actor information.
    :param relationship_dataframes:List of dataframes where actors are involved.
    """
    duplicated_ids = retrieve_duplicated_actors_ids(actor_dataframe)
    rematch_duplicated_actor_ids(
        duplicated_ids, actor_dataframe, relationship_dataframes)

# Helpers for IMDB integration


def dtypes_map(dtypes: list[type], cols: list[str]) -> dict:
    """
    Map the columns of a dataframe to a new dtype.

    :param dtypes: The dtypes to map to.
    :param cols: The columns to map.

    :return: A dictionary mapping the columns to the dtypes.
    """
    assert len(dtypes) == len(cols)
    return dict(zip(cols, dtypes))


def parse_dict(x) -> list:
    """
    Parse a string to a dictionary.

    :param x: The dictionary contained in the df.

    :return: A list of the values of the dictionary.
    """
    return list(eval(x).values())


def parse_imdb_list(x) -> list:
    """
    Parse a string to a list.

    :param x: The list contained in the df.

    :return: A list of the values of the list.
    """
    return x.split(",")


def load_cmu_char_metadata() -> pd.DataFrame:
    """
    Load the character metadata from the CMU dataset.

    :return: A dataframe with the character metadata.
    """
    dtypes = dtypes_map(DTYPES_CMU_CHAR_METADATA, COL_CMU_CHAR_METADATA)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_CMU}/character.metadata.tsv", sep="\t", names=COL_CMU_CHAR_METADATA, dtype=dtypes)

    # Fix the release date
    df.release_date.replace("1010-12-02", "2010-12-02", inplace=True)

    # Fix the actor birth date
    df["actor_age_at_release_date"].fillna(0, inplace=True)

    df.release_date = pd.to_datetime(df.release_date)
    df.actor_birth_date = pd.to_datetime(df.actor_birth_date, errors='coerce')

    return df


def load_cmu_movie_metadata() -> pd.DataFrame:
    """
    Load the movie metadata from the CMU dataset.

    :return: A dataframe with the movie metadata.
    """
    dtypes = dtypes_map(DTYPES_CMU_MOVIE_METADATA, COL_CMU_MOVIE_METADATA)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_CMU}/movie.metadata.tsv", sep="\t", names=COL_CMU_MOVIE_METADATA, dtype=dtypes)

    # Fix the release date
    df.release_date.replace("1010-12-02", "2010-12-02", inplace=True)

    df.runtime.fillna(0, inplace=True)

    df.languages = df.languages.apply(parse_dict)
    df.countries = df.countries.apply(parse_dict)
    df.genres = df.genres.apply(parse_dict)

    df.release_date = pd.to_datetime(df.release_date)

    return df


def load_cmu_name_clusters() -> pd.DataFrame:
    """
    Load the name clusters from the CMU dataset.

    :return: A dataframe with the name clusters.
    """
    dtypes = dtypes_map(DTYPES_CMU_NAME_CLUSTERS, COL_CMU_NAME_CLUSTERS)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_CMU}/name.clusters.tsv", sep="\t", names=COL_CMU_NAME_CLUSTERS, dtype=dtypes)

    return df


def load_cmu_plot_summaries() -> pd.DataFrame:
    """
    Load the plot summaries from the CMU dataset.

    :return: A dataframe with the plot summaries.
    """
    dtypes = dtypes_map(DTYPES_CMU_PLOT_SUMMARIES, COL_CMU_PLOT_SUMMARIES)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_CMU}/plot_summaries.txt", sep="\t", names=COL_CMU_PLOT_SUMMARIES, dtype=dtypes)
    return df


def load_cmu_tvtropes_clusters() -> pd.DataFrame:
    """
    Load the TVTropes clusters from the CMU dataset.

    :return: A dataframe with the TVTropes clusters.
    """
    dtypes = dtypes_map(DTYPES_CMU_TVTROPES_CLUSTERS,
                        COL_CMU_TVTROPES_CLUSTERS)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_CMU}/tvtropes.clusters.txt", sep="\t", names=COL_CMU_TVTROPES_CLUSTERS, dtype=dtypes)
    df.char_actor_map = df.char_actor_map.apply(eval)
    return df


def load_imdb_name_basics() -> pd.DataFrame:
    """
    Load the name basics from the IMDB dataset.

    :return: A dataframe with the name basics.
    """
    dtypes = dtypes_map(DTYPES_IMDB_NAME_BASICS, COL_IMDB_NAME_BASICS)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_IMDB}/name.basics.tsv.gz", sep="\t", compression="gzip", skiprows=1, names=COL_IMDB_NAME_BASICS, dtype=dtypes, na_values=NA_IMDB)

    df.primary_profession = df.primary_profession.map(
        parse_imdb_list, na_action='ignore')
    df.known_for_titles = df.known_for_titles.map(
        parse_imdb_list, na_action='ignore')
    return df


def load_imdb_title_basics() -> pd.DataFrame:
    """
    Load the title basics from the IMDB dataset.

    :return: A dataframe with the title basics.
    """
    dtypes = dtypes_map(DTYPES_IMDB_TITLE_BASICS, COL_IMDB_TITLE_BASICS)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_IMDB}/title.basics.tsv.gz", sep="\t", compression="gzip", skiprows=1, names=COL_IMDB_TITLE_BASICS, dtype=dtypes, na_values=NA_IMDB)

    # remove invalid runtime values
    invalids = ['Reality-TV', 'Talk-Show', 'Documentary',
                'Game-Show', 'Animation,Comedy,Family', 'Game-Show,Reality-TV']
    df.runtime_minutes = df.runtime_minutes.map(
        lambda r: np.NaN if r in invalids else r).astype(pd.Int64Dtype())

    df.runtime_minutes.fillna(0, inplace=True)

    df.genres = df.genres.map(parse_imdb_list, na_action='ignore')
    return df


def load_imdb_title_crew() -> pd.DataFrame:
    """
    Load the title crew from the IMDB dataset.

    :return: A dataframe with the title crew.
    """
    dtypes = dtypes_map(DTYPES_IMDB_TITLE_CREW, COL_IMDB_TITLE_CREW)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_IMDB}/title.crew.tsv.gz", sep="\t", compression="gzip", skiprows=1, names=COL_IMDB_TITLE_CREW, dtype=dtypes, na_values=NA_IMDB)

    df.directors = df.directors.map(parse_imdb_list, na_action='ignore')
    df.writers = df.writers.map(parse_imdb_list, na_action='ignore')
    return df


def load_imdb_title_principals() -> pd.DataFrame:
    """
    Load the title principals from the IMDB dataset.

    :return: A dataframe with the title principals.
    """
    dtypes = dtypes_map(DTYPES_IMDB_TITLE_PRINCIPALS,
                        COL_IMDB_TITLE_PRINCIPALS)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_IMDB}/title.principals.tsv.gz", sep="\t", compression="gzip", skiprows=1, names=COL_IMDB_TITLE_PRINCIPALS, dtype=dtypes, na_values=NA_IMDB)

    df.characters = df.characters.map(eval, na_action='ignore')
    return df


def load_imdb_title_ratings() -> pd.DataFrame:
    """
    Load the title ratings from the IMDB dataset.

    :return: A dataframe with the title ratings.
    """
    dtypes = dtypes_map(DTYPES_IMDB_RATE, COL_IMDB_RATE)
    df = pd.read_csv(
        f"{DATA_PATH}/{FOLDER_IMDB}/title.ratings.tsv.gz", sep="\t", compression="gzip", skiprows=1, names=COL_IMDB_RATE, dtype=dtypes, na_values=NA_IMDB)

    return df
