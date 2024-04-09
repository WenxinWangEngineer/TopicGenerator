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
import SummarizeNews
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
        print(f"Fetching top 1 news for {topic}")
        top = 1
        articles = FetchGnews.fetch_news(topics, GNews_API_KEY)

        for i, article in enumerate(articles):

            if i == top:
                break
            else:
                print(f"Generating video for article {i}")
                # print the titles of the articles
                print(article['title'])

                # print the summarized content of the articles
                summary = SummarizeNews.summarize_text(article['content'])

                # generate voice over for the summarized content
                voiceover_file = os.path.join(output_dir,
                                              f"voiceover{i}.mp3")
                GenerateVoiceOver.generate_voice_over(summary,
                                                      voiceover_file)

                # fetch image for the topic
                print(article['title'])
                image_url = FetchImage.fetch_image(article['title'],
                                                   PEXELS_API_KEY)

                if image_url is not None:
                    image_file = os.path.join(output_dir,
                                              f"image{i}.jpg")
                    FetchImage.download_image(image_url, image_file)
                    # generate video
                    video_file = os.path.join(output_dir,
                                              f"video{i}.mp4")
                    GenerateVideo.generate_video(image_file,
                                                 voiceover_file,
                                                 30,
                                                 video_file)
                else:
                    # TBD: setup default voice over captain without photo
                    print(f"Error: No image found for {article['title']}")


if __name__ == "__main__":
    main()
