from django import template
register = template.Library()
import re    

class RenderDataNode(template.Node):
    def __init__(self, content):
        self.content = template.Variable(content)

    def render(self, context):
        try:
            actual_content = self.content.resolve(context)
            if actual_content.find('{{') != -1:
                variables = re.findall(r"{{.*}}", actual_content)
                for var in variables:
                    try:
                        actual_var = template.Variable(var.strip('{{').strip('}}')).resolve(context)
                        actual_content = actual_content.replace(var,actual_var)
                    except template.VariableDoesNotExist:
                        pass
            actual_content = actual_content.replace("\n", '<br/>')
            return actual_content
        except template.VariableDoesNotExist:
            return ''

@register.tag
def render_data(parser, token):
    tag_name, content = token.split_contents()
    return RenderDataNode(content)
