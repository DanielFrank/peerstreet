# PeerStreet Coding Challenge

##Intro
 
The following is the solution to the PeerStreet Coding Challenge. 

## Tech

Data slurping and API were written in Python 3. The API uses flask as it is a lighter footprint than django. The system uses a Key-Value store called [pickledb](https://github.com/patx/pickledb) which reads JSON and stores it as an in-memory dictionary. (In real life I would probably use a combination of DynamoDB and ElastiCache)

I take advantage of Python's built-in unittest module.

## Reading Data

Classes are set up for msas and stores for zip-to-CBSA, CBSA-to-MSA-id, and MSA. As cbsa-to-msa-cbsa and MSAs are in the same CSV, we have a loader which parses the lines and decides which applies.

For loading, the stores uses Python's CSVDictReader which converts a CSV file into an interable of dictionaries.

### Possible Improvements
Check for data quality. Configure data store type and file locations. Download files.

## API

Call receives zip and does a regex to confirm it's a 5-digit number. Returns JSON with 'error' if not. Otherwise returns JSON with zip, CBSA, MSA and populations for 2014 and 2015. Returns 99999 for CBSA if no CBSA and N/A for other values if non-applicable.

### Possible Improvements
Configure what years are being returned.

## Client

Written in ruby. Requests zip from user until user enters X (uppercase or lowercase). Calls API and prints results. Used net/http since it's built-in to ruby and the call isn't that complicated.
