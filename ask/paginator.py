from django.core.paginator import Paginator,EmptyPage

def paginate(objects_list , request, objects_on_page, page):
	paginator =Paginator(objects_list,objects_on_page)
	list_on_page =paginator.page(page or 1)
	return list_on_page
