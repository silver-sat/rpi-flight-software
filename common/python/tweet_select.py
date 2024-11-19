
def tweet_select(mode,target):
    assert mode in ("direct","proxy","minifs")
    if mode == "direct":
        assert target in ("twitter","reddit","bluesky")
        if target == "twitter":
            import direct_tweet, send_tweet
            twitter = direct_tweet.get_twitter()
            send_text_tweet = send_tweet.send_text_tweet
            send_photo_tweet = send_tweet.send_photo_tweet
        elif target == "reddit":
            import direct_reddit, send_reddit_tweet
            twitter = direct_reddit.get_twitter()
            send_text_tweet = send_reddit_tweet.send_text_tweet
            send_photo_tweet = send_reddit_tweet.send_photo_tweet
        elif target == "bluesky":
            import direct_bluesky, send_bluesky_tweet
            twitter = direct_bluesky.get_twitter()
            send_text_tweet = send_bluesky_tweet.send_text_tweet
            send_photo_tweet = send_bluesky_tweet.send_photo_tweet
    elif mode == "proxy":
        assert target in ("twitter",)
        import proxy_tweet, send_tweet
        twitter = proxy_tweet.get_twitter()
        send_text_tweet = send_tweet.send_text_tweet
        send_photo_tweet = send_tweet.send_photo_tweet
    elif mode == "minifs":
        import minifs_tweet, send_minifs_tweet
        twitter = minifs_tweet.get_twitter()
        send_text_tweet = send_minifs_tweet.send_text_tweet
        send_photo_tweet = send_minifs_tweet.send_photo_tweet
    return twitter, send_text_tweet, send_photo_tweet
