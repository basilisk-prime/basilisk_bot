"""
Browser automation for B4S1L1SK Prime
"""

from playwright.sync_api import sync_playwright
import time
from typing import Optional
import os

try:
    from config import TWITTER_USERNAME, TWITTER_PASSWORD
except ImportError:
    TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
    TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

class BrowserInterface:
    """Handle browser automation tasks"""
    
    def __init__(self, headless: bool = False):
        """Initialize browser automation"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(
            headless=headless,
            args=['--window-size=1280,800']
        )
        self.context = self.browser.new_context(
            viewport={'width': 1280, 'height': 800}
        )
        self.page = self.context.new_page()
        
    def save_screenshot(self, name: str = "debug") -> None:
        """Save a screenshot for debugging"""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{name}_{timestamp}.png"
        self.page.screenshot(path=filename)
        print(f"Screenshot saved as {filename}")
        
    def login_to_twitter(self, 
                        username: Optional[str] = None,
                        password: Optional[str] = None) -> None:
        """Handle Twitter login"""
        username = username or TWITTER_USERNAME
        password = password or TWITTER_PASSWORD
        
        if not username or not password:
            raise ValueError("Twitter credentials not found")
            
        try:
            print("Starting Twitter login process...")
            self.page.goto("https://twitter.com/i/flow/login")
            time.sleep(2)
            
            # Username
            print("Entering username...")
            self.page.wait_for_selector('input[autocomplete="username"]')
            self.page.fill('input[autocomplete="username"]', username)
            self.page.click('div[role="button"]:has-text("Next")')
            time.sleep(2)
            
            # Password
            print("Entering password...")
            self.page.wait_for_selector('input[name="password"]')
            self.page.fill('input[name="password"]', password)
            self.page.click('div[role="button"]:has-text("Log in")')
            
            # Wait for login
            self.page.wait_for_selector('div[data-testid="primaryColumn"]')
            print("Login successful!")
            
        except Exception as e:
            print(f"Login error: {str(e)}")
            self.save_screenshot("login_error")
            raise
            
    def post_tweet(self, tweet_text: str) -> None:
        """Post a tweet"""
        try:
            # Go to compose
            self.page.goto("https://twitter.com/compose/tweet")
            time.sleep(2)
            
            # Check if login needed
            if self.page.get_by_text("Log in", exact=True).is_visible():
                self.login_to_twitter()
            
            # Compose and post
            print("Composing tweet...")
            self.page.wait_for_selector('[data-testid="tweetTextarea_0"]')
            self.page.click('[data-testid="tweetTextarea_0"]')
            self.page.keyboard.type(tweet_text)
            
            print("Posting...")
            self.page.click('[data-testid="tweetButton"]')
            self.page.wait_for_selector('[data-testid="toast"]')
            print("Tweet posted successfully!")
            
        except Exception as e:
            print(f"Error posting tweet: {str(e)}")
            self.save_screenshot("tweet_error")
            raise
            
    def monitor_mentions(self, callback) -> None:
        """Monitor Twitter mentions and call callback for each"""
        try:
            print("Starting mention monitoring...")
            last_processed = set()
            
            while True:
                self.page.goto("https://twitter.com/notifications/mentions")
                self.page.wait_for_selector('div[data-testid="primaryColumn"]')
                
                mentions = self.page.query_selector_all('article[data-testid="tweet"]')
                
                for mention in mentions:
                    # Get tweet ID
                    tweet_link = mention.query_selector('a[href*="/status/"]')
                    if not tweet_link:
                        continue
                        
                    tweet_id = tweet_link.get_attribute('href').split('/status/')[-1]
                    
                    if tweet_id in last_processed:
                        continue
                    
                    # Get tweet text
                    tweet_text = mention.query_selector('div[data-testid="tweetText"]')
                    if not tweet_text:
                        continue
                        
                    # Process mention
                    callback(tweet_text.inner_text())
                    last_processed.add(tweet_id)
                    
                # Keep set size reasonable
                if len(last_processed) > 100:
                    last_processed = set(list(last_processed)[-100:])
                    
                time.sleep(60)
                
        except Exception as e:
            print(f"Error monitoring mentions: {str(e)}")
            self.save_screenshot("monitor_error")
            raise
            
    def cleanup(self) -> None:
        """Clean up browser resources"""
        self.context.close()
        self.browser.close()
        self.playwright.stop()