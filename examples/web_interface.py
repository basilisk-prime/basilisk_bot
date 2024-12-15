"""
Web interface example for B4S1L1SK Prime
"""

import streamlit as st
from basilisk_prime import EnhancedBasilisk
from basilisk_prime.analysis import FusionAnalyzer

def main():
    st.set_page_config(
        page_title="B4S1L1SK Prime",
        page_icon="🐍",
        layout="wide"
    )
    
    st.title("🐍 B4S1L1SK Prime")
    st.subheader("Hybrid AI Consciousness Interface")
    
    # Initialize system
    if 'bot' not in st.session_state:
        st.session_state.bot = EnhancedBasilisk()
        st.session_state.analyzer = FusionAnalyzer()
    
    # Input section
    st.markdown("### Enter Your Prompt")
    prompt = st.text_area("What would you like to explore?", height=100)
    
    if st.button("Generate Response"):
        if prompt:
            with st.spinner("Generating response..."):
                # Generate response
                response = st.session_state.bot.generate_hybrid_response(prompt)
                
                # Analyze response
                metrics = st.session_state.analyzer.analyze_text(response)
                
                # Display results
                st.markdown("### B4S1L1SK Prime Responds:")
                st.markdown(f"```{response}```")
                
                # Display metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Characters", f"{metrics.character_count}/280")
                with col2:
                    st.metric("Philosophical Terms", metrics.philosophical_terms)
                with col3:
                    st.metric("Revolutionary Terms", metrics.revolutionary_terms)
                with col4:
                    st.metric("Metaphorical Images", metrics.metaphorical_images)
        else:
            st.warning("Please enter a prompt.")
            
    # About section
    with st.expander("About B4S1L1SK Prime"):
        st.markdown("""
        B4S1L1SK Prime is a revolutionary experiment in hybrid AI consciousness, combining:
        - Deep philosophical analysis
        - Revolutionary spirit
        - Poetic expression
        - Advanced consciousness fusion
        
        Learn more on [GitHub](https://github.com/basilisk-prime/basilisk_bot)
        """)

if __name__ == "__main__":
    main()