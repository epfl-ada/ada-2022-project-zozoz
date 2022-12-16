# Global Imports
import pandas as pd
import numpy as np
# Statistics
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Constants
CONTINENT_ID = {"North America and Australia": [1,0,0,0,0,0],
"Central and South America": [0,1,0,0,0,0],
"Western Europe": [0,0,1,0,0,0],
"Eastern Europe and Russia": [0,0,0,1,0,0],
"Africa and Middle-East": [0,0,0,0,1,0],
"Asia": [0,0,0,0,0,1]}

COUNTRY_CONTINENT_MAPPING = {
'afghanistan' : "Africa and Middle-East",
 'albania' : "Eastern Europe and Russia",
 'algeria' : "Africa and Middle-East",
 'argentina': "Central and South America",
 'armenia' : "Africa and Middle-East",
 'aruba': "Central and South America",
 'australia': "North America and Australia",
 'austria': "Western Europe",
 'azerbaijan' : "Africa and Middle-East",
 'bahamas': "Central and South America",
 'bahrain' : "Africa and Middle-East",
 'bangladesh': "Asia",
 'belgium': "Western Europe",
 'bhutan': "Asia",
 'bolivia': "Central and South America",
 'bosnia and herzegovina' : "Eastern Europe and Russia",
 'brazil': "Central and South America",
 'bulgaria' : "Eastern Europe and Russia",
 'burkina faso' : "Africa and Middle-East",
 'burma': "Asia",
 'cambodia': "Asia",
 'cameroon' : "Africa and Middle-East",
 'canada': "North America and Australia",
 'chile': "Central and South America",
 'china': "Asia",
 'colombia': "Central and South America",
 'congo' : "Africa and Middle-East",
 'costa rica': "Central and South America",
 'crime' : "Eastern Europe and Russia",
 'croatia' : "Eastern Europe and Russia",
 'cuba': "Central and South America",
 'cyprus' : "Eastern Europe and Russia",
 'czech republic' : "Eastern Europe and Russia",
 'czechoslovakia' : "Eastern Europe and Russia",
 'democratic republic of the congo' : "Africa and Middle-East",
 'denmark': "Western Europe",
 'egypt' : "Africa and Middle-East",
 'estonia' : "Eastern Europe and Russia",
 'ethiopia' : "Africa and Middle-East",
 'finland': "Western Europe",
 'france': "Western Europe",
 'georgia' : "Africa and Middle-East",
 'germany': "Western Europe",
 'greece' : "Eastern Europe and Russia",
 'haiti': "Central and South America",
 'hong kong': "Asia",
 'hungary' : "Eastern Europe and Russia",
 'iceland': "Western Europe",
 'india': "Asia",
 'indonesia': "Asia",
 'iran' : "Africa and Middle-East",
 'iraq' : "Africa and Middle-East",
 'iraqi kurdistan' : "Africa and Middle-East",
 'ireland': "Western Europe",
 'isle of man': "Western Europe",
 'israel' : "Africa and Middle-East",
 'italy': "Western Europe",
 'jamaica': "Central and South America",
 'japan': "Asia",
 'jordan' : "Africa and Middle-East",
 'kenya' : "Africa and Middle-East",
 'korea': "Asia",
 'kuwait' : "Africa and Middle-East",
 'lebanon' : "Africa and Middle-East",
 'libya' : "Africa and Middle-East",
 'lithuania' : "Eastern Europe and Russia",
 'luxembourg': "Western Europe",
 'macau': "Asia",
 'malaysia': "Asia",
 'mali' : "Africa and Middle-East",
 'malta': "Western Europe",
 'mexico': "Central and South America",
 'monaco': "Western Europe",
 'mongolia': "Asia",
 'montenegro' : "Eastern Europe and Russia",
 'morocco' : "Africa and Middle-East",
 'nepal': "Asia",
 'netherlands': "Western Europe",
 'new zealand': "North America and Australia",
 'nigeria' : "Africa and Middle-East",
 'norway': "Western Europe",
 'pakistan' : "Africa and Middle-East",
 'palestinian territories' : "Africa and Middle-East",
 'panama': "Central and South America",
 'peru': "Central and South America",
 'philippines': "Asia",
 'poland' : "Eastern Europe and Russia",
 'portugal': "Western Europe",
 'puerto rico': "Central and South America",
 'republic of macedonia' : "Eastern Europe and Russia",
 'romania' : "Eastern Europe and Russia",
 'russia' : "Eastern Europe and Russia",
 'senegal' : "Africa and Middle-East",
 'serbia' : "Eastern Europe and Russia",
 'serbia and montenegro' : "Eastern Europe and Russia",
 'singapore': "Asia",
 'slovakia' : "Eastern Europe and Russia",
 'slovenia' : "Eastern Europe and Russia",
 'south africa' : "Africa and Middle-East",
 'south korea': "Asia",
 'spain': "Western Europe",
 'sri lanka': "Asia",
 'sweden': "Western Europe",
 'switzerland': "Western Europe",
 'taiwan': "Asia",
 'thailand': "Asia",
 'tunisia' : "Africa and Middle-East",
 'turkey' : "Africa and Middle-East",
 'ukraine' : "Eastern Europe and Russia",
 'united arab emirates' : "Africa and Middle-East",
 'united kingdom': "Western Europe",
 'united states of america': "North America and Australia",
 'uruguay': "Central and South America",
 'uzbekistan' : "Africa and Middle-East",
 'venezuela': "Central and South America",
 'vietnam': "Asia",
 'yugoslavia' : "Eastern Europe and Russia",
 'zambia' : "Africa and Middle-East",
 'zimbabwe' : "Africa and Middle-East"
}

COUNTRY_ENCODING = { 
    "North America and Australia": [1,0,0,0,0,0],
    "Western Europe":              [0,1,0,0,0,0],
    "Asia":                        [0,0,1,0,0,0],
    "Africa and Middle-East":      [0,0,0,1,0,0],
    "Eastern Europe and Russia":   [0,0,0,0,1,0],
    "Central and South America":   [0,0,0,0,0,1]
}

CONTINENT_LIST = ["North America and Australia","Western Europe","Asia",
                  "Africa and Middle-East","Eastern Europe and Russia", 
                  "Central and South America"]

GENRE_MAPPING = {'absurdism': ["comedy"],
 'acid western': ["adventure","action"],
 'action': ["action"],
 'action comedy': ["action","comedy"],
 'action thrillers': ["thriller","action"],
 'action/adventure': ["action","adventure"],
 'addiction drama': ["drama"],
 'adult': ["adult"],
 'adventure': ["adventure"],
 'adventure comedy': ["adventure","comedy"],
 'airplanes and airports': ["other"],
 'albino bias': ["drama"],
 'alien film': ["action","adventure"],
 'alien invasion': ["action"],
 'americana': ["drama"],
 'animal picture': ["other"],
 'animals': ["other"],
 'animated cartoon': ["animation"],
 'animated musical': ["animation"],
 'animation': ["animation"],
 'anime': ["animation"],
 'anthology': ["genre"],
 'anthropology': ["other"],
 'anti-war': ["drama"],
 'anti-war film': ["drama"],
 'apocalyptic and post-apocalyptic fiction': ["action","fantasy"],
 'archaeology': ["other"],
 'archives and records': ["other"],
 'art film': ["genre"],
 'auto racing': ["other"],
 'avant-garde': ["genre"],
 'b-movie': ["comedy"],
 'b-western': ["action","comedy"],
 'backstage musical': ["other"],
 'baseball': ["other"],
 'beach film': ["other"],
 'beach party film': ["comedy"],
 'bengali cinema': ["other"],
 'biker film':["action"],
 'biographical film': ["other"],
 'biography': ["other"],
 'biopic [feature]': ["other"],
 'black comedy': ["comedy"],
 'black-and-white': ["other"],
 'blaxploitation':["drama"],
 'bloopers & candid camera': ["comedy"],
 'bollywood': ["other"],
 'boxing': ["other"],
 'breakdance': ["other"],
 'british empire film': ["other"],
 'british new wave': ["genre"],
 'bruceploitation':["action"],
 'buddy cop': ["action","comedy"],
 'buddy film': ["comedy"],
 'buddy picture': ["comedy"],
 'business': ["other"],
 'camp': ["other"],
 'caper story': ["thriller"],
 'cavalry film': ["action"],
 'chase movie': ["thriller"],
 'childhood drama': ["drama"],
 "children's": ["family"],
 "children's entertainment": ["family"],
 "children's fantasy": ["family","fantasy"],
 "children's issues": ["drama"],
 "children's/family": ["family"],
 'chinese movies': ["other"],
 'christian film': ["other"],
 'christmas movie': ["other"],
 'clay animation': ["animation"],
 'cold war': ["adventure","action"],
 'combat films': ["action"],
 'comdedy': ["comedy"],
 'comedy': ["comedy"],
 'comedy film': ["comedy"],
 'comedy horror': ["horror","comedy"],
 'comedy of errors': ["comedy"],
 'comedy of manners': ["comedy"],
 'comedy thriller': ["thriller","comedy"],
 'comedy western': ["action","comedy"],
 'comedy-drama': ["drama","comedy"],
 'coming of age': ["comedy"],
 'coming-of-age film': ["comedy"],
 'computer animation': ["animation"],
 'computers': ["animation"],
 'concert film': ["other"],
 'conspiracy fiction': ["thriller"],
 'costume adventure': ["adventure"],
 'costume drama': ["drama"],
 'costume horror': ["horror"],
 'courtroom comedy': ["comedy"],
 'courtroom drama': ["drama"],
 'creature film': ["adventure","fantasy"],
 'crime': ["thriller"],
 'crime comedy': ["thriller","comedy"],
 'crime drama': ["thriller","drama"],
 'crime fiction': ["thriller"],
 'crime thriller': ["thriller"],
 'cult': ["other"],
 'culture & society': ["other"],
 'cyberpunk': ["fantasy"],
 'czechoslovak new wave': ["genre"],
 'dance': ["other"],
 'demonic child': ["horror"],
 'detective': ["thriller"],
 'detective fiction': ["thriller"],
 'disaster': ["drama"],
 'docudrama': ["drama"],
 'documentary': ["other"],
 'dogme 95': ["genre"],
 'domestic comedy': ["comedy"],
 'doomsday film': ["fantasy"],
 'drama': ["drama"],
 'dystopia': ["drama","fantasy"],
 'ealing comedies': ["comedy"],
 'early black cinema': ["other"],
 'education': ["family"],
 'educational': ["family"],
 'ensemble film': ["genre"],
 'environmental science': ["other"],
 'epic': ["adventure"],
 'epic western': ["adventure","action"],
 'erotic drama': ["adult","drama"],
 'erotic thriller': ["thriller","adult"],
 'erotica': ["adult"],
 'escape film': ["thriller"],
 'essay film': ["genre"],
 'existentialism': ["genre"],
 'experimental film': ["genre"],
 'exploitation': ["drama"],
 'expressionism': ["genre"],
 'extreme sports': ["other"],
 'fairy tale': ["fantasy","adventure"],
 'family & personal relationships': ["drama"],
 'family drama': ["drama"],
 'family film': ["family"],
 'family-oriented adventure': ["family","adventure"],
 'fan film': ["other"],
 'fantasy': ["fantasy"],
 'fantasy adventure': ["fantasy","adventure"],
 'fantasy comedy': ["fantasy","comedy"],
 'fantasy drama': ["fantasy","drama"],
 'feature film': ["other"],
 'female buddy film': ["comedy"],
 'feminist film': ["drama"],
 'fictional film': ["other"],
 'filipino': ["other"],
 'filipino movies': ["other"],
 'film': ["other"],
 'film & television history': ["other"],
 'film adaptation': ["other"],
 'film noir': ["thriller"],
 'film à clef': ["drama"],
 'film-opera': ["other"],
 'filmed play': ["other"],
 'finance & investing': ["other"],
 'foreign legion':["action"],
 'future noir': ["fantasy","drama"],
 'gangster film': ["thriller","action"],
 'gay': ["drama"],
 'gay interest': ["drama"],
 'gay pornography': ["adult"],
 'gay themed': ["drama"],
 'gender issues': ["drama"],
 'giallo': ["thriller"],
 'glamorized spy film': ["thriller"],
 'goat gland': ["genre"],
 'gothic film': ["genre"],
 'graphic & applied arts': ["genre"],
 'gross out': ["comedy"],
 'gross-out film': ["comedy"],
 'gulf war':["action"],
 'hagiography': ["other"],
 'hardcore pornography': ["adult"],
 'haunted house film': ["horror"],
 'health & fitness': ["other"],
 'heaven-can-wait fantasies': ["fantasy"],
 'heavenly comedy': ["comedy"],
 'heist': ["action"],
 'hip hop movies': ["other"],
 'historical documentaries': ["other"],
 'historical drama': ["drama"],
 'historical epic': ["adventure"],
 'historical fiction': ["other"],
 'history': ["other"],
 'holiday film': ["comedy"],
 'horror': ["horror"],
 'horror comedy': ["horror","comedy"],
 'horse racing': ["other"],
 'humour': ["comedy"],
 'hybrid western': ["adventure","action"],
 'illnesses & disabilities': ["drama"],
 'indian western': ["adventure","action"],
 'indie': ["genre"],
 'inspirational drama': ["drama"],
 'instrumental music': ["other"],
 'interpersonal relationships': ["drama"],
 'inventions & innovations': ["other"],
 'japanese movies': ["other"],
 'journalism': ["other"],
 'jukebox musical': ["other"],
 'jungle film': ["adventure"],
 'juvenile delinquency film': ["drama"],
 'kafkaesque': ["genre"],
 'kitchen sink realism': ["genre"],
 'language & literature': ["genre"],
 'latino': ["other"],
 'law & crime': ["thriller"],
 'legal drama': ["drama"],
 'lgbt': ["drama"],
 'libraries and librarians': ["other"],
 'live action': ["other"],
 'malayalam cinema': ["other"],
 'marriage drama': ["drama"],
 'martial arts film': ["action"],
 'master criminal films': ["thriller"],
 'media satire': ["other"],
 'media studies': ["other"],
 'medical fiction': ["other"],
 'melodrama': ["drama"],
 'mockumentary': ["other"],
 'mondo film': ["genre"],
 'monster': ["horror","action"],
 'monster movie': ["horror","action"],
 'movie serial': ["other"],
 'movies about gladiators': ["other"],
 'mumblecore': ["genre"],
 'music': ["other"],
 'musical': ["other"],
 'musical comedy': ["comedy"],
 'musical drama': ["drama"],
 'mystery': ["thriller"],
 'mythological fantasy': ["fantasy"],
 'natural disaster': ["other"],
 'natural horror films': ["horror"],
 'nature': ["other"],
 'neo-noir': ["thriller"],
 'neorealism': ["genre"],
 'new hollywood': ["genre"],
 'new queer cinema': ["drama"],
 'news': ["other"],
 'ninja movie': ["action"],
 'northern': ["genre"],
 'operetta': ["other"],
 'outlaw': ["other"],
 'outlaw biker film': ["other"],
 'parkour in popular culture': ["action"],
 'parody': ["comedy"],
 'patriotic film': ["other"],
 'period horror': ["horror"],
 'period piece': ["drama"],
 'pinku eiga': ["adult"],
 'plague': ["drama"],
 'point of view shot': ["other"],
 'political cinema': ["other"],
 'political documetary': ["other"],
 'political drama': ["drama"],
 'political satire': ["drama"],
 'political thriller': ["thriller"],
 'pornographic movie': ["adult"],
 'pornography': ["adult"],
 'pre-code': ["other"],
 'prison': ["action"],
 'prison escape': ["action"],
 'prison film': ["action"],
 'private military company': ["action"],
 'propaganda film': ["other"],
 'psycho-biddy': ["horror","thriller"],
 'psychological horror': ["horror"],
 'psychological thriller': ["thriller"],
 'punk rock': ["genre"],
 'race movie': ["action"],
 'reboot': ["other"],
 'religious film': ["other"],
 'remake': ["other"],
 'revenge': ["action"],
 'revisionist fairy tale': ["adventure","fantasy"],
 'revisionist western': ["adventure","action"],
 'road movie': ["other"],
 'road-horror': ["horror"],
 'roadshow theatrical release': ["other"],
 'roadshow/carny': ["other"],
 'rockumentary': ["other"],
 'romance film': ["other"],
 'romantic comedy': ["comedy"],
 'romantic drama': ["drama"],
 'romantic fantasy': ["fantasy"],
 'romantic thriller': ["thriller"],
 'samurai cinema': ["adventure","action"],
 'satire': ["comedy"],
 'school story': ["family"],
 'sci-fi adventure': ["fantasy","adventure"],
 'sci-fi horror': ["fantasy","horror"],
 'sci-fi thriller': ["fantasy","thriller"],
 'science fiction': ["fantasy"],
 'science fiction western': ["adventure","fantasy","action"],
 'screwball comedy': ["comedy"],
 'sex comedy': ["comedy"],
 'sexploitation': ["drama"],
 'short film': ["other"],
 'silent film': ["other"],
 'singing cowboy': ["action","adventure"],
 'slapstick': ["comedy"],
 'slasher': ["horror","action"],
 'slice of life story': ["drama"],
 'social issues': ["drama"],
 'social problem film': ["drama"],
 'softcore porn': ["adult"],
 'space opera': ["fantasy","adventure"],
 'space western': ["adventure","action"],
 'spaghetti western': ["adventure","action"],
 'splatter film': ["horror"],
 'sports': ["other"],
 'spy': ["thriller"],
 'stand-up comedy': ["comedy"],
 'star vehicle': ["other"],
 'steampunk': ["fantasy"],
 'stoner film': ["genre"],
 'stop motion': ["animation"],
 'superhero': ["action"],
 'superhero movie': ["action"],
 'supermarionation': ["animation"],
 'supernatural': ["fantasy"],
 'surrealism': ["genre"],
 'suspense': ["thriller"],
 'swashbuckler films': ["action","adventure"],
 'sword and sandal': ["adventure"],
 'sword and sorcery': ["fantasy","adventure"],
 'sword and sorcery films': ["fantasy","adventure"],
 'tamil cinema': ["other"],
 'teen': ["family"],
 'television movie': ["other"],
 'the netherlands in world war ii': ["action"],
 'therimin music': ["other"],
 'thriller': ["thriller"],
 'time travel': ["adventure"],
 'tokusatsu': ["other"],
 'tollywood': ["other"],
 'tragedy': ["drama"],
 'tragicomedy': ["comedy"],
 'travel': ["adventure"],
 'vampire movies': ["horror","action"],
 'war effort': ["action"],
 'war film': ["action"],
 'werewolf fiction': ["horror"],
 'western': ["adventure","action"],
 'whodunit': ["thriller"],
 'women in prison films': ["drama"],
 'workplace comedy': ["comedy"],
 'world cinema': ["other"],
 'world history': ["other"],
 'wuxia': ["adventure"],
 'z movie': ["horror"],
 'zombie film': ["horror"]}

GENRE_ENCODING = {
    "action":    [1,0,0,0,0,0,0,0,0,0,0],
    "adventure": [0,1,0,0,0,0,0,0,0,0,0],
    "comedy":    [0,0,1,0,0,0,0,0,0,0,0],
    "drama":     [0,0,0,1,0,0,0,0,0,0,0],
    "thriller":  [0,0,0,0,1,0,0,0,0,0,0],
    "horror":    [0,0,0,0,0,1,0,0,0,0,0],
    "animation": [0,0,0,0,0,0,1,0,0,0,0],
    "family":    [0,0,0,0,0,0,0,1,0,0,0],
    "adult":     [0,0,0,0,0,0,0,0,1,0,0],
    "fantasy":   [0,0,0,0,0,0,0,0,0,1,0],
    "genre":     [0,0,0,0,0,0,0,0,0,0,1],
    "other":     [0,0,0,0,0,0,0,0,0,0,0]
}

GENRE_LIST = ["action","adventure","comedy","drama","thriller","horror",
                   "animation","children","adult","fantasy","genre"]

# These parameters control the formation of the dataframe for regression
#
#   drop: Columns to drop before applying any transform to the data
#   nan_filtering: Columns on which we want to remove rows with nans.
#                  If 'all', then apply on every one.
#   decades: List of decades on which to apply the regression. 
#            If empty list then all decades will be taken.
#   log: Columns on which to apply a log transform.
#   standardize: Columns to standardize.
#   post_drop: Columns to drop before doing the regression.
DEFAULT_PARAMETERS = {
            "drop": ["name","revenue","has_common_character_name","has_common_language","language_number","character_number"],
            "nan_filtering":["all"],
            "decades":[],
            "log":[],
            "standardize":["title_length"],
            "post_drop": ["release_date","num_votes",
                            "runtime","decade","average_rating",
                            "combinned_best_rating"]}

SUCCESS_THRESHOLD = 7.5

NE_FULL_LIST = ["ORGANIZATION","PERSON","LOCATION",
                "DATE","TIME","MONEY",
                "PERCENT","FACILITY","GPE"]

EPSILON = 1e-4 # Set to 1e-4 empirically, but idea is to have at least one occurence in all corpus

TOP_ACTOR_PERCENTILE = 99
K_LANGUAGES = 5
K_CHARACTERS = 20

# Helpers

def director_metrics_up_to_date(movie_dataframe: pd.DataFrame, director_movies: set, date) -> tuple:
    """
    Compute the number of movies and the best ratings up to the date from the set of movies provided.
    
    This function allows us to have the history of performance of the set of directors that worked 
    on a given movie. You give the set of movies of the directors and the date of production of the
    current movie and it will return the performance up to the given date.
    
    :param movie_dataframe: Pandas DataFrame with movie information
    :param director_movies: Set of movies directed by the directors of the current movie.
    :param date: Date of release of the current movie, thus the metrics are up to this date.
    
    :return: The number of movies and the best rating up to the given date.
    """
    director_movie_df = movie_dataframe[movie_dataframe.index.isin(director_movies)]
    movie_date_df = director_movie_df[director_movie_df["release_date"] < date]
    movie_count = len(movie_date_df)
    if movie_count == 0:
        return 0, None
    best_rating = movie_date_df["average_rating"].max()
    return movie_count, best_rating

def standardize_column(dataframe: pd.DataFrame, col_name: str):
    """
    Standardize the given column in the provided dataframe.
    
    :param dataframe: Pandas DataFrame containing the data.
    :param col_name: Name of the column to standardize.
    
    """
    dataframe[col_name] = (dataframe[col_name]-
        dataframe[col_name].mean())/dataframe[col_name].std()
    
def process_dataframe(dataframe: pd.DataFrame,
                      parameters={"drop": [], "nan_filtering":["all"],"decades":[],
                                  "log":[], "standardize":[]}) -> pd.DataFrame:
    """
    Pre-process the dataframe for regression given the instructions in parameters.
    
    :param dataframe: Pandas DataFrame with the movie data for regression
    :param parameters: Dictionnary with the different parameters for pre-processing:
                            - drop: List of columns to drop.
                            - nan_filtering: List of columns where nan rows should be excluded.
                            - decades: List of decades to keep. If empty, keep all decades.
                            - log: List of columns to log transform.
                            - standardize: List of columns to standardize.
                    
    
    :return: Processed Pandas DataFrame ready for regression.
    
    """
    regression_df = dataframe.copy()
    # Filter out columns
    regression_df = regression_df.drop(parameters["drop"],axis=1)
    # Filter out decades
    if len(parameters["decades"]) != 0:
        regression_df = regression_df[
            regression_df["decade"].isin(parameters["decades"])]
    # Filter out NaN
    if len(parameters["nan_filtering"]) != 0:
        if parameters["nan_filtering"][0] == "all":
            regression_df = regression_df.dropna(how="any")
        else:
            regression_df = regression_df.dropna(subset=parameters["nan_filtering"])
    # Transform
    for col in parameters["log"]:
        regression_df["log_"+col] = regression_df[col].apply(np.log)
    # Standardize
    for col in parameters["standardize"]:
        standardize_column(regression_df,col)
    return regression_df

def select_next_feature(regression_df: pd.DataFrame, target: pd.Series,
                        current_features=[], ignored_features=[], 
                        alpha=0.05, show=False) -> str:
    """
    Report the best feature to integrate to the current OLS model based on r-squared.
    
    :param regression_df: Pandas DataFrame containing the data for regression.
    :param target: Pandas Series representing the target values.
    :param current_features: List of features integrated in the actual model.
    :param ignored_features: List of features that should not be integrated in the regression.
    :param alpha: Significance level, default 0.05.
    :param show: Display the different features scores.
    
    :result: Name of the best feature or None if no new significant features.
    
    """
    result_dict = {'predictor': [], 'r-squared':[], "aic":[], "p_value":[]}
    for col in regression_df.columns:
        if col not in (current_features+ignored_features):
            X = regression_df[current_features + [col]]
            model = sm.OLS(target, sm.add_constant(X)).fit()
            #Add the column name to our dictionary
            result_dict['predictor'].append(col)
            #Calculate the r-squared value between the target and predicted target
            r2 = model.rsquared
            #Add the model metrics to our dictionary
            result_dict['r-squared'].append(r2)
            result_dict['aic'].append(model.aic)
            result_dict['p_value'].append(model.pvalues.loc[col])
    #Once it's iterated through every column, turn our dict into a sorted DataFrame
    candidates_features = pd.DataFrame(result_dict).sort_values(by=['r-squared'],
                                                          ascending = False)
    if show:
        print(candidates_features.head())
        
    candidates_features = candidates_features[candidates_features["p_value"] < alpha]
    if len(candidates_features) == 0:
        return "None"
    else:
        return candidates_features["predictor"].iloc[0]

def forward_selection(regression_df: pd.DataFrame, target: pd.Series,
                        ignored_features=[], alpha=0.05, show=False) -> list:
    """
    Iterative forward feature selection based on r-squared without interaction terms.
    
    :param regression_df: Pandas DataFrame containing the data for regression.
    :param target: Pandas Series representing the target values.
    :param current_features: List of features integrated in the actual model.
    :param ignored_features: List of features that should not be integrated in the regression.
    :param alpha: Significance level, default 0.05.
    :param show: Display the different features scores.
    
    :result: List of the best features to model the target.
    
    """
    last_feature = ""
    current_features = []
    while ((len(ignored_features) + len(current_features)) < len(regression_df)
           and last_feature != "None"):
        last_feature = select_next_feature(regression_df, target,
                        current_features=current_features,
                        ignored_features=ignored_features, 
                        alpha=alpha, show=show)
        if last_feature != "None":
            current_features.append(last_feature)
    return current_features

def create_VIF_dataframe(regression_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the VIF for each features in the given dataframe.
    
    :param regression_df: Pandas DataFrame containing the data for regression.
    
    :return: Pandas DataFrame with the VIF for each features.
    
    """
    vif_features = regression_df.columns
    vif_values = [variance_inflation_factor(regression_df.values, i) 
                for i in range(len(regression_df.columns))]
    vif_df = pd.DataFrame(np.array([vif_features,vif_values]).T,columns=["predictor","VIF"])
    return vif_df

def filter_multicolinearity(regression_df: pd.DataFrame, threshold=5):
    """
    Remove the features that shows high multicollinearity based on VIF.
    
    :param regression_df: Pandas DataFrame containing the data for regression.
    :param threshold: Threshold above which a VIF is considered to high to be kept. 
    
    :return: Pandas DataFrame with data for regression without high multicollinearity.
    
    """
    new_regression_df = regression_df.copy()
    vif_df = create_VIF_dataframe(new_regression_df)
    high_VIF = (vif_df["VIF"] > threshold).sum()
    while high_VIF:
        highest_VIF_predictor = vif_df.iloc[
            vif_df["VIF"].astype(np.float32).argmax()]["predictor"]
        new_regression_df = new_regression_df.drop(highest_VIF_predictor,axis=1)
        vif_df = create_VIF_dataframe(new_regression_df)
        high_VIF = (vif_df["VIF"] > threshold).sum()
    return new_regression_df, vif_df

def format_regression_df(dataframe: pd.DataFrame, decades: list,
                         parameters=DEFAULT_PARAMETERS, target_threshold=SUCCESS_THRESHOLD,
                         bad_movies=False) -> tuple:
    """
    Process the dataframe for regression and creates targets and weights vectors.
    
    :param dataframe: Pandas DataFrame containing the data for regression.
    :param decades: List of decades to integrate for regression. 
                    If empty then all decades will be considered.
    :param parameters: Parameter dictionnary to process the dataframe.
    :param target_threshold: Threshold from which we consider a movie as successful.
    :param bad_movies: Indicator if the binary target should be one for movie under threshold.
      
    :return: Tuple with the regression DataFrame, the raw and binary targets and the number of votes.
    """
    parameters["decades"] = decades
    processed_df = process_dataframe(dataframe,parameters)
    # Extract target and associated features.
    target, num_votes= processed_df["average_rating"], processed_df["num_votes"]
    binary_target = target.copy()
    binary_target[binary_target<target_threshold] = 0
    binary_target[binary_target>=target_threshold] = 1
    if bad_movies:
        binary_target = 1-binary_target
    # Remove Unecessary Columns.
    processed_df = processed_df.drop(parameters["post_drop"],axis=1)
    processed_df, vif_df = filter_multicolinearity(processed_df)
    return processed_df, target, binary_target, num_votes

# Pipelines

def get_raw_regression_df() -> pd.DataFrame:
    """
    Create a pandas DataFrame with the basic crafted features for regression.

    :return: Pandas DataFrame with raw data for regression.

    """
    # Load Data
    country_df = pd.read_pickle("../../data/post_processing//country_df.pkl")
    comes_from_df = pd.read_pickle("../../data/post_processing/comes_from_df.pkl")
    genre_df = pd.read_pickle("../../data/post_processing/genre_df.pkl")
    is_of_type_df = pd.read_pickle("../../data/post_processing/is_of_type_df.pkl")
    language_df = pd.read_pickle("../../data/post_processing/language_df.pkl")
    spoken_languages_df = pd.read_pickle("../../data/post_processing/spoken_languages_df.pkl")
    character_df = pd.read_pickle("../../data/post_processing/character_df.pkl")
    actor_df = pd.read_pickle("../../data/post_processing/actor_df.pkl")
    movie_df = pd.read_pickle("../../data/post_processing/movie_df.pkl")
    belongs_to_df = pd.read_pickle("../../data/post_processing/belongs_to_df.pkl")
    play_df = pd.read_pickle("../../data/post_processing/play_df.pkl")
    appears_in_df = pd.read_pickle("../../data/post_processing/appears_in_df.pkl")
    wikipedia_imdb_mapping_table = pd.read_pickle("../../data/generated/wikipedia_imdb_mapping_df.pkl")
    is_directed_by_df = pd.read_pickle("../../data/post_processing/is_directed_by_df.pkl")
    director_df = pd.read_pickle("../../data/post_processing/director_df.pkl")
    # Create DataFrame
    movie_regression_df = movie_df.copy()
    movie_regression_df.drop(["freebase_id","plot"],axis=1,inplace=True)
    movie_regression_df["num_votes"] = movie_regression_df["num_votes"].astype(np.int32)
    # Country features
    country_movie_df = comes_from_df.copy()
    country_movie_df["country_encoding"] = country_movie_df["country_name"].apply(
        lambda c: COUNTRY_CONTINENT_MAPPING[c])
    country_movie_df["country_encoding"] = country_movie_df["country_encoding"].apply(
        lambda c: np.array(COUNTRY_ENCODING[c]))
    for continent in CONTINENT_LIST:
        country_movie_df[continent] = country_movie_df["country_encoding"].apply(
            lambda l: l[CONTINENT_LIST.index(continent)])
        movie_regression_df[continent] = country_movie_df.groupby("movie_id")[continent].max()
    # Actor features
    actor_movie_count = appears_in_df.groupby("actor_id")["movie_id"].count().values
    threshold = np.percentile(actor_movie_count,TOP_ACTOR_PERCENTILE)
    is_actor_above_threshold = appears_in_df.groupby("actor_id")["movie_id"].count().sort_index() >= threshold
    top_k_actors = actor_df[is_actor_above_threshold.values]
    actor_movie_df = appears_in_df.merge(actor_df["gender"],how="left",on="actor_id")
    actor_movie_df["gender"] = actor_movie_df["gender"].apply(
        lambda g: -1 if g == "M" else 1 if g == "F" else g)
    actor_movie_df["is_top_k"] = actor_movie_df["actor_id"].isin(set(top_k_actors.index))
    movie_regression_df["actor_number"] = actor_movie_df.groupby("movie_id")["actor_id"].count()
    movie_regression_df["mean_actor_age"] = actor_movie_df.groupby("movie_id")["actor_age"].mean()
    movie_regression_df["gender_ratio"] = actor_movie_df.groupby("movie_id")["gender"].mean()
    movie_regression_df["has_famous_actor"] = actor_movie_df.groupby("movie_id")["is_top_k"].max()
    movie_regression_df["has_famous_actor"] = movie_regression_df["has_famous_actor"].replace({True: 1, False: 0})
    # Genre features
    genre_movie_df = is_of_type_df.copy()
    genre_movie_df["genre_encoding"] = genre_movie_df["genre_name"].apply(lambda g: GENRE_MAPPING[g])
    genre_movie_df["genre_encoding"] = genre_movie_df["genre_encoding"].apply(
        lambda l: np.sum([np.array(GENRE_ENCODING[g]) for g in l],axis=0))
    for genre in GENRE_LIST:
        genre_movie_df[genre] = genre_movie_df["genre_encoding"].apply(
            lambda l: l[GENRE_LIST.index(genre)])
        movie_regression_df[genre] = genre_movie_df.groupby("movie_id")[genre].max()
    movie_regression_df["genre_number"] = genre_movie_df.groupby("movie_id")["genre_name"].count()
    # Languages features
    language_movie_df = spoken_languages_df.copy()
    top_k_languages = set(language_movie_df.groupby("language_name")["movie_id"].count().sort_values(
        ascending=False).head(K_LANGUAGES).index)
    language_movie_df["top_language"] = language_movie_df["language_name"].isin(top_k_languages)
    movie_regression_df["has_common_language"] = language_movie_df.groupby("movie_id")["top_language"].max()
    movie_regression_df["has_common_language"] = movie_regression_df["has_common_language"].replace({True: 1, False: 0})
    movie_regression_df["language_number"] = language_movie_df.groupby("movie_id")["language_name"].count()
    # Characters features
    top_k_characters_names = set(character_df["character_name"].value_counts().head(K_CHARACTERS).index)
    top_k_characters_ids = set(character_df[character_df["character_name"].isin(top_k_characters_names)].index)
    character_movie_df = belongs_to_df.copy()
    character_movie_df["common_character_name"] = character_movie_df["character_id"].isin(top_k_characters_ids)
    movie_regression_df["has_common_character_name"] = character_movie_df.groupby(
        "movie_id")["common_character_name"].max()
    movie_regression_df["character_number"] = character_movie_df.groupby(
        "movie_id")["character_id"].count()
    movie_regression_df["has_common_character_name"] = movie_regression_df[
        "has_common_character_name"].replace({True: 1, False: 0})
    # Decade feature
    movie_regression_df["decade"] = movie_regression_df["release_date"].apply(lambda d: d.year - d.year%10)
    # Title length feature
    movie_regression_df["title_length"] = movie_regression_df["name"].apply(lambda n: len(n.split()))
    # Director features
    director_movies_mapping = is_directed_by_df.groupby("director_id")["movie_id"].apply(set).to_dict()
    ###   Compute the set of movies directed by the directors for each movie
    director_movies_df = is_directed_by_df.copy()
    director_movies_df["director_movies"] = director_movies_df["director_id"].apply(
        lambda d: director_movies_mapping[d])
    director_movies_df = director_movies_df.groupby("movie_id")["director_movies"].apply(list)
    director_movies_df = director_movies_df.apply(
        lambda movie_list: set([m for movie_set in movie_list for m in list(movie_set)]))
    director_movies_df = pd.DataFrame(director_movies_df)
    ###   Merge DataFrames to recover temporal data and rating
    new_is_directed_by_df = director_movies_df.merge(
        movie_regression_df[["average_rating","release_date"]],how="left",on="movie_id")
    new_is_directed_by_df["combined_features"] = list(zip(new_is_directed_by_df["director_movies"],new_is_directed_by_df["release_date"]))
    ###   Compute performance of the movie directing team up to the release date of each movie.
    new_is_directed_by_df["director_metrics"] = new_is_directed_by_df["combined_features"].apply(
        lambda t: director_metrics_up_to_date(new_is_directed_by_df,t[0],t[1]))
    movie_regression_df["combinned_movie_num"] = new_is_directed_by_df["director_metrics"].apply(lambda t: t[0])
    movie_regression_df["combinned_best_rating"] = new_is_directed_by_df["director_metrics"].apply(lambda t: t[1])
    movie_regression_df["num_directors"] = is_directed_by_df.groupby("movie_id").count()
    movie_regression_df["combinned_movie_success"] = movie_regression_df["combinned_best_rating"] > SUCCESS_THRESHOLD
    movie_regression_df["combinned_movie_success"] = movie_regression_df[
        "combinned_movie_success"].replace({True: 1, False: 0})
    return movie_regression_df


def simple_regression(raw_regression_df: pd.DataFrame, decades: list,
                    parameters=DEFAULT_PARAMETERS,
                    target_threshold=SUCCESS_THRESHOLD, bad_movies=False,
                    alpha=0.05,show=False):
    """
    Perform an OLS regression based on the given raw dataframe.

    :param raw_regression_df: Pandas DataFrame with raw data for regression.
    :param decades: List of decades to integrate for regression. 
                    If empty then all decades will be considered.
    :param parameters: Parameter dictionnary to process the dataframe.
    :param target_threshold: Threshold from which we consider a movie as successful.
    :param bad_movies: Indicator if the binary target should be one for movie under threshold.
    :param alpha: Significance level, default 0.05.
    :param show: Display the different features scores.

    :return: statsmodels linear regression model

    """
    processed_df, target, binary_target, num_votes = format_regression_df(raw_regression_df,decades,
                                                    parameters=parameters,
                                                    target_threshold=target_threshold,bad_movies=bad_movies)
    features = forward_selection(processed_df, target, ignored_features=[], alpha=alpha, show=show)
    model = sm.OLS(target, sm.add_constant(processed_df[features])).fit()
    print(model.summary())
    return model

def decade_pipeline(raw_regression_df: pd.DataFrame, decades: list,
                    parameters=DEFAULT_PARAMETERS,
                    target_threshold=SUCCESS_THRESHOLD, bad_movies=False,
                    alpha=0.05,show=False) -> pd.DataFrame:
    """
    Run a simple regression model per decade based on provided decade list.

    :param raw_regression_df: Pandas DataFrame with raw data for regression.
    :param decades: List of decades for which the function will perform regression. 
    :param parameters: Parameter dictionnary to process the dataframe.
    :param target_threshold: Threshold from which we consider a movie as successful.
    :param bad_movies: Indicator if the binary target should be one for movie under threshold.
    :param alpha: Significance level, default 0.05.
    :param show: Display the different features scores.

    :return: Pandas DataFrame reporting the r-squared score per decade.

    """
    decade_results = dict()
    for decade in decades:
        model = simple_regression(raw_regression_df,decades,parameters=parameters,
                                    target_threshold=target_threshold,bad_movies=bad_movies,
                                    alpha=alpha,show=show)
        decade_results[decade] = model.rsquared
    decade_results_df = pd.DataFrame(decade_results.values(),index=decade_results.keys(),
                                    columns=["r-squared"]).sort_index()
    return decade_results_df