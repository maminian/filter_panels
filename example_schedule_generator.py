import random
import datetime
import json

parallel_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

themes = ['Biology', 'Chemistry', 'PDEs', 'Fluids', 'UQ', 
            'Numerical Analysis', 'Iterative Solvers', 
            'Machine Learning', 'Artificial Intelligence', 
            ]
prepositions = [' at ', ' of ', ' to ', ' by ', '-inspired ']
names = ['Billy', 'Bob', 'Tammy', 'Joe', 'Laurie', 'Kristin', 'Ian', 'Sasha']
unis = ['Cal Poly Pomona', 'UNC Chapel Hill', 'CU Denver', 'Colorado State University', 
    'UT Knoxville', 'University of Utah', 'Worcester Polytechnic University', 
    'Emory University', 'Northeastern University']

prefixes = ['', 'On the ', 'Regarding ', 'A Deep Dive into ', '', '']
suffixes = ['...What Is It Good For?', ': Past, Present, and Future', 
    ' and the Meaning of Life', ': Applications to Cancer Treatment']

#
def gen_json(   filename='fake_conference.json',
                num_sessions=6, 
                talks_per_session=4, 
                num_parallel=4,
                minutes_per_talk=20):
    
    to_json = {}
    
    for i in range(num_parallel):
        pl = parallel_labels[i]
        for j in range(num_sessions):
            # Needed: 
            # session title; 
            # talks_per_session speakers;
            # talks_per_session affiliations;
            # talks_per_session titles.
            # talks_per_session unique identifiers.
            # For now, skip the abstracts.
            _c = random.choices(themes, k=2)
            
            session_title = _c[0] + random.choice(prepositions) + _c[1]
            for k in range(talks_per_session):
                
                name = ' '.join( random.choices(names, k=2) )
                uni = random.choice(unis)
                talk_title = random.choice(prefixes) + random.choice(_c) + random.choice(suffixes)
                
                _id = name + '_'.join( str(z).zfill(3) for z in [i,j,k] )
                to_json[_id] = {
                    'name': name,
                    'affiliation': uni,
                    'parallel_track':pl,
                    'parallel_num': i,
                    'session_num': j,
                    'session': session_title,
                    'title': talk_title,
                    '_id': _id,
                    #  TODO: talk time.
                }
    #
    with open(filename, 'w') as f:
        json.dump(to_json, f)
    return to_json
#

if __name__ == "__main__":
    _ = gen_json()

