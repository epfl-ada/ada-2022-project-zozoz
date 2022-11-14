"""
Contain the logic for loading data from the data folder.
"""

import pandas as pd
import numpy as np

DATA_PATH = "../data"

FOLDER_CMU = "MovieSummaries"
FOLDER_IMDB = "imdb"

CAT_GENDER = pd.CategoricalDtype(categories=['M', 'F'])

COL_CMU_CHAR_METADATA = ["wikipedia_movie_id", "freebase_movie_id",
                         "release_date", "character_name", "actor_birth_date",
                         "actor_gender", "actor_height", "actor_ethnicity", "actor_name",
                         "actor_age_at_release_date", "freebase_map_id", "freebase_character_id",
                         "freebase_actor_id"]
COL_CMU_MOVIE_METADATA = ["wikipedia_movie_id", "freebase_id",
                          "name", "release_date", "revenue",
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
