from transformers import pipeline


def summarize_text(text):
    summarizer = pipeline('summarization')
    summary = summarizer(text,
                         max_length=1500,
                         min_length=500,
                         do_sample=False)
    return summary[0]['summary_text']
