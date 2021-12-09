from django.shortcuts import render
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from django.contrib.auth.decorators import login_required #to protect function views


# Create your views here.
def home(request):
	return render(request, 'sales/home.html')

#define function-based view - records()
#keep protected
@login_required
def records(request):
	#create an instance of SalesSearchForm that you defined in sales/forms.py
	form = SalesSearchForm(request.POST or None)
	sales_df=None	#initialize dataframe to None
	chart = None	#initialize chart to None

	#check if the button is clicked
	if request.method =='POST':
		#read book_title and chart_type
		book_title = request.POST.get('book_title')
		chart_type = request.POST.get('chart_type')

		#apply filter to extract data
		qs =Sale.objects.filter(book__name=book_title)
		if len(qs) >0:		#if data found
			#convert the queryset values to pandas dataframe
			sales_df=pd.DataFrame(qs.values())	
			#convert the ID to Name of book
			sales_df['book_id']=sales_df['book_id'].apply(get_bookname_from_id)
			#call get_chart by passing chart_type from user input, sales dataframe and labels
			chart=get_chart(chart_type, sales_df, labels=sales_df['book_id'].values)
			#convert the dataframe to HTML
			sales_df=sales_df.to_html()


		'''
		The following block is to get introduced to querysets
		#display in terminal - needed for debugging during development only
		print (book_title, chart_type)

		print ('Exploring querysets:')
		print ('Output of Sale.objects.all()')
		qs=Sale.objects.all()
		print (qs)

		print ('Output of Sale.objects.filter(book__name=book_title)')
		qs =Sale.objects.filter(book__name=book_title)
		print (qs)
			
		print ('Output of qs.values()')
		print (qs.values())

		print ('Output of qs.values_list()')
		print (qs.values_list())

		print ('Output of Sale.objects.get(id=1)')
		obj = Sale.objects.get(id=1)
		print (obj)
		'''


	#pack up data to be sent to template in the context dictionary
	context={
			'form': form,
			'sales_df': sales_df,
			'chart': chart
			}

	#load the sales/record.html page using the data that you just prepared
	return render(request, 'sales/records.html', context)
