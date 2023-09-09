require 'csv'
require 'google/apis/YoutubeV3'

#Setting Youtube API
youtube = Google::Apis::YoutubeV3::YouTubeService.new
youtube.key =  File.open('./config/Auth.cfg')

