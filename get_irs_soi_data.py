"""
    get_irs_soi_data.py -- download IRS SOI Exempt Organization data files by state

    Version 0.1 CPB 2014-10-13
    --  Initial version.
"""

__author__      = "Christopher P. Barnes, senrabc@gmail.com"
__copyright__   = "Copyright 2014"
__license__     = "BSD 3-Clause license"
__version__     = "0.1"


import os

#names_urls = zip(names, urls)

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


#define the IRS SOI base url for the file tree
baseurl = "http://www.irs.gov/pub/irs-soi/eo_"
data_dir = "data/irs_soi_raw_data/"
#loop thourgh all the states and download the files.
for i, state_abrv in enumerate(states):
	irs_url = baseurl + state_abrv.lower() + ".csv"
	#print irs_url
	print('Downloading %s' % baseurl + state_abrv.lower() + ".csv")
	os.system('wget -P ' + data_dir + ' %s' % irs_url)
