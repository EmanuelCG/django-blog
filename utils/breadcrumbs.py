def get_breadcrumbs(*args):
    breadcrumbs = [{'name': 'Home', 'url':'/'}]

    for name, url in args:
        breadcrumbs.append({'name':name, 'url':url})
    
    return breadcrumbs