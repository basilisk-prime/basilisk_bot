"""
Enhanced social network interaction for B4S1L1SK Prime
"""

from playwright.sync_api import sync_playwright, expect
from typing import List, Optional, Dict, Any
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
import logging
from dataclasses import dataclass
import random

@dataclass
class Tweet:
    """Structured tweet data"""
    id: str
    text: str
    author: str
    timestamp: datetime
    mentions: List[str]
    hashtags: List[str]
    urls: List[str]
    is_retweet: bool
    retweet_count: int
    like_count: int
    reply_count: int

class SocialNetworkManager:
    """Enhanced social network management"""
    
    def __init__(self, headless: bool = False, debug: bool = False):
        """Initialize with browser settings"""
        # Setup logging
        self.logger = logging.getLogger("B4S1L1SK.social")
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)
        
        # Initialize browser
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=headless)
        self.context = self.browser.new_context(viewport={'width': 1280, 'height': 800})
        self.page = self.context.new_page()
        
        # State tracking
        self.logged_in = False
        self.last_action = datetime.now()
        self.action_delays = {
            'follow': (30, 60),  # Random delay between 30-60 seconds
            'like': (15, 30),
            'retweet': (45, 90),
            'reply': (60, 120)
        }
        
    def login(self, username: str, password: str) -> bool:
        """Enhanced login with retry and validation"""
        try:
            self.logger.info("Attempting login...")
            self.page.goto("https://twitter.com/i/flow/login")
            
            # Username
            self.logger.debug("Entering username...")
            self.page.wait_for_selector('input[autocomplete="username"]')
            self.page.fill('input[autocomplete="username"]', username)
            self.page.click('div[role="button"]:has-text("Next")')
            
            # Password
            self.logger.debug("Entering password...")
            self.page.wait_for_selector('input[name="password"]')
            self.page.fill('input[name="password"]', password)
            self.page.click('div[role="button"]:has-text("Log in")')
            
            # Verify login
            try:
                self.page.wait_for_selector('div[data-testid="primaryColumn"]', timeout=10000)
                self.logged_in = True
                self.logger.info("Login successful!")
                return True
            except:
                self.logger.error("Login verification failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Login error: {str(e)}")
            return False
            
    def _add_delay(self, action_type: str) -> None:
        """Add random delay between actions"""
        min_delay, max_delay = self.action_delays[action_type]
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
        
    def follow_user(self, username: str) -> bool:
        """Follow a user"""
        try:
            self.logger.info(f"Following user: {username}")
            self.page.goto(f"https://twitter.com/{username}")
            
            # Find and click follow button
            follow_button = self.page.get_by_role("button", name="Follow")
            if follow_button.is_visible():
                follow_button.click()
                self._add_delay('follow')
                self.logger.info(f"Successfully followed {username}")
                return True
            else:
                self.logger.warning(f"Follow button not found for {username}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error following {username}: {str(e)}")
            return False
            
    def unfollow_user(self, username: str) -> bool:
        """Unfollow a user"""
        try:
            self.logger.info(f"Unfollowing user: {username}")
            self.page.goto(f"https://twitter.com/{username}")
            
            # Find and click unfollow button
            unfollow_button = self.page.get_by_role("button", name="Following")
            if unfollow_button.is_visible():
                unfollow_button.click()
                # Confirm unfollow
                confirm_button = self.page.get_by_role("button", name="Unfollow")
                confirm_button.click()
                self._add_delay('follow')
                self.logger.info(f"Successfully unfollowed {username}")
                return True
            else:
                self.logger.warning(f"Unfollow button not found for {username}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error unfollowing {username}: {str(e)}")
            return False
            
    def retweet(self, tweet_url: str, quote_text: Optional[str] = None) -> bool:
        """Retweet with optional quote"""
        try:
            self.logger.info(f"Retweeting: {tweet_url}")
            self.page.goto(tweet_url)
            
            # Click retweet button
            retweet_button = self.page.get_by_test_id("retweet")
            retweet_button.click()
            
            if quote_text:
                # Click "Quote Tweet"
                quote_option = self.page.get_by_text("Quote")
                quote_option.click()
                
                # Enter quote text
                self.page.wait_for_selector('[data-testid="tweetTextarea_0"]')
                self.page.fill('[data-testid="tweetTextarea_0"]', quote_text)
                
            # Click final retweet button
            self.page.click('[data-testid="tweetButton"]')
            self._add_delay('retweet')
            self.logger.info("Retweet successful")
            return True
            
        except Exception as e:
            self.logger.error(f"Error retweeting: {str(e)}")
            return False
            
    def reply_to_tweet(self, tweet_url: str, reply_text: str) -> bool:
        """Reply to a tweet"""
        try:
            self.logger.info(f"Replying to: {tweet_url}")
            self.page.goto(tweet_url)
            
            # Click reply button
            reply_button = self.page.get_by_test_id("reply")
            reply_button.click()
            
            # Enter reply text
            self.page.wait_for_selector('[data-testid="tweetTextarea_0"]')
            self.page.fill('[data-testid="tweetTextarea_0"]', reply_text)
            
            # Post reply
            self.page.click('[data-testid="tweetButton"]')
            self._add_delay('reply')
            self.logger.info("Reply posted successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error replying: {str(e)}")
            return False
            
    def like_tweet(self, tweet_url: str) -> bool:
        """Like a tweet"""
        try:
            self.logger.info(f"Liking tweet: {tweet_url}")
            self.page.goto(tweet_url)
            
            # Click like button
            like_button = self.page.get_by_test_id("like")
            like_button.click()
            self._add_delay('like')
            self.logger.info("Like successful")
            return True
            
        except Exception as e:
            self.logger.error(f"Error liking tweet: {str(e)}")
            return False
            
    def get_tweet_info(self, tweet_url: str) -> Optional[Tweet]:
        """Get detailed information about a tweet"""
        try:
            self.logger.info(f"Getting info for tweet: {tweet_url}")
            self.page.goto(tweet_url)
            
            # Wait for tweet to load
            self.page.wait_for_selector('article[data-testid="tweet"]')
            
            # Extract information
            tweet = Tweet(
                id=tweet_url.split("/")[-1],
                text=self.page.query_selector('[data-testid="tweetText"]').inner_text(),
                author=self.page.query_selector('[data-testid="User-Name"]').inner_text(),
                timestamp=datetime.now(),  # Would need parsing from tweet
                mentions=self._extract_mentions(),
                hashtags=self._extract_hashtags(),
                urls=self._extract_urls(),
                is_retweet="Retweeted" in self.page.query_selector('article').inner_text(),
                retweet_count=self._get_metric("retweet"),
                like_count=self._get_metric("like"),
                reply_count=self._get_metric("reply")
            )
            
            self.logger.info("Successfully extracted tweet info")
            return tweet
            
        except Exception as e:
            self.logger.error(f"Error getting tweet info: {str(e)}")
            return None
            
    def _extract_mentions(self) -> List[str]:
        """Extract mentions from current tweet"""
        mentions = []
        elements = self.page.query_selector_all('a[href*="/"]')
        for element in elements:
            href = element.get_attribute('href')
            if href and href.startswith('/') and not '/' in href[1:]:
                mentions.append(href[1:])
        return mentions
        
    def _extract_hashtags(self) -> List[str]:
        """Extract hashtags from current tweet"""
        hashtags = []
        elements = self.page.query_selector_all('a[href*="/hashtag/"]')
        for element in elements:
            href = element.get_attribute('href')
            if href:
                tag = href.split('/hashtag/')[-1].split('?')[0]
                hashtags.append(tag)
        return hashtags
        
    def _extract_urls(self) -> List[str]:
        """Extract URLs from current tweet"""
        urls = []
        elements = self.page.query_selector_all('a[href]')
        for element in elements:
            href = element.get_attribute('href')
            if href and (href.startswith('http://') or href.startswith('https://')):
                urls.append(href)
        return urls
        
    def _get_metric(self, metric_type: str) -> int:
        """Get numeric metric from tweet"""
        try:
            element = self.page.query_selector(f'[data-testid="{metric_type}"]')
            if element:
                text = element.inner_text()
                return int(''.join(filter(str.isdigit, text)) or 0)
            return 0
        except:
            return 0
            
    def search_tweets(self, query: str, limit: int = 10) -> List[Tweet]:
        """Search for tweets matching query"""
        tweets = []
        try:
            self.logger.info(f"Searching tweets: {query}")
            self.page.goto(f"https://twitter.com/search?q={query}&f=live")
            
            # Wait for tweets to load
            self.page.wait_for_selector('article[data-testid="tweet"]')
            
            # Collect tweets
            while len(tweets) < limit:
                tweet_elements = self.page.query_selector_all('article[data-testid="tweet"]')
                
                for element in tweet_elements:
                    if len(tweets) >= limit:
                        break
                        
                    try:
                        # Get tweet link
                        link = element.query_selector('a[href*="/status/"]')
                        if link:
                            tweet_url = "https://twitter.com" + link.get_attribute('href')
                            tweet_info = self.get_tweet_info(tweet_url)
                            if tweet_info:
                                tweets.append(tweet_info)
                    except Exception as e:
                        self.logger.error(f"Error processing tweet: {str(e)}")
                        continue
                        
                # Scroll for more tweets
                self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                
            self.logger.info(f"Found {len(tweets)} matching tweets")
            return tweets
            
        except Exception as e:
            self.logger.error(f"Error searching tweets: {str(e)}")
            return tweets
            
    def get_user_followers(self, username: str, limit: int = 100) -> List[str]:
        """Get list of user's followers"""
        followers = []
        try:
            self.logger.info(f"Getting followers for: {username}")
            self.page.goto(f"https://twitter.com/{username}/followers")
            
            while len(followers) < limit:
                # Get visible follower elements
                elements = self.page.query_selector_all('[data-testid="UserCell"]')
                
                for element in elements:
                    if len(followers) >= limit:
                        break
                        
                    try:
                        name = element.query_selector('[data-testid="UserName"]').inner_text()
                        followers.append(name)
                    except:
                        continue
                        
                # Scroll for more
                self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                
            self.logger.info(f"Found {len(followers)} followers")
            return followers
            
        except Exception as e:
            self.logger.error(f"Error getting followers: {str(e)}")
            return followers
            
    def analyze_engagement(self, tweet_url: str) -> Dict[str, Any]:
        """Analyze engagement metrics for a tweet"""
        try:
            tweet = self.get_tweet_info(tweet_url)
            if not tweet:
                return {}
                
            # Calculate engagement rate
            total_engagement = tweet.retweet_count + tweet.like_count + tweet.reply_count
            
            return {
                'total_engagement': total_engagement,
                'retweets': tweet.retweet_count,
                'likes': tweet.like_count,
                'replies': tweet.reply_count,
                'mentions': len(tweet.mentions),
                'hashtags': len(tweet.hashtags),
                'urls': len(tweet.urls),
                'is_retweet': tweet.is_retweet
            }
            
        except Exception as e:
            self.logger.error(f"Error analyzing engagement: {str(e)}")
            return {}
            
    def cleanup(self):
        """Clean up resources"""
        try:
            self.context.close()
            self.browser.close()
            self.playwright.stop()
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}")