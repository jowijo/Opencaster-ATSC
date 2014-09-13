#
# EPG | Automatically generated. DO NOT EDIT
#
# EIT Tables. like their TVCT counterparts, use seperate items as opposed to individual tables, however, each EIT can only have 3 hours of content in it.
# meaning that every EIT table can only have six (6) 30-minute event_loop_item loops in it, or three (3) 1-hour event_loop_item loops in it.
# The FCC and ATSC mandate 16 days maximum of program info be braodcast.
# The EIT contains the program name, start time, length, rating, and audio language. An example item is below. It's output would read as:
#
# Title: Local News at Six, Rating: TV-G. Lamguage: English
#
# Start time is written in GPS Seconds. A good guide on how GPS time works, can be found here: http://www.andrews.edu/~tzs/timeconv/timealgorithm.html
# I also have a PHP conersion script if you want it. Simply email me.

event_loop_item(
	event_id = 200, #Incremental number that should always start at 200.
	title_length = 0x11, #length of compressed_string in bytes? Can't remember.
	start_time = 1091921416, #Start time (GPS format)
	length_in_seconds = 1800, #Length in seconds. 
	title_text = multiple_string_structure(
	number_strings = 0x1, #Number of string_loops. In this case, there is one.
		string_loop = [
			string_loop_item(
				ISO639_language_code = "eng", #This program is in English.
				number_segments = 0x1, #Again, only one segement. 
					segment_loop = [
						segment_loop_item(
							compression_type = 0x0, #No compression. Unless you like hoffman coding.
							mode = 0x0,
							number_bytes = 0x48, #Length in bytes of title string. This length is wrong.
							compressed_string = "\x4C\x6F\x63\x61\x6C\x20\x4E\x65\x77\x73\x20\x61\x74\x20\x53\x69\x78", #UTF-16 code points of program title.
							),],),],),
	ETM_location = 0x1,
	descriptor_loop = [
		content_advisory_descriptor( #US RATING SYSTEM
			rating_region_loop = [
				rating_region_loop_item(
					rating_region = 0x1, #United States
					rated_dimensions = 0x1, #Leave this alone.
					rating_description = 0x3, #Tried to get Region 1 ratings working. Not happening. 
					rated_dimension_loop = [
						rated_dimension_loop_item( 
							rating_dimension_j = 0x0, #Leave this alione
							rating_value = 0x3, #Leave this alione
							),
							], 
			rating_description_length = 0xD, #lenth in bytes of rating? Don't know.
			rating_description_text = multiple_string_structure(
				number_strings = 0x1, #One string loop.
					string_loop = [
						string_loop_item(
							ISO639_language_code = "eng", #This rating is in English.
								number_segments = 0x1,
									segment_loop = [
										segment_loop_item(
											compression_type = 0x0, #Again, we're not using compression.
											mode = 0x0,
											number_bytes = 0x5, #Length in bytes of rating string.
											compressed_string = "\x54\x56\x2D\x47", #TV-G
											),],),],),),],),],),
