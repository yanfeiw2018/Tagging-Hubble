# Tagging-Hubble
For a summary of results in presentation format, look inside the Documents folder.
Folder structure:
1. Data : processed data includes the two stopword dictionaries I constructed, json file for the programs, and keywords extracted from abstracts. Raw data and other processed data that contain information from full text of publications are not included here, as they were provided to me by my collaborator at Space Telescope Science Institute, and are protected by publisher copyright.
2. Documents: includes presentation and final report.
3. Python: function for nlp preprocessing.
4. notebooks:
  * Hubble_nlp is the main notebook for dealing with keyword extraction from publication text data. Main algorithms include training a phrase detection model with full texts of all available publications, tfidf model to find important words, constructing two vocabularies of stopwords.
  * hubble_db deals with mapping keywords from publications to datasets, and the metric of ranking datasets by their relavance to each keyword.
  * web_scraping_for_cat is needed for my ranking metric. It turns out that some datasets are calibration data and need to be down-weighted. This script deals with getting category information of datasets by scraping MAST website.
5. flask-webapp: includes python scripts, templates and css style files.
