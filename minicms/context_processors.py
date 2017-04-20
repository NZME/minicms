from models import *
import logging
logger = logging.getLogger(__name__)

def minicms_loader(request):
    page = request.META['PATH_INFO'].strip("/")
    if not page:
        page = '/'
    
    try:
        p = Page.objects.get(url=page)
        results = PageContent.objects.filter(page=p)
    except Page.DoesNotExist:
        results = []
        p = None
    
    #no results - check if we have any subpages
    if not p:
        page_bits = page.split("/")
        #check order: nain page, subpage1, subpage2 ...
        for page in page_bits:
            try:
                p = Page.objects.get(url=page)
                results = PageContent.objects.filter(page=p)
                if len(results) > 0:
                    break
            except: pass
            
    #if no results - use home page
    if not p == 0:
        try:
            p = Page.objects.get(url='/')
        except:
            pass
            
    content = {}
    content['page'] = p

    for page in results:
        #TODO: temporary hack to remove tinymce's <p> tags
        if page.content[:3] == '<p>':
            page.content = page.content[3:-4]
        content[page.container] = page.content

    return {'minicms_loader': content}
    

