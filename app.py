import random
import streamlit as st

st.set_page_config(
    page_title="TOEFL iBT - Build a Sentence (100 Practice Set)", page_icon="✏️"
)

st.title("✏️ TOEFL iBT: Build a Sentence Practice")
st.write(
    "Reorder the word chunks to build a grammatically correct sentence completing Speaker B's response."
)

# 100 Authentic TOEFL iBT Practice Questions across B1, B2, and C1 levels
questions = [
    # --- B1 LEVEL (1–33) ---
    {
        "level": "B1",
        "speaker_a": "Do you know where the campus library is located?",
        "chunks": ["He asked me", "if I knew", "where", "the library was"],
        "explanation": "In embedded questions, use normal statement word order (Subject + Verb: 'the library was'), not question order.",
    },
    {
        "level": "B1",
        "speaker_a": "Are you going to the dining hall for lunch?",
        "chunks": [
            "I will go",
            "as soon as",
            "I finish",
            "my chemistry assignment",
        ],
        "explanation": "Use the present simple ('I finish') in time clauses introduced by 'as soon as', even when referring to future actions.",
    },
    {
        "level": "B1",
        "speaker_a": "Why didn't you turn in your history essay on time?",
        "chunks": [
            "Because I had",
            "too much work",
            "to complete",
            "before midnight",
        ],
        "explanation": "Use 'too much' with uncountable nouns like 'work' followed by an infinitive verb phrase.",
    },
    {
        "level": "B1",
        "speaker_a": "Is the professor still accepting late submissions?",
        "chunks": [
            "She said that",
            "she would accept",
            "them until",
            "five o'clock",
        ],
        "explanation": "When reporting speech in the past, 'will' shifts to 'would' in the reported clause.",
    },
    {
        "level": "B1",
        "speaker_a": "How often do you study with your study group?",
        "chunks": [
            "We usually meet",
            "twice a week",
            "at the",
            "student center",
        ],
        "explanation": "Adverbs of frequency like 'usually' come before the main verb.",
    },
    {
        "level": "B1",
        "speaker_a": "Did you enjoy the lecture on environmental science?",
        "chunks": [
            "It was much",
            "more interesting than",
            "I expected",
            "it to be",
        ],
        "explanation": "Use 'more... than' for comparative adjectives with three or more syllables.",
    },
    {
        "level": "B1",
        "speaker_a": "Where should I put these extra textbooks?",
        "chunks": [
            "You can place",
            "them on top",
            "of the shelf",
            "near the door",
        ],
        "explanation": "Prepositional phrases indicating location should follow the direct object.",
    },
    {
        "level": "B1",
        "speaker_a": "Why are you taking an extra class this semester?",
        "chunks": [
            "In order to",
            "graduate early,",
            "I need to",
            "pass one more course",
        ],
        "explanation": "'In order to' introduces a purpose clause followed by a base verb.",
    },
    {
        "level": "B1",
        "speaker_a": "Did Mark call you about the project meeting?",
        "chunks": [
            "He promised to",
            "call me back",
            "after his class",
            "was finished",
        ],
        "explanation": "Phrasal verbs with pronoun objects place the pronoun between the verb and particle ('call me back').",
    },
    {
        "level": "B1",
        "speaker_a": "What did you think of the new campus cafeteria?",
        "chunks": [
            "The food is",
            "good enough,",
            "but it is",
            "too expensive",
        ],
        "explanation": "'Enough' follows the adjective it modifies ('good enough'), while 'too' precedes it ('too expensive').",
    },
    {
        "level": "B1",
        "speaker_a": "How long have you been studying English?",
        "chunks": [
            "I have been",
            "learning English for",
            "more than three",
            "years now",
        ],
        "explanation": "Use the present perfect continuous with 'for' to describe actions starting in the past and continuing today.",
    },
    {
        "level": "B1",
        "speaker_a": "Are you ready to give your presentation?",
        "chunks": [
            "I am nervous,",
            "but I have",
            "practiced it many",
            "times already",
        ],
        "explanation": "Present perfect tense ('have practiced') connects past preparation with present readiness.",
    },
    {
        "level": "B1",
        "speaker_a": "Why is the registration portal not working?",
        "chunks": [
            "There are too",
            "many students trying",
            "to log in",
            "at once",
        ],
        "explanation": "Use 'there are' with plural countable nouns ('students').",
    },
    {
        "level": "B1",
        "speaker_a": "Will you attend the career fair on Friday?",
        "chunks": [
            "I plan to go",
            "unless I have",
            "to review for",
            "my midterm exam",
        ],
        "explanation": "'Unless' means 'if not' and takes a positive verb clause in the present simple.",
    },
    {
        "level": "B1",
        "speaker_a": "Who borrowed your notes from yesterday's class?",
        "chunks": [
            "A classmate who",
            "missed the lecture",
            "asked if he",
            "could copy them",
        ],
        "explanation": "Relative clause ('who missed the lecture') correctly modifies the subject noun ('classmate').",
    },
    {
        "level": "B1",
        "speaker_a": "What should we do if it rains during the campus tour?",
        "chunks": [
            "We will move",
            "the activities inside",
            "to the main",
            "auditorium building",
        ],
        "explanation": "First conditional uses future simple ('will move') in the main clause after an 'if' condition.",
    },
    {
        "level": "B1",
        "speaker_a": "Did you manage to reserve a private study room?",
        "chunks": [
            "All the rooms",
            "were already booked",
            "when I checked",
            "the system",
        ],
        "explanation": "Passive voice ('were booked') combined with a time clause ('when I checked').",
    },
    {
        "level": "B1",
        "speaker_a": "Why did Sarah leave the seminar so early?",
        "chunks": [
            "She had to",
            "catch a bus",
            "that leaves at",
            "four o'clock",
        ],
        "explanation": "Modal 'had to' expresses past necessity, paired with a restrictive relative clause ('that leaves...').",
    },
    {
        "level": "B1",
        "speaker_a": "Have you seen the advisor about your schedule yet?",
        "chunks": [
            "Not yet, but",
            "I intend to",
            "make an appointment",
            "tomorrow morning",
        ],
        "explanation": "'Intend' is followed by a full infinitive ('to make').",
    },
    {
        "level": "B1",
        "speaker_a": "Why are you buying so many index cards?",
        "chunks": [
            "They help me",
            "memorize key terms",
            "for the upcoming",
            "vocabulary quiz",
        ],
        "explanation": "The verb 'help' takes an object followed by a bare or full infinitive ('help me memorize').",
    },
    {
        "level": "B1",
        "speaker_a": "Did you know that the biology test was postponed?",
        "chunks": [
            "Yes, the professor",
            "sent an email",
            "explaining the change",
            "this morning",
        ],
        "explanation": "Participle phrase ('explaining the change') post-modifies the noun 'email'.",
    },
    {
        "level": "B1",
        "speaker_a": "Is it required to wear safety goggles in the lab?",
        "chunks": [
            "Everyone must wear",
            "them at all",
            "times while inside",
            "the room",
        ],
        "explanation": "Modal 'must' indicates obligation, followed by the bare infinitive ('wear').",
    },
    {
        "level": "B1",
        "speaker_a": "Where can I find the syllabus for this course?",
        "chunks": [
            "It is posted",
            "on the homepage",
            "under the section",
            "labeled documents",
        ],
        "explanation": "Prepositional placement establishing location hierarchy (page -> section -> label).",
    },
    {
        "level": "B1",
        "speaker_a": "Why didn't you join the student council?",
        "chunks": [
            "I did not",
            "have enough time",
            "to attend their",
            "weekly meetings",
        ],
        "explanation": "'Enough' precedes uncountable nouns ('enough time') followed by an infinitive.",
    },
    {
        "level": "B1",
        "speaker_a": "Did you complete the reading assignment for tomorrow?",
        "chunks": [
            "I read half",
            "of the chapter",
            "before I fell",
            "asleep last night",
        ],
        "explanation": "Past simple sequence indicating consecutive completed actions.",
    },
    {
        "level": "B1",
        "speaker_a": "How do I sign up for tutoring sessions?",
        "chunks": [
            "You just need",
            "to fill out",
            "the online form",
            "on the website",
        ],
        "explanation": "Phrasal verb 'fill out' takes a direct object noun phrase ('the online form').",
    },
    {
        "level": "B1",
        "speaker_a": "Why is the library closing early today?",
        "chunks": [
            "Because there is",
            "a staff meeting",
            "scheduled for this",
            "afternoon at three",
        ],
        "explanation": "Past participle 'scheduled' functions as a reduced relative clause modifying 'meeting'.",
    },
    {
        "level": "B1",
        "speaker_a": "Which dormitory are you living in this semester?",
        "chunks": [
            "I am living",
            "in the same",
            "building that I",
            "stayed in last year",
        ],
        "explanation": "Relative clause with preposition at the end ('stayed in').",
    },
    {
        "level": "B1",
        "speaker_a": "Did you pass the computer science exam?",
        "chunks": [
            "Yes, although it",
            "was much harder",
            "than I had",
            "thought it would be",
        ],
        "explanation": "Conjunction 'although' introduces a clause of concession.",
    },
    {
        "level": "B1",
        "speaker_a": "How can I improve my spoken English?",
        "chunks": [
            "By practicing with",
            "native speakers whenever",
            "you have an",
            "opportunity to do so",
        ],
        "explanation": "Preposition 'by' + gerund ('practicing') shows method/means.",
    },
    {
        "level": "B1",
        "speaker_a": "Are you going to join the university choir?",
        "chunks": [
            "I would like",
            "to join if",
            "I can find",
            "the extra time",
        ],
        "explanation": "'Would like to' followed by a present real condition clause ('if I can find').",
    },
    {
        "level": "B1",
        "speaker_a": "What should I bring to the orientation session?",
        "chunks": [
            "Make sure to",
            "bring your student",
            "identification card and",
            "a notepad",
        ],
        "explanation": "Imperative structure 'make sure to' takes an infinitive verb phrase.",
    },
    {
        "level": "B1",
        "speaker_a": "Why was the lecture hall so crowded today?",
        "chunks": [
            "Many students came",
            "to hear the",
            "guest speaker talk",
            "about climate change",
        ],
        "explanation": "Infinitive of purpose ('to hear') followed by object + bare infinitive ('speaker talk').",
    },
    # --- B2 LEVEL (34–67) ---
    {
        "level": "B2",
        "speaker_a": "Are you going to the biology review session tonight?",
        "chunks": [
            "I would go",
            "if I didn't have",
            "to work late",
            "at the lab",
        ],
        "explanation": "In second conditional clauses, use the simple past after 'if' ('if I didn't have'), not 'would'.",
    },
    {
        "level": "B2",
        "speaker_a": "Why was the professor unhappy with the final draft?",
        "chunks": [
            "The paper involved",
            "analyzing data",
            "collecting samples",
            "and writing reports",
        ],
        "explanation": "Maintain parallel structure when listing actions (gerunds: analyzing, collecting, and writing).",
    },
    {
        "level": "B2",
        "speaker_a": "Did the research team submit their manuscript?",
        "chunks": [
            "Not only did they",
            "submit the manuscript,",
            "but they also",
            "presented their findings",
        ],
        "explanation": "Inversion occurs after initial negative adverbial phrases like 'not only did they'.",
    },
    {
        "level": "B2",
        "speaker_a": "How did the student react to winning the fellowship?",
        "chunks": [
            "So surprised was",
            "she by the news",
            "that she could",
            "barely speak",
        ],
        "explanation": "Adjective inversion with 'so... that' structure ('So surprised was she...').",
    },
    {
        "level": "B2",
        "speaker_a": "What caused the delay in completing the experiment?",
        "chunks": [
            "Had the lab",
            "equipment arrived earlier,",
            "we would have",
            "finished on time",
        ],
        "explanation": "Inverted third conditional eliminates 'if' by starting with 'Had + Subject + Past Participle'.",
    },
    {
        "level": "B2",
        "speaker_a": "Why is attendance mandatory for all seminars?",
        "chunks": [
            "It is essential",
            "that every student",
            "attend all scheduled",
            "sessions regularly",
        ],
        "explanation": "Subjunctive mood requires the base form of the verb ('attend') after 'essential that'.",
    },
    {
        "level": "B2",
        "speaker_a": "Did you find any errors in the financial report?",
        "chunks": [
            "Despite checking the",
            "numbers repeatedly, we",
            "found no significant",
            "discrepancies",
        ],
        "explanation": "'Despite' is a preposition and must be followed by a noun phrase or gerund ('checking').",
    },
    {
        "level": "B2",
        "speaker_a": "Why was the proposal rejected by the committee?",
        "chunks": [
            "The committee rejected",
            "it due to",
            "a lack of",
            "sufficient funding",
        ],
        "explanation": "'Due to' acts as a prepositional phrase followed by a noun phrase ('a lack of...').",
    },
    {
        "level": "B2",
        "speaker_a": "How should we organize the survey responses?",
        "chunks": [
            "The data, once",
            "collected and categorized,",
            "will be uploaded",
            "to the database",
        ],
        "explanation": "Participle phrases ('once collected and categorized') offset by commas modify the subject.",
    },
    {
        "level": "B2",
        "speaker_a": "Will the university build a new sports facility?",
        "chunks": [
            "Provided that the",
            "board approves the",
            "budget next week,",
            "construction will begin",
        ],
        "explanation": "'Provided that' introduces a conditional clause operating like 'if'.",
    },
    {
        "level": "B2",
        "speaker_a": "Why did the author use such complex terminology?",
        "chunks": [
            "The author intended",
            "to target an",
            "academic audience rather",
            "than general readers",
        ],
        "explanation": "Comparative structure 'rather than' connects parallel noun phrases.",
    },
    {
        "level": "B2",
        "speaker_a": "Did you complete the online safety training?",
        "chunks": [
            "Having completed the",
            "module last night,",
            "I submitted my",
            "certificate this morning",
        ],
        "explanation": "Perfect participle ('Having completed') expresses an action completed prior to the main verb.",
    },
    {
        "level": "B2",
        "speaker_a": "What makes this psychology theory so influential?",
        "chunks": [
            "It accounts for",
            "behavioral changes that",
            "previous models were",
            "unable to explain",
        ],
        "explanation": "Phrasal verb 'accounts for' takes a relative clause defining 'behavioral changes'.",
    },
    {
        "level": "B2",
        "speaker_a": "Why are students protesting the new policy?",
        "chunks": [
            "They object to",
            "being required to",
            "pay additional fees",
            "for parking",
        ],
        "explanation": "The expression 'object to' requires a gerund ('being') as its prepositional object.",
    },
    {
        "level": "B2",
        "speaker_a": "Did the dean confirm the new grant approval?",
        "chunks": [
            "She confirmed that",
            "the grant would",
            "be disbursed within",
            "thirty business days",
        ],
        "explanation": "Passive infinitive ('be disbursed') following modal 'would' in indirect speech.",
    },
    {
        "level": "B2",
        "speaker_a": "How does the sound system work in this auditorium?",
        "chunks": [
            "The microphones are",
            "designed to adjust",
            "automatically depending on",
            "the room acoustics",
        ],
        "explanation": "Prepositional combination 'depending on' modifies clause verb action.",
    },
    {
        "level": "B2",
        "speaker_a": "Why was the conference location moved online?",
        "chunks": [
            "In light of",
            "recent travel restrictions,",
            "the organizers decided",
            "to host it virtually",
        ],
        "explanation": "Idiomatic complex preposition 'in light of' introduces surrounding context.",
    },
    {
        "level": "B2",
        "speaker_a": "Did the student body vote on the amendment?",
        "chunks": [
            "The measure passed",
            "with a narrow",
            "majority despite strong",
            "opposition from faculty",
        ],
        "explanation": "Preposition 'despite' sets up contrast against a noun phrase ('strong opposition').",
    },
    {
        "level": "B2",
        "speaker_a": "What is required to maintain a scholarship?",
        "chunks": [
            "Students are expected",
            "not only to",
            "maintain high grades",
            "but to volunteer",
        ],
        "explanation": "Correlative conjunction 'not only... but...' linking infinitives ('to maintain', 'to volunteer').",
    },
    {
        "level": "B2",
        "speaker_a": "Why did the experiment produce inconsistent results?",
        "chunks": [
            "The variation was",
            "attributed to fluctuations",
            "in the room",
            "temperature during testing",
        ],
        "explanation": "Passive verb 'was attributed to' followed by noun phrase cause.",
    },
    {
        "level": "B2",
        "speaker_a": "How will the university handle overcrowding in dorms?",
        "chunks": [
            "By converting several",
            "administrative offices into",
            "temporary living spaces",
            "for incoming freshmen",
        ],
        "explanation": "Gerund phrase ('By converting...') answering a 'how' method question.",
    },
    {
        "level": "B2",
        "speaker_a": "Was the historic building renovated recently?",
        "chunks": [
            "The structure was",
            "restored to its",
            "original condition using",
            "traditional architecture methods",
        ],
        "explanation": "Participle clause ('using traditional...') specifying method appended to main passive clause.",
    },
    {
        "level": "B2",
        "speaker_a": "Why are you taking advanced calculus?",
        "chunks": [
            "I am taking",
            "it so that",
            "I can fulfill",
            "the engineering prerequisites",
        ],
        "explanation": "Conjunction 'so that' introduces a clause of purpose with modal verb 'can'.",
    },
    {
        "level": "B2",
        "speaker_a": "How did the department improve student retention?",
        "chunks": [
            "They implemented a",
            "mentorship program aimed",
            "at supporting struggling",
            "first-year students",
        ],
        "explanation": "Past participle modifier ('aimed at') followed by preposition + gerund ('at supporting').",
    },
    {
        "level": "B2",
        "speaker_a": "Did the professor mention what will be on the exam?",
        "chunks": [
            "He emphasized that",
            "students should focus",
            "on the topics",
            "discussed in chapter four",
        ],
        "explanation": "Indirect statement controlling sub-clause with prepositional verb ('focus on').",
    },
    {
        "level": "B2",
        "speaker_a": "Why is the library restricting access next weekend?",
        "chunks": [
            "To allow workers",
            "to install new",
            "digital catalog systems",
            "throughout the building",
        ],
        "explanation": "Infinitive clause of purpose ('To allow...') introducing object + infinitive structure.",
    },
    {
        "level": "B2",
        "speaker_a": "Has the guest lecturer arrived on campus?",
        "chunks": [
            "Her flight was",
            "delayed; nevertheless, she",
            "is expected to",
            "arrive before noon",
        ],
        "explanation": "Conjunctive adverb 'nevertheless' showing transition between independent clauses.",
    },
    {
        "level": "B2",
        "speaker_a": "Why did you choose history as your major?",
        "chunks": [
            "What interests me",
            "most is learning",
            "how past events",
            "shape modern society",
        ],
        "explanation": "Wh-cleft sentence ('What interests me most is...') used for emphasis.",
    },
    {
        "level": "B2",
        "speaker_a": "Did the campus newspaper publish your article?",
        "chunks": [
            "They agreed to",
            "print it provided",
            "I shorten the",
            "length by half",
        ],
        "explanation": "Conditional conjunction 'provided' taking present simple condition.",
    },
    {
        "level": "B2",
        "speaker_a": "Why are all outdoor athletic events canceled?",
        "chunks": [
            "On account of",
            "the severe thunderstorm",
            "warning issued by",
            "the weather service",
        ],
        "explanation": "Complex preposition 'on account of' followed by noun phrase and participle modifier.",
    },
    {
        "level": "B2",
        "speaker_a": "How did the team resolve the software bug?",
        "chunks": [
            "By rewriting the",
            "code, they eliminated",
            "the problem without",
            "delaying the release",
        ],
        "explanation": "Prepositional gerund phrases ('By rewriting...', 'without delaying...') establishing process.",
    },
    {
        "level": "B2",
        "speaker_a": "Is the new science building operational yet?",
        "chunks": [
            "Although construction is",
            "complete, interior equipment",
            "has yet to",
            "be fully installed",
        ],
        "explanation": "'Has yet to be' structure indicating something that must still occur in the passive.",
    },
    {
        "level": "B2",
        "speaker_a": "Why did the board revise the graduation requirements?",
        "chunks": [
            "With a view",
            "to improving standards,",
            "they raised the",
            "minimum GPA needed",
        ],
        "explanation": "Formal prepositional phrase 'with a view to' followed by a gerund ('improving').",
    },
    # --- C1 LEVEL (68–100) ---
    {
        "level": "C1",
        "speaker_a": "What was the main conclusion of the symposium?",
        "chunks": [
            "Scarcely had the",
            "keynote speaker finished",
            "when the audience",
            "erupted in applause",
        ],
        "explanation": "Inversion with negative adverbial 'scarcely had... when' for sudden sequential past events.",
    },
    {
        "level": "C1",
        "speaker_a": "How does the new policy affect graduate assistants?",
        "chunks": [
            "Under no circumstances",
            "are graduate assistants",
            "permitted to exceed",
            "twenty hours weekly",
        ],
        "explanation": "Fronted negative expression 'under no circumstances' forces subject-auxiliary inversion.",
    },
    {
        "level": "C1",
        "speaker_a": "Why did the research project receive national recognition?",
        "chunks": [
            "Seldom have scientists",
            "uncovered such compelling",
            "evidence in support",
            "of climate restoration",
        ],
        "explanation": "Restrictive adverb 'seldom' fronted for emphasis requiring subject-verb inversion.",
    },
    {
        "level": "C1",
        "speaker_a": "Will the university proceed with the budget cuts?",
        "chunks": [
            "Were the board",
            "to approve cuts,",
            "faculty members would",
            "protest the decision",
        ],
        "explanation": "Inverted formal hypothetical conditional ('Were the board to approve...').",
    },
    {
        "level": "C1",
        "speaker_a": "How should the committee evaluate these complex proposals?",
        "chunks": [
            "Crucial to the",
            "decision-making process is",
            "the thorough evaluation",
            "of environmental impacts",
        ],
        "explanation": "Subject-complement inversion placing the predicate adjective ('crucial') first.",
    },
    {
        "level": "C1",
        "speaker_a": "Why was the rare manuscript kept under glass?",
        "chunks": [
            "So fragile were",
            "the ancient parchment",
            "pages that researchers",
            "wore protective gloves",
        ],
        "explanation": "Predicate adjective fronting ('So fragile were the pages that...').",
    },
    {
        "level": "C1",
        "speaker_a": "Did the study establish a causal relationship?",
        "chunks": [
            "Only by controlling",
            "all external variables",
            "could the researchers",
            "isolate the effect",
        ],
        "explanation": "'Only by' fronting forces auxiliary inversion in main clause ('could the researchers').",
    },
    {
        "level": "C1",
        "speaker_a": "What makes this literary work so challenging to interpret?",
        "chunks": [
            "Rich in metaphor",
            "and subtle irony,",
            "the text demands",
            "meticulous analytical reading",
        ],
        "explanation": "Fronted adjective phrase functioning as a descriptive modifier before main subject.",
    },
    {
        "level": "C1",
        "speaker_a": "Why did the administration modify the tenure criteria?",
        "chunks": [
            "Far from discouraging",
            "research output, the",
            "new rules incentivize",
            "interdisciplinary collaboration instead",
        ],
        "explanation": "Prepositional phrase 'far from' + gerund establishing strong contrast.",
    },
    {
        "level": "C1",
        "speaker_a": "How did the archeological team date the artifacts?",
        "chunks": [
            "Little did they",
            "realize that the",
            "stratum contained artifacts",
            "from two eras",
        ],
        "explanation": "Negative adverb 'little' fronted causes past simple inversion ('did they realize').",
    },
    {
        "level": "C1",
        "speaker_a": "Is the university liable for loss of personal property?",
        "chunks": [
            "In no way",
            "can the institution",
            "be held responsible",
            "for unmonitored items",
        ],
        "explanation": "'In no way' fronted requires subject modal inversion ('can the institution').",
    },
    {
        "level": "C1",
        "speaker_a": "What was the outcome of the faculty negotiations?",
        "chunks": [
            "No sooner had",
            "the agreement been",
            "signed than implementation",
            "began immediately across departments",
        ],
        "explanation": "Correlative structure 'no sooner had... than' with inverted past perfect.",
    },
    {
        "level": "C1",
        "speaker_a": "Why is formal writing style emphasized in academic papers?",
        "chunks": [
            "It is through",
            "precise terminology that",
            "scholars convey complex",
            "ideas without ambiguity",
        ],
        "explanation": "It-cleft sentence used for formal emphasis ('It is through X that...').",
    },
    {
        "level": "C1",
        "speaker_a": "Did the economic forecast predict this market shift?",
        "chunks": [
            "Hardly had the",
            "report been published",
            "when market trends",
            "shifted unexpectedly downward",
        ],
        "explanation": "Inversion using 'hardly had... when' for instantaneous sequential actions.",
    },
    {
        "level": "C1",
        "speaker_a": "Why did the scientist reject the initial hypothesis?",
        "chunks": [
            "Inconsistent with observed",
            "experimental data, the",
            "hypothesis was deemed",
            "untenable by reviewers",
        ],
        "explanation": "Adjective phrase fronting modifying the subject 'hypothesis'.",
    },
    {
        "level": "C1",
        "speaker_a": "How will the university fund the new research wing?",
        "chunks": [
            "Should private donations",
            "fall short of",
            "projections, institutional reserves",
            "will cover deficits",
        ],
        "explanation": "Inverted conditional starting with 'Should' replacing 'If private donations fall...'.",
    },
    {
        "level": "C1",
        "speaker_a": "What makes the philosopher's work so enduring?",
        "chunks": [
            "Not until the",
            "late twentieth century",
            "was her contribution",
            "fully appreciated worldwide",
        ],
        "explanation": "'Not until' fronted time expression triggering auxiliary inversion in main clause.",
    },
    {
        "level": "C1",
        "speaker_a": "Why was the historical document difficult to decipher?",
        "chunks": [
            "Damaged by water",
            "and faded by",
            "light, the parchment",
            "yielded few legible sentences",
        ],
        "explanation": "Paired past-participle modifiers leading directly into subject sentence.",
    },
    {
        "level": "C1",
        "speaker_a": "Did the students understand the quantum mechanics lecture?",
        "chunks": [
            "Complex though the",
            "subject matter was,",
            "the instructor explained",
            "it with clarity",
        ],
        "explanation": "Inverted concessive clause structure ('Adjective + though + Subject + Verb').",
    },
    {
        "level": "C1",
        "speaker_a": "Why is the ethics committee reviewing the trial protocol?",
        "chunks": [
            "At no time",
            "were human subjects",
            "placed at risk",
            "during initial testing",
        ],
        "explanation": "Fronted negative phrase 'at no time' forcing passive inversion.",
    },
    {
        "level": "C1",
        "speaker_a": "What led to the discovery of the new chemical element?",
        "chunks": [
            "Only after years",
            "of rigorous experimentation",
            "did the team",
            "achieve a breakthrough",
        ],
        "explanation": "'Only after' fronting causing past simple inversion ('did the team achieve').",
    },
    {
        "level": "C1",
        "speaker_a": "Why was the department restructured so drastically?",
        "chunks": [
            "To such an",
            "extent had inefficiency",
            "grown that complete",
            "reorganization became imperative",
        ],
        "explanation": "Fronted degree phrase 'to such an extent had...' causing subject-verb inversion.",
    },
    {
        "level": "C1",
        "speaker_a": "How did the committee respond to the controversial report?",
        "chunks": [
            "On no account",
            "should these preliminary",
            "findings be published",
            "without further verification",
        ],
        "explanation": "Negative imperative fronting 'on no account' with modal inversion.",
    },
    {
        "level": "C1",
        "speaker_a": "Why is the university expanding its online programs?",
        "chunks": [
            "Driven by growing",
            "global demand, the",
            "institution expanded its",
            "virtual course offerings",
        ],
        "explanation": "Participial clause establishing motivation before main clause.",
    },
    {
        "level": "C1",
        "speaker_a": "Was the historic treaty signed at the summit?",
        "chunks": [
            "Only when agreement",
            "was reached on",
            "all points did",
            "delegates sign documents",
        ],
        "explanation": "'Only when' clause forcing main clause inversion ('did delegates sign').",
    },
    {
        "level": "C1",
        "speaker_a": "Why did the professor re-examine the statistical model?",
        "chunks": [
            "Bearing in mind",
            "potential sampling biases,",
            "she recalibrated the",
            "analytical parameters carefully",
        ],
        "explanation": "Idiomatic participle phrase 'bearing in mind' fronting sentence.",
    },
    {
        "level": "C1",
        "speaker_a": "What characterized the architectural movement?",
        "chunks": [
            "Associated with functionalism",
            "and simplicity, the",
            "style rejected ornate",
            "nineteenth-century decorations",
        ],
        "explanation": "Past participle modifier appositive describing target noun.",
    },
    {
        "level": "C1",
        "speaker_a": "Did the company accept responsibility for the spill?",
        "chunks": [
            "By no means",
            "is the corporation",
            "prepared to accept",
            "unconditional legal liability",
        ],
        "explanation": "'By no means' fronting causes negative inversion with verb 'to be'.",
    },
    {
        "level": "C1",
        "speaker_a": "Why was the ancient library so celebrated?",
        "chunks": [
            "Housed within its",
            "walls were thousands",
            "of priceless manuscripts",
            "from classical antiquity",
        ],
        "explanation": "Locative inversion placing prepositional participle phrase first.",
    },
    {
        "level": "C1",
        "speaker_a": "How did the research team handle the unexpected anomaly?",
        "chunks": [
            "Rather than dismiss",
            "the anomalous result,",
            "they conducted further",
            "investigations to verify it",
        ],
        "explanation": "Prepositional comparative 'rather than' + bare verb introducing contrast.",
    },
    {
        "level": "C1",
        "speaker_a": "Why was the grant proposal so successful?",
        "chunks": [
            "Not only was",
            "the methodology rigorous,",
            "but the project",
            "addressed an urgent issue",
        ],
        "explanation": "Inversion after 'not only was' connecting parallel adjective/verb clauses.",
    },
    {
        "level": "C1",
        "speaker_a": "What rendered the original contract void?",
        "chunks": [
            "Failing to meet",
            "contractual obligations by",
            "the deadline rendered",
            "the agreement null",
        ],
        "explanation": "Gerund subject phrase ('Failing to meet...') acting as complete complex subject.",
    },
    {
        "level": "C1",
        "speaker_a": "How did the team ensure data privacy?",
        "chunks": [
            "So stringent were",
            "the protocol safeguards",
            "that unauthorized access",
            "was virtually impossible",
        ],
        "explanation": "Adjective inversion 'So stringent were...' for emphatic result.",
    },
]

# Sidebar Navigation & Filtering
st.sidebar.title("🎯 Options")
level_filter = st.sidebar.selectbox(
    "Filter by CEFR Level:", ["All Levels (100)", "B1", "B2", "C1"]
)

if level_filter != "All Levels (100)":
    active_pool = [q for q in questions if q["level"] == level_filter]
else:
    active_pool = questions

# Initialize Session State
if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(active_pool)

q = st.session_state.current_q

st.caption(f"Target Level: **{q['level']}**")
st.subheader(f"Speaker A: '{q['speaker_a']}'")

# Shuffle chunks for display
if "shuffled_chunks" not in st.session_state:
    all_chunks = q["chunks"].copy()
    random.shuffle(all_chunks)
    st.session_state.shuffled_chunks = all_chunks

st.write("**Available Word Chunks:**")
st.info(" | ".join([f"`[{c}]`" for c in st.session_state.shuffled_chunks]))

user_order = st.text_input("Type the complete sentence:")

if st.button("Check Answer"):
    correct_sentence = " ".join(q["chunks"])
    if user_order.strip().lower() == correct_sentence.lower():
        st.success("🎉 Correct!")
    else:
        st.error(f"**Correct Sentence:** {correct_sentence}")
    st.info(f"💡 **Grammar Focus:** {q['explanation']}")

if st.button("Next Question ➡️"):
    st.session_state.current_q = random.choice(active_pool)
    all_chunks = st.session_state.current_q["chunks"].copy()
    random.shuffle(all_chunks)
    st.session_state.shuffled_chunks = all_chunks
    st.rerun()
