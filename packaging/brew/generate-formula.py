import json
import os
from poet import formula_for

with open(os.path.join(os.path.dirname(__file__), '..', '..', 'setup.json')) as f:
    setup_data = json.load(f)

data: str = formula_for('mpv-http-router')

data = data.replace('desc "Shiny new formula"', 'desc "%s"' % setup_data['description'])

with open('mpv-http-router.rb', 'w') as f:
    f.write(data)
