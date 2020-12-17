from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
app=Flask(__name__)
app.config['SECRET_KEY'] = "chickens"
debug= DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def home_page():
    my_prompts = story.prompts
    return render_template("home_page.html", descriptive_words = my_prompts)

@app.route('/story')
def create_madlib():
    my_prompts=story.prompts
    my_answers={}
    for prompt in my_prompts:
         user_input = request.args[f"{prompt}"]
         my_answers[prompt]=user_input
    # the result of my_answers should be a list of the user inputs
    my_story = story.generate(my_answers)
    return render_template("story.html", my_story=my_story)

    #ok so maybe instead of creating a list in the for-loop, create a dict since that's what we need to pass
    #intp the generate method. K that