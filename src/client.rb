require 'net/http'
require 'json'
url = 'http://127.0.0.1:5000/zipToDMA/90266'
uri = URI(url)
response = Net::HTTP.get(uri)
d=JSON.parse(response)
result_string = "Zip: %s\nCBSA: %s\nMSA: %s\nPop2014: %d\nPop2015: %d"
puts result_string % [d["Zip"], d["CBSA"], d["MSA"], d["Pop2014"], d["Pop2015"]]
