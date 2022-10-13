import stories
import uuid0
stories_DB = {}


def fill_stories_DB():
    """fills the stories_DB dictionary with a key of the story id and
    the values is an instace of Story"""
    with open('storiesDB.txt') as f:
        data = f.read()
    # strip EOL
    data = data.strip()
    for line in data.split('\n'):
        id, title, words, text = [item for item in line.split('/')]
        list_of_words = [word for word in words.split(',')]
        stories_DB[id] = stories.Story(id, title, list_of_words, text)


def submit_story(title, story):
    """takes the title and story from the users form and creates a string formatting to the 
    standard set for all stories in the storiesDB.txt"""
    id = str(uuid0.generate())
    text_nopunk = story.replace('.', '').replace(
        ',', '').replace('!', '').replace('?', '')
    text_list = text_nopunk.split()
    words_list = [x for x in text_list if x.startswith('{')]
    words_str = ','.join(words_list).replace('{', '').replace('}', '')
    parsed_story = ' '.join([x.strip() for x in story.splitlines()])
    data = '/'.join([id, title, words_str, parsed_story])
    with open('storiesDB.txt', 'a') as file:
        file.write(data + '\n')
    fill_stories_DB()
