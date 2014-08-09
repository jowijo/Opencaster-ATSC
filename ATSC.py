#!/usr/bin/env python2
#
# PSIP DATA
#
import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.PSI.MGT import *
from dvbobjects.PSI.TVCT import *

#
# Shared values
#
atsc_original_transport_stream_id = 2
atsc_transport_stream_id = 3
atsc_service_id = 1
atsc_pmt_pid = 1031
KCWQ_id = 27

#
# Terrestrial Virtual Channel Table
#
tvct = terrestrial_virtual_channel_section(
	transport_stream_id = atsc_transport_stream_id,
	ATSC_protocol_version = 0,
	channels_loop = [
		channel_loop_item(
			short_name = "\x00\x4B\x00\x42\x00\x4B\x00\x49\x00\x2D\x00\x48\x00\x44", 
			major_channel_number = 2,
			minor_channel_number = 1,
			modulation_mode = 0x04,
			carrier_frequency = 77000000, # deprecated
			channel_TSID = atsc_transport_stream_id,
			program_number = atsc_service_id,
			ETM_location = 0,
			access_controlled = 0,
			hidden = 0,
			hide_guide = 0,
			service_type = 0x2,
			source_id = KCWQ_id,
			descriptors_loop = [
],
		)
		
	],
	additional_descriptors_loop = [],
	version_number = 1,
	section_number = 0,
	last_section_number = 0,
	)

#
# ELECTRONIC PROGRAM GUIDE
#

from ATSC_EPG import * #Consult EIT.py for more info.

#
# EXTENDED TEXT
#

from ATSC_ETT import * #Consult ETT.py for info.
#
# Master Guide Table
#

mgt = master_guide_section(
	ATSC_protocol_version = 0,
	tables_loop = [
		table_loop_item(
			table_type = 0x0, # VIRTUAL CHANNEL
			table_type_pid = 0x1FFB,
			table_type_version_number = tvct.version_number,
			number_bytes = len(tvct.pack()),
			descriptors_loop = [],
		),
		table_loop_item(
			table_type = 0x0100, # EPG PAGE 1
			table_type_pid = 0x3E00,
			table_type_version_number = 1,
			number_bytes = 0x11,
			descriptors_loop = [],
		),
		table_loop_item(
			table_type = 0x0200, # EXT-EPG PAGE 1
			table_type_pid = 0x1DC8,
			table_type_version_number = 1,
			number_bytes = 0x11,
			descriptors_loop = [],
		),
	],
	descriptors_loop = [],
	version_number = 1,
	section_number = 0,
	last_section_number = 0,
	)



#
# Program Association Table (ISO/IEC 13818-1 2.4.4.3)
#

pat = program_association_section(
	transport_stream_id = atsc_transport_stream_id,
        program_loop = [
    	    program_loop_item(
	        program_number = atsc_service_id,
    		PID = atsc_pmt_pid,
    	    ),  
        ],
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
        )


#
# Program Map Table (ISO/IEC 13818-1 2.4.4.8)
#	

pmt = program_map_section(
	program_number = atsc_service_id,
	PCR_PID = 60,
	program_info_descriptor_loop = [],
	stream_loop = [
		stream_loop_item(
			stream_type = 2, # MPEG-2 Video 
			elementary_PID = 260,
			element_info_descriptor_loop = [
			
			
			]
		),
		stream_loop_item(
			stream_type = 129, # AC3 (Dolby) Audio
			elementary_PID = 265,
			element_info_descriptor_loop = [
				registration_descriptor(
					format_identifier="AC-3",
				),
					
                ISO_639_language_descriptor(
				     ISO_639_language_code = "eng",
				     Audio_type = 0x00,
				),
			]
		),
	],
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
        )    
		
###### EPG

##END

out = open("1080/pat.sec", "wb")
out.write(pat.pack())
out.close
out = open("1080/pat.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts 0 < 1080/pat.sec > 1080/pat.ts')

out = open("1080/pmt.sec", "wb")
out.write(pmt.pack())
out.close
out = open("1080/pmt.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts ' + str(atsc_pmt_pid) + ' < 1080/pmt.sec > 1080/pmt.ts')

out = open("1080/eit.sec", "wb")
out.write(eit.pack())
out.close
out = open("1080/eit.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts 7680 < 1080/eit.sec > 1080/eit.ts')

##NEW
out = open("1080/ett.sec", "wb")
out.write(ett.pack())
out.close
out = open("1080/ett.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts  7624 < 1080/ett.sec > 1080/ett.ts')

out = open("1080/mgt.sec", "wb")
out.write(mgt.pack())
out.close
out = open("1080/mgt.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts 8187 < 1080/mgt.sec > 1080/mgt.ts')

out = open("1080/tvct.sec", "wb")
out.write(tvct.pack())
out.close
out = open("1080/tvct.sec", "wb") # python   flush bug
out.close
os.system('/usr/bin/sec2ts 8187 < 1080/tvct.sec >> 1080/8187.ts')
