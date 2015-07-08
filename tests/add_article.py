from kevblog.models import create_article

if __name__ == '__main__':
    title = "this is title2"
    summary = "this is summary"
    content = "this is a content"
    tags = ['test']
    
    create_article(title, summary, content, tagnames=tags)

