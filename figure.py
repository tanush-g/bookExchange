import numpy as np
from matplotlib.figure import Figure

#search is the resulting table from the query
def create_figure(search):
	n_groups = 7  # You can change the number of genres to display
	i = 0
	count_buying, count_borrowing, count_exchanging = (), (), ()
	total = []
	genres = []

	# Ensure we don't exceed array bounds
	while i < len(search) and i < n_groups * 4:
		if search[i]['transaction_type'] == 1:
			# transaction_type 1 = borrowing/lending
			count_borrowing = count_borrowing + (search[i]['Total_Books'],)
		elif search[i]['transaction_type'] == 2:
			# transaction_type 2 = buying/selling
			count_buying = count_buying + (search[i]['Total_Books'],)
		elif search[i]['transaction_type'] == 3:
			# transaction_type 3 = exchanging
			count_exchanging = count_exchanging + (search[i]['Total_Books'],)
		elif search[i]['transaction_type'] is None:
			# This is the rollup total for the genre
			if search[i]['genre_name'] is not None:
				total.append(search[i]['Total_Books'])
				genres.append(search[i]['genre_name'] + "(" + str(search[i]['Total_Books']) + ")")
				
				# Ensure all counts have the same length
				if len(count_exchanging) < len(genres):
					count_exchanging = count_exchanging + (0,)
				if len(count_borrowing) < len(genres):
					count_borrowing = count_borrowing + (0,)
				if len(count_buying) < len(genres):
					count_buying = count_buying + (0,)
				
				if len(genres) == n_groups:
					break

		i = i + 1

	# Ensure we have at least some data
	if len(genres) == 0:
		# Create dummy data if no genres found
		genres = ['No Data']
		count_borrowing = (0,)
		count_buying = (0,)
		count_exchanging = (0,)
		n_groups = 1

	# Pad arrays to ensure they're all the same length
	target_length = len(genres)
	while len(count_borrowing) < target_length:
		count_borrowing = count_borrowing + (0,)
	while len(count_buying) < target_length:
		count_buying = count_buying + (0,)
	while len(count_exchanging) < target_length:
		count_exchanging = count_exchanging + (0,)

	# count_exchanging = () + (1,) + (2,) + (3,) + (4,)
	# count_borrowing = (2,3,1,2)
	# count_buying = (2,3,1,1)
	# genres = ('A','B','C','D')

	fig = Figure()
	plt = fig.add_subplot(1, 1, 1)

	index = np.arange(len(genres))
	bar_width = 0.25
	opacity = 0.8

	plt.bar(index, count_exchanging, bar_width,
		alpha=opacity,
		color='b',
		label='Exchanging')

	plt.bar(index + bar_width, count_borrowing, bar_width,
		alpha=opacity,
		color='g',
		label='Borrowing')

	plt.bar(index + (2*bar_width), count_buying, bar_width,
		alpha=opacity,
		color='r',
		label='Buying')

	plt.set_xlabel('Genres')
	plt.set_ylabel('Total_Books')
	plt.set_title('Book Distribution by Genre and Transaction Type')
	plt.set_xticks(index + bar_width)
	plt.set_xticklabels(tuple(genres), rotation=45, ha='right')
	plt.legend()
	
	# Use fig.tight_layout() instead of plt.tight_layout()
	fig.tight_layout()

	return fig
	