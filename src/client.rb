require 'net/http'
require 'json'

def check_exit(info)
    return info == 'X' || info =='x'
end

def call_api(zip)
    url = 'http://127.0.0.1:5000/zipToDMA/' + zip
    uri = URI(url)
    response = Net::HTTP.get(uri)
    d=JSON.parse(response)
    if d.key?("error")
        puts d["error"]
        return
    end
    result_string = "Zip: %s\nCBSA: %s\nMSA: %s\nPop2014: %d\nPop2015: %d"
    puts result_string % [d["Zip"], d["CBSA"], d["MSA"], d["Pop2014"], d["Pop2015"]]
end

zip = ''
while (true)
    puts "Enter a zip: (X to exit)"
    zip = gets.chomp
    break if check_exit(zip)
    call_api(zip)
end




