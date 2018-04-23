require 'net/http'
require 'json'

def check_exit(info)
    return info == 'X' || info =='x'
end

def check_pop(pop)
    if pop.is_a? Integer
        return "%d"
    end
    return "%s"
end

def call_api(zip)
    url = 'http://ec2-52-35-55-238.us-west-2.compute.amazonaws.com/zipToDMA/' + zip
    uri = URI(url)
    response = Net::HTTP.get(uri)
    d=JSON.parse(response)
    if d.key?("error")
        puts d["error"]
        return
    end
    result_string = "Zip: %s\nCBSA: %s\nMSA: %s\nPop2014: " +
        check_pop(d["Pop2014"]) + "\nPop2015: " +
        check_pop(d["Pop2015"]) 
    puts result_string % [d["Zip"], d["CBSA"], d["MSA"], d["Pop2014"], d["Pop2015"]]
end

zip = ''
while (true)
    puts "Enter a zip: (X to exit)"
    zip = gets.chomp
    break if check_exit(zip)
    call_api(zip)
end




