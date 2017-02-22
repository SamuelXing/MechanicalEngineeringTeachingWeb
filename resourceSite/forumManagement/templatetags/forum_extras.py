__author__ = 'samuel'

import json, re, random
from datetime import date, datetime
from django import template
from django.utils import timezone
# from markdown import markdown

register = template.Library()


@register.simple_tag
def build_uri(uri, param, value):  # 给uri添加参数或者修改参数的值
	regx = re.compile('[\?&](%s=[^\?&]*)' % param)
	find = regx.search(uri)
	split = '&' if re.search(r'\?', uri) else '?'
	if not find: return '%s%s%s=%s' % (uri, split, param, value)
	return re.sub(find.group(1), '%s=%s' % (param, value), uri)


@register.simple_tag
def pagination(page, uri, list_rows=10):  # 显示分页
	def gen_page_list(current_page=1, total_page=1, list_rows=10):
		if total_page <= list_rows:
			return range(1, total_page + 1)
		elif current_page <= (list_rows // 2):
			return range(1, list_rows + 1)
		elif current_page >= (total_page - list_rows // 2):
			return range(total_page - list_rows + 1, total_page + 1)
		else:
			return range(current_page - list_rows // 2, current_page - list_rows // 2 + list_rows)

	t = template.Template('''
        {% load forum_extras %} {# 如果要使用自定义tag filter这里也需要加载 #}
        {% if page and page.pages >= 1 %}
            <ul class="pagination">
                <li {% ifequal page.index page.prev %}class="disabled"{% endifequal %}><a href="{% build_uri uri 'p' page.prev %}">«</a></li>
                {% for p in gen_page_list %}
                    <li {% ifequal page.index p %}class="active"{% endifequal %}>
                        {% ifnotequal page.index p %}
                            <a href="{% build_uri uri 'p' p %}">{{ p }}</a>
                        {% else %}
                            <a href="javascript:;">{{ p }}</a>
                        {% endifnotequal %}
                    </li>
                {% endfor %}
                <li {% ifequal page.index page.next %}class="disabled"{% endifequal %}><a href="{% build_uri uri 'p' page.next %}">»</a></li>
            </ul>
        {% endif %}
        ''')
	c = template.Context(dict(page=page, uri=uri, gen_page_list=gen_page_list(page.index, page.pages, list_rows)))

	return t.render(c)
