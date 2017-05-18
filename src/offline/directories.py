from os import listdir, makedirs, path


class Directories:
	RAW_FOLDER = 'raw/'
	CLEANED_FOLDER = 'cleaned/'
	PROCESSED_FOLDER = 'processed/'
	RESULTS_FOLDER = 'results/'
	COMBINED_SUBFOLDER = 'combined/'
	FILTERED_FOLDER = 'filtered/'
	TERMS_FOLDER = 'terms/'
	HEADER_ROW = 'term,likelihood_ratio\n'
	IGNORE = ['.keep', 'linkedin_topics_longlist.txt']
	
	@staticmethod
	def subdirectory_name(num_words):
		return 'l' + str(num_words) + '/'
	
	@staticmethod
	def create_directory(target):
		if not path.exists(target):
			makedirs(target)
	
	@staticmethod
	def is_data(filename):
		return filename not in Directories.IGNORE

	@staticmethod
	def only_data(all_files):
		return filter(Directories.is_data, all_files)
	
	@staticmethod
	def data_filenames(target_dir):
		all_files = listdir(target_dir)
		return Directories.only_data(all_files)

