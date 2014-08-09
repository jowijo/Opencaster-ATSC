#
# EPG | Automatically generated. DO NOT EDIT
#
# A few things: Time as it pertains to 'start_time' is in GPS format. The  'length_in_seconds' means what you think it does -- the length in seconds. Examples provided. Make sure the shared values are the same as the ATSC document. Or else...
#
from dvbobjects.PSI.ATSC_EIT import *

KCWQ_id = 27
atsc_transport_stream_id = 2
atsc_service_id = 1

eit = event_information_section(
	table_id = 0xCB,
	service_id = atsc_service_id,
	transport_stream_id = atsc_transport_stream_id,
    source_id = KCWQ_id,
			event_loop = [
### START ITEM
event_loop_item(
					event_id = 200,
					title_length = 0x11,
					start_time = 1091592016, #9:00PM PST -- GPS FORMAT
					length_in_seconds = 1800, #30 MINUTES
					title_text = multiple_string_structure(
							number_strings = 0x1,
							string_loop = [
								string_loop_item(
									ISO639_language_code = "jpn",
									number_segments = 0x1,
									segment_loop = [
										segment_loop_item(
											compression_type = 0x0,
											mode = 0x0,
											number_bytes = 0x11,
											compressed_string = "\x43\x61\x72\x64\x63\x61\x70\x74\x6F\x72\x20\x53\x61\x6B\x75\x72\x61",
										),
									],
								),
							],
						),
					ETM_location = 0x2,
					descriptor_loop = [],
			),
### END ITEM
### START ITEM
event_loop_item(
					event_id = 201,
					title_length = 0x11,
					start_time = 1091593816, #9:30PM PST
					length_in_seconds = 3600, #1 HOUR
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
											number_bytes = 0x11,
											compressed_string = "\x44\x65\x6D\x6F\x63\x72\x61\x63\x79\x20\x4E\x6F\x77\x21",
										),
									],
								),
							],
						),
					ETM_location = 0x2,
					descriptor_loop = [],
			),
### END ITEM
### START ITEM
event_loop_item(
					event_id = 202,
					title_length = 0x11,
					start_time = 1091597416, #10:30 PM PST
					length_in_seconds = 10800, #3 HOURS
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
											number_bytes = 0x11,
											compressed_string = "\x4B\x42\x4B\x49\x20\x44\x4F\x43\x55\x4D\x45\x4E\x54\x41\x52\x59\x3A\x20\x43\x68\x61\x73\x69\x6E\x67\x20\x47\x68\x6F\x73\x74\x73\x20\x28\x42\x65\x79\x6F\x6E\x64\x20\x54\x68\x65\x20\x41\x72\x63\x61\x64\x65\x29",
										),
									],
								),
							],
						),
					ETM_location = 0x2,
					descriptor_loop = [],
			),
### END ITEM
### START ITEM
event_loop_item(
					event_id = 203,
					title_length = 0x11,
					start_time = 1091608216, #1:00 AM NEXT DAY
					length_in_seconds = 3600, # 1 HOUR
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
											number_bytes = 0x11,
											compressed_string = "\x45\x79\x65\x77\x69\x74\x6E\x65\x73\x73\x20\x4E\x65\x77\x73\x20\x40\x20\x31\x30\x3A\x33\x30",
										),
									],
								),
							],
						),
					ETM_location = 0x2,
					descriptor_loop = [],
			),
### END ITEM
	],
		version_number = 1,
        section_number = 0,
        last_section_number = 0,
		)	
