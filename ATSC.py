#!/usr/bin/env python2
#
# PSIP DATA
#
import os
from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.PSI.MGT import *
from dvbobjects.PSI.TVCT import *
from dvbobjects.PSI.ATSC_EIT import *
from dvbobjects.PSI.ETT import *

### Global variables
atsc_original_transport_stream_id = #Channel's TSID (You don't have one)
atsc_transport_stream_id = 3 #Channel's TSID. (You don't have one)
atsc_service_id = 1 #Must have one for each channel.
atsc_pmt_pid = 1031 #Must have one for each channel. Starts at 1031, increment by 10.

tvct = terrestrial_virtual_channel_section(
	transport_stream_id = atsc_transport_stream_id,
	ATSC_protocol_version = 0,
	channels_loop = [
	
## CHANNEL LOOP ITEMS GO HERE ##
						
],
	additional_descriptors_loop = [],
	version_number = 1,
	section_number = 0,
	last_section_number = 0,)
	
eit = event_information_section(
	table_id = 0xCB,
	service_id = atsc_service_id,
	transport_stream_id = atsc_transport_stream_id,
    source_id = 20,
			event_loop = [
			## EVENT LOOP ITEMS GO HERE ##
			],
		version_number = 1,
        section_number = 0,
        last_section_number = 0,
		)	

	## EXTENDED TEXT TABLES GO HERE
	
mgt = master_guide_section(
	ATSC_protocol_version = 0,
	tables_loop = [
		table_loop_item(
			table_type = 0x0, # VIRTUAL CHANNEL
			table_type_pid = 0x1FFB,
			table_type_version_number = tvct.version_number,
			number_bytes = len(tvct.pack()),
			descriptors_loop = [],),
			table_loop_item(
			table_type = 256, # EPG PAGE 1
			table_type_pid = 0x3E00,
			table_type_version_number = 1,
			number_bytes = 0x11,
			descriptors_loop = [],
		),
		### TABLE LOOP ITEMS FOR EIT/ETT GO HERE ###
		
	],
	descriptors_loop = [],
	version_number = 1,
	section_number = 0,
	last_section_number = 0,)
	
	
pat = program_association_section(
	 transport_stream_id = atsc_transport_stream_id,
        program_loop = [
	### PROGRAM LOOP ITEMS FOR EACH CHANNEL GO HERE ###
	],
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
        )

pmt1 = program_map_section(
	program_number = atsc1_service_id,
	PCR_PID = 260,
	program_info_descriptor_loop = [],
	stream_loop = [
### STREAM_LOOP_ITEMS FOR A SINGLE CHANNEL. VIDEO/AUDIO, OR JUST AUDIO FOR RADIO ###
],
        version_number = 1,
        section_number = 1,
        last_section_number = 2,
        )

		### Your output entries go here. Consult Opencaster documentation ###
