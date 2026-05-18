import markdown

def markdown_to_html(markdown_text):

    html = markdown.markdown(markdown_text)

    return html