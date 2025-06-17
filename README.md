# mood-food-journal
This is my final project for CS50. It is a command-line application that allows users to log the food they eat and the mood they experience afterward.

## Features
- Add new food/mood entries
- View past entries
- Store logs in a CSV file

## How to Run
In the terminal, run: python mood_food_journal.py

## Acknowledgments
structural help and suggestions from ChatGPT, but all code written and understood by me.

This is my final project for CS50 — it’s called Mood + Food Journal. I built it as a command-line app where people (or me, honestly) can track what they eat and how they feel. The whole idea came from this curiosity I’ve had about whether certain foods actually affect my mood. Like, do I always feel sluggish after eating a big lunch? Or more calm when I eat simple meals? That kind of thing.

So this program lets you log meals and moods and check for patterns. It’s not fancy or scientific, but it gives you a way to look back and maybe notice connections. I wanted it to feel simple enough that I’d actually use it.

Files (and What They Do)
I ended up splitting the project into a few different files so things didn’t get too messy. Here’s what each one does:

mood_food_journal.py – This is the main file. Basically, it runs the whole app, shows the menu, and connects all the other parts.

data_handler.py – Handles saving and loading journal entries from a JSON file. I didn't want to deal with a full database, so I just stuck with flat files.

analytics.py – Looks at the data and tries to do some basic mood analysis. Nothing too complex — mostly average mood scores and rough trends.

exporter.py – If someone wants to take their data and open it in Excel or whatever, this makes a CSV file out of it.

utils.py – Just has little helper functions I used in more than one place. For example, checking date formats or cleaning up text.

sample_data/ – I kept some example JSON files here to test stuff while I was coding. Not required, but helpful for me.

.gitignore – Pretty standard. I didn’t want Git tracking things like .DS_Store or cache folders.

Some Decisions I Had to Make
I wasn’t sure at first how to store the data. I looked into using SQLite or something more structured, but it honestly felt like overkill. JSON made more sense — it’s readable, and Python handles it easily.

For moods, I thought about having categories like “happy,” “anxious,” or whatever, but then I figured people feel things differently. So I just let them rate their mood from 1 to 10 and add a little description if they want.

Also, I debated whether to make this visual — like maybe add graphs — but I decided not to because I wanted to keep things light. I didn’t want to get stuck dealing with a bunch of chart libraries for what’s basically a journaling tool.

Stuff That Was Kind of a Pain
Time and date input was harder than I expected. Like, if someone writes "2pm" or "14:00" or forgets the colon, I had to figure out how to catch those cases and not crash everything. I think I got it mostly working, but it took a bit of trial and error.

Trying to find patterns between moods and meals was also a bit fuzzy. There’s only so much you can do without real stats or machine learning, and I didn’t want to make wild guesses. So I just stuck to showing averages and basic summaries for now.

Also just getting the flow of the menu right took a few tries. Like, do you go back to the menu after logging something? Should you get a confirmation message? These small things actually made a difference in how smooth it felt.

Things I’d Probably Add Later
Some sort of tagging system for meals, like “gluten-free,” “sugary,” or “comfort food” so you could filter moods by type of food

Graphs showing mood over time (maybe with colors or something)

A way to set reminders to check in, like after meals or at night

Privacy settings or even password protection (right now it's just open)

Maybe even a web version someday, if I keep working on it

Wrapping It Up
Making this taught me a lot — not just about Python or file handling, but about keeping code organized and thinking through how a user (even just me) would interact with a tool like this. It’s definitely not perfect, and there are rough edges for sure, but I kind of like that. It feels like something I made, and I actually use it. That’s a win in my book.

