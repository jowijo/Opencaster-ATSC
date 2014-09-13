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
	event_id = 200,
	title_length = 0x11,
	start_time = 1091921416,
	length_in_seconds = 1800,
	title_text = multiple_string_structure(
	number_strings = 0x1,
		string_loop = [
			string_loop_item(
				ISO639_language_code = "eng",
				number_segments = 0x1,
					segment_loop = [
						segment_loop_item(
							compression_type = 0x0,
							mode = 0x0,
							number_bytes = 0x48,
							compressed_string = "\x4C\x6F\x63\x61\x6C\x20\x4E\x65\x77\x73\x20\x61\x74\x20\x53\x69\x78",),],),],),
	ETM_location = 0x1,
	descriptor_loop = [
		content_advisory_descriptor( #US RATING SYSTEM
			rating_region_loop = [
				rating_region_loop_item(
					rating_region = 0x1,
					rated_dimensions = 0x1,
					rating_description = 0x3,
					rated_dimension_loop = [
						rated_dimension_loop_item( 
							rating_dimension_j = 0x0,
							rating_value = 0x3,),],
			rating_description_length = 0xD,
			rating_description_text = multiple_string_structure(
				number_strings = 0x1,
					string_loop = [
						string_loop_item(
							ISO639_language_code = "eng",
								number_segments = 0x1,
									segment_loop = [
										segment_loop_item(
											compression_type = 0x0,
											mode = 0x0,
											number_bytes = 0x5,
											compressed_string = "\x54\x56\x2D\x47",),],),],),),],),],),
