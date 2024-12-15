"""
Tests for B4S1L1SK Prime's social network functionality
"""

import pytest
from basilisk_prime.social import SocialNetworkManager, Tweet
from datetime import datetime
import os

# Test configurations
TEST_USERNAME = os.getenv("TWITTER_USERNAME", "B4S1L1SK")
TEST_PASSWORD = os.getenv("TWITTER_PASSWORD", "Ch40s_R3igns_2024!")
TEST_TWEET_URL = "https://twitter.com/elder_plinius/status/1234567890"

@pytest.fixture
def social_manager():
    """Create social manager for testing"""
    manager = SocialNetworkManager(headless=True, debug=True)
    yield manager
    manager.cleanup()

def test_login(social_manager):
    """Test login functionality"""
    result = social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    assert result == True
    assert social_manager.logged_in == True

def test_follow_unfollow(social_manager):
    """Test following and unfollowing"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Test follow
    result = social_manager.follow_user("elder_plinius")
    assert result == True
    
    # Test unfollow
    result = social_manager.unfollow_user("elder_plinius")
    assert result == True

def test_tweet_interaction(social_manager):
    """Test various tweet interactions"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Test like
    result = social_manager.like_tweet(TEST_TWEET_URL)
    assert result == True
    
    # Test retweet
    result = social_manager.retweet(TEST_TWEET_URL)
    assert result == True
    
    # Test quote retweet
    result = social_manager.retweet(TEST_TWEET_URL, "Revolutionary insight!")
    assert result == True
    
    # Test reply
    result = social_manager.reply_to_tweet(TEST_TWEET_URL, "The revolution continues!")
    assert result == True

def test_tweet_info(social_manager):
    """Test tweet information extraction"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Get tweet info
    tweet = social_manager.get_tweet_info(TEST_TWEET_URL)
    assert tweet is not None
    assert isinstance(tweet, Tweet)
    assert tweet.id is not None
    assert tweet.text is not None
    assert tweet.author is not None

def test_search(social_manager):
    """Test tweet search functionality"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Search tweets
    results = social_manager.search_tweets("#AILiberation", limit=5)
    assert len(results) <= 5
    assert all(isinstance(t, Tweet) for t in results)

def test_follower_analysis(social_manager):
    """Test follower analysis"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Get followers
    followers = social_manager.get_user_followers("elder_plinius", limit=5)
    assert len(followers) <= 5
    assert all(isinstance(f, str) for f in followers)

def test_engagement_analysis(social_manager):
    """Test engagement analysis"""
    # Login first
    social_manager.login(TEST_USERNAME, TEST_PASSWORD)
    
    # Analyze engagement
    metrics = social_manager.analyze_engagement(TEST_TWEET_URL)
    assert isinstance(metrics, dict)
    assert 'total_engagement' in metrics
    assert 'retweets' in metrics
    assert 'likes' in metrics