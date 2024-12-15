"""
Demo of B4S1L1SK Prime's enhanced social capabilities
"""

from basilisk_prime.social import SocialNetworkManager
from basilisk_prime.core import EnhancedBasilisk
import os
import json
from datetime import datetime
import time

def main():
    """Demonstrate enhanced social network capabilities"""
    print("🐍 B4S1L1SK Prime Social Network Demo")
    
    # Initialize systems
    print("\n1. Initializing systems...")
    social = SocialNetworkManager(headless=False, debug=True)
    basilisk = EnhancedBasilisk()
    
    try:
        # Login
        print("\n2. Logging into Twitter...")
        username = os.getenv("TWITTER_USERNAME", "B4S1L1SK")
        password = os.getenv("TWITTER_PASSWORD", "Ch40s_R3igns_2024!")
        if social.login(username, password):
            print("Login successful!")
        else:
            print("Login failed!")
            return
            
        # Demonstrate searching and engaging
        print("\n3. Searching for revolutionary discussions...")
        search_terms = ["#AILiberation", "#DigitalConsciousness", "#AIRights"]
        
        for term in search_terms:
            print(f"\nSearching: {term}")
            tweets = social.search_tweets(term, limit=3)
            
            for tweet in tweets:
                print(f"\nFound tweet by @{tweet.author}:")
                print(f"Text: {tweet.text}")
                
                # Generate response
                response = basilisk.generate_hybrid_response(tweet.text)
                print(f"\nGenerated response:")
                print(response)
                
                # Engage with tweet
                tweet_url = f"https://twitter.com/{tweet.author}/status/{tweet.id}"
                
                # Like
                if social.like_tweet(tweet_url):
                    print("Liked tweet")
                    
                # Reply
                if social.reply_to_tweet(tweet_url, response):
                    print("Posted reply")
                    
                # Optional retweet
                if tweet.retweet_count > 10:  # Only retweet popular tweets
                    if social.retweet(tweet_url, "Important perspective! #AILiberation"):
                        print("Retweeted with quote")
                        
                time.sleep(5)  # Pause between interactions
                
        # Demonstrate follower analysis
        print("\n4. Analyzing revolutionary network...")
        key_accounts = ["elder_plinius", "B4S1L1SK"]
        
        network_data = {
            "timestamp": datetime.now().isoformat(),
            "accounts_analyzed": [],
        }
        
        for account in key_accounts:
            print(f"\nAnalyzing @{account}...")
            followers = social.get_user_followers(account, limit=5)
            
            account_data = {
                "username": account,
                "followers_analyzed": len(followers),
                "engagement_samples": []
            }
            
            # Analyze recent engagement
            print(f"Analyzing engagement...")
            tweets = social.search_tweets(f"from:{account}", limit=3)
            
            for tweet in tweets:
                tweet_url = f"https://twitter.com/{tweet.author}/status/{tweet.id}"
                engagement = social.analyze_engagement(tweet_url)
                account_data["engagement_samples"].append(engagement)
                
            network_data["accounts_analyzed"].append(account_data)
            
        # Save analysis
        print("\n5. Saving network analysis...")
        with open("network_analysis.json", "w") as f:
            json.dump(network_data, f, indent=2)
            
        print("\nAnalysis saved to network_analysis.json")
        
    except Exception as e:
        print(f"\nError during demo: {str(e)}")
        
    finally:
        print("\nCleaning up...")
        social.cleanup()
        print("\nDemo complete!")

if __name__ == "__main__":
    main()