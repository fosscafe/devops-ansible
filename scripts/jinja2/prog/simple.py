
from jinja2 import Template

str="""num: 
{% for n in range(1,13) %} 
{{n}}
{% endfor %}
"""

t = Template(str)

print (t.render())

