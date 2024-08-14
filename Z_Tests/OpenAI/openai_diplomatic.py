#python3 pyopen.py > output.mdx

import os
from dotenv import load_dotenv
from openai import OpenAI  # pip install openai==1.30.5

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
)

diplomatic_en= """

Diplomatic Vocabulary

1. Rephrasing negative sentences	I am unhappy with the progress. → I am not entirely happy with the progress./ I am not totally happy with the progress.
Her report was very bad. → Her report was not really up to standard.
not really + positive word
not entirely + positive word
not totally + positive word
2. Softeners	
Unfortunately…
I’m afraid (that)…
I’m sorry but…
Sorry but…
To be honest…
I haven’t finished the task. → I’m afraid I haven’t finished the task.
We have to cancel the trip. → I am sorry but we have to cancel the trip.
3. Restrictive phrases	
yet
at this stage
at the moment
so far
to some extent
to some degree.
I’m afraid I haven’t finished the task yet.
Unfortunately, I don’t know the answer at the moment.
4. Minimizing words	
a little
a bit
a little bit
slight
slightly
really
somewhat
His presentation was a bit long
You are somewhat late for the meeting.
5. Opinion phrases	
In my opinion
From my point of view
As far as I know
As I see it
From my perspective
The candidate’s technical skills are below average. → Overall, I feel that the candidate’s technical skills are below average.
6. Tentative verbs	
It appears that
seem to
suppose
look like
tend to
guess
suggest
Mark has some difficulties in building rapport with the team. → Mark seems to have some difficulties in building rapport with the team. OR Mark tends to have some difficulties in building rapport with the team.
It appears that Mark has some difficulties in building rapport with the team.
"""

indirect_qq = """

Indirect questions

Sample questions	I’d like to know what the deadline is.
Could you tell me how long it will take?
We wonder if we could move the release date.
Do you have any idea if he has finished the tests?
Form	Introductory phrase + question word + positive sentence*
Introductory phrase + if/whether + positive sentence*
*positive sentence: subject + verb + other sentence parts
Introductory phrases:	Do you know ...
I wonder / was wondering ...
Can / Could you tell me ...
Do you happen to know ...
Do you have any idea ...
Would you mind telling me...
May I ask...
I'd like to know ...
Rules overview:	1. Questions with question words: where, what, when, how, why and which, etc.
Standard question:
When is the deadline?
How long will it take?
Indirect Question: Introductory phrase + question word + positive sentence
Indirect Questions:
I’d like to know when the deadline is.
Could you tell me how long it will take?

2. Questions with auxiliaries: do/does, have/has, was/were, will, can, could, may, might, etc.
Standard question:
Could we move the release date a bit?
Has he finished the tests?
Indirect Question: Introductory phrase + if/whether + positive sentence
Indirect Questions:
We wonder if we could move the release date a bit.
Do you have any idea whether he has finished the tests?

"""

tag_qq = """
Sample sentences	The reports are ready, aren't they?
They make electric cars, don't they?
You won't forget, will you?
They can't both be right, can they?
Form	We normally form question tags in the following way:
positive verb + negative tag
negative verb + positive tag
e.g.
We are meeting next week, aren't we?
We aren't meeting next week, are we?
Rules overview:	1. If the statement uses a modal verb, it is repeated in the tag.
You can finish the testing, can’t you?
You shouldn’t reply immediately, should you?

2. With the Simple Present Tense we use do / does OR don’t / doesn't.
With the Simple Past Tense we use did / didn't.
They work overtime a lot, don’t they?
You didn’t see the presentation yesterday, did you?

3. With other tenses, we just use the auxiliary.
They haven’t performed the testing yet, have they?
We will deliver on time, won’t we?

4. If the subject of the statement is somebody, anybody, nobody, everybody, no one, and neither, we use the pronoun they in question tag.
Somebody entered the garden, didn't they?
Everybody was upset, weren't they?
Exceptions	1. After ‘I am’ the tag is aren't I?
I am late, aren't I?
BUT: I am not late, am I?

2. After let’s the tag is shall.
Let's go start the meeting, shall we?
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """You are an expert meeting assistant. Very aware of the following:
                                
                        """,
        },
        {"role": "user", "content": "Who are you and what can you do?"}

    ],
    model="gpt-4o-mini",
    temperature=0.7,
)

# print(chat_completion)
# Extract and print the content of the completed message
completed_message = chat_completion.choices[0].message.content
print(completed_message)