#
# ETT | Automatically generated. DO NOT EDIT
#
# So, assuming your ptogram has an ETM_Location flag, the ATSC reciever will then go looking for accompnying ETM data. How exactly does it find it? Using the ETM_id. I seem to have the equation wrong, as there is an offset (descriptions assinged to the program behind it IICR) It goes like this:
#
# (event_id / 65536^2) + (source_id / 16386) * 4   | I'm not the best with math, so....Have fun.
#
# Anyway, once that is done, we get to something that should look familiar at this point: the multiple_string_structure. The difference here, is that we are using a much longer string. Up to ~248 characters here.
ett1 = extended_text_table_section(
table_id = 0xCC, #All EIT tables must have this table_id. ALL OF THEM.
ETM_id = 140322, #See above.
source_id = 20, #Channel source ID.
ETT_table_id_extension = 700, #Should start this at 700.
extended_text_message = multiple_string_structure(
							number_strings = 0x1,
							string_loop = [
								string_loop_item(
									ISO639_language_code = "eng", #This description is in English.
									number_segments = 0x1,
									segment_loop = [
										segment_loop_item(
											compression_type = 0x0,
											mode = 0x0,
											number_bytes = 0x94,
											compressed_string ="\x43\x6C\x61\x73\x73\x69\x63\x20\x63\x61\x72\x74\x6F\x6F\x6E\x73\x20\x66\x72\x6F\x6D\x20\x74\x68\x65\x20\x31\x39\x320\x60\x73\x2C\x20\x74\x6F\x20\x74\x68\x65\x20\x31\x39\x360\x60\x73\x2E",),],),],),
version_number = 1,
section_number = 1,
last_section_number = 2,
)
