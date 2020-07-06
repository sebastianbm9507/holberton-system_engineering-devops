#!/usr/bin/env ruby
#puts ARGV[0].scan(/\[[f|t]\w{1,5}:[\w\\+-]+:?\d?:?-?\d?:?\d?:?-?\d?\]/).join(",")
puts ARGV[0].scan(/(?<=from:|to:|flags:)[\-+\d\w:]*/).join(",")
