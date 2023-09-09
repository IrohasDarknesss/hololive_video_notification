require 'csv'
require 'google/apis/YoutubeV3'

#Setting Youtube API
youtube = Google::Apis::YoutubeV3::YouTubeService.new
youtube.key =  File.open('./config/Auth.cfg')

# Get info
channel_ids = File.readlines('channel_ids.txt').map(&:chomp)

#Create CSV
CSV.open('Streaming_data.csv', "wb") do |csv|
    csv << ['Channel Name', 'Video URL']
    channel_ids.each do |channel_id|
        res = Youtube.list_channel_activities(
            part:'snippet', channel_id:channel_id,max_result: 3
        )