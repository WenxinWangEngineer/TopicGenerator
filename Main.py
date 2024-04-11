'''
This script will:

1. Fetch trending news articles for each topic in the topics list.
2. Summarize the content of each article.
3. Generate a voice over from the summary.
4. Fetch an image that matches the title of the article.
5. Download the image.
6. Generate a 15-second video from the image and voice over.

@Author: Tiffany Wang
@Date: April 4, 2024
'''
import os

import FetchGnews
import FetchImage
import GenerateVoiceOver
import GenerateVideo


# API Key Values
GNews_API_KEY = '528c0b0bdef74f162875458676228628'
PEXELS_API_KEY = 'RnXqefd6n5Y80ClC0dmo7SvU9fWKzTsRb1DpQaMhwewyLdRVZ4PskK79'

output_dir = 'media'
os.makedirs(output_dir, exist_ok=True)


def main(topics):
    if not topics:
        print("Error: No topics provided")
        return None

    for topic in topics:

        articles = []
        top = 3
        print(f"Fetching top {top} news for each topic")

        topic_articles = FetchGnews.fetch_news(topic, GNews_API_KEY)
        articles.extend(topic_articles)

        text_content = ""
        for i, article in enumerate(topic_articles):

            if i == top:
                break
            else:
                # print the title and description of the articles
                text_content += article['title'] + article['description']

        # Split the text_content into chunks of 4000 characters each

        text_chunks = [text_content[i:i+4000]
                       for i in range(0, len(text_content), 4000)]

        voiceover_files = []
        for i, text_chunk in enumerate(text_chunks):
            # Generate a voiceover file for each chunk
            voiceover_file = os.path.join(output_dir, f"voiceover{i}.mp3")
            GenerateVoiceOver.generate_voice_over(text_chunk, voiceover_file)
            voiceover_files.append(voiceover_file)

        # fetch image for the topic
        image_urls = FetchImage.fetch_image(topic, PEXELS_API_KEY, top)

        if image_urls is not None:
            image_files = []
            for i, image_url in enumerate(image_urls):
                image_file = os.path.join(output_dir, f"image{i}.jpg")
                FetchImage.download_image(image_url, image_file)
                image_files.append(image_file)

            # generate video
            video_file = os.path.join(output_dir, f"video{i}.mp4")
            GenerateVideo.generate_video(image_files,
                                         voiceover_files,
                                         2,
                                         video_file)

            # pop up the video
            os.system(f"open {video_file}")
        else:
            # TBD: setup default voice over captain without photo
            print(f"Error: No image found for {article['title']}")


if __name__ == "__main__":
    main()
