from .headline_aljaz import get_aljaz_words
from .headline_cnn import get_cnn_words
from .headline_fox import get_fox_words
from .headline_nyt import get_nyt_words
from .headline_theblaze import get_theblaze_words
from .headline_wsj import get_wsj_words
from models.words import WordModel

def scrape_words(name):
    if name == "aljaz":
        return get_aljaz_words()
    elif name == "cnn":
        return get_cnn_words()
    elif name == "fox":
        return get_fox_words()
    elif name == "nyt":
        return get_nyt_words()
    elif name == "theblaze":
        return get_theblaze_words()
    elif name == "wsj":
        return get_wsj_words()

def update_single(name):
    news_org = WordModel.find_by_name(name)
    print (news_org)
    # if news_org cannot be found, add new
    if news_org is None:
        new = WordModel(name, scrape_words(name))
        new.save_to_db()
    else:
        news_org.words = scrape_words(name)
        news_org.save_to_db()
    # if found, load new, and
    # news_org.words = scrape_words(name)
    # news_org.save_to_db()

def update_all():
    all_news_orgs = ["aljaz", "cnn", "fox", "nyt", "theblaze", "wsj"]
    for name in all_news_orgs:
        update_single(name)
