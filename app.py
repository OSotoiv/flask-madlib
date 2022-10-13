from crypt import methods
# from re import X
from flask import Flask, request, render_template, redirect
import stories
import helpers

app = Flask(__name__)


@app.route("/")
def home():
    """show home/landing page"""
    helpers.fill_stories_DB()
    return render_template("base.html")


@app.route('/about')
def about():
    """show about page"""
    return render_template("about.html")


@app.route('/stories')
def stories():
    """show all avalible stories"""
    return render_template("stories.html", stories=helpers.stories_DB)


@app.route('/get_subs/<story_id>')
def get_subs(story_id):
    """show words for the user to substitue"""
    story = helpers.stories_DB[story_id]
    # request.args is for q string
    # story_id = request.args['madlib-story']
    # words = story.prompts
    return render_template('getsubs.html', story=story)


@app.route('/generate/<story_id>', methods=['POST'])
def generate(story_id):
    """gnerate a story with the substituted words from the user.
    each story instance has a generate method"""
    story = helpers.stories_DB[story_id]
    story_text = story.generate(request.form)
    return render_template("show.html", text=story_text, story=story)


@app.route('/write_story')
def write_story():
    """show the template for createing your own story"""
    return render_template("write.html")


@app.route('/create', methods=['POST'])
def create_story():
    """submit the users story and redirect to show all stories"""
    title = request.form['title']
    story = request.form['story']
    helpers.submit_story(title, story)
    return redirect('/stories')
