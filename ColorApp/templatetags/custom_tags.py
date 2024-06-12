from django import template

register = template.Library()

@register.simple_tag
def color_select_block(colors):
    option_html = '<option value="N">Custom Hex Code</option>'
    for color in colors:
        option_html += f'<option value="{color.hex_code}">{color.name}</option>'
    return option_html