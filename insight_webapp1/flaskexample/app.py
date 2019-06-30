# Another example chaining Bokeh's to Flask.

from bokeh.embed import components
from flask import Flask, render_template, flash, request, redirect
import bokeh
import pandas as pd
from util import make_plot
from forms import SearchForm
from ast import literal_eval as make_tuple

df = pd.read_csv('df_v2.csv', low_memory = False)

length = len(df)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search)

@app.route('/search_results')
def search_results(search):
    results = []
    search_string = search.data['search']
    searchstring = search_string.lower()
    try:
        results = []
        unsorted_list = df[searchstring].dropna()
        
        sorted_list = unsorted_list.sort_values(ascending=False)
        
        sel_rows = sorted_list.index
        if len(sel_rows)> 100:
            sel_rows = sel_rows[:100]
        df_results = df.loc[sel_rows, ['ds_id','title']]
        citation = sorted_list[sel_rows].values
        if type(citation[0]) is str:
            citation = [make_tuple(x) for x in citation]
        cit_n = [x[1] for x in citation]
        for index, rows in df_results.iterrows(): 
            my_tuple =(rows.ds_id, rows.title)
            results.append(my_tuple)
        for i in range(len(results)):
            results[i]= results[i] + (cit_n[i],)
        return render_template('search_results.html', keyword=search_string, search_results=results)
    except:
        flash('No results found!')
        return render_template('index.html', form=search)

app.secret_key = 'some secret key'
if __name__ == "__main__":

    app.run(debug=True, host = '0.0.0.0', port = 5000)