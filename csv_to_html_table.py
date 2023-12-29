import pandas

# convert CSV with fields "name", "affiliation", 
# "parallel_num", "session_num", "session", "title" 
# into an HTML table.

df = pandas.read_csv('fake_conference.csv')

#def build_entry(inputs):
#    return ''''''

session_prefix = "<div class='session'>"
session_suffix = "</div>"
talk_item = "<div class='conf-talk'>%s</div>"


def pivot_agg(x):
    print(x)
    td_contents = ''.join([talk_item%_xi for _xi in x])
    return session_prefix + td_contents + session_suffix

df_p = df.pivot_table(
    values='name', 
    columns='parallel_track', 
    index='session_num', 
    aggfunc=pivot_agg
)

df_p.to_html('inner_table.html',
    classes='table-class',
    table_id='conference_table',
    escape=False
)
